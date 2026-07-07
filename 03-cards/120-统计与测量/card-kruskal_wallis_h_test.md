---
concept: kruskal_wallis_h_test
concept_cn: Kruskal-Wallis H检验
domain: psychometrics
tags:
- 学科/统计与测量
- 非参数检验
- Kruskal-Wallis H
- 多组比较
- 秩次检验
- 心理统计
citekeys: []
relations:
- target: nonparametric_tests
  type: is-a
- target: mann_whitney_u_test
  type: extends
- target: one_way_anova
  type: contrasts
---

# Kruskal-Wallis H 检验 / Kruskal-Wallis H Test

## 定义

Kruskal-Wallis H 检验是一种用于比较三个或更多独立样本分布位置差异的非参数检验，是单因素方差分析（One-Way ANOVA）的非参数替代方法。

## 核心要点

- **适用数据**：三个及以上独立样本；因变量为连续或顺序变量；不满足正态分布或方差齐性假设。
- **核心思想**：将所有组数据合并排序赋秩，通过比较各组平均秩次判断是否存在组间差异。
- **统计量**：$H = \frac{12}{N(N+1)} \sum_{i=1}^{k} \frac{R_i^2}{n_i} - 3(N+1)$
  - N：总样本量；
  - k：组数；
  - $n_i$：第 i 组样本量；
  - $R_i$：第 i 组秩和。
- **自由度**：df = k − 1。
- **零假设 H₀**：各组分布相同（或中位数相同，分布形状相同时）。
- **近似分布**：当样本量足够大时，H 近似服从自由度为 k−1 的卡方分布。
- **事后比较**：若 H 检验显著，通常需进行 Dunn's 检验或 Bonferroni 校正的 Mann-Whitney U 两两比较。

## 理论背景

- **提出者/流派**：由 William H. Kruskal 与 W. Allen Wallis 于 1952 年提出，是 Mann-Whitney U 检验向多组的自然推广。
- **发展脉络**：两样本秩和检验 → Kruskal-Wallis 多组秩检验 → 事后检验方法（Dunn、Nemenyi）→ 非参数重复测量方法（Friedman）。
- **关键假设**：各组样本相互独立；因变量至少为顺序尺度；各组分布形状相似（用于中位数解释）。

## 经典实验

- **Kruskal & Wallis (1952) 原始论文**：提出 H 统计量并研究其卡方近似性质。
- **多组疗效比较**：用于比较三种及以上药物或干预在小型非正态样本中的效果。

## 评价与争议

- **优势**：
  - 不依赖正态性与方差齐性假设；
  - 可处理顺序数据；
  - 是 ANOVA 的稳健替代。
- **争议/反例**：
  - 只能判断是否存在差异，不能确定具体哪两组不同；
  - 组间分布形状差异大时，中位数解释需谨慎；
  - 存在大量结值时需要校正。
- **与相近概念的区别**：Kruskal-Wallis 用于三组及以上独立样本；Mann-Whitney U 用于两组独立样本；Friedman 检验用于三组及以上配对样本。

## 生活实例

- **不同教学方法效果比较**：比较三种教学方法下学生的考试成绩（成绩偏态分布）。
- **多品牌满意度调查**：比较四个品牌产品的满意度评分差异。

## 考研重点

- **常考题型**：名词解释、选择题（K-W 检验适用条件与自由度）、简答题（K-W 与单因素方差分析区别）。
- **易混淆点**：
  - K-W 是 Mann-Whitney U 的多组扩展，不是配对检验；
  - H 近似卡方分布，df = k−1；
  - 显著后需做事后两两比较。
- **记忆口诀**："三组以上非正态，合并排秩算 H 值；卡方近似 k 减一，显著还要两两比。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 10 章；甘怡群《心理与行为科学统计》第 12 章。
- 经典论文：Kruskal, W. H., & Wallis, W. A. (1952). Use of ranks in one-criterion variance analysis. *Journal of the American Statistical Association*, 47(260), 583–621.
- 网页/综述：DataCamp. (n.d.). Kruskal-Wallis Test: Comparing Multiple Groups Without Normality. https://www.datacamp.com/tutorial/kruskal-wallis-test
