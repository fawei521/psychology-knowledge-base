---
concept: type_i_error
concept_cn: I 型错误
domain: psychometrics
tags:
- 学科/统计与测量
- I型错误
- 假设检验
- 显著性水平
- alpha
- 假阳性
citekeys: []
relations:
- target: sampling_and_experimental_error
  type: part-of
- target: hypothesis_testing
  type: part-of
- target: type_ii_error
  type: contrasts
- target: statistical_power
  type: correlates-with
- target: significance_level
  type: is-a
---

# I 型错误 / Type I Error

## 定义

I 型错误（Type I Error）是指在假设检验中，当零假设（H₀）实际上为真时，却错误地拒绝了 H₀ 的决策错误，也称为 "弃真" 错误或假阳性（false positive）。

## 核心要点

- **概率记为 α**：I 型错误发生的概率等于显著性水平 α，通常设定为 0.05、0.01 或 0.001。
- **本质**：研究者宣称发现了效应或差异，但该效应实际上并不存在。
- **控制方式**：通过设定 α 水平直接控制；α 越小，犯 I 型错误的概率越低。
- **与 II 型错误的权衡**：在样本量固定时，降低 α 会增加 II 型错误概率 β。
- **实际后果**：可能导致错误的理论结论、无效的干预措施被推广或资源浪费。

## 理论背景

- **提出者/流派**：I 型错误与 II 型错误的区分由 Jerzy Neyman 和 Egon Pearson 在 1933 年的论文中正式提出，构成 Neyman-Pearson 假设检验框架的核心。
- **发展脉络**：Fisher 的显著性检验强调 p 值 → Neyman-Pearson 引入两类错误和决策规则 → 现代统计报告要求报告 p 值、置信区间和效应量。
- **关键假设**：
  - 零假设在统计检验前已被明确定义；
  - α 水平在数据收集前预先设定；
  - 检验统计量的分布已知或可由理论近似。

## 经典实验

- **Neyman & Pearson (1933)**：在《On the Problem of the Most Efficient Tests of Statistical Hypotheses》中首次区分 α 与 β，提出检验力概念，并证明似然比检验在某些条件下最优。
- **心理学复制危机中的 I 型错误**：Ioannidis (2005) 论证在低先验概率、低功效和出版偏倚下，大多数阳性发现可能是假阳性，凸显 I 型错误在实证研究中的实际影响。

## 评价与争议

- **优势**：设定 α 提供了明确、可重复的错误控制标准，使研究结论具有可操作的决策边界。
- **争议/反例**：
  - 固定 α = 0.05 被批评为武断，且 p 值接近 0.05 时结论不稳定；
  - p-hacking、选择性报告和多重比较会显著放大实际 I 型错误率；
  - 仅控制 I 型错误不足以保证研究结论可靠，需要结合功效、效应量和先验概率。
- **与相近概念的区别**：I 型错误是 "弃真"（H₀ 为真却拒绝）；II 型错误是 "取伪"（H₀ 为假却不拒绝）。

## 生活实例

- **司法审判**：无辜者被判有罪，即 I 型错误；司法系统强调 "疑罪从无" 就是为了控制这类错误。
- **医学筛查**：健康人被检测为患病（假阳性），需要进一步检查确认，可能造成心理负担和医疗资源浪费。

## 考研重点

- **常考题型**：选择题（判断情境属于哪类错误）、简答题（两类错误关系、α 的控制）。
- **易混淆点**：
  - I 型错误发生在 H₀ 为真时；II 型错误发生在 H₀ 为假时；
  - α 不是 "犯错误的总概率"，而是特定条件下的条件概率；
  - 拒绝 H₀ 只说明数据与 H₀ 不一致，不证明 H₁ 一定为真。
- **记忆口诀**："H₀ 为真拒 H₀，I 型错误假阳性；α 越小越保守，β 随之往上升。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8 章；Gravetter & Wallnau《行为科学统计》第 8 章。
- 经典论文：Neyman, J., & Pearson, E. S. (1933). On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society A*, 231, 289–337.
- 网页/综述：Ioannidis, J. P. A. (2005). Why most published research findings are false. *PLOS Medicine*, 2(8), e124.
