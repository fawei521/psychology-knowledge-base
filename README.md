# 个人知识库合集

本仓库聚合三类个人数字资产，统一备份到 GitHub。

## 目录结构

| 目录 | 内容 | 说明 |
|---|---|---|
| [`03-cards/`](03-cards/) | 心理学知识库 | 面向心理学考研复习的概念卡片、关系网络、数据库。 |
| [`memory/`](memory/) | Claude 记忆规则 | 跨会话复用的 AI 行为规则、触发地图、经验教训、项目索引。 |
| [`me-me/`](me-me/) | 个人作品/日记 | `moo/` 日记库、`Twilight-of-the-Day/` 个人写作与邮件存档。 |

## 主要入口

- 心理学知识库总纲：[`CLAUDE.md`](CLAUDE.md)
- 记忆规则总索引：[`memory/MEMORY.md`](memory/MEMORY.md)
- 日记库规则：[`me-me/moo/CLAUDE.md`](me-me/moo/CLAUDE.md)

## 备份原则

- 文本与 Markdown 是主要备份对象。
- 图片、原始导出文件、Obsidian 配置、Python 缓存不推送。
- 各子目录的原始大文件仍保留在本地，本仓库只保留可恢复的核心内容。

## 常用命令

```bash
cd /e/psychology-knowledge-base
python tools/sync_backup.py --push
python tools/import_md.py
python tools/auto_tag.py --apply
```

`tools/sync_backup.py --push` 会先把 `memory/` 和 `me-me/` 的源目录最新内容复制到本仓库，然后提交、推送到 GitHub，最后清理本仓库内的副本。
