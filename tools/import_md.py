#!/usr/bin/env python3
"""
Import Markdown files into the SQLite knowledge base.

Supports incremental sync and vector search via sqlite-vec.

Usage:
    python tools/import_md.py
"""

import sqlite3
import sqlite_vec
import re
import yaml
import hashlib
import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / "kb.db"

RAW_DIR = BASE_DIR / "01-raw"
SUMMARIES_DIR = BASE_DIR / "02-summaries"
CARDS_DIR = BASE_DIR / "03-cards"
OBSERVATIONS_DIR = BASE_DIR / "05-observations"


def get_embedding_model():
    """Lazy load sentence-transformers model. Returns None if unavailable."""
    import os
    # Use hf-mirror and disable SSL verification for environments with certificate issues
    os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
    os.environ.setdefault("CURL_CA_BUNDLE", "")
    os.environ.setdefault("REQUESTS_CA_BUNDLE", "")
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        print("Embedding model loaded.")
        return model
    except Exception as e:
        print(f"Warning: could not load embedding model: {e}")
        print("Vector indexing will be skipped.")
        return None


def generate_embedding(text, model):
    """Generate 384-dim embedding for text."""
    if not model or not text or not text.strip():
        return None
    try:
        vec = model.encode(text.strip())
        return vec.tolist()
    except Exception as e:
        print(f"Warning: embedding generation failed: {e}")
        return None


def serialize_vector(vec):
    """Serialize vector for sqlite-vec as JSON array."""
    if vec is None:
        return None
    return json.dumps([float(v) for v in vec])


def file_hash(path):
    """Return SHA256 hash of file content."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    """Extract definition from card body."""
    for pattern in [
        r"## 定义\n+(.+?)(?=\n## |$)",
        r"## Definition\n+(.+?)(?=\n## |$)",
    ]:
        match = re.search(pattern, body, re.DOTALL)
        if match:
            return match.group(1).strip()
    return ""


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
        m = re.match(r"^#\s*所属学科：\s*(.+)$", line)
        if m:
            meta["domain"] = m.group(1).strip()
        m = re.match(r"^#\s*相关概念：\s*(.+)$", line)
        if m:
            related_raw = m.group(1).strip()
            links = re.findall(r"\[\[(card-[^\]]+)\]\]", related_raw)
            meta["relations"] = [{"target": t, "type": "related-to"} for t in links]
    return meta


def extract_headings_as_snippets(content, source_id, source_file, cursor):
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
        elif any(k in heading_lower for k in ["结果", "发现", "finding", "result", "核心发现", "核心观点", "核心要点"]):
            snippet_type = "result"
        elif any(k in heading_lower for k in ["理论", "theory", "讨论", "discussion"]):
            snippet_type = "theory"
        elif any(k in heading_lower for k in ["定义", "definition"]):
            snippet_type = "abstract"
        else:
            snippet_type = "note"

        cursor.execute(
            """
            INSERT INTO snippets (source_id, source_file, anchor_id, heading, snippet_type, content)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (source_id, source_file, f"{source_id}-{i}", heading, snippet_type, section_content),
        )


def delete_file_records(filename, cursor):
    """Delete all database records associated with a source file."""
    # Find entities
    cursor.execute("SELECT id FROM entities WHERE source_file = ?", (filename,))
    for row in cursor.fetchall():
        entity_id = row[0]
        cursor.execute("DELETE FROM tags WHERE target_type = 'entity' AND target_id = ?", (entity_id,))
        cursor.execute("DELETE FROM relations WHERE from_type = 'entity' AND from_id = ?", (entity_id,))
        cursor.execute("DELETE FROM relations WHERE to_type = 'entity' AND to_id = ?", (entity_id,))
        cursor.execute("DELETE FROM vec_documents WHERE doc_type = 'entity' AND doc_id = ?", (entity_id,))
    cursor.execute("DELETE FROM entities WHERE source_file = ?", (filename,))

    # Find sources
    cursor.execute("SELECT id FROM sources WHERE source_file = ?", (filename,))
    for row in cursor.fetchall():
        source_id = row[0]
        cursor.execute("DELETE FROM tags WHERE target_type = 'source' AND target_id = ?", (source_id,))
        cursor.execute("DELETE FROM snippets WHERE source_id = ?", (source_id,))
        cursor.execute("DELETE FROM vec_documents WHERE doc_type = 'source' AND doc_id = ?", (source_id,))
    cursor.execute("DELETE FROM sources WHERE source_file = ?", (filename,))

    # Find observations
    cursor.execute("SELECT id FROM observations WHERE source_file = ?", (filename,))
    for row in cursor.fetchall():
        obs_id = row[0]
        cursor.execute("DELETE FROM tags WHERE target_type = 'observation' AND target_id = ?", (obs_id,))
        cursor.execute("DELETE FROM vec_documents WHERE doc_type = 'observation' AND doc_id = ?", (obs_id,))
    cursor.execute("DELETE FROM observations WHERE source_file = ?", (filename,))

    cursor.execute("DELETE FROM sync_log WHERE filename = ?", (filename,))


