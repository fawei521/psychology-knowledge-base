#!/usr/bin/env python3
"""一次性检查规则文件中的硬编码 .md / .py 引用是否指向真实文件。"""
from __future__ import annotations

import re
from pathlib import Path

BASE = Path("E:/psychology-knowledge-base")

# 扫描这些目录下的 .md 文件
SCAN_DIRS = ["00-prompts/rules", "meta", "04-index", "tools"]

# 匹配代码块、行内代码、markdown 链接、纯文本中的 .md / .py 文件名
PATTERNS = [
    re.compile(r"`([^`]*?\.(?:md|py))`"),       # 行内代码
    re.compile(r"\[([^\]]+?)\]\(([^)]+?\.(?:md|py))\)"),  # markdown 链接
    re.compile(r"\b([a-zA-Z0-9_\-/]+\.(?:md|py))\b"),      # 一般文本
]

# 尝试解析引用的可能位置
SEARCH_ROOTS = [
    BASE,
    BASE / "00-prompts/rules",
    BASE / "00-prompts",
    BASE / "meta",
    BASE / "04-index",
    BASE / "04-index/startup",
    BASE / "tools",
    BASE / "03-cards",
    BASE / "05-observations",
    BASE / "02-summaries",
    Path("C:/Users/乏味/.claude/projects/C--Users---/memory"),
]

# 排除模板/通配符/命令片段
SKIP_PATTERNS = [
    re.compile(r"[*?{}\[\]]"),           # glob / f-string 占位符
    re.compile(r"^\s*$"),                  # 空
    re.compile(r"^(?:python|grep|cd|mv|cp|mkdir|pip)\s"),  # 命令行
]


def should_skip(ref: str) -> bool:
    for pat in SKIP_PATTERNS:
        if pat.search(ref):
            return True
    return False


def resolve_ref(ref: str, source_dir: Path) -> Path | None:
    """尝试把引用解析为真实路径。"""
    # 1. 相对 source 文件目录
    candidate = source_dir / ref
    if candidate.exists():
        return candidate

    # 2. 相对各搜索根
    for root in SEARCH_ROOTS:
        candidate = root / ref
        if candidate.exists():
            return candidate

    # 3. 去掉目录前缀再试
    ref_name = Path(ref).name
    for root in SEARCH_ROOTS:
        candidate = root / ref_name
        if candidate.exists():
            return candidate

    return None


def main():
    broken: list[tuple[Path, str]] = []
    seen: set[tuple[str, str]] = set()

    for ns in SCAN_DIRS:
        for f in (BASE / ns).rglob("*.md"):
            source_dir = f.parent
            text = f.read_text(encoding="utf-8")
            refs: set[str] = set()

            for pat in PATTERNS:
                for match in pat.finditer(text):
                    # 取最后一个捕获组（通常是路径）
                    ref = match.groups()[-1].strip()
                    if not ref or "/" in ref and ref.startswith(("http://", "https://")):
                        continue
                    refs.add(ref)

            for ref in refs:
                key = (str(f), ref)
                if key in seen:
                    continue
                seen.add(key)

                # 跳过模板、通配符、命令片段、URL、锚点
                if should_skip(ref):
                    continue
                if ref.startswith(("http://", "https://", "#", "../")):
                    continue

                resolved = resolve_ref(ref, source_dir)
                if resolved is None:
                    broken.append((f, ref))

    if broken:
        print(f"[BROKEN_REF] {len(broken)} broken references found:")
        for f, ref in sorted(broken):
            print(f"  {f.relative_to(BASE)} -> {ref}")
    else:
        print("No broken hard-coded references found.")


if __name__ == "__main__":
    main()
