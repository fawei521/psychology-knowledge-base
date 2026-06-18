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
citekeys: []                        # Zotero Better BibTeX citekeys（可选）
relations:                          # 概念关系（可选）
  - target: "related_concept"       # 使用目标卡片的 concept 字段值，不要带 card- 前缀
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

## 文件存放位置

```
03-cards/{学科编号}-{学科名}/card-{english_concept}.md
```

- 学科子目录编号见 `03-cards/` 实际结构（如 `10-普通心理学`、`20-社会心理学`）。
- 多词概念用下划线连接：`card-cognitive_dissonance.md`
- 如果概念跨多个学科，选择最核心的一门放主文件，其他学科通过 `tags` 和 `relations` 体现。

## 正文结构（八段式）

```markdown
# 概念中文名 / English Concept Name

## 定义
用一句话精确描述这个概念是什么。

## 核心要点
- 要点1：...
- 要点2：...
- 要点3：...

## 理论背景
- 提出者/流派
- 发展脉络
- 关键假设

## 经典实验
- 实验名称、研究者、年份
- 实验设计/关键操作
- 主要发现及其与概念的关系

## 评价与争议
- 优势
- 争议/反例
- 与相近理论的区别

## 生活实例
- 例1：...
- 例2：...

## 考研重点
- 常考题型
- 易混淆点
- 记忆口诀

## 文献来源
- 教材章节
- 经典论文（可用 Zotero citekey）
- 网页/综述（作为补充）
```

## 字段说明

- **`citekeys`**：Zotero 已通过 Better BibTeX 部署，填写 citekey 即可与文献库联动。没有文献时留空 `[]`。
- **`relations.target`**：统一使用目标卡片的 `concept` 字段值，不要加 `card-` 前缀。例如 `target: working_memory`。
- **`tags`**：建议至少包含 `#学科/xxx` 自动标签，方便 Obsidian 标签面板分组。
