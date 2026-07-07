---
concept: multiple_regression
concept_cn: 多元回归
domain: psychometrics
tags:
- 学科/统计与测量
- 多元回归
- 多重回归
- 自变量
- 偏回归系数
- 心理统计
citekeys: []
relations:
- target: correlation_and_regression
  type: part-of
- target: linear_regression
  type: extends
- target: regression_equation
  type: part-of
- target: coefficient_of_determination
  type: supports
- target: least_squares_method
  type: supports
- target: standard_error_of_estimate
  type: supports
---

# 多元回归 / Multiple Regression

## 定义

多元回归（Multiple Regression）是包含两个或两个以上自变量的线性回归方法，用于同时考察多个自变量对因变量的独立预测作用。

## 核心要点

- **回归方程**：$\hat{Y} = a + b_1X_1 + b_2X_2 + \dots + b_kX_k$
  - $b_i$：偏回归系数，表示控制其他自变量后，$X_i$ 对 Y 的净效应。
- **复相关系数 R**：因变量 Y 与所有自变量线性组合之间的相关，$R^2$ 即多元决定系数。
- **调整 R²**：$R^2_{\text{adj}} = 1 - \frac{(1-R^2)(n-1)}{n-k-1}$，用于校正自变量个数带来的虚高。
- **整体显著性**：用 F 检验判断所有自变量 jointly 是否显著预测 Y。
- **各自变量显著性**：用 t 检验判断每个偏回归系数是否显著不为 0。
- **前提假设**：线性关系、残差正态独立同分布、方差齐性、自变量间无严重多重共线性。

## 理论背景

- **提出者/流派**：多元回归由 Yule、Pearson 与 Fisher 等人在 19 世纪末 20 世纪初发展。
- **发展脉络**：简单回归 → 多元回归 → 逐步回归 → 岭回归/Lasso 等正则化方法 → 结构方程模型。
- **关键假设**：自变量间不存在完全多重共线性；样本量应远大于自变量个数（通常 n > 10k 或 n > 50+8k）。

## 经典实验

- **Yule (1899) 贫困原因研究**：最早使用多元回归分析英国贫困率与教育、人口迁移等因素的关系。
- **Duncan 职业声望研究**：用父亲教育、父亲职业、本人教育等自变量预测职业声望，成为社会科学多元回归经典案例。

## 评价与争议

- **优势**：
  - 可同时控制多个变量，评估各自变量的独立效应；
  - 提高预测精度；
  - 是路径分析、结构方程模型的基础。
- **争议/反例**：
  - 多重共线性使偏回归系数不稳定；
  - 自变量选择（逐步回归）可能产生过拟合；
  - 统计控制不等于实验控制，仍不能推断因果。
- **与相近概念的区别**：简单回归只有一个自变量；多元回归有多个自变量；Logistic 回归用于因变量为分类变量的情形。

## 生活实例

- **房价预测**：同时用面积、地段、房龄、楼层等多个因素预测房价。
- **心理健康研究**：用生活压力、社会支持、人格特质同时预测抑郁水平。

## 考研重点

- **常考题型**：选择题（偏回归系数含义、调整 R² 作用）、简答题（多元回归与简单回归区别、前提假设）、计算题（求复相关系数 R）。
- **易混淆点**：
  - 偏回归系数不是简单相关系数，需控制其他变量解释；
  - R² 随自变量增加而增加，调整 R² 不一定；
  - 自变量多不等于模型好，需考虑样本量与多重共线性。
- **记忆口诀**："多元回归多自变，偏回归系数看净效；复 R 平方总解释，调整之后不虚高。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 9 章；甘怡群《心理与行为科学统计》第 9 章。
- 经典论文：Yule, G. U. (1899). An investigation into the causes of changes in pauperism in England, chiefly during the last two intercensal decades. *Journal of the Royal Statistical Society*, 62(2), 249–295.
- 网页/综述：Gravetter, F. J., & Wallnau, L. B. (2017). *Statistics for the Behavioral Sciences* (10th ed.). Cengage Learning.
