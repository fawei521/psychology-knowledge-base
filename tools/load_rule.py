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
import re
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


def load_global_aliases(registry: dict) -> dict[str, str | tuple[str, str]]:
    """Load global_aliases section from registry.

    Values can be:
      - an absolute path string (e.g. "E:/.../CLAUDE.md")
      - a namespace/alias reference in the form "namespace/alias"
    """
    return registry.get("global_aliases", {}) or {}


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
    """Return a list of (namespace, alias) tuples, including global aliases."""
    aliases = []
    for ns_name, ns_config in registry.get("namespaces", {}).items():
        for alias in ns_config.get("aliases", {}).keys():
            aliases.append((ns_name, alias))
    for alias in load_global_aliases(registry).keys():
        aliases.append(("global", alias))
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
    """Search aliases across all namespaces and global aliases."""
    keyword = keyword.lower().strip()
    matches = []
    for ns_name, ns_config in registry.get("namespaces", {}).items():
        base_dir = Path(ns_config.get("base_dir", ""))
        for alias, value in ns_config.get("aliases", {}).items():
            if keyword in alias.lower() or keyword in value.lower():
                matches.append((ns_name, alias, resolve_path(value, base_dir)))

    global_aliases = load_global_aliases(registry)
    for alias, value in global_aliases.items():
        resolved = resolve_global_alias(registry, alias)
        if isinstance(resolved, tuple):
            matches.append((resolved[0], f"🌐 {alias}", Path(value)))
        elif isinstance(resolved, Path):
            matches.append(("global", f"🌐 {alias}", resolved))

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


def _collect_registered_paths(registry: dict) -> tuple[set[str], set[str]]:
    """Return (absolute_paths, filenames) for all registered files."""
    abs_paths: set[str] = set()
    filenames: set[str] = set()
    for ns_config in registry.get("namespaces", {}).values():
        base_dir = Path(ns_config.get("base_dir", ""))
        for value in ns_config.get("aliases", {}).values():
            path = resolve_path(value, base_dir)
            if path.exists():
                abs_paths.add(str(path.resolve()))
                filenames.add(path.name)
    return abs_paths, filenames


def _resolve_ref(ref: str, source: Path, project_root: Path) -> Path | None:
    """Try multiple resolution strategies for a reference string."""
    ref = ref.strip().strip('"\'').replace("\\", "/")
    if not ref or any(
        ref.lower().startswith(p) for p in ("http://", "https://", "#", "mailto:", "data:")
    ):
        return None

    # Absolute Windows path E:/... or E:\...
    if len(ref) >= 2 and ref[1] == ":":
        p = Path(ref)
        return p if p.exists() else None

    candidates: list[Path] = []

    # Relative to project root (e.g. rules/output.md, 04-index/spec-card.md)
    if "/" in ref:
        candidates.append(project_root / ref)

    # Relative to source file directory (e.g. card-template.md in rules/stage-d.md)
    candidates.append(source.parent / ref)

    # Known parent directories relative to project root
    for parent in ("00-prompts", "00-prompts/rules", "04-index", "04-index/startup", "meta", "tools"):
        candidates.append(project_root / parent / ref)

    for candidate in candidates:
        try:
            if candidate.exists():
                return candidate
        except OSError:
            continue
    return None


def check_hardcoded_refs(registry: dict) -> list[str]:
    """Scan research-partner rules for broken hardcoded cross-references.

    These rules live under 00-prompts/rules/ and frequently reference each
    other with paths like `rules/output.md` or `card-template.md`. Moving or
    renaming a rule file silently breaks these references, so we verify them.
    """
    project_root = REGISTRY_PATH.parent.parent
    registered_paths, _ = _collect_registered_paths(registry)

    # Only check the research-partner namespace for now; other namespaces
    # use too many example/placeholder/external references that create noise.
    ns_config = registry.get("namespaces", {}).get("research-partner")
    if not ns_config:
        return []

    base_dir = Path(ns_config.get("base_dir", ""))
    aliases = ns_config.get("aliases", {})

    ref_patterns = [
        (re.compile(r"`([^`]*\.(?:md|py))`"), 1),
    ]

    issues: list[str] = []
    seen: set[tuple[str, str]] = set()

    for alias, value in aliases.items():
        path = resolve_path(value, base_dir)
        if not path.exists() or not path.is_file() or path.suffix != ".md":
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue

        found_refs: set[str] = set()
        for pattern, group in ref_patterns:
            for match in pattern.finditer(text):
                ref = match.group(group).strip()
                if not ref:
                    continue
                # Skip examples, globs, placeholders, commands, URLs.
                if any(c in ref for c in "*{}<>"):
                    continue
                if ref.lower().startswith(("python", "pythonw", "grep", "http://", "https://")):
                    continue
                if ref in (".md", ".py"):
                    continue
                found_refs.add(ref)

        for ref in found_refs:
            key = (str(path), ref)
            if key in seen:
                continue
            seen.add(key)

            resolved = _resolve_ref(ref, path, project_root)
            if resolved is None:
                issues.append(f"[BROKEN_REF] [research-partner] {path.name} -> '{ref}'")
            elif str(resolved.resolve()) not in registered_paths:
                issues.append(
                    f"[UNREGISTERED_REF] [research-partner] {path.name} -> '{ref}' ({resolved})"
                )

    return issues


