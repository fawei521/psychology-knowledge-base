---
concept: correlation_and_regression
concept_cn: 相关与回归基础
domain: psychometrics
tags:
- 学科/统计与测量
- 相关
- 回归
- 描述统计
- 推断统计
- Pearson相关
- 心理统计
citekeys: []
relations:
- target: descriptive_statistics
  type: is-a
- target: inferential_statistics
  type: is-a
- target: pearson_correlation_coefficient
  type: part-of
- target: covariance
  type: part-of
- target: linear_regression
  type: part-of
- target: regression_equation
  type: part-of
- target: coefficient_of_determination
  type: part-of
- target: multiple_regression
  type: part-of
- target: least_squares_method
  type: part-of
- target: standard_error_of_estimate
  type: part-of
---

# 相关与回归基础 / Correlation and Regression Basics

## 定义

相关与回归是描述和推断两个或多个变量之间数量关系的基础统计方法：相关分析衡量变量间关系的强度与方向，回归分析则建立用自变量预测因变量的数学模型。

## 核心要点

- **相关分析**：量化变量间共变关系的强度与方向，常用 Pearson 相关系数 r。
- **回归分析**：用自变量 X 预测因变量 Y，建立回归方程并估计参数。
- **联系**：在简单线性回归中，决定系数 R² 等于 Pearson r 的平方；回归斜率与相关系数成正比。
- **区别**：相关是对称的、不区分因果；回归是不对称的、具有预测功能。
- **应用**：心理学研究中广泛用于探索变量关系、构建预测模型、控制混杂变量。
- **前提假设**：线性关系、变量近似正态、方差齐性、观测独立；相关分析要求两变量均为连续变量。

## 理论背景

- **提出者/流派**：Pearson 相关系数由 Karl Pearson 发展；Galton 最早提出"回归"概念；最小二乘法由 Gauss 与 Legendre 完善。
- **发展脉络**：协方差 → Pearson 相关 → 简单线性回归 → 多元回归 → 广义线性模型与正则化回归。
- **关键假设**：变量间存在线性关系；残差独立且近似正态分布；自变量无严重测量误差。

## 经典实验

- **Galton 身高研究**：Galton 发现父母身高与子女身高相关，但子女身高倾向于向均值"回归"，提出"回归"概念。
- **Pearson (1896) 相关系数推导**：基于 Galton 工作，提出 Pearson 积矩相关系数公式。

## 评价与争议

- **优势**：
  - 方法简洁，计算与解释直观；
  - 是多元统计与高级建模的入门基础；
  - 广泛应用于心理、教育、社会科学研究。
- **争议/反例**：
  - 相关不等于因果；
  - 对异常值敏感；
  - 只能刻画线性关系，非线性关系会被低估；
  - 受限制取值范围影响。
- **与相近概念的区别**：相关只描述关系；回归用于预测；因果推断需要实验设计或额外假设。

## 生活实例

- **学习时间 vs 考试成绩**：相关分析可判断两者是否正向关联；回归分析可建立"学习时长预测成绩"的方程。
- **焦虑与睡眠质量**：相关发现焦虑越高睡眠越差；回归可控制年龄、性别后看焦虑的独立预测作用。

## 考研重点

- **常考题型**：计算题（求 r、回归方程、R²）、选择题（相关与回归区别）、简答题（相关不等于因果、回归假设）。
- **易混淆点**：
  - 相关对称，回归不对称；
  - r = 0 只说明无线性相关，不排除非线性关系；
  - R² 在多元回归中不等于任何单一 r 的平方。
- **记忆口诀**："相关看方向强弱，回归做预测方程；r 平方是 R 方，因果关系不能碰。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 7–9 章；甘怡群《心理与行为科学统计》第 6–8 章。
- 经典论文：Pearson, K. (1896). Mathematical contributions to the theory of evolution—III. Regression, heredity, and panmixia. *Philosophical Transactions of the Royal Society A*, 187, 253–318.
- 网页/综述：Gravetter, F. J., & Wallnau, L. B. (2017). *Statistics for the Behavioral Sciences* (10th ed.). Cengage Learning.
