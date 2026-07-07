---
concept: linear_regression
concept_cn: 线性回归
domain: psychometrics
tags:
- 学科/统计与测量
- 线性回归
- 回归分析
- 预测
- 自变量
- 因变量
citekeys: []
relations:
- target: correlation_and_regression
  type: part-of
- target: pearson_correlation_coefficient
  type: correlates-with
- target: regression_equation
  type: part-of
- target: least_squares_method
  type: supports
- target: coefficient_of_determination
  type: supports
- target: standard_error_of_estimate
  type: supports
- target: multiple_regression
  type: extends
---

# 线性回归 / Linear Regression

## 定义

线性回归（Linear Regression）是用一条最优拟合直线描述一个自变量 X 与一个因变量 Y 之间线性关系，并用 X 预测 Y 的统计方法。

## 核心要点

- **简单线性回归方程**：$\hat{Y} = a + bX$，其中 a 为截距，b 为斜率。
- **斜率 b**：X 每增加一个单位，Y 的平均变化量；$b = r \cdot \frac{S_Y}{S_X}$。
- **截距 a**：当 X = 0 时 Y 的预测值；$a = \bar{Y} - b\bar{X}$。
- **最小二乘估计**：通过最小化残差平方和 $\sum (Y_i - \hat{Y}_i)^2$ 求解 a 与 b。
- **前提假设**：
  - X 与 Y 存在线性关系；
  - 残差独立且近似正态分布；
  - 残差方差齐性（homoscedasticity）；
  - 自变量测量误差较小。
- **显著性检验**：回归系数 b 可用 t 检验，整体方程可用 F 检验。

## 理论背景

- **提出者/流派**：Galton 提出"回归"概念；Pearson 发展相关与回归的数学形式；Yule 将回归推广到多元情形。
- **发展脉络**：最小二乘法 → 简单线性回归 → 多元回归 → 广义线性模型与正则化方法。
- **关键假设**：变量间为线性关系；模型设定正确；误差项独立同分布。

## 经典实验

- **Galton 身高回归研究**：发现子女身高对父母身高的"回归"现象，即高个子父母的子女身高趋于群体均值。
- **Pearson & Lee (1903) 人体特征回归**：用回归分析研究人体多个测量指标之间的预测关系。

## 评价与争议

- **优势**：
  - 模型简洁，参数解释直观；
  - 可用于预测与控制；
  - 是多元回归与高级模型的基础。
- **争议/反例**：
  - 强相关也不一定适合线性回归，需检查散点图；
  - 外推预测风险大；
  - 自变量与因变量方向不能反推因果。
- **与相近概念的区别**：相关分析对称且不预测；回归分析不对称，用 X 预测 Y；多元回归包含多个自变量。

## 生活实例

- **房价预测**：用房屋面积预测房价，建立面积→价格的回归方程。
- **心理干预效果**：用干预前焦虑分数预测干预后焦虑分数，评估干预效果。

## 考研重点

- **常考题型**：计算题（求回归方程、预测值、残差）、选择题（斜率与截距含义）、简答题（回归与相关的区别）。
- **易混淆点**：
  - 回归系数 b 不是相关系数 r，但两者符号相同；
  - 回归方程中的 Ŷ 是预测值，不是实际值；
  - 外推预测（X 超出样本范围）不可靠。
- **记忆口诀**："Y 帽等于 a 加 bX，最小二乘求最佳；斜率截距会解释，预测莫要乱外推。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8 章；甘怡群《心理与行为科学统计》第 7 章。
- 经典论文：Galton, F. (1886). Regression towards mediocrity in hereditary stature. *Journal of the Anthropological Institute*, 15, 246–263.
- 网页/综述：Gravetter, F. J., & Wallnau, L. B. (2017). *Statistics for the Behavioral Sciences* (10th ed.). Cengage Learning.
