# Psychology Knowledge Base

> 版本：v1.0
> 规范：Markdown + YAML Frontmatter
> 检索策略：先查 03-cards → 再查 02-summaries → 最后查 01-raw

## 目录结构

```
psychology-knowledge-base/
├── index.md              # 总规范 + 目录说明
├── kb.db                 # SQLite 数据库（核心存储）
├── tools/                # 数据库工具脚本
│   ├── db_init.py
│   ├── import_md.py
│   └── query.py
├── 01-raw/              # 原始文献（只存不检）
│   ├── pdfs/
│   └── web-pages/
├── 02-summaries/        # 结构化摘要（论文/书籍/资料总结）
│   ├── _template-summary.md
│   └── ...
├── 03-cards/            # 原子化概念卡片（理论、概念、人物、实验）
│   ├── _template-card.md
│   └── ...
├── 04-index/            # 索引文件
│   ├── concept-map.md   # 概念关系总图
│   └── tag-index.md     # 标签索引
└── 05-observations/     # 个人经验、典型案例、时事分析
    ├── personal-experiences/
    ├── typical-cases/
    └── current-events/
```

## 文件命名规范

- 摘要：`summary-{主题}-{年份}-{作者或来源}.md`
- 卡片：`card-{概念名}-{年份}.md`
- 多词用连字符 `-` 连接
- 优先使用英文标签，文件名可用英文

## YAML 字段规范

### 摘要文件模板

```yaml
---
title: "论文/资料标题"
authors: ["作者1", "作者2"]
year: 2024
source: "期刊名或网址"
type: "summary"  # summary / review / book-chapter
tags: ["tag1", "tag2"]
methods: ["RCT", "n=120", "fMRI"]
key_findings: ["发现1", "发现2"]
concepts: ["概念A", "概念B"]
relations:
  - target: "card-concept-a-2024"
    type: "supports"
  - target: "summary-related-topic-2023"
    type: "contrasts"
---
```

### 卡片文件模板

```yaml
---
concept: "概念名称"
domain: "人格心理学 / 情绪 / 社会心理学 / 进化心理学"
tags: ["tag1", "tag2"]
source_papers: ["summary-source-2024"]
relations:
  - target: "card-related-concept"
    type: "is-a"        # is-a / part-of / causes / correlates-with / opposes
  - target: "card-another-concept"
    type: "correlates-with"
---
```

### 观察/经验/案例分析文件模板

```yaml
---
observation_type: "personal_experience"  # personal_experience / typical_case / current_event
title: "标题"
event_date: "2026-06-12"
context: "事件发生的情境"
behavior: "观察到的行为或反应"
tags: ["tag1", "tag2"]
related_entities: ["big_five_personality", "attachment_theory"]
sources: ["summary-source-2024"]
---
```

## 关系类型说明

| 关系类型 | 含义 |
|---|---|
| `is-a` | 是一种/属于 |
| `part-of` | 是...的一部分 |
| `causes` | 导致 |
| `correlates-with` | 相关 |
| `supports` | 支持 |
| `contrasts` | 对比/反对 |
| `applies-to` | 适用于 |
| `extends` | 扩展 |

## 使用流程

1. 新文献/资料进入 → 先存 `01-raw/`
2. 写结构化摘要 → 放 `02-summaries/`
3. 拆出概念卡片 → 放 `03-cards/`
4. 个人经验/案例/时事分析 → 放 `05-observations/`
5. 运行 `python tools/import_md.py` 同步到 `kb.db`
6. 更新 `04-index/concept-map.md` 和 `04-index/tag-index.md`

## 当前状态

- [x] 目录结构建立（五层）
- [x] SQLite 数据库创建（sources/snippets/entities/observations/relations/tags）
- [x] YAML 规范定义
- [x] 模板文件创建
- [x] 示例摘要、卡片、观察导入数据库
- [x] PyYAML 依赖安装
- [ ] 等待用户填充真实文献和个人经验
- [ ] 未来：sqlite-vec 语义检索扩展
- [ ] 未来：同步脚本自动增量更新
