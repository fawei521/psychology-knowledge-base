---
concept: classical_test_theory
concept_cn: 经典测量理论
domain: psychometrics
tags:
- 学科/统计与测量
- 经典测量理论
- CTT
- 真分数理论
- 信度
- 效度
- 项目分析
citekeys: []
relations:
- target: psychological_measurement_basics
  type: is-a
- target: item_analysis
  type: supports
- target: reliability
  type: supports
- target: validity
  type: supports
- target: item_difficulty
  type: supports
- target: item_discrimination
  type: supports
---

# 经典测量理论 / Classical Test Theory

## 定义

经典测量理论（Classical Test Theory, CTT）是心理与教育测量中最基础的理论框架，其核心假设是观测分数（X）由真分数（T）和测量误差（E）组成，即 X = T + E。

## 核心要点

- **真分数模型**：$X = T + E$，其中 X 为观测分数，T 为真分数，E 为随机误差。
- **随机误差假设**：
  - 误差均值为 0；
  - 误差与真分数相互独立；
  - 不同测量间的误差相互独立。
- **信度定义**：真分数方差与观测分数方差之比，$r_{XX} = \frac{\sigma_T^2}{\sigma_X^2} = 1 - \frac{\sigma_E^2}{\sigma_X^2}$。
- **项目参数依赖样本**：在 CTT 中，项目难度（P 值）和区分度（D 值、rpbis）会随被试样本的能力分布而变化。
- **应用广泛**：CTT 是项目分析、信度分析、效度分析和常模建立的主流工具。

## 理论背景

- **提出者/流派**：Charles Spearman 于 1904 年提出真分数概念； later Gulliksen (1950) 和 Lord & Novick (1968) 将其系统化。
- **发展脉络**：Spearman 的相关与误差理论 → 真分数模型 → CTT 体系化 → 与项目反应理论（IRT）并存，互为补充。
- **关键假设**：
  - 测量误差随机且与真分数独立；
  - 测验分数可加；
  - 样本代表性足够。

## 经典实验

- **Spearman (1904) "General Intelligence"**：通过相关矩阵提出一般能力因子 g，并讨论测量误差对观测相关的影响，奠定真分数理论基础。
- **Gulliksen (1950) *Theory of Mental Tests***：系统总结 CTT 的信度、效度、项目分析等方法，成为 20 世纪中叶心理测量的标准教材。

## 评价与争议

- **优势**：
  - 理论简单，计算方便，适用于大多数教育测验和问卷调查；
  - 对样本量要求相对较低；
  - 项目分析、信度效度指标直观易懂。
- **争议/反例**：
  - 题目参数（难度、区分度）依赖样本，缺乏跨样本不变性；
  - 无法对不同测验或被试能力进行直接等值比较；
  - 真分数无法直接观测，模型假设在现实中可能不完全成立。
- **与相近理论的区别**：CTT 将题目难度和区分度视为样本依赖指标；IRT 则将题目参数（a, b, c）和被试能力 θ 放在同一潜在特质尺度上估计，具有样本不变性。

## 生活实例

- **期末考试**：教师用 Cronbach's α 评估试卷内部一致性，用项目难度和区分度筛选题目，这些都是 CTT 的应用。
- **人格问卷**：大五人格量表的重测信度、内部一致性信度和效标效度评估均基于 CTT 框架。

## 考研重点

- **常考题型**：选择题（CTT 基本假设）、简答题（CTT 与 IRT 的区别）、计算题（根据真分数模型推导信度）。
- **易混淆点**：
  - CTT 中误差是随机的，系统误差不归入 E；
  - 信度是群体概念，不能简单推广到个体分数；
  - CTT 题目参数依赖样本，IRT 参数具有样本不变性。
- **记忆口诀**："X 等于 T 加 E，误差随机均值为零；CTT 简单好用，IRT 更精细。"

## 文献来源

- 教材章节：郑日昌《心理测量学》第 4 章；戴海崎《心理与教育测量》第 4 章。
- 经典论文：Spearman, C. (1904). "General intelligence," objectively determined and measured. *American Journal of Psychology*, 15(2), 201–292.
- 网页/综述：Lord, F. M., & Novick, M. R. (1968). *Statistical Theories of Mental Test Scores*. Addison-Wesley.
