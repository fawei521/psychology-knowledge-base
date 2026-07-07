---
concept: mediation_and_moderation
concept_cn: 中介与调节
domain: experimental_psychology
tags: [experimental_psychology, statistics, research_methods, causal_inference, regression]
relations:
  - target: advanced_experimental_design
    type: part-of
---

# 中介与调节 / Mediation and Moderation

## 定义
中介（mediation）与调节（moderation）是解释自变量 X 如何影响因变量 Y 的两类统计概念：**中介变量 M 揭示作用机制**（how/why），**调节变量 W 揭示边界条件**（when/for whom）。

## 核心要点
- **中介模型**：X → M → Y。
  - 总效应 c = 直接效应 c' + 间接效应 ab。
  - 完全中介：c' 不显著；部分中介：c' 显著但减小。
- **调节模型**：Y = b₀ + b₁X + b₂W + b₃XW。
  - 交互项 XW 显著，说明 X 对 Y 的作用随 W 水平变化。
- **有调节的中介（moderated mediation）**：间接效应 ab 随调节变量水平变化。
- **有中介的调节（mediated moderation）**：交互效应通过中介变量传递。
- 现代分析工具：**Hayes PROCESS 宏**、结构方程模型（SEM）、多层模型、贝叶斯方法。

## 理论背景
- **Baron & Kenny（1986）**：提出经典四步因果步骤法，区分中介与调节变量。
- **MacKinnon（2008）**：推广基于间接效应与置信区间的方法。
- **Hayes（2013, 2018）**：发展 PROCESS 宏与条件过程分析，主张以 Bootstrap 置信区间取代 Sobel 检验。
- **Preacher & Hayes（2004, 2008）**：推动 Bootstrap 与多重中介分析。

## 经典实验
- **Baron & Kenny 的社会支持-压力-健康研究示例**：解释社会支持如何通过缓冲压力影响健康。
- **Hayes 条件过程分析示例**：检验自尊在负面反馈与情绪反应之间的调节作用。
- **实验性中介研究**：通过操纵中介过程（如情绪诱发）来强化因果推断。

## 评价与争议
- **优势**：
  - 中介分析揭示心理机制，提升理论深度。
  - 调节分析明确效应边界，增强实践针对性。
  - 二者结合可回答更复杂的因果问题。
- **批评**：
  - Baron & Kenny 四步法统计效力低、对总效应要求过强，已被现代方法取代。
  - 横截面数据难以确立时间优先性与因果方向。
  - 模型等价性问题：同一数据可能对应多个因果模型。
- **与实验设计的关系**：
  - 随机化实验可确立 X→Y 因果；中介分析需额外设计（如实验性中介、纵向设计）才能强化 M 的因果解释。
  - 调节分析可与实验结合，检验干预效果在不同亚群体中的差异。

## 生活实例
- **中介**：运动（X）通过改善睡眠质量（M）提升学业表现（Y）。
- **调节**：社会支持（W）缓冲压力（X）对抑郁（Y）的影响，即高支持时压力影响更小。
- **有调节的中介**：冥想训练对焦虑的间接效应在情绪调节能力高的人群中更强。

## 考研重点
- **常考题型**：名词解释“中介变量/调节变量”；比较中介与调节；设计一个包含中介或调节的研究。
- **易混淆点**：
  - 中介解释“为什么”，调节解释“对谁/何时”。
  - 完全中介与部分中介的判定。
  - 调节效应通过交互项检验，而非相关或简单斜率。
- **记忆口诀**：
  - “中介走机制 X→M→Y，调节看边界 XW 交互；Bootstrap 区间定间接，条件过程两相宜。”

## 文献来源
- Baron, R. M., & Kenny, D. A. (1986). The moderator-mediator variable distinction in social psychological research. *Journal of Personality and Social Psychology, 51*(6), 1173–1182.
- Hayes, A. F. (2018). *Introduction to Mediation, Moderation, and Conditional Process Analysis* (2nd ed.). Guilford Press.
- MacKinnon, D. P. (2008). *Introduction to Statistical Mediation Analysis*. Erlbaum.
- Preacher, K. J., & Hayes, A. F. (2008). Asymptotic and resampling strategies for assessing and comparing indirect effects in multiple mediator models. *Behavior Research Methods, 40*(3), 879–891.
- 温忠麟, 张雷, 侯杰泰. (2006). 有中介的调节变量和有调节的中介变量. *心理学报, 38*(3), 448–452.
