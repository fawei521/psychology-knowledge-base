---
concept: standard_error_of_estimate
concept_cn: 估计标准误差
domain: psychometrics
tags:
- 学科/统计与测量
- 估计标准误差
- 回归误差
- 残差
- 预测精度
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
- target: least_squares_method
  type: supports
---

# 估计标准误差 / Standard Error of Estimate

## 定义

估计标准误差（Standard Error of Estimate, SEE）是回归模型中预测值与实际观测值之间残差的标准差，反映回归方程预测因变量时的平均误差大小。

## 核心要点

- **公式（简单线性回归）**：$S_e = \sqrt{\frac{\sum (Y_i - \hat{Y}_i)^2}{n-2}} = \sqrt{\frac{SS_{\text{残差}}}{n-2}}$
- **公式（多元回归）**：$S_e = \sqrt{\frac{\sum (Y_i - \hat{Y}_i)^2}{n-k-1}}$，其中 k 为自变量个数。
- **与残差的关系**：SEE 本质上是残差的标准差，衡量数据点围绕回归线的离散程度。
- **与 R² 的关系**：$S_e = \sqrt{\frac{(1-R^2) \cdot SS_Y}{n-2}}$；R² 越大，SEE 越小，预测越精确。
- **解释**：约 68% 的观测值落在回归线 ±1 个 SEE 范围内（近似正态残差假设下）。
- **应用**：评估回归方程预测精度；构建预测区间。

## 理论背景

- **提出者/流派**：估计标准误差概念伴随回归分析与最小二乘法发展，Fisher 与 Yule 等人在其应用中明确其意义。
- **发展脉络**：残差概念 → 残差平方和 → 估计标准误差 → 预测区间与标准误差的进一步分解。
- **关键假设**：残差独立、近似正态、方差齐性；模型设定正确。

## 经典实验

- **Galton 身高回归研究**：估计亲子身高回归线的离散程度，是估计标准误差的早期应用雏形。
- **Fisher 方差分析框架**：将残差平方和与自由度结合，给出 SEE 的正式定义。

## 评价与争议

- **优势**：
  - 与原始因变量同单位，解释直观；
  - 直接反映模型预测精度；
  - 可用于构建预测区间。
- **争议/反例**：
  - 受因变量量纲影响，不便于跨研究比较；
  - 异常值会夸大 SEE；
  - 仅反映平均误差，不说明具体预测点的误差。
- **与相近概念的区别**：SEE 是残差的标准差；回归系数标准误衡量参数估计精度；标准误（SE）通常指样本统计量的抽样变异。

## 生活实例

- **高考成绩预测模型**：若 SEE = 15 分，说明用模考分数预测高考成绩的平均误差约为 15 分。
- **房价预测模型**：若 SEE = 10 万元，说明模型预测房价平均偏差约 10 万元。

## 考研重点

- **常考题型**：计算题（由残差平方和求 SEE）、选择题（SEE 含义）、简答题（SEE 与 R² 的关系）。
- **易混淆点**：
  - SEE 与回归系数标准误不同；
  - SEE 越小不代表模型一定更好，需结合 R² 与模型复杂度；
  - 简单回归分母为 n−2，多元回归为 n−k−1。
- **记忆口诀**："估计标准误看残差，平均预测偏多少；R 方越大它越小，分母自由度要记牢。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8 章；甘怡群《心理与行为科学统计》第 7 章。
- 经典论文：Fisher, R. A. (1925). *Statistical Methods for Research Workers*. Oliver & Boyd.
- 网页/综述：Online Statistics Book. (n.d.). Standard Error of the Estimate. https://onlinestatbook.com/2/regression/accuracy.html
