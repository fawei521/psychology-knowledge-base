#!/usr/bin/env python3
"""
Re-index embeddings for all documents in the knowledge base.

Usage:
    python tools/reindex_vectors.py
"""

import sqlite3
import sqlite_vec
import os
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "kb.db"


def get_embedding_model():
    """Load sentence-transformers model."""
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    os.environ.setdefault("CURL_CA_BUNDLE", "")
    os.environ.setdefault("REQUESTS_CA_BUNDLE", "")
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def serialize_vector(vec):
    return json.dumps([float(v) for v in vec])


def main():
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}")
        return

    print("Loading embedding model...")
    model = get_embedding_model()
    print("Model loaded.")

    conn = sqlite3.connect(DB_PATH)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    cursor = conn.cursor()

    # Clear existing vectors
    cursor.execute("DELETE FROM vec_documents")

    # Index entities
    cursor.execute("SELECT id, name, name_cn, definition, content, source_file FROM entities")
    for row in cursor.fetchall():
        entity_id, name, name_cn, definition, content, source_file = row
        text = f"{name} {name_cn or ''}\n{definition or ''}\n{content or ''}"
        vec = model.encode(text.strip()).tolist()
        preview = text[:500].replace("\n", " ")
        cursor.execute(
            "INSERT INTO vec_documents (doc_id, doc_type, source_file, content_preview, embedding) VALUES (?, ?, ?, ?, ?)",
            (entity_id, "entity", source_file, preview, serialize_vector(vec)),
        )
        print(f"Indexed entity: {name}")

    # Index sources
    cursor.execute("SELECT id, title, content, source_file FROM sources")
    for row in cursor.fetchall():
        source_id, title, content, source_file = row
        text = f"{title or ''}\n{content or ''}"
        vec = model.encode(text.strip()).tolist()
        preview = text[:500].replace("\n", " ")
        cursor.execute(
            "INSERT INTO vec_documents (doc_id, doc_type, source_file, content_preview, embedding) VALUES (?, ?, ?, ?, ?)",
            (source_id, "source", source_file, preview, serialize_vector(vec)),
        )
        print(f"Indexed source: {title}")

    # Index observations
    cursor.execute("SELECT id, title, context, behavior, analysis, source_file FROM observations")
    for row in cursor.fetchall():
        obs_id, title, context, behavior, analysis, source_file = row
        text = f"{title or ''}\n{context or ''}\n{behavior or ''}\n{analysis or ''}"
        vec = model.encode(text.strip()).tolist()
        preview = text[:500].replace("\n", " ")
        cursor.execute(
            "INSERT INTO vec_documents (doc_id, doc_type, source_file, content_preview, embedding) VALUES (?, ?, ?, ?, ?)",
            (obs_id, "observation", source_file, preview, serialize_vector(vec)),
        )
        print(f"Indexed observation: {title}")

    conn.commit()
    conn.close()
    print("\nVector reindex complete.")


if __name__ == "__main__":
    main()