def verify_registry(registry: dict) -> str:
    """Check registry integrity and return a human-readable report."""
    lines: list[str] = []
    namespaces = registry.get("namespaces", {})

    # Per-namespace checks.
    for ns_name, ns_config in namespaces.items():
        base_dir = Path(ns_config.get("base_dir", ""))
        aliases = ns_config.get("aliases", {})
        is_external = ns_config.get("external", False)

        if not base_dir.exists():
            lines.append(f"[MISSING_BASE_DIR] [{ns_name}] {base_dir}")
            continue

        registered_paths: set[str] = set()

        # 1. Registered aliases must exist and be non-empty.
        for alias, value in aliases.items():
            path = resolve_path(value, base_dir)
            abs_path = str(path.resolve()) if path.exists() else str(path)
            registered_paths.add(abs_path)
            if not path.exists():
                lines.append(f"[MISSING] [{ns_name}] {alias} -> {path}")
            elif path.stat().st_size == 0:
                lines.append(f"[EMPTY] [{ns_name}] {alias} -> {path}")

        # 2. Constitution file, if present, must exist.
        constitution = ns_config.get("constitution")
        if constitution:
            path = resolve_path(constitution, base_dir)
            registered_paths.add(str(path.resolve()) if path.exists() else str(path))
            if not path.exists():
                lines.append(f"[MISSING_CONSTITUTION] [{ns_name}] -> {path}")

        # 3. Scan base_dir for unregistered .md / .py files (skip external namespaces).
        if not is_external and base_dir.is_dir():
            for f in base_dir.iterdir():
                if f.is_file() and f.suffix in (".md", ".py"):
                    f_abs = str(f.resolve())
                    if f_abs not in registered_paths:
                        lines.append(f"[UNREGISTERED] [{ns_name}] {f.name}")

    # Cross-namespace alias conflicts.
    alias_to_namespaces: dict[str, list[str]] = {}
    for ns_name, ns_config in namespaces.items():
        for alias in ns_config.get("aliases", {}).keys():
            alias_to_namespaces.setdefault(alias, []).append(ns_name)

    for alias, ns_list in sorted(alias_to_namespaces.items()):
        if len(ns_list) > 1:
            lines.append(f"[DUPLICATE_ALIAS] '{alias}' in: {', '.join(sorted(ns_list))}")

    # Duplicate paths within the same namespace (informational: multi-language aliases).
    for ns_name, ns_config in namespaces.items():
        base_dir = Path(ns_config.get("base_dir", ""))
        path_to_aliases: dict[str, list[str]] = {}
        for alias, value in ns_config.get("aliases", {}).items():
            path = str(resolve_path(value, base_dir).resolve())
            path_to_aliases.setdefault(path, []).append(alias)
        for path, alias_list in sorted(path_to_aliases.items()):
            if len(alias_list) > 1:
                lines.append(
                    f"[INFO] [{ns_name}] {path} <- {', '.join(sorted(alias_list))}"
                )

    # Hardcoded reference checks between rule files.
    ref_issues = check_hardcoded_refs(registry)
    lines.extend(ref_issues)

    if lines:
        return "\n".join(lines)
    return "All checks passed."


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


def resolve_global_alias(registry: dict, keyword: str) -> tuple[str, str] | Path | None:
    """
    Resolve a single-keyword global alias.

    Returns:
      - (namespace, alias) tuple if value is namespace/alias form
      - absolute Path if value is an absolute file path
      - None if no global alias matches
    """
    global_aliases = load_global_aliases(registry)
    value = global_aliases.get(keyword)
    if value is None:
        # Case-insensitive fallback.
        lowered = keyword.lower()
        for a, v in global_aliases.items():
            if a.lower() == lowered:
                value = v
                break

    if value is None:
        return None

    if isinstance(value, str) and "/" in value and not Path(value).is_absolute():
        parts = value.split("/", 1)
        if len(parts) == 2 and parts[0] and parts[1]:
            return (parts[0], parts[1])

    path = Path(value)
    if path.is_absolute():
        return path

    # Relative paths are resolved against the project root (registry parent).
    return REGISTRY_PATH.parent / value


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
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify registry integrity (missing/unregistered/duplicate/broken-ref checks)",
    )
    args = parser.parse_args()

    registry = load_registry()

    if args.list:
        print(list_rules(registry))
        return

    if args.search:
        print(search_aliases(registry, args.search))
        return

    if args.verify:
        print(verify_registry(registry))
        return

    # Determine namespace / alias from positional args.
    if args.alias:
        namespace = args.keyword
        alias = args.alias
    elif args.keyword:
        # Single argument: try global aliases first, then fall back to
        # backwards-compatible research-partner default.
        resolved = resolve_global_alias(registry, args.keyword)
        if isinstance(resolved, tuple):
            namespace, alias = resolved
        elif isinstance(resolved, Path):
            if not resolved.exists():
                print(f"Global alias resolved but file not found: {resolved}", file=sys.stderr)
                sys.exit(1)
            print(resolved.read_text(encoding="utf-8"))
            return
        else:
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
