"""
Generic rule loader for multiple rule namespaces.

Rules are defined in tools/rules-registry.yaml. Each namespace has its own
base directory and alias map, keeping different rule sets isolated while
still allowing quick lookup by keyword.

Usage:
    python tools/load_rule.py --list
    python tools/load_rule.py research-partner stage-a
    python tools/load_rule.py memory-rules 规则维护
    python tools/load_rule.py --search 阶段

For backwards compatibility, a single alias argument defaults to the
"research-partner" namespace, matching the old behavior of this script.
"""
import argparse
import io
import sys
from pathlib import Path
from difflib import get_close_matches

# Force UTF-8 for stdout on Windows so Chinese aliases print correctly.
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

try:
    import yaml
except ImportError as e:  # pragma: no cover
    raise ImportError(
        "PyYAML is required to load rules-registry.yaml. "
        "Install it with: pip install pyyaml"
    ) from e


DEFAULT_NAMESPACE = "research-partner"
REGISTRY_PATH = Path(__file__).with_name("rules-registry.yaml")


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    """Load the rule registry from YAML."""
    if not path.exists():
        raise FileNotFoundError(f"Rule registry not found: {path}")
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def resolve_path(alias_value: str, base_dir: Path) -> Path:
    """Resolve an alias value to an absolute Path."""
    p = Path(alias_value)
    if p.is_absolute():
        return p
    return base_dir / p


def build_lookup_table(registry: dict) -> dict:
    """
    Build a flat lookup table:
        (namespace, alias) -> absolute Path
    Also collect all aliases for suggestion generation.
    """
    table = {}
    namespaces = registry.get("namespaces", {})
    for ns_name, ns_config in namespaces.items():
        base_dir = Path(ns_config.get("base_dir", ""))
        aliases = ns_config.get("aliases", {})
        for alias, value in aliases.items():
            table[(ns_name, alias)] = resolve_path(value, base_dir)
    return table


def collect_all_aliases(registry: dict) -> list:
    """Return a list of (namespace, alias) tuples."""
    aliases = []
    for ns_name, ns_config in registry.get("namespaces", {}).items():
        for alias in ns_config.get("aliases", {}).keys():
            aliases.append((ns_name, alias))
    return aliases


def list_rules(registry: dict) -> str:
    """Format all namespaces and aliases for --list."""
    lines = ["Available rule namespaces and aliases:\n"]
    for ns_name, ns_config in registry.get("namespaces", {}).items():
        description = ns_config.get("description", "")
        header = f"[{ns_name}]"
        if description:
            header += f" {description}"
        lines.append(header)

        aliases = ns_config.get("aliases", {})
        base_dir = Path(ns_config.get("base_dir", ""))
        grouped = {}
        for alias, value in aliases.items():
            path = resolve_path(value, base_dir)
            grouped.setdefault(str(path), []).append(alias)

        for path, alias_list in sorted(grouped.items()):
            alias_str = ", ".join(sorted(alias_list))
            lines.append(f"  {path}")
            lines.append(f"    aliases: {alias_str}")
        lines.append("")
    return "\n".join(lines)


def search_aliases(registry: dict, keyword: str) -> str:
    """Search aliases across all namespaces."""
    keyword = keyword.lower().strip()
    matches = []
    for ns_name, ns_config in registry.get("namespaces", {}).items():
        base_dir = Path(ns_config.get("base_dir", ""))
        for alias, value in ns_config.get("aliases", {}).items():
            if keyword in alias.lower() or keyword in value.lower():
                matches.append((ns_name, alias, resolve_path(value, base_dir)))

    if not matches:
        return f"No aliases matching '{keyword}'."

    lines = [f"Search results for '{keyword}':\n"]
    for ns_name, alias, path in sorted(matches, key=lambda x: (x[0], x[1])):
        lines.append(f"  {ns_name:<25} {alias:<20} -> {path}")
    return "\n".join(lines)


def suggest_aliases(registry: dict, target_ns: str, keyword: str) -> str:
    """Return a suggestion string for typos."""
    candidates = [
        alias
        for ns_name, alias in collect_all_aliases(registry)
        if ns_name == target_ns
    ]
    # Also include aliases from all namespaces if namespace itself is unknown.
    if not candidates:
        candidates = [alias for _, alias in collect_all_aliases(registry)]

    suggestions = get_close_matches(keyword.lower(), [a.lower() for a in candidates], n=5, cutoff=0.4)
    if suggestions:
        return f"Did you mean: {', '.join(suggestions)}"
    return "Run `python tools/load_rule.py --list` for all aliases."


def load_rule(registry: dict, namespace: str, alias: str) -> str:
    """Load the content of a rule file by namespace and alias."""
    namespaces = registry.get("namespaces", {})
    if namespace not in namespaces:
        available = ", ".join(sorted(namespaces.keys()))
        raise FileNotFoundError(
            f"Unknown namespace '{namespace}'.\n"
            f"Available namespaces: {available}"
        )

    ns_config = namespaces[namespace]
    aliases = ns_config.get("aliases", {})
    base_dir = Path(ns_config.get("base_dir", ""))

    # Try exact alias match.
    value = aliases.get(alias)
    if value is None:
        # Try case-insensitive match.
        for a, v in aliases.items():
            if a.lower() == alias.lower():
                value = v
                break

    if value is None:
        raise FileNotFoundError(
            f"No rule file matches '{alias}' in namespace '{namespace}'.\n"
            f"{suggest_aliases(registry, namespace, alias)}"
        )

    path = resolve_path(value, base_dir)
    if not path.exists():
        raise FileNotFoundError(
            f"Rule file registered but not found on disk: {path}\n"
            f"Check the registry path for alias '{alias}' in namespace '{namespace}'."
        )
    return path.read_text(encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Load rules by namespace and alias."
    )
    parser.add_argument(
        "keyword",
        nargs="?",
        help="Rule alias, or namespace when two positional args are given.",
    )
    parser.add_argument(
        "alias",
        nargs="?",
        help="Rule alias (when namespace is given as the first positional arg).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all namespaces and aliases",
    )
    parser.add_argument(
        "--search",
        metavar="KEYWORD",
        help="Search aliases across all namespaces",
    )
    args = parser.parse_args()

    registry = load_registry()

    if args.list:
        print(list_rules(registry))
        return

    if args.search:
        print(search_aliases(registry, args.search))
        return

    # Determine namespace / alias from positional args.
    if args.alias:
        namespace = args.keyword
        alias = args.alias
    elif args.keyword:
        # Backwards compatibility: single alias defaults to research-partner.
        namespace = DEFAULT_NAMESPACE
        alias = args.keyword
    else:
        parser.print_help()
        sys.exit(1)

    try:
        print(load_rule(registry, namespace, alias))
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
