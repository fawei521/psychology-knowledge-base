# spec-observation.md — 观察记录规范

> **触发条件**：用户要写/改事件分析、个人经验、典型案例
> 本文件独立自足，不需要跨文件引用。

---

## YAML 模板

```yaml
---
observation_type: personal_experience   # personal_experience / typical_case / current_event
title: 简短标题
event_date: 2026-06-15
context: 事件发生的情境
behavior: 观察到的行为或反应
tags: [tag1, tag2]
related_entities: [english_concept_1, english_concept_2]
---
```

## 三种类型

| observation_type | 含义 | 目录 |
|-----------------|------|------|
| `personal_experience` | 个人亲身经历 | `05-observations/personal-experiences/` |
| `typical_case` | 典型案例/教材案例 | `05-observations/typical-cases/` |
| `current_event` | 社会热点/时事 | `05-observations/current-events/` |

## 事件类型（自动标签用，≥2 关键词命中确认）

| 事件类型 | 关键词示例 |
|---------|-----------|
| 威胁-防御 | 威胁、恐惧、防御、焦虑、回避、保护、风险 |
| 认同-团结 | 认同、我们、归属、内群体、凝聚力、团结 |
| 权威-服从 | 权威、服从、命令、层级、领导、从众 |
| 公平-互惠 | 公平、互惠、回报、交换、平等、不公 |
| 竞争-冲突 | 竞争、冲突、对抗、争夺、零和、敌对 |
| 合作-利他 | 合作、利他、帮助、分享、协作、共情 |
| 规范-道德 | 规范、道德、应该、对错、谴责、正义 |
| 认知-理解 | 归因、理解、解释、认知、判断、推理 |

## 正文结构

```markdown
# {标题}

## 事件描述
用 2-5 句话描述发生了什么。

## 多视角分析
### 视角1：理论/概念名
- 解释：用这个理论如何解释该事件
- 局限：这个解释什么时候不适用

### 视角2：理论/概念名
- 解释：...
- 局限：...

## 可验证的假设
1. 如果……，那么……
2. 如果……，那么……

## 涉及概念
- [[card-english_concept_1]]
- [[card-english_concept_2]]
```
