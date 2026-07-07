---
concept: wilcoxon_signed_rank_test
concept_cn: Wilcoxon符号秩检验
domain: psychometrics
tags:
- 学科/统计与测量
- 非参数检验
- Wilcoxon符号秩检验
- 配对样本
- 秩次检验
- 心理统计
citekeys: []
relations:
- target: nonparametric_tests
  type: is-a
- target: mann_whitney_u_test
  type: contrasts
- target: paired_samples_t_test
  type: contrasts
---

# Wilcoxon 符号秩检验 / Wilcoxon Signed-Rank Test

## 定义

Wilcoxon 符号秩检验是一种用于配对样本或相关样本的非参数检验，通过比较差值的符号与秩次，判断两组相关测量是否存在系统性差异。

## 核心要点

- **适用数据**：配对样本、重复测量、前后测设计；数据为连续或顺序变量。
- **核心思想**：计算每对观测的差值，对差值绝对值编秩，再分别计算正秩和 $W^+$ 与负秩和 $W^-$。
- **统计量**：取 $T = \min(W^+, W^-)$ 作为检验统计量。
- **零假设 H₀**：配对差值的中位数为 0（两组相关测量无系统差异）。
- **大样本近似**：当 n > 15 或 20 时，T 近似正态分布：$Z = \frac{T - \frac{n(n+1)}{4}}{\sqrt{\frac{n(n+1)(2n+1)}{24}}}$。
- **与配对 t 检验关系**：当差值正态分布时，配对 t 检验功效更高；非正态或有异常值时优先使用 Wilcoxon 符号秩检验。

## 理论背景

- **提出者/流派**：由 Frank Wilcoxon 于 1945 年提出，是符号检验的改进版，充分利用了差值大小信息。
- **发展脉络**：符号检验 → Wilcoxon 符号秩检验 → Friedman 检验（多组配对）→ 现代配对秩方法。
- **关键假设**：配对观测相关；差值分布对称；差值至少为顺序尺度。

## 经典实验

- **Wilcoxon (1945) 原始论文**：提出符号秩检验，用于比较成对生物测定数据。
- **临床试验前后测**：评估同一组患者治疗前后的症状评分变化。

## 评价与争议

- **优势**：
  - 比简单符号检验功效更高，利用了差值大小信息；
  - 不依赖正态分布假设；
  - 对异常值相对稳健。
- **争议/反例**：
  - 差值为 0 的样本需剔除，减少有效样本量；
  - 差值分布不对称时解释受限；
  - 存在结值时需校正秩次。
- **与相近概念的区别**：Wilcoxon 符号秩检验用于配对样本；Mann-Whitney U 用于独立样本；符号检验只考虑差值符号，不利用大小信息。

## 生活实例

- **减肥药效果评估**：同一批受试者服药前后体重比较。
- **培训课程效果**：学员培训前后测试成绩对比。

## 考研重点

- **常考题型**：名词解释、选择题（与配对 t 检验选择）、简答题（Wilcoxon 与 Mann-Whitney U 区别）。
- **易混淆点**：
  - Wilcoxon 符号秩检验用于配对/相关样本；
  - 差值为 0 的观测不参与计算；
  - 不是 Mann-Whitney U 检验。
- **记忆口诀**："配对前后比差值，绝对值编秩再符号；正秩负秩取最小，符号检验更进步。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 10 章；甘怡群《心理与行为科学统计》第 12 章。
- 经典论文：Wilcoxon, F. (1945). Individual comparisons by ranking methods. *Biometrics Bulletin*, 1(6), 80–83.
- 网页/综述：DataCamp. (n.d.). Kruskal-Wallis Test: Comparing Multiple Groups Without Normality. https://www.datacamp.com/tutorial/kruskal-wallis-test