def import_file(md_file, cursor, model, phase="import"):
    """Import a single Markdown file based on its location and frontmatter.

    phase='import': insert/update records (entities, sources, observations, tags, snippets).
    phase='relations': resolve and write entity relations (run after all entities exist).
    """
    content = md_file.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)
    relative_dir = md_file.parent.name
    source_file = str(md_file.relative_to(BASE_DIR))

    result = None
    if relative_dir == "02-summaries":
        result = import_as_source(md_file, fm, body, cursor, source_file, default_type="summary")
    elif relative_dir == "03-cards":
        result = import_as_entity(md_file, fm, body, cursor, source_file, phase=phase)
    elif relative_dir == "05-observations":
        result = import_as_observation(md_file, fm, body, cursor, source_file)
    elif relative_dir in ["01-raw", "pdfs", "web-pages"]:
        result = import_as_source(md_file, fm, body, cursor, source_file, default_type="other")
    else:
        if "concept" in fm:
            result = import_as_entity(md_file, fm, body, cursor, source_file, phase=phase)
        elif "observation_type" in fm or "case_type" in fm:
            result = import_as_observation(md_file, fm, body, cursor, source_file)
        else:
            result = import_as_source(md_file, fm, body, cursor, source_file, default_type="other")

    if phase == "import" and result:
        doc_type, doc_id, embedding_text = result
        vec = generate_embedding(embedding_text, model)
        if vec:
            preview = embedding_text[:500].replace("\n", " ")
            cursor.execute(
                """
                INSERT INTO vec_documents (doc_id, doc_type, source_file, content_preview, embedding)
                VALUES (?, ?, ?, ?, ?)
                """,
                (doc_id, doc_type, source_file, preview, serialize_vector(vec)),
            )

    return result


def import_as_source(md_file, fm, body, cursor, source_file, default_type="other"):
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
        INSERT INTO sources (source_type, filename, source_file, title, authors, year, source, url, content, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (ptype, md_file.name, source_file, title, authors, year, source, url, body, yaml.safe_dump(metadata)),
    )
    source_id = cursor.lastrowid

    full_content = md_file.read_text(encoding="utf-8")
    extract_headings_as_snippets(full_content, source_id, source_file, cursor)

    for tag in fm.get("tags", []):
        cursor.execute(
            "INSERT INTO tags (name, target_type, target_id) VALUES (?, ?, ?)",
            (tag, "source", source_id),
        )

    print(f"Imported source: {md_file.name} -> source_id={source_id}")
    embedding_text = f"{title}\n{body}"
    return "source", source_id, embedding_text


