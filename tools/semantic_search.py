#!/usr/bin/env python3
"""
Semantic search over the knowledge base.

Usage:
    python tools/semantic_search.py "和注意力有关的概念"
"""

import sqlite3
import sqlite_vec
import os
import sys
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "kb.db"


def get_embedding_model():
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    os.environ.setdefault("CURL_CA_BUNDLE", "")
    os.environ.setdefault("REQUESTS_CA_BUNDLE", "")
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def search(query, top_k=5):
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}")
        return

    print(f"Query: {query}")
    print("Loading model...")
    model = get_embedding_model()
    vec = model.encode(query).tolist()

    conn = sqlite3.connect(DB_PATH)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT doc_type, doc_id, source_file, content_preview, distance
        FROM vec_documents
        WHERE embedding MATCH ?
        ORDER BY distance
        LIMIT ?
        """,
        (json.dumps([float(v) for v in vec]), top_k),
    )

    print(f"\nTop {top_k} results:\n")
    for row in cursor.fetchall():
        doc_type, doc_id, source_file, preview, distance = row
        # Fetch name/title for display
        title = ""
        if doc_type == "entity":
            cursor.execute("SELECT name_cn, name FROM entities WHERE id = ?", (doc_id,))
            r = cursor.fetchone()
            title = r[0] or r[1] if r else ""
        elif doc_type == "source":
            cursor.execute("SELECT title FROM sources WHERE id = ?", (doc_id,))
            r = cursor.fetchone()
            title = r[0] if r else ""
        elif doc_type == "observation":
            cursor.execute("SELECT title FROM observations WHERE id = ?", (doc_id,))
            r = cursor.fetchone()
            title = r[0] if r else ""

        print(f"[{doc_type}] {title}")
        print(f"  file: {source_file}")
        print(f"  distance: {distance:.4f}")
        print(f"  preview: {preview[:200]}...")
        print()

    conn.close()


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "工作记忆"
    search(query)
