# 03-cards: 原子化概念卡片层

> 跨文献的碎片化知识点，高频调用层。

## 文件格式

每个文件必须包含 YAML Frontmatter + Markdown 正文。

## YAML 字段

```yaml
---
concept: "概念名称"
domain: "所属领域"
tags: ["tag1", "tag2"]
source_papers: ["summary-source-2024"]
relations:
  - target: "card-related-concept"
    type: "is-a"  # is-a / part-of / causes / correlates-with / opposes
---
```

## 当前卡片

- `card-psychology-definition.md`
- `card-big-five-personality.md`
- `card-attachment-theory.md`
- `card-james-lange-theory.md`
- `card-fundamental-attribution-error.md`
- `card-evolutionary-mismatch.md`
