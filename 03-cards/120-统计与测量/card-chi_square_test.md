---
concept: chi_square_test
concept_cn: 卡方检验
domain: psychometrics
tags:
- 学科/统计与测量
- 卡方检验
- 非参数检验
- 分类数据
- 拟合优度
- 独立性检验
citekeys: []
relations:
- target: nonparametric_tests
  type: is-a
- target: chi_square_goodness_of_fit
  type: extends
- target: chi_square_test_of_independence
  type: extends
- target: hypothesis_testing
  type: is-a
---

# 卡方检验 / Chi-Square Test (χ² Test)

## 定义

卡方检验（Chi-Square Test, χ² Test）是一种基于观测频数与期望频数差异的非参数检验方法，常用于分类数据的统计推断。

## 核心要点

- **基本公式**：$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$，其中 $O_i$ 为观测频数，$E_i$ 为期望频数。
- **主要类型**：
  - **拟合优度卡方**：检验一个分类变量的观测分布是否符合某理论分布；
  - **独立性卡方**：检验两个分类变量是否相互独立。
- **前提假设**：
  - 观测相互独立；
  - 数据为分类变量；
  - 期望频数一般应 ≥ 5（或至少 80% 单元格 ≥ 5）。
- **自由度**：
  - 拟合优度：df = k − 1（k 为类别数）；
  - 独立性：df = (r − 1)(c − 1)（r、c 为列联表行列数）。
- **结果解释**：χ² 越大、自由度对应 p 值越小，越倾向于拒绝原假设。

## 理论背景

- **提出者/流派**：由 Karl Pearson 于 1900 年提出，是统计学中最早发展的假设检验方法之一。
- **发展脉络**：拟合优度检验 → 独立性检验 → 配对卡方（McNemar）→ Logistic 回归与广义线性模型。
- **关键假设**：期望频数不宜过小；样本观测独立；类别互斥且完备。

## 经典实验

- **Mendel 遗传实验的拟合优度检验**：用卡方检验验证孟德尔豌豆实验的 3:1 分离比。
- **Pearson (1900) 生物统计应用**：将卡方检验引入生物与社会科学，奠定现代分类数据分析基础。

## 评价与争议

- **优势**：
  - 方法简单，应用广泛；
  - 可处理名义与顺序分类数据；
  - 是列联表分析的基础工具。
- **争议/反例**：
  - 期望频数过小时结果不可靠；
  - 只能检验关联是否存在，不能说明关联强度；
  - 大样本时容易得到显著结果。
- **与相近概念的区别**：卡方检验用于分类数据；t 检验/F 检验用于连续数据；Fisher 精确检验用于小样本 2×2 表。

## 生活实例

- **品牌偏好调查**：检验消费者对五种饮料品牌的偏好是否均匀分布。
- **性别与职业选择**：用独立性卡方分析性别与专业选择是否有关联。

## 考研重点

- **常考题型**：计算题（拟合优度或独立性卡方）、选择题（自由度计算、适用条件）、简答题（卡方检验前提与类型）。
- **易混淆点**：
  - 拟合优度卡方涉及一个变量，独立性卡方涉及两个变量；
  - 期望频数由理论比例（拟合优度）或行列边际（独立性）计算；
  - 小样本 2×2 表应使用 Fisher 精确检验。
- **记忆口诀**："卡方看频数，观测期望来相除；一维拟合二维独，期望太小用精确。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 10 章；甘怡群《心理与行为科学统计》第 12 章。
- 经典论文：Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. *Philosophical Magazine*, 50(302), 157–175.
- 网页/综述：Scribbr. (n.d.). Chi-Square Test of Independence. https://www.scribbr.com/statistics/chi-square-test-of-independence/
