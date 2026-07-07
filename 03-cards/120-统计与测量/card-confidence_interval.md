---
concept: confidence_interval
concept_cn: 置信区间
domain: psychometrics
tags:
- 学科/统计与测量
- 置信区间
- 区间估计
- 标准误
- 假设检验
- 点估计
citekeys: []
relations:
- target: sampling_and_experimental_error
  type: part-of
- target: standard_error
  type: part-of
- target: point_estimate
  type: contrasts
- target: hypothesis_testing
  type: correlates-with
- target: sampling_distribution
  type: supports
---

# 置信区间 / Confidence Interval

## 定义

置信区间（Confidence Interval, CI）是基于样本统计量和抽样分布计算出的一个区间估计，用于表示总体参数可能落入的范围及其估计精度。最常见的 95% 置信区间表示：若重复抽样多次，约有 95% 的区间会包含真实的总体参数。

## 核心要点

- **区间估计 vs. 点估计**：点估计给出一个具体数值（如样本均值）；置信区间给出一个范围，同时反映估计的不确定性。
- **均值置信区间公式**：$CI = \bar{X} \pm z_{\alpha/2} \times SE$（总体 σ 已知或大样本）；若 σ 未知且小样本，用 t 分布临界值：$CI = \bar{X} \pm t_{\alpha/2, df} \times SE$。
- **宽度决定精度**：区间越窄，估计越精确；宽度受标准误、置信水平和样本量影响。
- **与假设检验的等价性**：若 95% CI 不包含零假设值（如 μ₀ = 0），则在 α = 0.05 水平拒绝 H₀。
- **正确解释**：95% CI 不是 "总体参数有 95% 概率落在这个区间"（参数固定，区间随机），而是 "重复抽样下，95% 的类似区间会覆盖真实参数"。

## 理论背景

- **提出者/流派**：Jerzy Neyman 于 1937 年正式提出置信区间的频率学派理论，将其作为点估计的不确定性量化工具。
- **发展脉络**：点估计 → 区间估计 → 置信区间与假设检验统一 → 现代 APA 报告规范要求同时报告 CI 与效应量。
- **关键假设**：
  - 样本为随机抽样；
  - 样本统计量的抽样分布已知或可近似（正态或 t 分布）；
  - 置信水平在计算前确定（常用 90%、95%、99%）。

## 经典实验

- **Neyman (1937) "Outline of a Theory of Statistical Estimation Based on the Classical Theory of Probability"**：系统建立置信区间的频率学派理论基础，区分置信区间与贝叶斯可信区间（credible interval）。
- **Cumming & Finch (2001)**：在心理学中推广置信区间的理解与使用，强调误差条（error bars）与置信区间在结果呈现中的作用。

## 评价与争议

- **优势**：
  - 同时提供估计值和精度信息；
  - 与假设检验结果等价，但信息量更丰富；
  - 有助于避免对 p 值的过度解读。
- **争议/反例**：
  - 研究者常误解 CI 为 "参数落在此区间的概率"，这是贝叶斯解释，与频率学派 CI 不同；
  - 多重比较时，CI 的联合覆盖概率会下降；
  - 当模型假设不成立（如异方差、聚类）时，常规 CI 不准确。
- **与相近概念的区别**：置信区间是频率学派概念；可信区间（credible interval）是贝叶斯概念，表示参数的后验概率分布范围。

## 生活实例

- **民意调查**：支持率 52%，95% CI [49%, 55%] 表示在重复抽样下，95% 的类似调查区间会覆盖真实支持率；该区间不包含 50% 时，可认为候选人领先。
- **医学研究**：新药使血压平均降低 15 mmHg，95% CI [5, 25]，说明真实效应可能低至 5、高至 25；若 CI 包含 0，则效应不确定。

## 考研重点

- **常考题型**：计算题（求均值、比例的置信区间）、选择题（CI 宽度影响因素、CI 与假设检验关系）、简答题（正确解释 95% CI）。
- **易混淆点**：
  - 95% CI 不是参数的概率区间；
  - 置信水平越高，区间越宽；
  - CI 与标准误的关系：95% CI ≈ 均值 ± 1.96 × SE（大样本）。
- **记忆口诀**："点估计一个点，区间估计一段；不含 H₀ 就拒绝，含了零就保留。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 7 章；Gravetter & Wallnau《行为科学统计》第 12 章。
- 经典论文：Neyman, J. (1937). Outline of a theory of statistical estimation based on the classical theory of probability. *Philosophical Transactions of the Royal Society A*, 236, 333–380.
- 网页/综述：Cumming, G. (2014). The new statistics: Why and how. *Psychological Science*, 25(1), 7–29.
