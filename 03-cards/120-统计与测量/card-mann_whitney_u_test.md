---
concept: mann_whitney_u_test
concept_cn: Mann-Whitney U检验
domain: psychometrics
tags:
- 学科/统计与测量
- 非参数检验
- Mann-Whitney U
- 秩和检验
- 两独立样本
- 心理统计
citekeys: []
relations:
- target: nonparametric_tests
  type: is-a
- target: wilcoxon_signed_rank_test
  type: contrasts
- target: kruskal_wallis_h_test
  type: extends
- target: independent_samples_t_test
  type: contrasts
---

# Mann-Whitney U 检验 / Mann-Whitney U Test

## 定义

Mann-Whitney U 检验（又称 Wilcoxon 秩和检验）是一种用于比较两个独立样本分布位置差异的非参数检验，是独立样本 t 检验的非参数替代方法。

## 核心要点

- **适用数据**：两个独立样本，因变量为连续或顺序变量，且不满足正态分布或方差齐性假设。
- **核心思想**：将两组数据合并排序后赋秩，通过比较两组秩和判断分布差异。
- **统计量**：
  - $U_1 = n_1n_2 + \frac{n_1(n_1+1)}{2} - R_1$
  - $U_2 = n_1n_2 + \frac{n_2(n_2+1)}{2} - R_2$
  - 取 $U = \min(U_1, U_2)$
- **零假设 H₀**：两组数据来自相同分布（或中位数相同，分布形状相同时）。
- **大样本近似**：当 n₁、n₂ 较大时，U 近似正态分布，可用 Z 检验。
- **与 t 检验关系**：当数据正态时，t 检验功效更高；非正态或存在异常值时优先使用 U 检验。

## 理论背景

- **提出者/流派**：由 H. B. Mann 与 D. R. Whitney 于 1947 年提出；F. Wilcoxon 于 1945 年独立提出等价形式（秩和检验）。
- **发展脉络**：两样本秩和检验 → Kruskal-Wallis 多组扩展 → 现代秩检验与稳健统计。
- **关键假设**：两组样本相互独立；因变量至少为顺序尺度；两组分布形状相似（用于中位数解释）。

## 经典实验

- **Mann & Whitney (1947) 原始论文**：从随机性角度证明 U 统计量的分布性质。
- **临床疗效比较**：用于比较两种药物在小型非正态样本中的疗效差异。

## 评价与争议

- **优势**：
  - 不依赖正态分布假设；
  - 对异常值稳健；
  - 可处理顺序数据。
- **争议/反例**：
  - 严格来说是检验分布是否相同，只有在分布形状相同时才等价于中位数检验；
  - 存在结值（ties）时需要校正；
  - 功效低于 t 检验（正态数据时）。
- **与相近概念的区别**：Mann-Whitney U 用于独立样本；Wilcoxon 符号秩检验用于配对样本；Kruskal-Wallis 用于三组及以上。

## 生活实例

- **两种教学方法效果比较**：比较实验班与对照班的成绩（成绩偏态分布）。
- **用户满意度评分**：比较两个品牌产品的 1–5 分满意度差异。

## 考研重点

- **常考题型**：名词解释、选择题（U 检验适用条件）、简答题（U 检验与 t 检验区别）。
- **易混淆点**：
  - Mann-Whitney U 与 Wilcoxon 秩和检验等价但提出者不同；
  - 用于独立样本，不是配对样本；
  - 中位数解释需假设两组分布形状相同。
- **记忆口诀**："两组独立非正态，合并排秩比和差；U 小显著分布异，t 正态时它功效差。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 10 章；甘怡群《心理与行为科学统计》第 12 章。
- 经典论文：Mann, H. B., & Whitney, D. R. (1947). On a test of whether one of two random variables is stochastically larger than the other. *Annals of Mathematical Statistics*, 18(1), 50–60.
- 网页/综述：R-statistics.co. (n.d.). Kruskal-Wallis Test in R. https://r-statistics.co/Kruskal-Wallis-Test-in-R.html
