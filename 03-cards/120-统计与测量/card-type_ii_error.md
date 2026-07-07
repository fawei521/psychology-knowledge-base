---
concept: type_ii_error
concept_cn: II 型错误
domain: psychometrics
tags:
- 学科/统计与测量
- II型错误
- 假设检验
- beta
- 假阴性
- 统计检验力
citekeys: []
relations:
- target: sampling_and_experimental_error
  type: part-of
- target: hypothesis_testing
  type: part-of
- target: type_i_error
  type: contrasts
- target: statistical_power
  type: correlates-with
---

# II 型错误 / Type II Error

## 定义

II 型错误（Type II Error）是指在假设检验中，当零假设（H₀）实际上为假时，却未能拒绝 H₀ 的决策错误，也称为 "取伪" 错误或假阴性（false negative）。

## 核心要点

- **概率记为 β**：II 型错误发生的概率为 β，统计检验力定义为 1 − β。
- **本质**：真实存在的效应或差异未被检测到。
- **影响因素**：效应量越小、样本量越小、α 水平越低、测量误差/总体方差越大，β 越大。
- **与 I 型错误的权衡**：在样本量固定时，降低 α 会使 β 升高；要同时降低两类错误，需增加样本量或降低测量误差。
- **实际后果**：可能遗漏有效的治疗方法、掩盖真实的理论关系或造成研究资源浪费。

## 理论背景

- **提出者/流派**：与 I 型错误一起由 Neyman 和 Pearson 于 1933 年形式化。
- **发展脉络**：经典假设检验关注 α 控制 → Cohen (1962, 1988) 强调功效分析与 β 控制 → 现代研究伦理和基金申请要求预先进行功效分析（power analysis）。
- **关键假设**：
  - 备择假设 H₁ 有明确的效应方向或效应量；
  - 样本量、α 和效应量在检验前已知或可估计；
  - 检验统计量服从特定分布。

## 经典实验

- **Cohen (1962) 功效研究**：回顾《异常与社会心理学杂志》的研究，发现平均检验力仅约 0.48，意味着许多真实效应有 50% 以上的概率被漏掉（II 型错误）。
- **Dietrich & Kanso (2010) 关于创造力的研究综述**：指出早期许多 "创造力与认知无关" 的阴性结论可能源于小样本导致的低功效和 II 型错误。

## 评价与争议

- **优势**：关注 β 促使研究者设计足够大的样本，提高发现真实效应的能力。
- **争议/反例**：
  - 阴性结果（不拒绝 H₀）常被错误解释为 "没有效应"，而实际上可能是 II 型错误；
  - 过度追求高功效而大样本化，可能使极小效应也变得统计显著，引发实际意义问题；
  - 事后功效分析（post-hoc power）被统计学界普遍批评，应使用置信区间和效应量代替。
- **与相近概念的区别**：II 型错误是 "取伪"（H₀ 为假却不拒绝）；I 型错误是 "弃真"（H₀ 为真却拒绝）。

## 生活实例

- **司法审判**：罪犯因证据不足被判无罪，即 II 型错误；司法中 "宁可错放，不可错判" 的倾向体现了对 I 型错误的控制优先。
- **医学筛查**：患者实际患病但检测未检出（假阴性），可能延误治疗；提高灵敏度可降低 II 型错误。

## 考研重点

- **常考题型**：选择题（判断错误类型、影响 β 的因素）、简答题（如何降低 II 型错误）。
- **易混淆点**：
  - II 型错误发生在 H₀ 为假时；I 型错误发生在 H₀ 为真时；
  - 不拒绝 H₀ ≠ H₀ 为真；
  - β 与功效 1−β 互补，但 α + β ≠ 1。
- **记忆口诀**："H₀ 为假不拒 H₀，II 型错误假阴性；功效就是 1−β，样本越大越灵敏。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8 章；Gravetter & Wallnau《行为科学统计》第 8 章。
- 经典论文：Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.). Lawrence Erlbaum.
- 网页/综述：Hoenig, J. M., & Heisey, D. M. (2001). The abuse of power: The pervasive fallacy of power calculations for data analysis. *The American Statistician*, 55(1), 19–24.
