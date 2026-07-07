---
concept: covariance
concept_cn: 协方差
domain: psychometrics
tags:
- 学科/统计与测量
- 协方差
- 相关
- 方差
- 描述统计
- 心理统计
citekeys: []
relations:
- target: correlation_and_regression
  type: part-of
- target: pearson_correlation_coefficient
  type: supports
- target: variance
  type: is-a
- target: descriptive_statistics
  type: is-a
---

# 协方差 / Covariance

## 定义

协方差（Covariance）是描述两个连续变量共同变化方向与程度的指标，反映变量间离差乘积的平均趋势。

## 核心要点

- **公式**：$\text{Cov}(X,Y) = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{n-1}$（样本协方差）。
- **符号含义**：
  - 正值：X 高于均值时 Y 也倾向于高于均值，两者同向变化；
  - 负值：X 高于均值时 Y 倾向于低于均值，两者反向变化；
  - 零：两变量无线性共变趋势。
- **单位依赖**：协方差值受变量测量单位影响，不便跨变量比较。
- **与 Pearson r 的关系**：Pearson r 是标准化后的协方差，消除了单位影响：$r = \frac{\text{Cov}(X,Y)}{S_X S_Y}$。
- **应用**：是相关分析、回归分析、因素分析与结构方程模型的基础构件。

## 理论背景

- **提出者/流派**：协方差概念与方差、相关系数同步发展，Galton 与 Pearson 对其形式化有重要贡献。
- **发展脉络**：方差（单个变量）→ 协方差（两个变量）→ 协方差矩阵（多个变量）→ 因素分析与结构方程模型。
- **关键假设**：变量为连续变量；线性关系；观测独立。

## 经典实验

- **Galton 人体特征共变研究**：Galton 在研究身高、臂长等人体特征时，发现多个特征存在共同变化趋势，为协方差与相关分析奠定基础。
- **Pearson 生物统计应用**：将协方差应用于遗传与进化研究，推动相关系数的诞生。

## 评价与争议

- **优势**：
  - 直接反映变量共同变化的方向与程度；
  - 是多元统计分析的核心基础。
- **争议/反例**：
  - 数值受单位影响，难以解释绝对大小；
  - 不能反映非线性共变；
  - 对异常值敏感。
- **与相近概念的区别**：方差描述单个变量的离散程度；协方差描述两个变量的共同变化；相关系数是标准化协方差。

## 生活实例

- **收入与消费**：通常呈正协方差，收入增加时消费也倾向于增加。
- **气温与羽绒服销量**：通常呈负协方差，气温升高时销量下降。

## 考研重点

- **常考题型**：选择题（协方差符号含义）、计算题（由协方差求 r）、简答题（协方差与相关系数的区别）。
- **易混淆点**：
  - 协方差大小不能直接比较关系强弱；
  - 协方差为 0 只说明没有线性共变，不排除其他关系；
  - 样本协方差分母为 n−1，不是 n。
- **记忆口诀**："协方差看同反向，正负同变与反变；单位依赖难比较，标准化后成 r 看。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 4、7 章；甘怡群《心理与行为科学统计》第 5 章。
- 经典论文：Galton, F. (1886). Regression towards mediocrity in hereditary stature. *Journal of the Anthropological Institute*, 15, 246–263.
- 网页/综述：Gravetter, F. J., & Wallnau, L. B. (2017). *Statistics for the Behavioral Sciences* (10th ed.). Cengage Learning.
