#!/usr/bin/env python3
"""
Import Markdown files into the SQLite knowledge base.

Usage:
    python tools/import_md.py
"""

import sqlite3
import re
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "kb.db"

# Directories to scan
RAW_DIR = BASE_DIR / "01-raw"
SUMMARIES_DIR = BASE_DIR / "02-summaries"
CARDS_DIR = BASE_DIR / "03-cards"
OBSERVATIONS_DIR = BASE_DIR / "05-observations"  # for future use


def parse_frontmatter(content):
    """Parse YAML frontmatter from Markdown content."""
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except Exception as e:
        print(f"Warning: failed to parse frontmatter: {e}")
        fm = {}

    body = parts[2].strip()
    return fm, body


def extract_definition(body):
    """Extract definition from card body. Supports both old and new templates."""
    patterns = [
        r"## 定义\n+(.+?)(?=\n## |$)",
        r"## Definition\n+(.+?)(?=\n## |$)",
        r"## 一、定义\n+(.+?)(?=\n## |$)",
    ]
    for pattern in patterns:
        match = re.search(pattern, body, re.DOTALL)
        if match:
            return match.group(1).strip()
    return ""


def extract_metadata_from_new_template(body):
    """Extract metadata from the new seven-section card template (no YAML frontmatter)."""
    meta = {}
    lines = body.strip().split('\n')
    for line in lines[:10]:
        m = re.match(r'^#\s*卡片编号：\s*(.+)$', line)
        if m:
            meta['card_number'] = m.group(1).strip()
        m = re.match(r'^#\s*概念名称：\s*(.+)$', line)
        if m:
            meta['concept_cn'] = m.group(1).strip()
        m = re.match(r'^#\s*所属学科：\s*(.+)$', line)
        if m:
            meta['domain'] = m.group(1).strip()
        m = re.match(r'^#\s*相关概念：\s*(.+)$', line)
        if m:
            related_raw = m.group(1).strip()
            links = re.findall(r'\[\[(card-[^\]]+)\]\]', related_raw)
            meta['relations'] = [{'target': t, 'type': 'related-to'} for t in links]
    return meta


def extract_headings_as_snippets(content, source_id, cursor):
    """Split a source into snippets by headings."""
    heading_pattern = re.compile(r"^(#{1,3})\s+(.+)$", re.MULTILINE)
    matches = list(heading_pattern.finditer(content))

    for i, match in enumerate(matches):
        heading = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section_content = content[start:end].strip()

        heading_lower = heading.lower()
        if any(k in heading_lower for k in ["方法", "method", "设计", "procedure"]):
            snippet_type = "method"
        elif any(k in heading_lower for k in ["结果", "发现", "finding", "result", "核心发现", "核心观点"]):
            snippet_type = "result"
        elif any(k in heading_lower for k in ["理论", "theory", "讨论", "discussion"]):
            snippet_type = "theory"
        elif any(k in heading_lower for k in ["定义", "definition"]):
            snippet_type = "abstract"
        else:
            snippet_type = "note"

        cursor.execute(
            """
            INSERT INTO snippets (source_id, anchor_id, heading, snippet_type, content)
            VALUES (?, ?, ?, ?, ?)
            """,
            (source_id, f"{source_id}-{i}", heading, snippet_type, section_content),
        )


def import_file(md_file, cursor):
    """Import a single Markdown file based on its location and frontmatter."""
    content = md_file.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)

    relative_dir = md_file.parent.name

    # Determine content type from directory or frontmatter
    if relative_dir == "02-summaries":
        import_as_source(md_file, fm, body, cursor, default_type="summary")
    elif relative_dir == "03-cards":
        import_as_entity(md_file, fm, body, cursor)
    elif relative_dir == "05-observations":
        import_as_observation(md_file, fm, body, cursor)
    elif relative_dir in ["01-raw", "pdfs", "web-pages"]:
        import_as_source(md_file, fm, body, cursor, default_type="other")
    else:
        # Fallback: use frontmatter type if available
        if "concept" in fm:
            import_as_entity(md_file, fm, body, cursor)
        elif "observation_type" in fm or "case_type" in fm:
            import_as_observation(md_file, fm, body, cursor)
        else:
            import_as_source(md_file, fm, body, cursor, default_type="other")


