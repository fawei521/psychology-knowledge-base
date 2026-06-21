# spec-archive.md — 归档与同步规范

> **触发条件**：用户要同步数据库、批量导入、重建数据库
> 本文件独立自足，不需要跨文件引用。

---

## 目录结构详情

```
psychology-knowledge-base/
├── 01-raw/              ← 原始材料（PDF、网页存档）。只存不检索，作为原始备份
│   ├── pdfs/
│   └── web-pages/
├── 02-summaries/        ← 结构化摘要。从 raw 材料提取，含关键发现/方法/涉及概念
├── 03-cards/            ← 概念卡片。核心资产，每张一个概念，格式统一
├── 04-index/            ← 索引文件 + 技术规范（概念图、标签索引、spec-*.md）
├── 05-observations/     ← 事件/经验/案例
│   ├── personal-experiences/
│   ├── typical-cases/
│   └── current-events/
├── tools/               ← 脚本工具（见 spec-tools.md）
├── meta/                ← 模式约定
├── 00-prompts/          ← 子模式规则
├── kb.db                ← SQLite 数据库（由 Markdown 生成，可删除重建）
├── CLAUDE.md            ← 项目总纲
├── project-logs/      ← 项目日志归档（按日期）
├── PROJECT_LOG.md     ← 项目日志索引
└── CURRENT_STATE.md     ← 当前状态 + 待办
```

## 同步数据库

```bash
cd /e/psychology-knowledge-base
python tools/import_md.py
```

- **增量同步**：对比文件 mtime + hash，只处理新增/修改/删除
- 不会每次全量重建
- 数据库可随时删除，重新跑 `import_md.py` 即可重建

## 摘要文件模板（`02-summaries/`）

```yaml
---
title: "论文/资料标题"
authors: ["作者1", "作者2"]
year: 2024
source: "期刊名或网址"
type: "summary"                    # summary / review / book-chapter
tags: ["tag1", "tag2"]
methods: ["RCT", "n=120", "fMRI"]
key_findings: ["发现1", "发现2"]
concepts: ["概念A", "概念B"]
relations:
  - target: "concept_a"              # 使用目标卡片的 concept 字段值，不要带 card- 前缀
    type: "supports"
---
```

## 文件命名规则

| 类型 | 格式 | 示例 |
|------|------|------|
| 摘要 | `summary-{主题}-{年份}-{来源}.md` | `summary-stroop-1935-original.md` |
| 卡片 | `card-{english_concept}.md` | `card-cognitive_dissonance.md` |
| 观察 | `obs-{类型}-{日期}-{简短标题}.md` | `obs-ce-2026-06-15-彩礼事件.md` |
| 多词 | 下划线 `_` 连接 | |
