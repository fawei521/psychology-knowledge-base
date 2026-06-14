# spec-card.md — 概念卡片规范

> **触发条件**：用户要写/改概念卡片
> 本文件独立自足，不需要跨文件引用。

---

## YAML 模板

```yaml
---
concept: english_concept_name       # 英文概念名，唯一标识，用作文件名
concept_cn: 中文概念名               # 用于检索和展示
domain: general_psychology          # 所属学科，见下方学科列表
tags: [tag1, tag2, tag3]           # 3-8 个，帮助分类检索
source_papers: ["summary-xxx"]      # 来源摘要（可选）
relations:                          # 概念关系（可选）
  - target: "card-related-concept"
    type: "is-a"
---
```

## 学科列表（domain 字段取值）

| domain | 中文 |
|--------|------|
| `general_psychology` | 普通心理学 |
| `social_psychology` | 社会心理学 |
| `developmental_psychology` | 发展心理学 |
| `personality_psychology` | 人格心理学 |
| `cognitive_psychology` | 认知心理学 |
| `abnormal_psychology` | 异常心理学 |
| `biological_psychology` | 生物心理学 |
| `positive_psychology` | 积极心理学 |
| `evolutionary_psychology` | 进化心理学 |
| `educational_psychology` | 教育心理学 |
| `experimental_psychology` | 实验心理学 |
| `clinical_psychology` | 临床心理学 |
| `organizational_psychology` | 组织/管理心理学 |

## 关系类型表

| 关系类型 | 含义 |
|---------|------|
| `is-a` | 是一种/属于 |
| `part-of` | 是……的一部分 |
| `causes` | 导致 |
| `correlates-with` | 相关 |
| `supports` | 支持 |
| `contrasts` | 对比/反对 |
| `applies-to` | 适用于 |
| `extends` | 扩展 |

## 文件命名

```
card-{english_concept}.md          # 多词用下划线：card-cognitive_dissonance.md
```

## 正文结构

```markdown
# 概念中文名

## 定义
精确描述这个概念是什么。

## 适用条件
- 什么时候成立？在什么人群中更常见？

## 反例/争议
- 什么时候不成立？学界有什么争议？

## 应用提示
分析他人时如何观察这个概念的表达？

## 关联概念
- [[card-related-concept]]
- [[card-parent-concept]]
```
