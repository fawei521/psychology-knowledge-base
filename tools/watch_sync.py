#!/usr/bin/env python3
"""
自动同步 Markdown 修改到 kb.db

用法：
    python tools/watch_sync.py              # 启动时全量同步一次，然后轮询监控
    python tools/watch_sync.py --no-initial-sync  # 启动时不立即全量同步
    python tools/watch_sync.py --interval 3       # 每 3 秒轮询一次（默认 5 秒）

说明：
- 监控 01-raw/pdfs、01-raw/web-pages、02-summaries、03-cards、05-observations 下的 .md 文件
- 检测到文件 mtime 或 hash 变化后，等待 2 秒防抖（debounce），然后调用 import_md.py
- 日志同时输出到控制台和 tools/watch_sync.log
"""

import argparse
import hashlib
import subprocess
import sys
import time
from pathlib import Path

# Windows 下控制台默认可能是 GBK，确保中文和特殊字符能正常输出
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

BASE = Path(__file__).parent.parent
LOG_FILE = BASE / "tools" / "watch_sync.log"

WATCH_DIRS = [
    BASE / "01-raw" / "pdfs",
    BASE / "01-raw" / "web-pages",
    BASE / "02-summaries",
    BASE / "03-cards",
    BASE / "05-observations",
]

DEBOUNCE_SECONDS = 2.0


def log(msg):
    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def scan_files():
    """扫描所有监控目录下的 .md 文件，返回 {rel_path: (mtime, hash, abs_path)}"""
    files = {}
    for d in WATCH_DIRS:
        if not d.exists():
            continue
        for p in d.rglob("*.md"):
            if p.name.startswith("_") or p.name == "README.md":
                continue
            rel = str(p.relative_to(BASE))
            stat = p.stat()
            h = hashlib.sha256(p.read_bytes()).hexdigest()
            files[rel] = (stat.st_mtime, h, p)
    return files


def run_import():
    """调用 import_md.py 并记录输出"""
    log("运行 import_md.py ...")
    try:
        result = subprocess.run(
            [sys.executable, str(BASE / "tools" / "import_md.py")],
            cwd=BASE,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if result.returncode == 0:
            log("import_md.py 完成")
        else:
            log(f"import_md.py 出错，返回码 {result.returncode}")
        if result.stdout:
            for line in result.stdout.strip().split("\n"):
                log(f"  [OUT] {line}")
        if result.stderr:
            for line in result.stderr.strip().split("\n"):
                log(f"  [ERR] {line}")
    except Exception as e:
        log(f"运行 import_md.py 异常: {e}")


def main():
    parser = argparse.ArgumentParser(description="自动同步 Markdown 修改到 kb.db")
    parser.add_argument(
        "--no-initial-sync",
        action="store_true",
        help="启动时不立即全量同步一次",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=5,
        help="轮询间隔秒数（默认 5）",
    )
    args = parser.parse_args()

    log("=" * 50)
    log("watch_sync 启动")
    log(f"轮询间隔: {args.interval}s")

    if not args.no_initial_sync:
        run_import()

    last_state = scan_files()
    log(f"初始监控文件数: {len(last_state)}")

    # 防抖队列：rel_path -> 最早可以同步的时间戳
    pending = {}

    try:
        while True:
            time.sleep(args.interval)
            new_state = scan_files()

            # 检测新增或变更的文件
            changed = []
            for rel, (mtime, h, p) in new_state.items():
                if rel not in last_state:
                    changed.append(rel)
                else:
                    old_mtime, old_h, _ = last_state[rel]
                    if mtime != old_mtime or h != old_h:
                        changed.append(rel)

            # 检测删除的文件
            deleted = [rel for rel in last_state if rel not in new_state]

            for rel in changed:
                pending[rel] = time.time() + DEBOUNCE_SECONDS
                log(f"检测到变化: {rel}")

            for rel in deleted:
                pending[rel] = time.time() + DEBOUNCE_SECONDS
                log(f"检测到删除: {rel}")

            now = time.time()
            ready = [rel for rel, t in pending.items() if t <= now]
            if ready:
                log(f"准备同步 {len(ready)} 个文件...")
                run_import()
                pending.clear()
                # 同步完成后重新扫描，避免同步期间的变化被漏掉或重复触发
                last_state = scan_files()
            else:
                last_state = new_state

    except KeyboardInterrupt:
        log("收到中断信号，退出 watch_sync")


if __name__ == "__main__":
    main()
