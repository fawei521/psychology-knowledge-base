# 03-cards: 原子化概念卡片层

> 跨文献的碎片化知识点，高频调用层。

## 文件格式

每个文件必须包含 YAML Frontmatter + Markdown 正文。

## YAML 字段

```yaml
---
concept: english_concept_name       # 英文概念名，唯一标识，用作文件名
concept_cn: 中文概念名               # 用于检索和展示
domain: general_psychology          # 所属学科，见 04-index/spec-card.md
tags: [tag1, tag2]                 # 建议包含 #学科/xxx 自动标签
citekeys: []                        # Zotero Better BibTeX citekeys（可选）
relations:                          # 概念关系（可选）
  - target: related_concept         # 使用目标卡片的 concept 字段值，不带 card- 前缀
    type: is-a
---
```

完整规范见 [`04-index/spec-card.md`](../04-index/spec-card.md)。

## 目录结构

卡片按学科放在子目录下：

```
03-cards/
├── 10-普通心理学/
├── 20-社会心理学/
├── 30-人格心理学/
└── ...
```

## 当前卡片

- `card-psychology-definition.md`
- `card-big-five-personality.md`
- `card-attachment-theory.md`
- `card-james-lange-theory.md`
- `card-fundamental-attribution-error.md`
- `card-evolutionary-mismatch.md`
