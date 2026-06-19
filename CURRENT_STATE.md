# 当前项目状态

## 项目目标

这是一个面向**心理学考研复习**的个人知识库项目。核心目标是让 AI 成为复习助手——通过结构化卡片和语义检索，用户提问时 AI 能从知识库中精准找到相关内容并作答。

## 当前架构（2026-06-14）

```
psychology-knowledge-base/
├── 03-cards/                  ← 概念卡片（平铺，用 #学科/xxx 标签分类）
│   ├── 10-普通心理学/...      ← 13 个学科子目录（首页导航入口）
│   └── card-*.md              ← 41 张概念卡片
├── 04-index/
│   ├── concept-map.md
│   ├── tag-index.md
│   └── event-classification.md ← 社会事件分类手册（8 类型）
├── 05-observations/
│   ├── current-events/        ← 3 个文件（碳水脸 ×2, 明星塌房 ×1）
│   ├── personal-experiences/  ← 2 个文件
│   └── typical-cases/         ← 1 个文件（彩礼事件深度分析）
├── tools/
│   ├── auto_tag.py            ← 自动标签脚本（核心工具）
│   ├── import_md.py           ← 增量导入数据库
│   ├── semantic_search.py     ← 语义检索
│   └── ...
└── PROJECT_LOG.md
```

## 已完成

| 事项 | 状态 |
|---|---|
| 41 张概念卡片（含完整 YAML frontmatter） | ✅ |
| 增量同步导入脚本 (import_md.py) | ✅ |
| sqlite-vec 语义检索 | ✅ |
| Observations 模板与流程 | ✅ |
| Git 仓库 + GitHub 推送 | ✅ |
| 13 学科目录结构 | ✅ |
| 标签替代子目录（#学科/xxx, #事件类型/xxx） | ✅ |
| 自动标签脚本 (auto_tag.py) | ✅ |
| 社会事件分类手册整合 (event-classification.md) | ✅ |
| 删除 06-event-cards/，事件归入 05-observations | ✅ |

## 进行中 / 待处理

| 事项 | 优先级 |
|---|---|
| 13 个学科子目录写入首页导航卡片 | 中 |
| 5 张占位符卡片（彩礼事件卡片 11-15）填充 | 低 |
| Zotero 文献 + citekeys 字段填充 | 低 |
| 自动生成 tag-index.md 和 concept-map.md 的脚本 | 中 |
| 分析报告附录路径引用更新（仍引旧 06-event-cards/） | 低 |
| `03-cards/` 中 `card-*-2026.md` 事件卡迁移到 `05-observations/` | 低 |
| `02-summaries/` 模板和流程优化 | 远期 |
| sqlite-vec 语义搜索升级 | 远期 |

## 最近关键决策

- **标签 > 子目录**：一张卡多标签解决跨学科归属。Obsidian 标签面板原生支持嵌套标签筛选。
- **auto_tag.py 扫描策略**：概念卡片只看 YAML 字段；事件文件只看 YAML + 正文前 800 字，≥2 关键词命中才确认。
- **不合并 05 和 06**：05-observations 三子目录（current-events, personal-experiences, typical-cases），结构清晰。

## 日常使用流程

```
加新概念卡片 → 写 domain / tags → python tools/auto_tag.py --apply
加新事件     → 写 YAML + 正文   → python tools/auto_tag.py --apply
找内容       → Obsidian 标签面板点击筛选
```

---
*最后更新：2026-06-14*
