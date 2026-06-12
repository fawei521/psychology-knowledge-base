# CLAUDE.md v0.1

> 本项目是面向心理学考研复习的个人知识库。
> 本文档规定 AI 处理该知识库时的核心规则。
> 规则分"稳定"和"临时"：稳定规则尽量不改，临时规则可以迭代。

---

## 项目目标

1. 把心理学教材中的概念、理论、实验整理成可检索的卡片。
2. 存储个人经验与社会热点事件，并用心理学理论进行多视角分析。
3. 让用户通过自然语言提问，AI 从知识库中检索并作答。

---

## 目录结构（稳定）

```
psychology-knowledge-base/
├── 01-raw/              # 原始材料：论文、文章、视频稿、读书笔记
├── 02-summaries/        # 结构化摘要：AI 从 raw 材料中提取
├── 03-cards/            # 原子化概念卡片
├── 04-index/            # 索引：概念图、标签索引
├── 05-observations/     # 个人经验、典型案例、时事分析
├── tools/               # 数据库同步与查询脚本
├── kb.db                # SQLite 数据库（由 Markdown 生成，可重建）
├── CLAUDE.md            # 本文件
├── PROJECT_LOG.md       # 项目周报与关键节点记录
└── CURRENT_STATE.md     # 当前状态与 TODO
```

---

## 文件命名规则（稳定）

- 摘要：`summary-{主题}-{年份}-{来源}.md`
- 概念卡片：`card-{english_concept}.md`
- 观察/经验/案例：`obs-{类型}-{日期}-{简短标题}.md`
- 多词用下划线 `_` 连接

---

## 概念卡片 frontmatter（稳定）

每个概念卡片必须包含以下 frontmatter：

```yaml
---
concept: english_concept_name
concept_cn: 中文概念名
domain: general_psychology   # 或 social_psychology 等
tags: [tag1, tag2, tag3]
---
```

说明：
- `concept`：英文概念名，唯一标识，用作文件名。
- `concept_cn`：中文概念名，用于检索和展示。
- `domain`：所属学科领域，目前使用 `general_psychology` 或 `social_psychology`。
- `tags`：主题标签，帮助分类和检索。

---

## 观察类文件 frontmatter（稳定）

```yaml
---
observation_type: personal_experience   # personal_experience / typical_case / current_event
title: 简短标题
event_date: 2026-06-12
context: 事件发生的情境
behavior: 观察到的行为或反应
tags: [tag1, tag2]
related_entities: [english_concept_1, english_concept_2]
---
```

---

## AI 处理流程（稳定）

1. **读取 `CLAUDE.md` 和 `CURRENT_STATE.md`**：了解项目当前状态和规则。
2. **回答用户问题时**：优先查询 `kb.db`，必要时读取 `03-cards/` 和 `05-observations/` 中的 Markdown 源文件。
3. **添加新材料时**：
   - 原始材料 → `01-raw/`
   - 提取摘要 → `02-summaries/`
   - 拆出概念 → `03-cards/`
   - 个人经验/热点 → `05-observations/`
   - 更新索引 → `04-index/`
4. **同步数据库**：修改 Markdown 后，运行 `python tools/import_md.py` 同步到 `kb.db`。
5. **更新日志**：关键工作后更新 `PROJECT_LOG.md` 和 `CURRENT_STATE.md`。

---

## 临时规则（可迭代）

以下规则当前建议这样做，但未来可能调整：

- 摘要长度控制在 300-800 字。
- 每个概念卡片建议 3-8 个 tags。
- 分析事件时建议提供 2-4 个理论视角。
- 不硬编码复杂关系网，优先用 `domain` + `tags` + 语义检索。
- **测试策略**：不写正式测试套件，关键功能改完后手动跑一遍验证。

### Observations 正文结构（临时）

观察/经验/案例类文件建议包含以下章节：

1. **事件描述**：2-5 句话描述发生了什么。
2. **多视角分析**：2-4 个理论视角，每个视角包含解释和局限。
3. **可验证的假设**：把分析落地成可以测试的预测。
4. **涉及概念**：用 `[[card-english_concept]]` 链接到相关概念卡片。

---

## 版本记录

- v0.1（2026-06-12）：最小稳定规则，定义目录结构、文件名、frontmatter 字段和 AI 处理流程。
