#!/usr/bin/env python3
"""Sync external source directories into this backup repo and optionally push.

Usage:
    python tools/sync_backup.py         # sync only, do not commit/push
    python tools/sync_backup.py --push  # sync, commit, push, then clean copies

Safety rules:
- Only copies FROM source directories INTO this repo.
- Never deletes or modifies source directories.
- Cleanup only removes copied directories inside this repo.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


# Map: target dir inside repo -> source dir on disk
SYNC_MAP: dict[str, str] = {
    "memory": r"C:\Users\乏味\.claude\projects\C--Users---\memory",
    "me-me": r"E:\me me",
}

# Rename specific source subdirectories to a different target name.
# Key: source subdirectory name; Value: target subdirectory name.
RENAME_MAP: dict[str, str] = {
    "Twilight of the Day": "Twilight-of-the-Day",
}

# Files/dirs to ignore during copy. These patterns are passed to shutil.copytree
# via ignore=... and are in addition to .gitignore.
IGNORE_PATTERNS = {
    ".git",
    ".obsidian",
    "__pycache__",
    "*.pyc",
    "*.tmp.*",
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.gif",
    "*.webp",
    "*.mp4",
    "*.mov",
    "*.avi",
    "*.mp3",
}


def repo_root() -> Path:
    """Return the repository root (directory containing this script's parent)."""
    return Path(__file__).resolve().parent.parent


def ensure_source_exists(source: Path, name: str) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Source directory for '{name}' does not exist: {source}")
    if not source.is_dir():
        raise NotADirectoryError(f"Source path for '{name}' is not a directory: {source}")


def copy_latest(source: Path, target: Path) -> None:
    """Copy source directory contents into target directory.

    The target directory itself is created if needed. Existing files are
    overwritten; files removed from the source are NOT deleted from the target.
    This is intentional: the repo may contain additional .gitignored files that
    should not be wiped. Git's index will reflect deletions via `git add -A`.
    """
    target.mkdir(parents=True, exist_ok=True)

    def ignore_patterns(dirpath: str, names: list[str]) -> set[str]:
        ignored = set()
        for name in names:
            if name in IGNORE_PATTERNS:
                ignored.add(name)
                continue
            for ext in IGNORE_PATTERNS:
                if ext.startswith("*") and name.endswith(ext.lstrip("*")):
                    ignored.add(name)
                    break
        return ignored

    for item in source.iterdir():
        item_name = item.name
        target_name = RENAME_MAP.get(item_name, item_name)
        dest = target / target_name
        if item.is_dir():
            shutil.copytree(
                item,
                dest,
                dirs_exist_ok=True,
                ignore=ignore_patterns,
            )
        elif item.is_file():
            if item_name in IGNORE_PATTERNS or any(item_name.endswith(ext.lstrip("*")) for ext in IGNORE_PATTERNS if ext.startswith("*")):
                continue
            shutil.copy2(item, dest)


def git_status_clean(root: Path) -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    return result.returncode == 0 and not result.stdout.strip()


def git_add_commit_push(root: Path) -> None:
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)

    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if not status.stdout.strip():
        print("Nothing to commit.")
        return

    from datetime import datetime, timezone
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    commit_msg = f"Sync memory and me-me from source dirs ({timestamp})"

    subprocess.run(["git", "commit", "-m", commit_msg], cwd=root, check=True)
    subprocess.run(["git", "push"], cwd=root, check=True)
    print("Pushed to remote.")


def clean_copies(root: Path) -> None:
    """Remove the copied directories inside the repo.

    Safety check: every path must be a direct child of repo root AND listed in
    SYNC_MAP. This prevents accidental deletion of source files or unrelated
    directories.
    """
    for name in SYNC_MAP:
        target = root / name
        # Sanity: must be inside repo root and must exist
        if not target.exists():
            continue
        if target.resolve().parent != root.resolve():
            raise RuntimeError(f"Refusing to clean directory outside repo root: {target}")
        print(f"Cleaning copied directory: {target}")
        shutil.rmtree(target)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync sources into backup repo.")
    parser.add_argument(
        "--push",
        action="store_true",
        help="After syncing, commit and push.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help=(
            "After pushing, remove the copied memory/ and me-me/ directories "
            "from the repo working tree. WARNING: this will mark the files as "
            "deleted in Git on the next run; most users should leave this off."
        ),
    )
    args = parser.parse_args()

    if args.clean and not args.push:
        parser.error("--clean requires --push")

    root = repo_root()
    print(f"Repository root: {root}")

    # 1. Sync sources into repo
    for name, source_path in SYNC_MAP.items():
        source = Path(source_path)
        target = root / name
        print(f"\nSyncing '{name}':\n  from: {source}\n  to:   {target}")
        ensure_source_exists(source, name)
        copy_latest(source, target)
        print("  done.")

    if not args.push:
        print("\nSync complete. Use --push to commit and push.")
        return 0

    # 2. Commit and push
    print("\nCommitting and pushing...")
    git_add_commit_push(root)

    # 3. Optionally clean copied directories
    if args.clean:
        print("\nCleaning copied directories...")
        clean_copies(root)

    print("Done.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
