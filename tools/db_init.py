#!/usr/bin/env python3
"""
Initialize the psychology knowledge base SQLite database with a long-term schema.

Supports: papers, theories, concepts, cases, personal experiences, current event analyses.

Usage:
    python tools/db_init.py
"""

import sqlite3
import json
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

    # 1. sources: literature, books, webpages, videos, raw materials
    cursor.execute("""
        CREATE TABLE sources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_type TEXT NOT NULL CHECK(source_type IN (
                'paper', 'book', 'book_chapter', 'book-chapter', 'webpage', 'video',
                'summary', 'review', 'personal_note', 'other'
            )),
            filename TEXT,
            title TEXT,
            authors TEXT,
            year INTEGER,
            source TEXT,
            url TEXT,
            content TEXT NOT NULL,
            metadata TEXT,  -- JSON
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_sources_type ON sources(source_type)")
    cursor.execute("CREATE INDEX idx_sources_year ON sources(year)")
    cursor.execute("CREATE INDEX idx_sources_title ON sources(title)")

    # 2. snippets: paragraphs, quotes, excerpts from sources
    cursor.execute("""
        CREATE TABLE snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source_id INTEGER NOT NULL,
            anchor_id TEXT,
            heading TEXT,
            snippet_type TEXT CHECK(snippet_type IN (
                'abstract', 'introduction', 'method', 'result', 'discussion',
                'theory', 'quote', 'note', 'summary', 'other'
            )),
            content TEXT NOT NULL,
            page_range TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (source_id) REFERENCES sources(id) ON DELETE CASCADE
        )
    """)
    cursor.execute("CREATE INDEX idx_snippets_source ON snippets(source_id)")
    cursor.execute("CREATE INDEX idx_snippets_type ON snippets(snippet_type)")

    # 3. entities: concepts, theories, persons, experiments, classic studies
    cursor.execute("""
        CREATE TABLE entities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_type TEXT NOT NULL CHECK(entity_type IN (
                'concept', 'theory', 'model', 'person', 'experiment',
                'scale', 'method', 'effect', 'law', 'principle', 'other'
            )),
            name TEXT NOT NULL,           -- primary name (often English)
            name_cn TEXT,                 -- Chinese name
            name_en TEXT,                 -- English name
            domain TEXT,                  -- e.g., personality psychology
            definition TEXT,
            content TEXT NOT NULL,
            source_ids TEXT,              -- comma-separated source IDs
            metadata TEXT,                -- JSON
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_entities_type ON entities(entity_type)")
    cursor.execute("CREATE INDEX idx_entities_name ON entities(name)")
    cursor.execute("CREATE INDEX idx_entities_domain ON entities(domain)")

    # 4. observations: personal experiences, typical cases, current event analyses
    cursor.execute("""
        CREATE TABLE observations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            observation_type TEXT NOT NULL CHECK(observation_type IN (
                'personal_experience', 'typical_case', 'current_event', 'reflection', 'other'
            )),
            title TEXT NOT NULL,
            event_date TEXT,
            context TEXT,
            behavior TEXT,
            analysis TEXT,
            related_entity_ids TEXT,      -- comma-separated entity IDs
            source_ids TEXT,              -- comma-separated source IDs
            metadata TEXT,                -- JSON
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_observations_type ON observations(observation_type)")
    cursor.execute("CREATE INDEX idx_observations_date ON observations(event_date)")

    # 5. relations: the core knowledge graph
    cursor.execute("""
        CREATE TABLE relations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_type TEXT NOT NULL CHECK(from_type IN ('source', 'snippet', 'entity', 'observation')),
            from_id INTEGER NOT NULL,
            to_type TEXT NOT NULL CHECK(to_type IN ('source', 'snippet', 'entity', 'observation')),
            to_id INTEGER NOT NULL,
            relation_type TEXT NOT NULL CHECK(relation_type IN (
                'is-a', 'part-of', 'causes', 'enables', 'inhibits',
                'correlates-with', 'supports', 'contradicts', 'extends',
                'applies-to', 'influences', 'describes', 'related-to'
            )),
            evidence TEXT,
            confidence REAL CHECK(confidence >= 0 AND confidence <= 1),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_relations_from ON relations(from_type, from_id)")
    cursor.execute("CREATE INDEX idx_relations_to ON relations(to_type, to_id)")
    cursor.execute("CREATE INDEX idx_relations_type ON relations(relation_type)")

    # 6. tags: flexible tag index
    cursor.execute("""
        CREATE TABLE tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            target_type TEXT NOT NULL CHECK(target_type IN ('source', 'snippet', 'entity', 'observation')),
            target_id INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_tags_name ON tags(name)")
    cursor.execute("CREATE INDEX idx_tags_target ON tags(target_type, target_id)")

    # 7. sync_log: track when Markdown files were last synced to DB
    cursor.execute("""
        CREATE TABLE sync_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            synced_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("CREATE INDEX idx_sync_log_file ON sync_log(filename)")

    conn.commit()
    conn.close()

    print(f"Database created at {DB_PATH}")
    print("Schema supports: sources, snippets, entities, observations, relations, tags")


if __name__ == "__main__":
    init_db()
