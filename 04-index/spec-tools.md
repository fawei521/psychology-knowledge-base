# spec-tools.md — 工具脚本规范

> **触发条件**：用户要跑脚本、改工具、写新脚本
> 本文件独立自足，不需要跨文件引用。

---

## 脚本清单

| 脚本 | 用途 | 用法 |
|------|------|------|
| `import_md.py` | 同步 Markdown → SQLite | `python tools/import_md.py` |
| `auto_tag.py` | 自动补全标签 | `python tools/auto_tag.py`（预览）；`--apply`（写入） |
| `db_init.py` | 初始化数据库 | `python tools/db_init.py` |
| `query.py` | 命令行查询数据库 | `python tools/query.py "SQL语句"` |
| `semantic_search.py` | 语义搜索（384 维向量） | `python tools/semantic_search.py "查询文本"` |
| `reindex_vectors.py` | 重建向量索引 | `python tools/reindex_vectors.py` |
| `load_rule.py` | 加载研究搭档规则文件 | `python tools/load_rule.py <别名>` |
| `rewrite_cards.py` | 批量重写卡片 | 历史脚本，谨慎使用 |
| `split_rules.py` | 拆分规则文件 | 历史脚本，谨慎使用 |

## 脚本约定

- **先预览再执行**：`auto_tag.py` 不带 `--apply` 先看效果，确认后再写入
- **绝对路径**：Bash 命令前先 `cd /e/psychology-knowledge-base`，或使用绝对路径
- **PowerShell 不要内联**：复杂 PowerShell 先 `Write` 到 `.ps1` 文件，再用 `pwsh -File` 执行
- **批量操作前先 git commit**：涉及 >5 个文件的改动，先打 checkpoint

## auto_tag.py 行为

| 文件类型 | 匹配范围 | 对照表 | 阈值 |
|---------|---------|-------|------|
| `03-cards/` | YAML 的 `domain` + `tags` + `concept` 字段 | 13 学科关键词表 | 1 命中即可 |
| `05-observations/` | YAML + 正文前 800 字 | 8 种事件类型关键词表 | ≥2 命中确认 |
