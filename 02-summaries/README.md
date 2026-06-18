# 02-summaries: 结构化摘要层

> 每篇文献/资料的浓缩报告，优先检索层。

## 文件格式

每个文件必须包含 YAML Frontmatter + Markdown 正文。

## YAML 字段

```yaml
---
title: "标题"
authors: ["作者1", "作者2"]
year: 2024
source: "期刊名或网址"
type: "summary"  # summary / review / book-chapter
tags: ["tag1", "tag2"]
methods: ["RCT", "n=120"]
key_findings: ["发现1", "发现2"]
concepts: ["概念A", "概念B"]
relations:
  - target: "concept_a"              # 使用目标卡片的 concept 字段值，不要带 card- 前缀
    type: "supports"
---
```

## 当前摘要

- `summary-intro-psychology-openstax-2020.md`：OpenStax 心理学导论第一章
- `summary-personality-analysis-framework-2026.md`：人格分析框架
- `summary-emotion-analysis-framework-2026.md`：情绪分析框架
- `summary-social-behavior-framework-2026.md`：社会行为分析框架
- `summary-evolutionary-psychology-framework-2026.md`：进化心理学框架