def import_as_entity(md_file, fm, body, cursor, source_file, phase="import"):
    """Import a single Markdown file as an entity (concept card).

    phase='import': insert/update entity, tags, definition, content, vector text.
    phase='relations': resolve and insert relations from frontmatter.
    """
    template_meta = extract_metadata_from_new_template(body) if not fm else {}

    if template_meta:
        card_number = template_meta.get("card_number", "")
        concept = card_number.lower().replace("-", "_") if card_number else md_file.stem
        concept_cn = template_meta.get("concept_cn", "")
        domain = template_meta.get("domain", "")
    else:
        concept = fm.get("concept", md_file.stem)
        concept_cn = fm.get("concept_cn", "")
        domain = fm.get("domain", "")

    if phase == "relations":
        # Resolve target entity id from existing entities
        cursor.execute(
            "SELECT id FROM entities WHERE name = ? OR name_cn = ?",
            (concept, concept_cn or concept),
        )
        row = cursor.fetchone()
        if not row:
            print(f"    Warning: entity '{concept}' not found during relations phase")
            return None
        entity_id = row[0]
        template_meta = extract_metadata_from_new_template(body) if not fm else {}
        relations = fm.get("relations", []) + template_meta.get("relations", [])
        _insert_entity_relations(entity_id, concept, relations, cursor)
        return None

    concept_en = fm.get("concept_en", "")
    entity_type = fm.get("entity_type", "concept")
    source_papers = fm.get("source_papers", [])
    definition = extract_definition(body) or fm.get("definition", "")
    name_cn = concept_cn or (concept if any("一" <= c <= "鿿" for c in concept) else "")

    metadata = {"original_path": str(md_file.relative_to(BASE_DIR))}

    cursor.execute(
        """
        INSERT INTO entities (entity_type, name, name_cn, name_en, domain, source_file, definition, content, source_ids, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            entity_type,
            concept,
            name_cn,
            concept_en,
            domain,
            source_file,
            definition,
            body,
            ", ".join(str(s) for s in source_papers),
            yaml.safe_dump(metadata),
        ),
    )
    entity_id = cursor.lastrowid

    for tag in fm.get("tags", []):
        cursor.execute(
            "INSERT INTO tags (name, target_type, target_id) VALUES (?, ?, ?)",
            (tag, "entity", entity_id),
        )

    print(f"Imported entity: {md_file.name} -> entity_id={entity_id}")
    embedding_text = f"{concept} {name_cn}\n{definition}\n{body}"
    return "entity", entity_id, embedding_text


def _insert_entity_relations(entity_id, concept, relations, cursor):
    """Resolve relation targets and insert relations for an entity."""
    for rel in relations:
        target = rel.get("target", "")
        rel_type = rel.get("type", "related-to")
        candidates = [target]
        if target.startswith("card-"):
            candidates.append(target[5:].replace("-", "_"))
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


def import_as_observation(md_file, fm, body, cursor, source_file):
    """Import a Markdown file as an observation."""
    obs_type = fm.get("observation_type", "other")
    title = fm.get("title", md_file.stem)
    event_date = fm.get("event_date", "")
    context = fm.get("context", "")
    behavior = fm.get("behavior", "")
    analysis = body
    related_entities = fm.get("related_entities", [])
    sources = fm.get("sources", [])
    metadata = {"original_path": str(md_file.relative_to(BASE_DIR))}

    cursor.execute(
        """
        INSERT INTO observations (observation_type, source_file, title, event_date, context, behavior, analysis, related_entity_ids, source_ids, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            obs_type,
            source_file,
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
    embedding_text = f"{title}\n{context}\n{behavior}\n{analysis}"
    return "observation", obs_id, embedding_text


def main():
    if not DB_PATH.exists():
        print(f"Database not found at {DB_PATH}")
        print("Please run: python tools/db_init.py")
        return

    model = get_embedding_model()

    conn = sqlite3.connect(DB_PATH)
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    cursor = conn.cursor()

    # Collect current files
    directories = [SUMMARIES_DIR, CARDS_DIR]
    if OBSERVATIONS_DIR.exists():
        directories.append(OBSERVATIONS_DIR)
    for raw_sub in [RAW_DIR / "pdfs", RAW_DIR / "web-pages"]:
        if raw_sub.exists():
            directories.append(raw_sub)

    current_files = {}
    for directory in directories:
        if not directory.exists():
            continue
        for md_file in sorted(directory.rglob("*.md")):
            if md_file.name.startswith("_") or md_file.name == "README.md":
                continue
            rel = str(md_file.relative_to(BASE_DIR))
            current_files[rel] = md_file

    # Load previously synced files
    cursor.execute("SELECT filename, mtime, hash FROM sync_log")
    synced = {row[0]: {"mtime": row[1], "hash": row[2]} for row in cursor.fetchall()}

    # Determine changed and deleted files
    changed_files = []
    for rel, md_file in current_files.items():
        mtime = md_file.stat().st_mtime
        h = file_hash(md_file)
        if rel not in synced or synced[rel]["mtime"] != mtime or synced[rel]["hash"] != h:
            changed_files.append(rel)

    deleted_files = [rel for rel in synced if rel not in current_files]

    print(f"Current files: {len(current_files)}")
    print(f"Changed files: {len(changed_files)}")
    print(f"Deleted files: {len(deleted_files)}")

    # Delete removed files
    for rel in deleted_files:
        print(f"Deleting records for removed file: {rel}")
        delete_file_records(rel, cursor)

    # Delete removed files
    for rel in deleted_files:
        print(f"Deleting records for removed file: {rel}")
        delete_file_records(rel, cursor)

    # Phase 1: Import changed files (entities, sources, observations, tags, snippets, vectors)
    for rel in changed_files:
        md_file = current_files[rel]
        print(f"Importing: {rel}")
        # Delete old records for this file first (in case of update)
        delete_file_records(rel, cursor)
        import_file(md_file, cursor, model, phase="import")

    # Phase 2: Resolve and write entity relations after all entities exist.
    # Only process changed cards, since unchanged cards already have their relations.
    print("\nResolving entity relations...")
    for rel in changed_files:
        md_file = current_files[rel]
        import_file(md_file, cursor, model, phase="relations")

    # Update sync log
    for rel in changed_files:
        md_file = current_files[rel]
        mtime = md_file.stat().st_mtime
        h = file_hash(md_file)
        cursor.execute(
            """
            INSERT INTO sync_log (filename, mtime, hash, synced_at)
            VALUES (?, ?, ?, datetime('now'))
            ON CONFLICT(filename) DO UPDATE SET
                mtime=excluded.mtime,
                hash=excluded.hash,
                synced_at=excluded.synced_at
            """,
            (rel, mtime, h),
        )

    conn.commit()
    conn.close()

    print("\nImport complete.")


if __name__ == "__main__":
    main()
