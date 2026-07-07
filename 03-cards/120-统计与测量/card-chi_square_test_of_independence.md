---
concept: chi_square_test_of_independence
concept_cn: 卡方独立性检验
domain: psychometrics
tags:
- 学科/统计与测量
- 卡方检验
- 独立性检验
- 列联表
- 非参数检验
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

# 卡方独立性检验 / Chi-Square Test of Independence

## 定义

卡方独立性检验用于判断两个分类变量之间是否存在统计关联，即一个变量的分布是否依赖于另一个变量的取值。

## 核心要点

- **研究问题**：两个分类变量是否相互独立？
- **数据形式**：r × c 列联表（r 行 × c 列）。
- **期望频数**：$E_{ij} = \frac{R_i \times C_j}{N}$，其中 $R_i$ 为第 i 行合计，$C_j$ 为第 j 列合计，N 为总样本量。
- **公式**：$\chi^2 = \sum_{i=1}^{r} \sum_{j=1}^{c} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$
- **自由度**：df = (r − 1)(c − 1)。
- **零假设 H₀**：两个变量相互独立。
- **备择假设 H₁**：两个变量不独立（存在关联）。
- **前提条件**：观测独立；每个单元格期望频数一般 ≥ 5。

## 理论背景

- **提出者/流派**：卡方独立性检验由 Karl Pearson 在 20 世纪初发展，与拟合优度检验共同构成卡方统计体系。
- **发展脉络**：2×2 列联表 → r×c 列联表 → 分层卡方（Mantel-Haenszel）→ Logistic 回归与对数线性模型。
- **关键假设**：变量为分类变量；观测独立；单元格期望频数足够大。

## 经典实验

- **吸烟与肺癌研究**：Doll & Hill 的病例对照研究用列联表卡方分析吸烟与肺癌的关联。
- **性别与投票偏好**：政治学研究常用卡方独立性检验分析人口学变量与投票行为的关系。

## 评价与争议

- **优势**：
  - 可检验任意大小列联表；
  - 计算直观，结果易于解释；
  - 是分类变量关联分析的基础工具。
- **争议/反例**：
  - 只能判断关联是否存在，不能说明方向与强度；
  - 小样本或期望频数过小时结果不可靠；
  - 大样本下 trivial 关联也可能显著。
- **与相近概念的区别**：独立性卡方用于两个分类变量；拟合优度卡方用于一个变量与理论分布；相关系数用于连续变量。

## 生活实例

- **教育研究**：检验性别与专业选择（文科/理科/工科）是否有关联。
- **市场调研**：检验不同年龄段消费者对产品包装的偏好是否不同。

## 考研重点

- **常考题型**：计算题（列联表 χ² 计算）、选择题（自由度、期望频数公式）、简答题（独立性卡方与拟合优度卡方区别）。
- **易混淆点**：
  - 期望频数由行列合计计算，不是理论比例；
  - df = (r−1)(c−1)，不是 rc−1；
  - 小样本 2×2 表用 Fisher 精确检验替代。
- **记忆口诀**："二维列联看独立，行列合计算期望；df 行减一乘列减一，关联强弱另度量。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 10 章；甘怡群《心理与行为科学统计》第 12 章。
- 经典论文：Pearson, K. (1900). On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling. *Philosophical Magazine*, 50(302), 157–175.
- 网页/综述：Statistics by Jim. (n.d.). Chi-Square Test of Independence and an Example. https://statisticsbyjim.com/hypothesis-testing/chi-square-test-independence-example/
