---
concept: pearson_correlation_coefficient
concept_cn: Pearson相关系数
domain: psychometrics
tags:
- 学科/统计与测量
- Pearson相关
- 相关系数
- 线性关系
- 相关分析
- 心理统计
citekeys: []
relations:
- target: correlation_and_regression
  type: part-of
- target: covariance
  type: is-a
- target: linear_regression
  type: correlates-with
- target: coefficient_of_determination
  type: supports
- target: descriptive_statistics
  type: is-a
---

# Pearson 相关系数 / Pearson Correlation Coefficient

## 定义

Pearson 相关系数（r）是衡量两个连续变量之间线性关系强度与方向的标准化指标，取值范围为 −1 到 +1。

## 核心要点

- **公式**：$r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2 \sum (Y_i - \bar{Y})^2}} = \frac{\text{Cov}(X,Y)}{S_X S_Y}$
- **取值解释**：
  - +1：完全正线性相关；
  - −1：完全负线性相关；
  - 0：无线性相关（但可能存在非线性关系）。
- **强度经验标准**：|r| ≈ 0.1 弱相关，0.3 中等，0.5 强相关（社会科学常见标准）。
- **前提假设**：两变量为连续变量、线性关系、近似正态分布、方差齐性、观测独立。
- **显著性检验**：常用 t 检验判断 r 是否显著不为 0，df = n − 2。

## 理论背景

- **提出者/流派**：由 Karl Pearson 于 1896 年基于 Francis Galton 的相关思想系统提出，又称积矩相关系数。
- **发展脉络**：协方差 → Pearson r → 偏相关 → 多元相关 → 其他相关系数（Spearman、Kendall、点二列相关等）。
- **关键假设**：变量为等距或比率量表；关系为线性；异常值会显著影响 r。

## 经典实验

- **Galton 人体测量研究**：发现父子身高、兄弟身高之间的相关，为 Pearson r 的发展奠定经验基础。
- **Pearson (1896) 公式推导**：将 Galton 的相关系数思想数学化，提出现代 Pearson 积矩相关系数。

## 评价与争议

- **优势**：
  - 计算简单，解释直观；
  - 标准化指标，便于跨研究比较；
  - 是回归分析与因素分析的基础。
- **争议/反例**：
  - 对异常值敏感；
  - 只能反映线性关系；
  - 存在"相关不等于因果"的误用风险；
  - 受样本量与取值范围影响。
- **与相近概念的区别**：Pearson r 适用于连续变量；Spearman 等级相关适用于顺序变量；点二列相关适用于一个连续、一个真正的二分变量。

## 生活实例

- **体重与身高**：在成年人中，体重与身高通常呈中等正相关。
- **考试焦虑与成绩**：研究发现两者常呈负相关，即焦虑越高，成绩可能越低。

## 考研重点

- **常考题型**：计算题（求 r、解释 r 含义）、选择题（r 取值意义）、简答题（使用前提与局限）。
- **易混淆点**：
  - r = 0 不代表无关，只说明没有线性关系；
  - r 无量纲，不受测量单位影响；
  - 相关显著不代表效应量大。
- **记忆口诀**："Pearson r 看线性，正负方向强弱明；零非无关非因果，异常分布要小心。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 7 章；甘怡群《心理与行为科学统计》第 6 章。
- 经典论文：Pearson, K. (1896). Mathematical contributions to the theory of evolution—III. Regression, heredity, and panmixia. *Philosophical Transactions of the Royal Society A*, 187, 253–318.
- 网页/综述：Cogn-IQ. (n.d.). Pearson Correlation Coefficient. https://www.cogn-iq.org/learn/theory/pearson-correlation/
