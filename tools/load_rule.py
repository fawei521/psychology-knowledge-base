"""
Deterministic rule loader for the cross-disciplinary research partner mode.

This is the primary way to retrieve rules. It maps keywords/stages/topics to
exact files, avoiding the unpredictability of vector retrieval for structured
constraints.

Usage:
    python tools/load_rule.py stage-a
    python tools/load_rule.py role
    python tools/load_rule.py --list
"""
import argparse
import sys
from pathlib import Path

RULES_DIR = Path(r"E:\psychology-knowledge-base\00-prompts\rules")
CONSTITUTION = Path(r"E:\psychology-knowledge-base\00-prompts\research-partner-constitution.md")

# Map aliases to filenames. Multiple aliases can point to the same file.
ALIAS_MAP = {
    # Core files
    "constitution": CONSTITUTION,
    "宪法": CONSTITUTION,
    "core": CONSTITUTION,
    "meta": RULES_DIR / "meta.md",
    "前言": RULES_DIR / "meta.md",
    "元规则": RULES_DIR / "meta.md",
    "role": RULES_DIR / "role.md",
    "角色": RULES_DIR / "role.md",
    "workflow": RULES_DIR / "workflow.md",
    "工作流": RULES_DIR / "workflow.md",
    # Stages
    "stage-a": RULES_DIR / "stage-a.md",
    "阶段a": RULES_DIR / "stage-a.md",
    "事实锚定": RULES_DIR / "stage-a.md",
    "stage-b": RULES_DIR / "stage-b.md",
    "阶段b": RULES_DIR / "stage-b.md",
    "角度速览": RULES_DIR / "stage-b.md",
    "stage-c": RULES_DIR / "stage-c.md",
    "阶段c": RULES_DIR / "stage-c.md",
    "分轮深入": RULES_DIR / "stage-c.md",
    "stage-d": RULES_DIR / "stage-d.md",
    "阶段d": RULES_DIR / "stage-d.md",
    "卡片归档": RULES_DIR / "stage-d.md",
    # Other rule files
    "output": RULES_DIR / "output.md",
    "输出": RULES_DIR / "output.md",
    "commands": RULES_DIR / "commands.md",
    "指令": RULES_DIR / "commands.md",
    "交互指令": RULES_DIR / "commands.md",
    "scenarios": RULES_DIR / "scenarios.md",
    "场景": RULES_DIR / "scenarios.md",
    "traps": RULES_DIR / "traps.md",
    "陷阱": RULES_DIR / "traps.md",
    "card-template": RULES_DIR / "card-template.md",
    "卡片模板": RULES_DIR / "card-template.md",
    "testing": RULES_DIR / "testing.md",
    "测试": RULES_DIR / "testing.md",
    "theory-blacklist": RULES_DIR / "theory-blacklist.md",
    "理论禁用": RULES_DIR / "theory-blacklist.md",
    "source-template": RULES_DIR / "source-template.md",
    "信源": RULES_DIR / "source-template.md",
}


def list_rules():
    """Print all available rule aliases grouped by file."""
    by_file = {}
    for alias, path in ALIAS_MAP.items():
        by_file.setdefault(str(path), []).append(alias)
    print("Available rule aliases:\n")
    for path, aliases in sorted(by_file.items()):
        print(f"  {path}")
        print(f"    aliases: {', '.join(sorted(aliases))}\n")


def load_rule(keyword: str) -> str:
    keyword = keyword.lower().strip()
    path = ALIAS_MAP.get(keyword)
    if not path or not path.exists():
        suggestions = [a for a in ALIAS_MAP if keyword in a or a in keyword]
        raise FileNotFoundError(
            f"No rule file matches '{keyword}'.\n"
            f"Did you mean: {', '.join(suggestions[:5]) or '?' }\n"
            f"Run `python tools/load_rule.py --list` for all aliases."
        )
    return path.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Load research partner rules by keyword.")
    parser.add_argument("keyword", nargs="?", help="Rule alias, e.g. stage-a, role, meta")
    parser.add_argument("--list", action="store_true", help="List all available aliases")
    args = parser.parse_args()

    if args.list:
        list_rules()
        return

    if not args.keyword:
        parser.print_help()
        sys.exit(1)

    try:
        print(load_rule(args.keyword))
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
