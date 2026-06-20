---
concept: anova_basics
concept_cn: 方差分析基础
domain: general_psychology
tags: [anova, analysis_of_variance, f_test, post_hoc, tukey_hsd, between_subjects, 学科/统计与测量, 学科/普通心理学]
citekeys: []
relations:
  - target: "hypothesis_testing"
    type: "is-a"
  - target: "t_test"
    type: "extends"
---

# 方差分析基础 / ANOVA Basics

## 定义
方差分析（Analysis of Variance, ANOVA）是通过分解总变异为组间变异与组内变异，并计算 F 比值，来检验三组及以上均值差异是否显著的参数检验方法。

## 核心要点
- 要点1：基本思想——将总平方和（SST）分解为组间平方和（SSB）与组内平方和（SSW）；F = MSB / MSW。
- 要点2：单因素被试间方差分析——一个自变量，被试只接受一个水平；F 显著说明至少有一组均值与其他组不同。
- 要点3：事后检验——F 显著后，需用 Tukey HSD、Bonferroni、Scheffé 等方法比较具体组间差异，控制族系错误率。
- 要点4：效应量——常用 η²（eta-squared）或 ω²（omega-squared）表示自变量解释因变量变异的百分比；一般标准：.01 小、.06 中、.14 大。
- 要点5：基本假设——独立性、正态性、方差齐性（可用 Levene 检验）；违背假设时可用非参数替代（Kruskal-Wallis）或稳健方差分析。

## 理论背景
- 提出者/流派：Ronald A. Fisher 在 20 世纪 20 年代提出，最初用于农业实验；后广泛应用于心理学、教育学、医学等领域。
- 发展脉络：单因素 ANOVA → 多因素 ANOVA → 重复测量 ANOVA → 协方差分析（ANCOVA） → 多层线性模型（HLM）。
- 关键假设：各组观测独立；因变量在各组内近似正态分布；各组方差齐性。

## 经典实验/研究
- **Fisher 农业实验（1920s）**
  - 设计：比较不同肥料处理下作物产量
  - 贡献：提出方差分解与 F 检验，解决多组比较时多次 t 检验导致 Type I 错误膨胀的问题
- **心理学中的单因素 ANOVA 应用**
  - 例如比较三种教学方法对学生成绩的影响
  - 相比做 3 次 t 检验，ANOVA 将整体 α 控制在 .05

## 评价与争议
- 优势：有效控制多组比较时的族系错误率；可扩展至多因素、重复测量等复杂设计。
- 争议/反例：
  - F 显著只能说明“至少有一组不同”，不能指出具体哪一组不同，必须配合事后检验。
  - 方差不齐或样本量不等时，传统 F 检验不够稳健。
  - ANOVA 只告诉组间差异是否存在，不说明因果关系；因果推断依赖实验设计。
- 与相近概念的区别：
  - ANOVA 用于三组及以上均值比较；t 检验是两组均值的特例。
  - 事后检验（post-hoc） ≠ 计划比较（planned comparison）：前者在 F 显著后探索性进行，后者在研究前确定。

## 生活实例
- 例1：比较三种广告策略对购买意愿的影响，使用单因素 ANOVA 分析三组均值差异。
- 例2：研究四种训练方案对运动员反应时的影响，F 显著后再用 Tukey HSD 找出哪些方案之间存在显著差异。

## 考研重点
- 常考题型：名词解释（方差分析、F 检验、事后检验、η²）、简答题（ANOVA 与多次 t 检验的区别）、计算题（填写 ANOVA 表）。
- 易混淆点：F 显著 ≠ 所有组之间都不同；η² 与 ω² 都反映效应量，但 ω² 对总体估计更无偏。
- 记忆口诀：“总变异分两组，F比越大越显著；Tukey 事后找差异，eta平方看大小。”

## 文献来源
- 教材章节：张厚粲《现代心理与教育统计学》第10章；舒华《心理与教育研究中的多因素实验设计》
- 经典论文：Fisher, R. A. (1925). *Statistical methods for research workers*.; Tukey, J. W. (1949). Comparing individual means in the analysis of variance. *Biometrics*.
