---
concept: regression_equation
concept_cn: 回归方程
domain: psychometrics
tags:
- 学科/统计与测量
- 回归方程
- 线性回归
- 回归系数
- 预测
- 心理统计
citekeys: []
relations:
- target: correlation_and_regression
  type: part-of
- target: linear_regression
  type: part-of
- target: multiple_regression
  type: part-of
- target: least_squares_method
  type: supports
- target: standard_error_of_estimate
  type: supports
---

# 回归方程 / Regression Equation

## 定义

回归方程是用数学形式表达自变量与因变量之间预测关系的方程，通过样本数据估计参数后，可用于预测或解释因变量的变化。

## 核心要点

- **简单线性回归方程**：$\hat{Y} = a + bX$
  - $\hat{Y}$：因变量预测值；
  - $a$：截距，X=0 时的预测值；
  - $b$：回归系数/斜率，X 每变化一个单位时 Y 的变化量。
- **多元回归方程**：$\hat{Y} = a + b_1X_1 + b_2X_2 + \dots + b_kX_k$，每个 $b_i$ 表示控制其他自变量后 $X_i$ 对 Y 的独立贡献。
- **参数估计**：通常采用最小二乘法，使残差平方和最小。
- **回归系数解释**：
  - 简单回归中，$b = r \cdot \frac{S_Y}{S_X}$；
  - 多元回归中，偏回归系数需考虑自变量间的相关。
- **预测与误差**：预测值与实际值之差称为残差，残差分布反映模型拟合优劣。

## 理论背景

- **提出者/流派**：回归方程的形式由 Galton、Pearson、Yule 等人发展；最小二乘参数估计由 Gauss 与 Legendre 奠定。
- **发展脉络**：简单回归方程 → 多元回归方程 → 矩阵形式的广义线性模型 → 非线性回归与机器学习预测模型。
- **关键假设**：自变量与因变量关系形式正确；残差独立同分布；无严重多重共线性（多元回归）。

## 经典实验

- **Galton 身高回归方程**：最早用回归方程描述亲子身高关系，揭示"向均值回归"现象。
- **Yule (1897) 贫困率回归研究**：用多元回归方程分析英国贫困率与社会经济因素关系。

## 评价与争议

- **优势**：
  - 将关系量化为可操作的预测工具；
  - 参数具有明确解释意义；
  - 多元回归可控制混淆变量。
- **争议/反例**：
  - 回归方程只反映统计关系，不等于因果关系；
  - 方程外推预测可能严重失真；
  - 多重共线性会使偏回归系数不稳定。
- **与相近概念的区别**：回归方程是数学表达式；回归分析是方法学总称；回归系数是方程中的参数。

## 生活实例

- **体重预测 BMI**：建立"体重 = a + b×身高"的回归方程，用于健康筛查。
- **高考成绩预测**：用模考分数、学习时长等自变量建立多元回归方程预测高考成绩。

## 考研重点

- **常考题型**：计算题（建立回归方程、由 X 预测 Ŷ）、选择题（回归系数含义）、简答题（简单回归与多元回归方程区别）。
- **易混淆点**：
  - 简单回归方程只有一个自变量，多元回归有多个；
  - 多元回归系数是"偏"系数，需控制其他变量后解释；
  - 截距 a 有时无实际意义（如 X=0 不在观测范围内）。
- **记忆口诀**："Y 帽等于 a 加 bX，多元加上若干项；回归系数要偏着看，预测别出样本边。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8 章；甘怡群《心理与行为科学统计》第 7 章。
- 经典论文：Yule, G. U. (1897). On the theory of correlation. *Journal of the Royal Statistical Society*, 60(4), 812–854.
- 网页/综述：Online Statistics Book. (n.d.). Prediction (continued). https://onlinestatbook.com/2/regression/accuracy.html
