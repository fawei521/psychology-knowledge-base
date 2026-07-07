---
concept: chi_square_goodness_of_fit
concept_cn: 卡方拟合优度检验
domain: psychometrics
tags:
- 学科/统计与测量
- 卡方检验
- 拟合优度
- 非参数检验
- 分类数据
- 心理统计
citekeys: []
relations:
- target: chi_square_test
  type: is-a
- target: nonparametric_tests
  type: is-a
- target: hypothesis_testing
  type: is-a
---

# 卡方拟合优度检验 / Chi-Square Goodness-of-Fit Test

## 定义

卡方拟合优度检验用于判断一个分类变量的观测频数分布是否与某一理论或预期分布相吻合。

## 核心要点

- **研究问题**：单个分类变量的观测比例是否等于期望比例？
- **公式**：$\chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i}$
  - $O_i$：第 i 类观测频数；
  - $E_i = N \times p_i$：第 i 类期望频数；
  - $p_i$：第 i 类理论比例。
- **自由度**：df = k − 1，k 为类别数；若从样本估计参数，自由度相应减少。
- **零假设 H₀**：观测分布与理论分布一致。
- **备择假设 H₁**：观测分布与理论分布不一致。
- **期望频数要求**：通常每类期望频数 ≥ 5。

## 理论背景

- **提出者/流派**：由 Karl Pearson 于 1900 年提出，是卡方检验的最初形式。
- **发展脉络**：Pearson 拟合优度检验 → 卡方独立性检验 → 现代分类数据分析与 Logistic 回归。
- **关键假设**：分类变量类别互斥且完备；观测独立；期望频数足够大。

## 经典实验

- **孟德尔豌豆实验**：用拟合优度卡方验证子代性状比例是否符合 3:1 或 9:3:3:1 等理论比例。
- **骰子公平性检验**：检验六面骰各面出现概率是否均为 1/6。

## 评价与争议

- **优势**：
  - 可检验任何预设理论分布；
  - 计算简便，解释直观。
- **争议/反例**：
  - 期望频数过小会使 χ² 近似失效；
  - 只能判断整体拟合，不能定位具体哪类偏离；
  - 类别划分方式可能影响结果。
- **与相近概念的区别**：拟合优度卡方检验单个变量的分布；独立性卡方检验两个变量之间的关联。

## 生活实例

- **血型分布调查**：检验某地区人群 A/B/O/AB 血型比例是否符合已知比例。
- **顾客购买偏好**：检验消费者对几种产品包装的选择是否符合等比例偏好假设。

## 考研重点

- **常考题型**：计算题（根据观测频数与理论比例求 χ²）、选择题（自由度计算）。
- **易混淆点**：
  - 拟合优度只涉及一个分类变量；
  - 期望频数 = 总样本量 × 理论比例；
  - 若理论比例由样本估计，df 需减去估计参数个数。
- **记忆口诀**："一维分类看拟合，观测期望来比较；df 类别减个一，期望太小不可靠。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 10 章；甘怡群《心理与行为科学统计》第 12 章。
- 经典论文：Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. *Philosophical Magazine*, 50(302), 157–175.
- 网页/综述：Statistics by Jim. (n.d.). Chi-Square Goodness-of-Fit Test. https://statisticsbyjim.com/hypothesis-testing/chi-square-goodness-of-fit-test/
