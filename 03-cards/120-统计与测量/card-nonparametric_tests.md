---
concept: nonparametric_tests
concept_cn: 非参数检验
domain: psychometrics
tags:
- 学科/统计与测量
- 非参数检验
- 假设检验
- 秩次检验
- 卡方检验
- 心理统计
citekeys: []
relations:
- target: hypothesis_testing
  type: is-a
- target: inferential_statistics
  type: is-a
- target: chi_square_test
  type: part-of
- target: mann_whitney_u_test
  type: part-of
- target: wilcoxon_signed_rank_test
  type: part-of
- target: kruskal_wallis_h_test
  type: part-of
- target: parametric_tests
  type: contrasts
---

# 非参数检验 / Nonparametric Tests

## 定义

非参数检验（Nonparametric Tests）是一类不依赖总体分布具体形式（如正态分布）的统计假设检验方法，常用于分类数据、等级数据或无法满足参数检验前提的连续数据。

## 核心要点

- **基本特点**：不对总体参数（如均值、方差）做假设，也不假设总体服从特定分布。
- **适用条件**：
  - 数据为分类变量或顺序变量；
  - 样本量小，难以判断正态性；
  - 数据明显偏态或存在异常值；
  - 方差不齐，不满足参数检验假设。
- **常用方法**：卡方检验、Mann-Whitney U 检验、Wilcoxon 符号秩检验、Kruskal-Wallis H 检验、Friedman 检验、Spearman 等级相关等。
- **与参数检验关系**：
  - 当数据满足参数检验假设时，参数检验统计功效更高；
  - 非参数检验是参数检验的稳健替代方案。
- **优缺点**：
  - 优点：适用范围广、对异常值不敏感、计算相对简单；
  - 缺点：功效通常低于参数检验；损失部分数据信息（如只用秩次）。

## 理论背景

- **提出者/流派**：非参数方法在 20 世纪中叶快速发展，代表学者包括 Kruskal、Wallis、Mann、Whitney、Wilcoxon、Spearman 等。
- **发展脉络**：符号检验 → 秩和检验 → 卡方检验体系 → 现代非参数与稳健统计方法。
- **关键假设**：观测独立；分类变量类别互斥；顺序变量至少具有等级意义。

## 经典实验

- **Kruskal & Wallis (1952) 秩方差分析**：提出 K-W 检验，拓展了 Mann-Whitney U 检验到多组比较。
- **Wilcoxon (1945) 符号秩检验**：为配对样本提供非参数检验方法，广泛应用于生物与心理实验。

## 评价与争议

- **优势**：
  - 对分布形态要求低；
  - 对异常值稳健；
  - 可处理等级与分类数据。
- **争议/反例**：
  - 数据满足正态假设时，非参数检验功效较低；
  - 部分方法对结值（ties）处理敏感；
  - 结果解释有时不如参数检验直观。
- **与相近概念的区别**：参数检验估计总体参数；非参数检验基于秩次、频数或符号；Robust 统计则关注对假设偏离的稳健性。

## 生活实例

- **消费者满意度调查**：Likert 量表数据常不满足正态分布，可用 Mann-Whitney U 或 Kruskal-Wallis 比较不同群体。
- **医学疗效评估**：小样本、疗效指标为有序等级时，用 Wilcoxon 符号秩检验比较治疗前后差异。

## 考研重点

- **常考题型**：选择题（何时用非参数检验）、简答题（非参数与参数检验的区别与选择）、名词解释（非参数检验）。
- **易混淆点**：
  - 非参数检验不是"无假设"，而是不假设总体分布；
  - 非参数检验仍需要观测独立性；
  - Mann-Whitney U 对应独立样本 t 检验，Wilcoxon 符号秩对应配对 t 检验。
- **记忆口诀**："分布未知用非参，秩次频数来帮忙；卡方 U 检符号秩，K-W 多组不用方。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 10 章；甘怡群《心理与行为科学统计》第 12 章。
- 经典论文：Kruskal, W. H., & Wallis, W. A. (1952). Use of ranks in one-criterion variance analysis. *Journal of the American Statistical Association*, 47(260), 583–621.
- 网页/综述：Statistics by Jim. (n.d.). Chi-Square Test of Independence and an Example. https://statisticsbyjim.com/hypothesis-testing/chi-square-test-independence-example/
