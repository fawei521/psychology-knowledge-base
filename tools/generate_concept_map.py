#!/usr/bin/env python3
"""
Generate concept-map.md from card frontmatter relations.

Usage:
    python tools/generate_concept_map.py        # dry-run, print to stdout
    python tools/generate_concept_map.py --apply # write to 04-index/concept-map.md
"""

import os
import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent.parent
CARDS_DIR = BASE / "03-cards"
OUTPUT = BASE / "04-index" / "concept-map.md"
OVERRIDE = BASE / "04-index" / "concept-map-override.md"

RELATION_TYPES = {
    "is-a", "part-of", "causes", "correlates-with", "supports",
    "contrasts", "applies-to", "extends", "requires",
}

DOMAIN_CN = {
    "general_psychology": "普通心理学",
    "social_psychology": "社会心理学",
    "developmental_psychology": "发展心理学",
    "personality_psychology": "人格心理学",
    "cognitive_psychology": "认知心理学",
    "abnormal_psychology": "异常心理学",
    "biological_psychology": "生物心理学",
    "positive_psychology": "积极心理学",
    "evolutionary_psychology": "进化心理学",
    "educational_psychology": "教育心理学",
    "experimental_psychology": "实验心理学",
    "clinical_psychology": "临床心理学",
    "organizational_psychology": "组织/管理心理学",
}


