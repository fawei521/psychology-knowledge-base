# tools/ 脚本索引

本目录存放心理学知识库的辅助脚本。分为「当前使用」和「历史保留」两类。

## 当前使用脚本

| 脚本 | 用途 | 常用命令 | 备注 |
|------|------|---------|------|
| `import_md.py` | 同步 Markdown → SQLite | `python tools/import_md.py` | 增量同步，基于 mtime + hash |
| `watch_sync.py` | 自动监控 .md 变化并调用 `import_md.py` | `python tools/watch_sync.py` | 2 秒防抖，日志写入 `tools/watch_sync.log` |
| `auto_tag.py` | 自动补全学科/事件标签 | `python tools/auto_tag.py`（预览）；`--apply`（写入） | 先预览再写入 |
| `db_init.py` | 初始化数据库 | `python tools/db_init.py` | 会清空数据库，谨慎使用 |
| `query.py` | 命令行查询数据库 | `python tools/query.py "SQL语句"` | 快速查 `entities`/`relations` |
| `semantic_search.py` | 语义搜索 | `python tools/semantic_search.py "查询文本"` | 基于 384 维向量 |
| `reindex_vectors.py` | 重建向量索引 | `python tools/reindex_vectors.py` | 向量异常时重跑 |
| `load_rule.py` | 加载规则文件（多规则集通用） | `python tools/load_rule.py --list` | 基于 `rules-registry.yaml`，支持 namespace + 别名 |

## 新增/修改脚本时的同步清单

新增、删除、重命名脚本，或改变脚本的常用命令时，必须同步更新以下三处，否则索引会再次脱节：

1. **本文件（`tools/README.md`）** — 更新脚本清单、用途、常用命令、备注。
2. **`04-index/spec-tools.md`** — 更新脚本清单和约定说明；如果脚本是新类型，补充使用规范。
3. **`tools/rules-registry.yaml`** — 在 `kb-tools` namespace 下新增/删除/重命名别名，保持中英文别名可用。

如果脚本触发的是全局钩子或影响记忆库加载链，还需同步更新：
- 对应的 `memory/*.md` 入口文件
- `MEMORY.md` 总索引（若该文件需要在对话中被 AI 自动加载）

## 历史保留脚本

以下脚本不再主动使用，但保留在仓库中供参考或必要时手动调用。

| 脚本 | 原用途 | 保留原因 | 使用注意 |
|------|--------|---------|---------|
| `rewrite_cards.py` | 批量重写卡片内容 | 历史工具，可能有特定批量替换场景 | 修改前先备份，仔细阅读参数 |
| `split_rules.py` | 拆分规则文件 | 研究搭档模式规则管理历史工具 | 仅在规则文件结构大改时考虑使用 |

## 子目录

| 目录 | 说明 |
|------|------|
| `weread-exporter/` | 微信读书导出工具（独立 git 仓库，已加入 `.gitignore`） |
| `__pycache__/` | Python 缓存，无需关心 |

## 使用原则

1. **先预览再执行**：尤其 `auto_tag.py`，不带 `--apply` 先看效果。
2. **批量操作前先 commit**：涉及 >5 个文件的改动，先打 git checkpoint。
3. **绝对路径优先**：Bash 命令前先 `cd /e/psychology-knowledge-base`，或用绝对路径。
4. **历史脚本谨慎使用**：`rewrite_cards.py` 和 `split_rules.py` 使用前务必备份。

## 与 `04-index/spec-tools.md` 的关系

- `spec-tools.md` 是**规范**，说明什么时候用哪个脚本、有什么约定。
- `tools/README.md` 是**目录索引**，快速查看脚本清单和状态。
- 两者应保持同步：新增/删除脚本时同时更新两个文件。
