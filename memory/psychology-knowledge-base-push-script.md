---
name: psychology-knowledge-base-push-script
description: 推送到 psychology-knowledge-base 仓库时必须使用 sync_backup.py 脚本
metadata: 
  node_type: memory
  type: project
  originSessionId: b9f979a2-8324-49cb-87e6-facd5e002ce8
---

推送到 `E:\psychology-knowledge-base` GitHub 仓库时，统一使用脚本 `tools/sync_backup.py`，不要手动 `git add/commit/push`。

标准命令：

```bash
cd /e/psychology-knowledge-base
python tools/sync_backup.py --push
```

脚本行为：
- 复制 `C:\Users\乏味\.claude\projects\C--Users---\memory` → `E:\psychology-knowledge-base\memory`
- 复制 `E:\me me` → `E:\psychology-knowledge-base\me-me`（`Twilight of the Day` 重命名为 `Twilight-of-the-Day`）
- 排除 `原文件`、`原始备份` 目录以及图片/视频/音频文件
- `git add -A`、`git commit`、`git push`
- 默认保留仓库内的 `memory/` 和 `me-me/` 副本，不自动清理

清理副本是可选的：`python tools/sync_backup.py --push --clean`（不推荐，因为 Git 会把这些文件标记为删除）。

**触发关键词**：用户说"推送 psychology-knowledge-base"、"推送到 GitHub"、"备份 memory 和 me-me"、"同步备份"等，都执行本脚本。

**规则加载器别名**：`kb-tools/sync-backup`（即 `tools/sync_backup.py`）。

**Why:** 手动推送容易遗漏 memory/me-me 的更新，或者误把原始备份/图片推上去。脚本保证只推送核心文本内容，且源目录和仓库副本不会搞混。

**How to apply:** 只要用户提到"推送 psychology-knowledge-base"、"推送到 GitHub"、"备份 memory 和 me-me"等，就执行上述脚本命令。