def parse_frontmatter(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return None, content
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None, content
    return fm, content


def card_quality(card_info, body_len):
    """Heuristic: prefer cards with concept_cn, more relations, longer body."""
    has_cn = 1 if card_info.get("concept_cn") else 0
    rel_count = len(card_info.get("relations", []) or [])
    return (has_cn, rel_count, body_len)


def collect_cards():
    cards = {}
    duplicates = {}
    for path in sorted(CARDS_DIR.rglob("card-*.md")):
        if path.name.startswith("_"):
            continue
        fm, body = parse_frontmatter(path)
        if not fm or "concept" not in fm:
            continue
        concept = fm["concept"]
        candidate = {
            "concept": concept,
            "concept_cn": fm.get("concept_cn", ""),
            "domain": fm.get("domain", ""),
            "tags": fm.get("tags", []) or [],
            "relations": fm.get("relations", []) or [],
            "file": path.name,
            "rel_path": str(path.relative_to(BASE)).replace("\\", "/"),
        }
        if concept in cards:
            duplicates.setdefault(concept, [cards[concept]["rel_path"]]).append(candidate["rel_path"])
            old_quality = card_quality(cards[concept], 0)
            new_quality = card_quality(candidate, len(body))
            if new_quality <= old_quality:
                continue
        cards[concept] = candidate
    return cards, duplicates


def normalize_relation_type(t):
    t = (t or "").strip().lower()
    if t in RELATION_TYPES:
        return t
    return "related-to"


def normalize_concept_name(name):
    """Convert hyphenated concept names to underscore style used in concept field."""
    return str(name).strip().lower().replace("-", "_")


def build_graph(cards):
    # nodes: concept -> card info
    # edges: list of (source, target, type)
    edges = []
    adjacency = defaultdict(list)
    for concept, card in cards.items():
        for rel in card.get("relations", []):
            target = normalize_concept_name(rel.get("target", ""))
            rel_type = normalize_relation_type(rel.get("type", ""))
            if not target:
                continue
            edges.append((concept, target, rel_type))
            adjacency[concept].append((target, rel_type))
            adjacency[target].append((concept, rel_type))  # treat as undirected for clustering
    return edges, adjacency


def find_clusters(cards, adjacency):
    visited = set()
    clusters = []
    for concept in cards:
        if concept in visited:
            continue
        # BFS
        stack = [concept]
        component = set()
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            visited.add(cur)
            component.add(cur)
            for neighbor, _ in adjacency.get(cur, []):
                if neighbor not in visited:
                    stack.append(neighbor)
        # Only keep components that contain at least one real card
        real = [c for c in component if c in cards]
        if real:
            clusters.append(real)
    return clusters


def format_card_link(concept, cards):
    if concept in cards:
        c = cards[concept]
        cn = c.get("concept_cn", "")
        name = f"[[{c['rel_path'].replace('.md', '')}|{concept}]]"
        if cn:
            return f"{name} {cn}"
        return name
    return f"[[{concept}]] (待创建)"


def label_for(concept, cards):
    """Return concept_cn if available, else concept name; never empty."""
    if concept in cards:
        cn = cards[concept].get("concept_cn", "")
        if cn:
            return cn
    return concept


def escape_pipes(text):
    return str(text).replace("|", "\\|")


def generate(cards, duplicates=None):
    edges, adjacency = build_graph(cards)
    clusters = find_clusters(cards, adjacency)

    # Sort clusters: larger first, then alphabetically by first member
    clusters.sort(key=lambda c: (-len(c), sorted(c)[0]))

    # Cards not in any cluster
    clustered = set()
    for c in clusters:
        clustered.update(c)
    orphan_concepts = sorted([c for c in cards if c not in clustered])

    # Relation statistics (only for edges where source is a real card)
    stat = defaultdict(int)
    for src, tgt, rel_type in edges:
        if src in cards:
            stat[rel_type] += 1

    lines = []
    lines.append("# Concept Map")
    lines.append("")
    lines.append("> 本文件由 `tools/generate_concept_map.py` 自动生成，请勿手动编辑。")
    lines.append("> 如需调整概念簇划分或关系，请修改卡片 YAML frontmatter 中的 `relations` 字段，然后重新运行脚本。")
    lines.append("> 人工修正可写入 `04-index/concept-map-override.md`，下次生成时会自动追加到末尾。")
    lines.append("")

    # Duplicate warnings
    if duplicates:
        lines.append("> [WARNING] 检测到以下 concept 对应多个文件，已自动选择内容更完整的版本：")
        for concept, paths in sorted(duplicates.items()):
            lines.append(f"> - `{concept}`: {', '.join(paths)}")
        lines.append("")

    # Summary
    lines.append("## 概览")
    lines.append("")
    lines.append(f"- 总卡片数：{len(cards)}")
    lines.append(f"- 概念簇数：{len(clusters)}")
    lines.append(f"- 孤立卡片数：{len(orphan_concepts)}")
    lines.append(f"- 关系总数：{sum(stat.values())}")
    lines.append("")

    # Clusters
    lines.append("## 概念簇")
    lines.append("")

    for idx, cluster in enumerate(clusters, 1):
        # Pick core node: highest degree within cluster, then alphabetically
        def cluster_degree(c):
            return sum(1 for n, _ in adjacency.get(c, []) if n in cluster)
        core = max(cluster, key=lambda c: (cluster_degree(c), -ord(c[0]) if c else 0))
        # Sort members: core first, then alphabetical
        members = sorted(cluster)
        members.remove(core)
        members.insert(0, core)

        core_card = cards.get(core, {})
        core_cn = core_card.get("concept_cn", "")
        core_domain = core_card.get("domain", "")
        domain_cn = DOMAIN_CN.get(core_domain, core_domain)
        header = f"### {idx}. "
        header += format_card_link(core, cards)
        if domain_cn:
            header += f"（{domain_cn}）"
        lines.append(header)
        lines.append("")

        # Build intra-cluster edges
        intra_edges = []
        seen_pairs = set()
        for src, tgt, rel_type in edges:
            if src in cluster and tgt in cluster:
                pair = tuple(sorted([src, tgt]) + [rel_type])
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    intra_edges.append((src, tgt, rel_type))

        if intra_edges:
            lines.append("```")
            for src, tgt, rel_type in intra_edges:
                src_label = label_for(src, cards)
                tgt_label = label_for(tgt, cards)
                lines.append(f"{src_label} -- {rel_type} --> {tgt_label}")
            lines.append("```")
            lines.append("")

        # Member table
        lines.append("| 成员 | 中文名 | 学科 | 簇内连接数 |")
        lines.append("|------|--------|------|-----------|")
        for m in members:
            card = cards.get(m, {})
            cn = card.get("concept_cn", "")
            dm = card.get("domain", "")
            dm_cn = DOMAIN_CN.get(dm, dm)
            deg = cluster_degree(m)
            lines.append(f"| {format_card_link(m, cards)} | {cn} | {dm_cn} | {deg} |")
        lines.append("")

    # Orphan cards
    if orphan_concepts:
        lines.append("## 孤立卡片（暂无关系）")
        lines.append("")
        lines.append("| 卡片 | 中文名 | 学科 |")
        lines.append("|------|--------|------|")
        for c in orphan_concepts:
            card = cards.get(c, {})
            cn = card.get("concept_cn", "")
            dm = card.get("domain", "")
            dm_cn = DOMAIN_CN.get(dm, dm)
            lines.append(f"| {format_card_link(c, cards)} | {cn} | {dm_cn} |")
        lines.append("")

    # External relations (relations pointing to cards not yet created)
    external = []
    for src, tgt, rel_type in edges:
        if src in cards and tgt not in cards:
            external.append((src, tgt, rel_type))
    if external:
        lines.append("## 指向未创建卡片的关系")
        lines.append("")
        lines.append("| 源卡片 | 关系 | 目标（待创建） |")
        lines.append("|--------|------|----------------|")
        for src, tgt, rel_type in external:
            src_label = cards.get(src, {}).get("concept_cn", src)
            lines.append(f"| {format_card_link(src, cards)} | {rel_type} | `{tgt}` |")
        lines.append("")

    # Relation statistics
    lines.append("## 关系统计")
    lines.append("")
    lines.append("| 关系类型 | 数量 |")
    lines.append("|---------|------|")
    for rel_type in sorted(stat.keys(), key=lambda x: -stat[x]):
        lines.append(f"| {rel_type} | {stat[rel_type]} |")
    lines.append("")

    # Append override if exists
    if OVERRIDE.exists():
        lines.append("")
        lines.append("---")
        lines.append("")
        with open(OVERRIDE, "r", encoding="utf-8") as f:
            override_content = f.read()
        lines.append(override_content)

    return "\n".join(lines)


def main():
    cards, duplicates = collect_cards()
    output = generate(cards, duplicates)
    apply = "--apply" in sys.argv
    if apply:
        with open(OUTPUT, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Wrote {OUTPUT} ({len(cards)} cards)")
        if duplicates:
            print("\n[WARNING] 检测到重复 concept 文件（已自动选择更完整版本）：")
            for concept, paths in sorted(duplicates.items()):
                print(f"  {concept}: {', '.join(paths)}")
    else:
        print(output)
        if duplicates:
            print("\n[WARNING] 检测到重复 concept 文件（已自动选择更完整版本）：")
            for concept, paths in sorted(duplicates.items()):
                print(f"  {concept}: {', '.join(paths)}")
        print("\n---\n这是预览。要写入文件请运行: python tools/generate_concept_map.py --apply")


if __name__ == "__main__":
    main()