def import_as_source(md_file, fm, body, cursor, default_type="other"):
    """Import a Markdown file as a source."""
    title = fm.get("title", md_file.stem)
    authors = ", ".join(fm.get("authors", [])) if isinstance(fm.get("authors"), list) else fm.get("authors", "")
    year = int(fm["year"]) if fm.get("year") and str(fm["year"]).isdigit() else None
    source = fm.get("source", "")
    url = fm.get("url", "")
    ptype = fm.get("type", default_type)

    metadata = {
        "original_path": str(md_file.relative_to(BASE_DIR)),
        "key_findings": fm.get("key_findings", []),
        "methods": fm.get("methods", []),
    }

    cursor.execute(
        """
        INSERT INTO sources (source_type, filename, title, authors, year, source, url, content, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (ptype, md_file.name, title, authors, year, source, url, body, yaml.safe_dump(metadata)),
    )
    source_id = cursor.lastrowid

    # Extract snippets from full content (including frontmatter area is fine for heading search)
    full_content = md_file.read_text(encoding="utf-8")
    extract_headings_as_snippets(full_content, source_id, cursor)

    # Import tags
    for tag in fm.get("tags", []):
        cursor.execute(
            "INSERT INTO tags (name, target_type, target_id) VALUES (?, ?, ?)",
            (tag, "source", source_id),
        )

    print(f"Imported source: {md_file.name} -> source_id={source_id}")
    return source_id


def import_as_entity(md_file, fm, body, cursor):
    """Import a Markdown file as an entity (concept card)."""
    # Try to extract metadata from new template if no frontmatter
    template_meta = extract_metadata_from_new_template(body) if not fm else {}

    if template_meta:
        # New template: card number becomes identifier, concept name is Chinese
        card_number = template_meta.get("card_number", "")
        concept = card_number.lower().replace("-", "_") if card_number else md_file.stem
        concept_cn = template_meta.get("concept_cn", "")
        domain = template_meta.get("domain", "")
    else:
        concept = fm.get("concept", md_file.stem)
        concept_cn = ""
        domain = fm.get("domain", "")

    concept_en = fm.get("concept_en", "")
    entity_type = fm.get("entity_type", "concept")
    source_papers = fm.get("source_papers", [])

    definition = extract_definition(body) or fm.get("definition", "")

    metadata = {
        "original_path": str(md_file.relative_to(BASE_DIR)),
    }

    name_cn = concept_cn or (concept if any("一" <= c <= "鿿" for c in concept) else "")

    cursor.execute(
        """
        INSERT INTO entities (entity_type, name, name_cn, name_en, domain, definition, content, source_ids, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            entity_type,
            concept,
            name_cn,
            concept_en,
            domain,
            definition,
            body,
            ", ".join(str(s) for s in source_papers),
            yaml.safe_dump(metadata),
        ),
    )
    entity_id = cursor.lastrowid

    # Import tags
    for tag in fm.get("tags", []):
        cursor.execute(
            "INSERT INTO tags (name, target_type, target_id) VALUES (?, ?, ?)",
            (tag, "entity", entity_id),
        )

    # Import relations (resolve target by name)
    relations = fm.get("relations", []) + template_meta.get("relations", [])
    for rel in relations:
        target = rel.get("target", "")
        rel_type = rel.get("type", "related-to")

        # Normalize target: support both "card-james-lange-theory" and "james_lange_theory"
        candidates = [target]
        if target.startswith("card-"):
            concept_from_filename = target[5:].replace("-", "_")
            candidates.append(concept_from_filename)

        to_id = None
        for candidate in candidates:
            cursor.execute(
                "SELECT id FROM entities WHERE name = ? OR name_cn = ?",
                (candidate, candidate),
            )
            row = cursor.fetchone()
            if row:
                to_id = row[0]
                break

        if to_id:
            cursor.execute(
                """
                INSERT INTO relations (from_type, from_id, to_type, to_id, relation_type)
                VALUES (?, ?, ?, ?, ?)
                """,
                ("entity", entity_id, "entity", to_id, rel_type),
            )
        else:
            print(f"    Warning: could not resolve relation target '{target}' for entity '{concept}'")

    print(f"Imported entity: {md_file.name} -> entity_id={entity_id}")
    return entity_id


def import_as_observation(md_file, fm, body, cursor):
    """Import a Markdown file as an observation (case, experience, current event)."""
    obs_type = fm.get("observation_type", "other")
    title = fm.get("title", md_file.stem)
    event_date = fm.get("event_date", "")
    context = fm.get("context", "")
    behavior = fm.get("behavior", "")
    analysis = body

    related_entities = fm.get("related_entities", [])
    sources = fm.get("sources", [])

    metadata = {
        "original_path": str(md_file.relative_to(BASE_DIR)),
    }

    cursor.execute(
        """
        INSERT INTO observations (observation_type, title, event_date, context, behavior, analysis, related_entity_ids, source_ids, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            obs_type,
            title,
            event_date,
            context,
            behavior,
            analysis,
            ", ".join(str(e) for e in related_entities),
            ", ".join(str(s) for s in sources),
            yaml.safe_dump(metadata),
        ),
    )
    obs_id = cursor.lastrowid

    for tag in fm.get("tags", []):
        cursor.execute(
            "INSERT INTO tags (name, target_type, target_id) VALUES (?, ?, ?)",
            (tag, "observation", obs_id),
        )

    print(f"Imported observation: {md_file.name} -> observation_id={obs_id}")
    return obs_id


def main():
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}")
        print("Please run: python tools/db_init.py")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    # Clear existing data for full re-sync (incremental sync can be added later)
    print("Clearing existing data for full re-sync...")
    cursor.execute("DELETE FROM tags")
    cursor.execute("DELETE FROM relations")
    cursor.execute("DELETE FROM snippets")
    cursor.execute("DELETE FROM observations")
    cursor.execute("DELETE FROM entities")
    cursor.execute("DELETE FROM sources")
    cursor.execute("DELETE FROM sync_log")
    conn.commit()
    print("Existing data cleared.")

    # Import from all relevant directories
    directories = [SUMMARIES_DIR, CARDS_DIR]
    if OBSERVATIONS_DIR.exists():
        directories.append(OBSERVATIONS_DIR)
    for raw_sub in [RAW_DIR / "pdfs", RAW_DIR / "web-pages"]:
        if raw_sub.exists():
            directories.append(raw_sub)

    for directory in directories:
        if not directory.exists():
            continue
        for md_file in sorted(directory.rglob("*.md")):
            if md_file.name.startswith("_") or md_file.name == "README.md":
                continue
            import_file(md_file, cursor)

    conn.commit()
    conn.close()

    print("\nImport complete.")


if __name__ == "__main__":
    main()
