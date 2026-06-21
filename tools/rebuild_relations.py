#!/usr/bin/env python3
"""
Rebuild entity relations from Markdown card frontmatter.

Usage:
    python tools/rebuild_relations.py --all
    python tools/rebuild_relations.py --topic concepts.txt

Where concepts.txt contains one concept name per line.
"""

import sqlite3
import yaml
import argparse
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "kb.db"
CARDS_DIR = BASE_DIR / "03-cards"


def parse_frontmatter(content):
    """Parse YAML frontmatter from Markdown content."""
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except Exception as e:
        print(f"Warning: failed to parse frontmatter: {e}")
        return {}


def extract_metadata_from_new_template(body):
    """Extract metadata from the new seven-section card template (no YAML frontmatter)."""
    meta = {}
    lines = body.strip().split("\n")
    for line in lines[:10]:
        m = re.match(r"^#\s*卡片编号：\s*(.+)$", line)
        if m:
            meta["card_number"] = m.group(1).strip()
        m = re.match(r"^#\s*概念名称：\s*(.+)$", line)
        if m:
            meta["concept_cn"] = m.group(1).strip()
    if "card_number" in meta:
        meta["relations"] = []
    return meta


def resolve_target(cursor, target):
    """Resolve a relation target to an entity id."""
    candidates = [target]
    if target.startswith("card-"):
        candidates.append(target[5:].replace("-", "_"))
    for candidate in candidates:
        cursor.execute(
            "SELECT id FROM entities WHERE name = ? OR name_cn = ?",
            (candidate, candidate),
        )
        row = cursor.fetchone()
        if row:
            return row[0]
    return None


def collect_concepts_from_file(md_file):
    """Return (concept, concept_cn, relations) for a card file, or None."""
    content = md_file.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)
    if not fm:
        body = content
        template_meta = extract_metadata_from_new_template(body)
        if not template_meta:
            return None
        card_number = template_meta.get("card_number", "")
        concept = card_number.lower().replace("-", "_") if card_number else md_file.stem
        concept_cn = template_meta.get("concept_cn", "")
        relations = []
    else:
        concept = fm.get("concept", md_file.stem)
        concept_cn = fm.get("concept_cn", "")
        relations = fm.get("relations", [])
    return concept, concept_cn, relations


def main():
    parser = argparse.ArgumentParser(
        description="Rebuild entity relations from Markdown card frontmatter."
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Rebuild relations for all cards in 03-cards/.",
    )
    parser.add_argument(
        "--topic",
        type=Path,
        metavar="FILE",
        help="Path to a file containing concept names (one per line) to rebuild.",
    )
    args = parser.parse_args()

    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}")
        sys.exit(1)

    if not args.all and not args.topic:
        parser.print_help()
        sys.exit(1)

    target_concepts = set()
    if args.topic:
        if not args.topic.exists():
            print(f"Topic file not found: {args.topic}")
            sys.exit(1)
        for line in args.topic.read_text(encoding="utf-8").splitlines():
            concept = line.strip()
            if concept:
                target_concepts.add(concept)
        print(f"Rebuilding relations for {len(target_concepts)} concepts from {args.topic}")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Collect cards and their concepts
    cards = []
    concept_to_file = {}
    for md_file in sorted(CARDS_DIR.rglob("*.md")):
        if md_file.name.startswith("_") or md_file.name == "README.md":
            continue
        parsed = collect_concepts_from_file(md_file)
        if not parsed:
            continue
        concept, concept_cn, relations = parsed
        concept_to_file[concept] = md_file
        if args.all or concept in target_concepts:
            cards.append((concept, concept_cn, relations, md_file))

    if not args.all:
        missing = target_concepts - {c[0] for c in cards}
        if missing:
            print(f"Warning: {len(missing)} concepts not found in cards: {', '.join(sorted(missing))}")

    print(f"Processing {len(cards)} cards...")

    # Map concept -> entity id
    concept_to_id = {}
    for concept, concept_cn, _, _ in cards:
        cursor.execute(
            "SELECT id FROM entities WHERE name = ? OR name_cn = ?",
            (concept, concept_cn or concept),
        )
        row = cursor.fetchone()
        if row:
            concept_to_id[concept] = row[0]
        else:
            print(f"Warning: entity not found for concept '{concept}'")

    if not concept_to_id:
        print("No entities found to rebuild relations for.")
        conn.close()
        sys.exit(0)

    # Delete existing relations among these entities
    entity_ids = tuple(concept_to_id.values())
    if len(entity_ids) == 1:
        cursor.execute(
            """
            DELETE FROM relations
            WHERE from_type = 'entity' AND to_type = 'entity'
            AND (from_id = ? OR to_id = ?)
            """,
            (entity_ids[0], entity_ids[0]),
        )
    else:
        placeholders = ",".join("?" * len(entity_ids))
        cursor.execute(
            f"""
            DELETE FROM relations
            WHERE from_type = 'entity' AND to_type = 'entity'
            AND (from_id IN ({placeholders}) OR to_id IN ({placeholders}))
            """,
            entity_ids + entity_ids,
        )
    deleted = cursor.rowcount
    print(f"Deleted {deleted} existing relations")

    # Insert relations
    inserted = 0
    warnings = 0
    for concept, _, relations, md_file in cards:
        if concept not in concept_to_id:
            continue
        from_id = concept_to_id[concept]
        for rel in relations:
            target = rel.get("target", "")
            rel_type = rel.get("type", "related-to")
            to_id = resolve_target(cursor, target)
            if to_id is None:
                print(f"    Warning: could not resolve relation target '{target}' for entity '{concept}'")
                warnings += 1
                continue
            cursor.execute(
                """
                INSERT INTO relations (from_type, from_id, to_type, to_id, relation_type)
                VALUES ('entity', ?, 'entity', ?, ?)
                """,
                (from_id, to_id, rel_type),
            )
            inserted += 1

    conn.commit()
    conn.close()
    print(f"Inserted {inserted} relations ({warnings} warnings)")
    print("Done.")


if __name__ == "__main__":
    main()
