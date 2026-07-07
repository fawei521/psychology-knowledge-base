---
concept: coefficient_of_determination
concept_cn: 决定系数
domain: psychometrics
tags:
- 学科/统计与测量
- 决定系数
- R方
- 回归拟合
- 解释方差
- 心理统计
citekeys: []
relations:
- target: correlation_and_regression
  type: part-of
- target: pearson_correlation_coefficient
  type: supports
- target: linear_regression
  type: supports
- target: multiple_regression
  type: supports
- target: variance
  type: supports
---

# 决定系数 / Coefficient of Determination (R²)

## 定义

决定系数（R²，R-squared）表示回归模型能够解释因变量变异的比例，取值范围为 0 到 1，是衡量模型拟合优度的核心指标。

## 核心要点

- **公式**：$R^2 = \frac{SS_{\text{回归}}}{SS_{\text{总}}} = 1 - \frac{SS_{\text{残差}}}{SS_{\text{总}}}$
  - $SS_{\text{总}} = \sum (Y_i - \bar{Y})^2$：因变量总平方和；
  - $SS_{\text{回归}} = \sum (\hat{Y}_i - \bar{Y})^2$：模型解释的平方和；
  - $SS_{\text{残差}} = \sum (Y_i - \hat{Y}_i)^2$：未被解释的平方和。
- **与 Pearson r 的关系**：简单线性回归中，$R^2 = r^2$。
- **解释**：R² = 0.64 表示模型解释了因变量 64% 的变异。
- **调整 R²**：多元回归中，$R^2_{\text{adj}} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}$，用于校正自变量个数带来的虚高。
- **注意事项**：R² 高不代表模型正确或具有因果解释力；增加自变量通常会使 R² 增大。

## 理论背景

- **提出者/流派**：决定系数概念由 Pearson 与 Fisher 等人发展，Fisher 将方差分析思想引入回归。
- **发展脉络**：相关平方 → 决定系数 → 多元决定系数 → 调整 R² 与模型选择准则（AIC、BIC）。
- **关键假设**：模型设定正确；残差独立同分布；因变量方差可被分解。

## 经典实验

- **Fisher 方差分析在回归中的应用**：Fisher 将总变异分解为解释变异与误差变异，奠定 R² 的理论基础。
- **社会科学预测研究**：如用社会经济地位预测学业成就，R² 通常介于 0.1–0.4 之间。

## 评价与争议

- **优势**：
  - 直观量化模型解释力；
  - 便于比较不同模型拟合优度；
  - 与 F 检验配合可评估整体方程显著性。
- **争议/反例**：
  - R² 高可能是过拟合或模型误设；
  - 社会科学中 R² 常被高估重要性；
  - 多元回归中应报告调整 R²。
- **与相近概念的区别**：R² 是拟合优度指标；r 是相关强度指标；在简单回归中 $R^2 = r^2$，多元回归中 R² 是复相关系数的平方。

## 生活实例

- **广告投入与销售额**：若 R² = 0.72，说明广告投入可解释销售额 72% 的变异，其余受其他因素影响。
- **学习时间与考试成绩**：R² = 0.25 表示学习时间解释了成绩 25% 的个体差异。

## 考研重点

- **常考题型**：计算题（由 SS 求 R²、由 r 求 R²）、选择题（R² 含义）、简答题（R² 与 r 的区别、调整 R² 作用）。
- **易混淆点**：
  - R² 在多元回归中不等于任意单一 r 的平方；
  - 调整 R² 可能为负；
  - R² 高不等于回归系数显著。
- **记忆口诀**："R 平方看解释，总变里面占多少；简单回归 r 平方，多元要用调整的。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8 章；甘怡群《心理与行为科学统计》第 7 章。
- 经典论文：Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver & Boyd.
- 网页/综述：Statistics By Jim. (n.d.). How To Interpret R-squared in Regression Analysis. https://statisticsbyjim.com/regression/interpret-r-squared-regression/
