---
concept: internal_consistency_reliability
concept_cn: 内部一致性信度
domain: psychometrics
tags:
- 学科/统计与测量
- 内部一致性信度
- 同质性信度
- Cronbach's alpha
- KR-20
- 信度
- 经典测量理论
citekeys: []
relations:
- target: reliability
  type: is-a
- target: split_half_reliability
  type: extends
- target: classical_test_theory
  type: part-of
- target: cronbachs_alpha
  type: supports
- target: item_discrimination
  type: supports
---

# 内部一致性信度 / Internal Consistency Reliability

## 定义

内部一致性信度（Internal Consistency Reliability），也称同质性信度，是指测验内部各题目之间测量同一特质的程度，反映测验题目得分的一致性和测验内容的同质性。

## 核心要点

- **误差来源**：主要控制**题目异质性误差**，即测验题目是否都测量同一心理特质。
- **常用指标**：
  - **Cronbach's α（克龙巴赫 α 系数）**：最常用，适用于多级评分题目，可视为所有可能分半信度的平均值；
  - **KR-20（Kuder-Richardson 20）**：适用于二分计分题目，是 Cronbach's α 的特例；
  - **KR-21**：二分计分且难度相近时的简化公式。
- **评价标准**：
  - α ≥ 0.90：优秀；
  - 0.80–0.89：非常好；
  - 0.70–0.79：可接受；
  - α < 0.70：需修订。
- **与分半信度的关系**：Cronbach's α 等价于所有可能分半信度的平均值；在单侧面人×题设计中，G 系数与 α 等价。
- **注意事项**：α 高不代表测验测量单一维度，也不代表效度高；题目数量增加会提高 α。

## 理论背景

- **提出者/流派**：Kuder 与 Richardson (1937) 提出 KR-20 和 KR-21；Cronbach (1951) 提出 α 系数并推广。
- **发展脉络**：分半信度 → KR 公式 → Cronbach's α → McDonald's ω → 验证性因素分析中的组合信度（composite reliability）。
- **关键假设**：
  - 测验测量单一潜在特质或维度；
  - 题目之间具有正向相关；
  - 测验为 tau-equivalent 或 essentially tau-equivalent（对 α 而言）。

## 经典实验

- **Cronbach (1951) "Coefficient Alpha and the Internal Structure of Tests"**：提出 Cronbach's α 并证明其与所有可能分半信度平均值的关系，成为心理测量学引用最高的论文之一。
- **心理量表内部一致性报告**：绝大多数现代心理量表（如大五人格、抑郁自评量表）都报告 Cronbach's α 作为基本信度指标。

## 评价与争议

- **优势**：
  - 只需一次施测即可计算；
  - 计算简便，几乎所有统计软件均支持；
  - 与项目-总分相关直接关联，便于题目筛选。
- **争议/反例**：
  - α 受题目数量影响，增加题目可能人为提高 α；
  - α 高不一定表示单维，多维测验若各维度内部相关高，α 也可能高；
  - 当 tau-equivalent 假设不满足时，McDonald's ω 更准确。
- **与相近概念的区别**：内部一致性关注测验内部题目同质性；重测信度关注跨时间稳定性；复本信度关注跨版本等值性。

## 生活实例

- **量表质量评估**：一份焦虑量表若 20 个题目都测量焦虑，且 α = 0.92，说明题目高度一致；若 α = 0.55，则题目可能测量了不同内容。
- **问卷设计**：在设计顾客满意度问卷时，会通过内部一致性信度筛选题目，删除与总分相关低的题目。

## 考研重点

- **常考题型**：名词解释、选择题（适用条件、评价标准）、简答题（内部一致性信度与分半信度的关系）。
- **易混淆点**：
  - Cronbach's α 适用于多级评分，KR-20 适用于二分计分；
  - α 高不等于单维或高效度；
  - 分半信度经斯皮尔曼-布朗校正后与 α 有联系，但不完全等同。
- **记忆口诀**："内部一致看题目，α 系数最常见；KR 用于二分题，零点七以上可接受。"

## 文献来源

- 教材章节：郑日昌《心理测量学》第 4 章；戴海崎《心理与教育测量》第 4 章。
- 经典论文：Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297–334.
- 网页/综述：Cogn-IQ. (n.d.). Internal consistency reliability: Cronbach's alpha & related coefficients. https://www.cogn-iq.org/learn/theory/internal-consistency/
