---
concept: least_squares_method
concept_cn: 最小二乘法
domain: psychometrics
tags:
- 学科/统计与测量
- 最小二乘法
- 参数估计
- 回归分析
- 拟合优度
- 心理统计
citekeys: []
relations:
- target: correlation_and_regression
  type: part-of
- target: linear_regression
  type: supports
- target: multiple_regression
  type: supports
- target: regression_equation
  type: supports
- target: standard_error_of_estimate
  type: supports
---

# 最小二乘法 / Least Squares Method

## 定义

最小二乘法（Least Squares Method）是一种通过最小化观测值与模型预测值之间残差平方和来估计回归模型参数的统计方法。

## 核心要点

- **目标函数**：最小化 $Q = \sum_{i=1}^{n} (Y_i - \hat{Y}_i)^2 = \sum_{i=1}^{n} e_i^2$。
- **简单线性回归中的解**：
  - 斜率：$b = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}$
  - 截距：$a = \bar{Y} - b\bar{X}$
- **几何意义**：在所有可能的直线中，选择使各数据点到直线垂直距离（残差）平方和最小的那条直线。
- **最优性**：在高斯-马尔可夫假设下，最小二乘估计是最佳线性无偏估计（BLUE）。
- **应用范围**：简单线性回归、多元回归、曲线拟合、方差分析等多种统计模型。

## 理论背景

- **提出者/流派**：最小二乘法由 Gauss（1809）与 Legendre（1805）分别独立提出；Gauss 后来给出其统计最优性证明。
- **发展脉络**：天文观测数据拟合 → 线性模型参数估计 → 广义最小二乘 → 正则化最小二乘（岭回归、Lasso）。
- **关键假设**：模型关于参数线性；误差项零均值、同方差、不相关；自变量非随机或固定设计。

## 经典实验

- **Gauss 谷神星轨道预测**：Gauss 用最小二乘法根据有限观测数据预测谷神星轨道，是该方法早期著名应用。
- **Legendre 测地线研究**：Legendre 在测量误差分析中提出最小化误差平方和的思想。

## 评价与争议

- **优势**：
  - 计算简便，有解析解；
  - 在高斯-马尔可夫条件下具有良好统计性质；
  - 应用广泛，易于扩展。
- **争议/反例**：
  - 对异常值敏感，单个极端值会显著影响参数估计；
  - 要求误差方差齐性，异方差时需用加权最小二乘；
  - 只能最小化平方误差，不能处理某些复杂损失函数。
- **与相近概念的区别**：最小二乘是参数估计方法；最大似然是另一估计方法；最小一乘法最小化残差绝对值和，对异常值更稳健。

## 生活实例

- **趋势线拟合**：Excel 中为散点图添加"趋势线"即默认使用最小二乘法。
- **身高体重关系研究**：用最小二乘法拟合体重对身高的回归直线。

## 考研重点

- **常考题型**：计算题（用最小二乘法求 a、b）、选择题（最小二乘法目标）、简答题（最小二乘估计的性质）。
- **易混淆点**：
  - 最小二乘是估计方法，不是模型本身；
  - 残差平方和最小，不是残差和最小；
  - 高斯-马尔可夫定理的条件是 BLUE，不是无偏性的唯一保证。
- **记忆口诀**："残差平方和最小，a 和 b 由此出；BLUE 性质高斯证，异常值来会捣蛋。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8 章；甘怡群《心理与行为科学统计》第 7 章。
- 经典论文：Gauss, C. F. (1809). *Theoria Motus Corporum Coelestium in Sectionibus Conicis Solem Ambientium*. Hamburg: Perthes & Besser.
- 网页/综述：Duke University. (n.d.). Mathematics of simple regression. https://people.duke.edu/~rnau/mathreg.htm
