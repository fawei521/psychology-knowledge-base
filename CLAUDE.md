# CLAUDE.md

> 心理学知识库 · 项目总纲。本文件每次进入项目目录自动加载。
> 技术规范不写在这里——见 `04-index/spec-*.md`，按任务触发。

---

## 这是什么

一个面向心理学考研复习的个人知识库。把教材概念、社会事件、个人经验整理成可检索的卡片和分析。

---

## 核心原则

1. **Markdown 是唯一真相源**。数据库（kb.db）由 Markdown 生成，可随时删除重建。
2. **概念卡片是核心资产**。每张卡片 = 一个心理学概念，格式统一、可独立检索。
3. **先去知识库里找答案**。回答心理学问题前，先查 kb.db 或翻 `03-cards/`，不要凭记忆编。
4. **改前 commit，改后同步**。批量修改前先 `git commit` 做安全网；改完 Markdown 后跑 `python tools/import_md.py` 同步数据库。
5. **模式要显式确认**。进入/退出任何模式时，必须告知用户"已加载 X 和 Y"。

---

## 目录一览

```
psychology-knowledge-base/
├── CLAUDE.md          ← 本文件
├── 01-raw/            ← 原始材料（只存不检索）
│   ├── pdfs/
│   └── web-pages/
├── 02-summaries/      ← 结构化摘要
├── 03-cards/          ← 概念卡片（核心资产）
│   └── {学科编号}-{学科名}/   ← 按学科分子目录，如 10-普通心理学、20-社会心理学
├── 04-index/          ← 索引文件 + 技术规范（spec-*.md，按需触发）
│   ├── concept-map.md         ← 概念关系总图
│   ├── tag-index.md           ← 标签索引目录
│   ├── event-classification.md ← 事件分类手册
│   └── spec-*.md              ← 各任务规范
├── 05-observations/   ← 事件/经验/案例
│   ├── personal-experiences/
│   ├── typical-cases/
│   └── current-events/
├── tools/             ← 脚本工具
├── meta/              ← 模式约定
├── 00-prompts/        ← 子模式规则
├── .obsidian/         ← Obsidian 库配置
├── kb.db              ← SQLite 数据库（可重建）
├── project-logs/      ← 项目日志归档（按日期）
├── PROJECT_LOG.md     ← 项目日志索引
└── CURRENT_STATE.md   ← 当前状态 + 待办
```

---

## 读取规则

> **总则**：日常回答心理学问题 → 直接查 kb.db 或翻 `03-cards/`，**不读任何 spec 文件**。

| 用户任务 | 读取文件 |
|---------|---------|
| 写/改概念卡片 | `04-index/spec-card.md` |
| 批量填充知识库/为主题填充理论卡片 | `04-index/spec-kb-fill-workflow.md` |
| 写/改事件/经验/案例 | `04-index/spec-observation.md` |
| 同步数据库、归档 | `04-index/spec-archive.md` |
| 跑脚本、改工具 | `04-index/spec-tools.md` |
| 更新概念图/标签索引 | `04-index/spec-index.md` |
| 阶段性完成后自查 | `04-index/spec-maintenance.md` |
| 开启专家模式 | `meta/psychology-expert-mode.md` |
| 开启研究搭档模式 | `meta/psychology-expert-mode.md` → `00-prompts/research-partner-constitution.md` |
[心理学知识库保存验证钩子](psychology-kb-verify-hook.md) — 自动触发、生效条件与配置位置
---

```
回答问题（查 kb.db / 03-cards）
   ↓
添加内容（写 Markdown → 01~05 对应目录）
   ↓
打标签（python tools/auto_tag.py --apply）
   ↓
同步数据库（python tools/import_md.py）
   ↓
收尾（更新索引 + PROJECT_LOG + git commit）
```

---

## 版本

- v0.2（2026-06-15）：精简为总纲。技术规范移至 `04-index/spec-*.md`；新增读取规则表。
- v0.3（2026-06-15）：`index.md` 拆分为 6 个独立 spec 文件放入 `04-index/`，按任务精确触发。
- v0.1（2026-06-12）：初版，混合技术规范与流程。
