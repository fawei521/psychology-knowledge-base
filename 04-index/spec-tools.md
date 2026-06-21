# spec-tools.md — 工具脚本规范

> **触发条件**：用户要跑脚本、改工具、写新脚本
> 本文件独立自足，不需要跨文件引用。
> 完整脚本清单与状态索引见 [`tools/README.md`](../tools/README.md)。

---

## 脚本清单

| 脚本 | 用途 | 用法 |
|------|------|------|
| `import_md.py` | 同步 Markdown → SQLite | `python tools/import_md.py` |
| `watch_sync.py` | 自动监控 .md 变化并调用 `import_md.py` | `python tools/watch_sync.py` |
| `auto_tag.py` | 自动补全标签 | `python tools/auto_tag.py`（预览）；`--apply`（写入） |
| `db_init.py` | 初始化数据库 | `python tools/db_init.py` |
| `query.py` | 命令行查询数据库 | `python tools/query.py "SQL语句"` |
| `semantic_search.py` | 语义搜索（384 维向量） | `python tools/semantic_search.py "查询文本"` |
| `reindex_vectors.py` | 重建向量索引 | `python tools/reindex_vectors.py` |
| `generate_concept_map.py` | 从卡片 `relations` 生成概念关系图 | `python tools/generate_concept_map.py`（预览）；`--apply`（写入） |
| `load_rule.py` | 加载规则文件（多规则集通用） | `python tools/load_rule.py --list`<br>`python tools/load_rule.py --verify` |
| `check_rule_refs.py` | 扫描规则文件中的硬编码引用 | `python tools/check_rule_refs.py`（实验性） |
| `rewrite_cards.py` | 批量重写卡片 | 历史脚本，谨慎使用 |
| `split_rules.py` | 拆分规则文件 | 历史脚本，谨慎使用 |

## 注册表完整性检查

`load_rule.py --verify` 用于审计 `tools/rules-registry.yaml` 与实际文件的一致性，建议在以下场景运行：

- 新增、删除、重命名规则文件或脚本后
- 修改 namespace 的 `base_dir` 后
- 批量维护后发现 `load_rule.py` 加载异常

检查项包括：注册文件是否缺失、base_dir 下是否有未注册文件、别名是否跨 namespace 冲突。

## 新增/修改脚本时的同步清单

新增、删除、重命名脚本，或改变脚本的常用命令时，必须同步更新以下三处：

1. **`tools/README.md`** — 更新脚本清单、用途、常用命令、备注。
2. **本文件（`04-index/spec-tools.md`）** — 更新脚本清单和约定说明。
3. **`tools/rules-registry.yaml`** — 在 `kb-tools` namespace 下新增/删除/重命名别名。

## 脚本约定

- **先预览再执行**：`auto_tag.py` 不带 `--apply` 先看效果，确认后再写入
- **绝对路径**：Bash 命令前先 `cd /e/psychology-knowledge-base`，或使用绝对路径
- **PowerShell 不要内联**：复杂 PowerShell 先 `Write` 到 `.ps1` 文件，再用 `pwsh -File` 执行
- **批量操作前先 git commit**：涉及 >5 个文件的改动，先打 checkpoint

## watch_sync.py 行为

- 启动时默认先跑一次全量同步（`import_md.py`），可用 `--no-initial-sync` 跳过。
- 轮询监控以下目录的 `.md` 文件：
  - `01-raw/pdfs/`
  - `01-raw/web-pages/`
  - `02-summaries/`
  - `03-cards/`
  - `05-observations/`
- 检测到文件 `mtime` 或 `hash` 变化后，等待 **2 秒防抖（debounce）**，然后调用 `import_md.py`。
- 日志同时输出到控制台和 `tools/watch_sync.log`。

### 使用方式

```bash
# 前台运行（适合临时开启，Ctrl+C 停止）
python tools/watch_sync.py

# 后台运行（当前终端不退出）
python tools/watch_sync.py &

# 只监控，启动时不全量同步
python tools/watch_sync.py --no-initial-sync

# 每 3 秒轮询一次
python tools/watch_sync.py --interval 3
```

### 注意事项

- `watch_sync.py` **只调用 `import_md.py`**，不会自动运行 `auto_tag.py`，避免标签脚本修改文件导致循环触发。
- 如果 embedding 模型加载较慢，首次同步可能需要几十秒，后续增量同步通常很快。
- Windows 下如需长期后台运行，建议使用 `pythonw.exe tools/watch_sync.py`（无控制台窗口），或配置为系统服务/计划任务。

## auto_tag.py 行为

| 文件类型 | 匹配范围 | 对照表 | 阈值 |
|---------|---------|-------|------|
| `03-cards/` | YAML 的 `domain` + `tags` + `concept` 字段 | 13 学科关键词表 | 1 命中即可 |
| `05-observations/` | YAML + 正文前 800 字 | 8 种事件类型关键词表 | ≥2 命中确认 |

### 已知问题（已修复）

- ~~`auto_tag.py` 会在文件末尾追加新的 `tags:` 字段，导致 frontmatter 重复。~~
- 当前版本 `patch_tags()` 已改为合并已有 tags 并覆盖写回 frontmatter，支持 inline 和 list 两种格式。运行后仍建议用 `grep -n "^tags:" 03-cards/card-*.md` 抽查。
