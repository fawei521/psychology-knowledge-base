#!/usr/bin/env python3
"""
Query the psychology knowledge base SQLite database.

Usage examples:
    python tools/query.py "SELECT * FROM cards"
    python tools/query.py "SELECT concept, domain FROM cards WHERE domain LIKE '%personality%'"
    python tools/query.py "SELECT p.title, s.heading FROM sections s JOIN papers p ON s.paper_id=p.id WHERE s.content LIKE '%Big Five%'"
"""

import sqlite3
import sys
import io
from pathlib import Path

# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

DB_PATH = Path(__file__).parent.parent / "kb.db"


def query(sql):
    """Execute a SQL query and print results."""
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}")
        print("Please run: python tools/db_init.py")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print("No results.")
            return

        # Print column headers
        headers = rows[0].keys()
        print(" | ".join(headers))
        print("-" * (len(" | ".join(headers)) + 20))

        # Print rows
        for row in rows:
            values = []
            for key in headers:
                value = row[key]
                if value is None:
                    values.append("NULL")
                else:
                    text = str(value).replace("\n", " ")
                    # Truncate long text
                    if len(text) > 120:
                        text = text[:120] + "..."
                    values.append(text)
            print(" | ".join(values))

        print(f"\nTotal: {len(rows)} rows")

    except sqlite3.Error as e:
        print(f"SQL Error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nCommon queries:")
        print('  python tools/query.py "SELECT * FROM cards"')
        print('  python tools/query.py "SELECT * FROM papers"')
        print('  python tools/query.py "SELECT name, COUNT(*) FROM tags GROUP BY name"')
        sys.exit(1)

    query(sys.argv[1])
