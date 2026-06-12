#!/usr/bin/env python3
"""
Initialize the psychology knowledge base SQLite database.

Supports incremental sync and vector search via sqlite-vec.

Usage:
    python tools/db_init.py
"""

import sqlite3
import sqlite_vec
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "kb.db"


def init_db():
    """Create tables and indexes for the psychology knowledge base."""
    if DB_PATH.exists():
        print(f"Database already exists at {DB_PATH}")
        print("If you want to recreate it, delete the file first.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # Enable sqlite-vec extension
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)

    # 1. sources
    cursor.execute("""
        CREATE TABLE sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT NOT NULL,
            filename TEXT,
            source_file TEXT,
            title TEXT,
            authors TEXT,
            year INTEGER,
            source TEXT,
            url TEXT,
            content TEXT NOT NULL,
            metadata TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_sources_type ON sources(source_type)")
    cursor.execute("CREATE INDEX idx_sources_year ON sources(year)")
    cursor.execute("CREATE INDEX idx_sources_title ON sources(title)")
    cursor.execute("CREATE INDEX idx_sources_file ON sources(source_file)")

    # 2. snippets
    cursor.execute("""
        CREATE TABLE snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id INTEGER NOT NULL,
            source_file TEXT,
            anchor_id TEXT,
            heading TEXT,
            snippet_type TEXT,
            content TEXT NOT NULL,
            page_range TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (source_id) REFERENCES sources(id) ON DELETE CASCADE
        )
    """)
    cursor.execute("CREATE INDEX idx_snippets_source ON snippets(source_id)")
    cursor.execute("CREATE INDEX idx_snippets_type ON snippets(snippet_type)")
    cursor.execute("CREATE INDEX idx_snippets_file ON snippets(source_file)")

    # 3. entities
    cursor.execute("""
        CREATE TABLE entities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_type TEXT NOT NULL,
            name TEXT NOT NULL,
            name_cn TEXT,
            name_en TEXT,
            domain TEXT,
            source_file TEXT,
            definition TEXT,
            content TEXT NOT NULL,
            source_ids TEXT,
            metadata TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_entities_type ON entities(entity_type)")
    cursor.execute("CREATE INDEX idx_entities_name ON entities(name)")
    cursor.execute("CREATE INDEX idx_entities_domain ON entities(domain)")
    cursor.execute("CREATE INDEX idx_entities_file ON entities(source_file)")

    # 4. observations
    cursor.execute("""
        CREATE TABLE observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            observation_type TEXT NOT NULL,
            source_file TEXT,
            title TEXT NOT NULL,
            event_date TEXT,
            context TEXT,
            behavior TEXT,
            analysis TEXT,
            related_entity_ids TEXT,
            source_ids TEXT,
            metadata TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_observations_type ON observations(observation_type)")
    cursor.execute("CREATE INDEX idx_observations_date ON observations(event_date)")
    cursor.execute("CREATE INDEX idx_observations_file ON observations(source_file)")

    # 5. relations
    cursor.execute("""
        CREATE TABLE relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_type TEXT NOT NULL,
            from_id INTEGER NOT NULL,
            to_type TEXT NOT NULL,
            to_id INTEGER NOT NULL,
            relation_type TEXT NOT NULL,
            evidence TEXT,
            confidence REAL CHECK(confidence >= 0 AND confidence <= 1),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_relations_from ON relations(from_type, from_id)")
    cursor.execute("CREATE INDEX idx_relations_to ON relations(to_type, to_id)")
    cursor.execute("CREATE INDEX idx_relations_type ON relations(relation_type)")

    # 6. tags
    cursor.execute("""
        CREATE TABLE tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            target_type TEXT NOT NULL,
            target_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_tags_name ON tags(name)")
    cursor.execute("CREATE INDEX idx_tags_target ON tags(target_type, target_id)")

    # 7. sync_log
    cursor.execute("""
        CREATE TABLE sync_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL UNIQUE,
            mtime REAL,
            hash TEXT,
            target_type TEXT,
            target_id INTEGER,
            synced_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_sync_log_file ON sync_log(filename)")

    # 8. vec_documents: unified vector table for semantic search
    cursor.execute("""
        CREATE VIRTUAL TABLE vec_documents USING vec0(
            doc_id INTEGER,
            doc_type TEXT,
            source_file TEXT,
            +content_preview TEXT,
            embedding FLOAT[384]
        )
    """)

    conn.commit()
    conn.close()

    print(f"Database created at {DB_PATH}")
    print("Schema supports: sources, snippets, entities, observations, relations, tags, sync_log, vec_documents")


if __name__ == "__main__":
    init_db()
