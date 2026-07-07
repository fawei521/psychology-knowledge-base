---
concept: one_parameter_logistic_model
concept_cn: 单参数Logistic模型
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- 1PL
- Rasch模型
- 难度参数
- 心理测量
citekeys: []
relations:
- target: item_response_theory
  type: is-a
- target: item_characteristic_curve
  type: applies-to
- target: irt_assumptions
  type: supports
- target: two_parameter_logistic_model
  type: extends
- target: rasch_model
  type: correlates-with
---

# 单参数 Logistic 模型 / One-Parameter Logistic Model (1PL)

## 定义

单参数 Logistic 模型（1PL）是项目反应理论中最简单的 Logistic 模型，假设所有项目具有相同的区分度，仅通过难度参数 b 来描述项目特性。

## 核心要点

- **公式**：$P_i(\theta) = \frac{1}{1 + e^{-D(\theta - b_i)}}$，其中 D ≈ 1.702，b_i 为项目 i 的难度参数。
- **参数**：仅含一个项目参数——难度 b；所有项目共享相同区分度（通常 D 固定）。
- **ICC 特征**：所有项目的 ICC 曲线形状相同，仅沿 θ 轴平移，b 越大曲线越靠右（越难）。
- **与 Rasch 模型的关系**：
  - 数学形式相似，但 1PL 是统计拟合导向，Rasch 是测量结构导向；
  - 1PL 常引入 D=1.702 以近似正态卵形，Rasch 通常不引入 D；
  - Rasch 更强调数据与模型的拟合、可加性测量。
- **适用场景**：样本量较小、项目区分度相似、强调简洁解释时。

## 理论背景

- **提出者/流派**：1PL 由 Lord 与 Birnbaum 在 IRT 框架下提出，作为 2PL/3PL 的简化；Rasch 模型由 Georg Rasch 独立提出。
- **发展脉络**：正态卵形模型 → Logistic 1PL → 2PL/3PL 参数逐步释放 → Rasch 测量学派与 IRT 学派并行发展。
- **关键假设**：单维性、局部独立性、所有项目区分度相等、无猜测效应（c=0）。

## 经典实验

- **Rasch (1960) 阅读与智力研究**：展示了仅含难度参数的可加性测量模型。
- **Wright & Stone (1979) 教育成就测验**：推广 Rasch/1PL 在课堂评估中的应用。

## 评价与争议

- **优势**：
  - 参数少，小样本下更稳定；
  - 模型简洁，易于解释；
  - 满足特定条件时具有可加性测量属性。
- **争议/反例**：
  - 假设所有题目区分度相同，现实中常不成立；
  - 忽略猜测效应，对多选题可能拟合不佳。
- **与相近概念的区别**：1PL 是 IRT 模型族的一员；Rasch 有独立的测量哲学；2PL 在 1PL 基础上释放区分度。

## 生活实例

- **课堂小测验**：若所有题目质量相近，可用 1PL 快速估计学生能力与题目难度。
- **医学结局量表**：某些功能状态量表假设各项目同等敏感，适合 Rasch/1PL 框架。

## 考研重点

- **常考题型**：选择题（1PL 参数个数、公式）、简答题（1PL 与 2PL/3PL 的区别、1PL 与 Rasch 的区别）。
- **易混淆点**：
  - 1PL 不是 Rasch，虽然公式相似；
  - 1PL 中 "1" 指项目参数为 1 个（难度），不是能力维度为 1；
  - D=1.702 是缩放常数，用于近似正态卵形。
- **记忆口诀**："一参数只看 b，区分固定无 c；1PL 拟合 Rasch 量，理论不同要记清。"

## 文献来源

- 教材章节：戴海崎《心理与教育测量》第 8 章；漆书青《现代教育与心理测量学原理》第 8 章。
- 经典论文：Lord, F. M. (1952). A theory of test scores. *Psychometric Monograph*, 7.
- 网页/综述：Rasch Measurement Transactions. (n.d.). Rasch dichotomous model vs. One-parameter Logistic Model. https://www.rasch.org/rmt/rmt193h.htm
