---
concept: rasch_model
concept_cn: Rasch模型
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- Rasch模型
- 测量理论
- 可加性测量
- 心理测量
citekeys: []
relations:
- target: item_response_theory
  type: is-a
- target: one_parameter_logistic_model
  type: correlates-with
- target: item_characteristic_curve
  type: applies-to
- target: irt_assumptions
  type: supports
---

# Rasch 模型 / Rasch Model

## 定义

Rasch 模型是一种由丹麦数学家 Georg Rasch 提出的潜变量测量模型，强调通过项目难度与被试能力的可加性结构，实现客观、等距的心理测量。

## 核心要点

- **公式**：$P_{ni}(X_{ni}=1|\theta_n, \delta_i) = \frac{e^{\theta_n - \delta_i}}{1 + e^{\theta_n - \delta_i}}$，其中 θ_n 为被试能力，δ_i 为项目难度。
- **核心思想**：被试能力 θ 与项目难度 δ 处于同一等距量尺上，两者差异决定答对概率。
- **区分度固定**：Rasch 模型不估计区分度，假设所有项目具有相同的自然 Logistic 斜率（约 1）。
- **无猜测参数**：c = 0，即低能力者答对概率可趋近于 0。
- **测量属性**：
  - **充分统计量**：总分是能力的充分统计量；
  - **项目独立**：项目参数估计不依赖于被试样本分布；
  - **被试独立**：能力估计不依赖于所施测的具体项目集合。
- **拟合要求**：Rasch 学派认为若数据与模型不匹配，应修正数据或项目，而非增加模型参数。

## 理论背景

- **提出者/流派**：Georg Rasch（1960）；Benjamin Wright 将其引入社会科学测量领域。
- **发展脉络**：Rasch 概率模型 → 评分量表模型（RSM）→ 分部评分模型（PCM）→ 多维度 Rasch 模型。
- **关键假设**：单维性、局部独立性、单调性、项目间区分度相等、项目与样本不变性。

## 经典实验

- **Rasch (1960) 丹麦阅读能力研究**：分析学生在阅读测验上的作答，提出项目-被试可加性模型，奠定 Rasch 测量基础。
- **Wright & Masters (1982) 教育评估应用**：将 Rasch 模型推广到评分量表与课堂评价中。

## 评价与争议

- **优势**：
  - 提供严格、可重复的客观测量；
  - 能力与项目难度共尺，解释直观；
  - 项目功能差异（DIF）与拟合诊断成熟。
- **争议/反例**：
  - 严格区分度相等假设常被现实数据违反；
  - "数据拟合模型" 的立场在统计学界有争议；
  - 对多选题等含猜测的题型不适用。
- **与相近概念的区别**：Rasch 与 1PL 数学相似，但 Rasch 是测量哲学导向，1PL 是统计拟合导向；2PL/3PL 通过增加参数提高拟合，违背 Rasch 的简洁测量原则。

## 生活实例

- **大型教育监测（如 PISA 部分分析）**：部分国家报告使用 Rasch 模型将学生能力与题目难度放在同一尺度上。
- **康复医学功能评估**：FIM（功能独立性测量）等工具使用 Rasch 模型确保各项目难度有序。

## 考研重点

- **常考题型**：名词解释（Rasch 模型）、简答题（Rasch 与 1PL/2PL 的区别）、选择题（Rasch 的核心特征）。
- **易混淆点**：
  - Rasch 不是 1PL，虽然公式形式相近；
  - Rasch 模型不估计区分度，但区分度固定不等于没有区分度；
  - "项目独立"指参数估计不依赖特定被试样本，不是项目之间独立。
- **记忆口诀**："Rasch 一尺量人与题，θ 减 δ 定概率；区分固定无猜测，数据不拟合就修题。"

## 文献来源

- 教材章节：漆书青《现代教育与心理测量学原理》第 9 章；Wright & Masters《Rasch Measurement》相关章节。
- 经典论文：Rasch, G. (1960). *Probabilistic Models for Some Intelligence and Attainment Tests*. Copenhagen: Danish Institute for Educational Research.
- 网页/综述：Rasch Measurement Transactions. (n.d.). Rasch dichotomous model vs. One-parameter Logistic Model. https://www.rasch.org/rmt/rmt193h.htm
