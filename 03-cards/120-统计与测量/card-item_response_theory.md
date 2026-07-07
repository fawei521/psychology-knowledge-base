---
concept: item_response_theory
concept_cn: 项目反应理论
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- IRT
- 潜变量
- 心理测量
- 现代测量理论
citekeys: []
relations:
- target: classical_test_theory
  type: extends
- target: irt_assumptions
  type: part-of
- target: item_characteristic_curve
  type: part-of
- target: item_information_function
  type: part-of
- target: test_information_function
  type: part-of
- target: one_parameter_logistic_model
  type: part-of
- target: two_parameter_logistic_model
  type: part-of
- target: three_parameter_logistic_model
  type: part-of
---

# 项目反应理论 / Item Response Theory (IRT)

## 定义

项目反应理论（Item Response Theory, IRT）是一类现代心理与教育测量理论，通过建立被试潜在特质水平（θ）与项目作答概率之间的数学模型，来刻画每个项目在不同能力水平上的测量特性。

## 核心要点

- **潜变量取向**：将被试能力视为连续潜变量 θ，而非用原始总分直接代表能力。
- **项目参数化**：每个项目可用区分度 a、难度 b、猜测度 c 等参数描述其测量功能。
- **项目特征曲线（ICC）**：以曲线形式表示不同能力水平下答对/赞同某项目的概率。
- **信息函数**：项目信息函数 IIF 与测验信息函数 TIF 用于评估在不同 θ 水平上的测量精度。
- **模型族**：最常见的是单参数、双参数、三参数 Logistic 模型（1PL/2PL/3PL），以及 Rasch 模型。
- **应用优势**：可进行计算机自适应测验（CAT）、项目功能差异（DIF）分析、测验等值、题库建设等。

## 理论背景

- **提出者/流派**：IRT 的理论根源可追溯至 Lawley（1943）与 Tucker，现代形式由丹麦数学家 Georg Rasch（1960）与美国心理测量学家 Frederic Lord（1952）分别发展。
- **发展脉络**：经典测验理论（CTT）的局限 → IRT/Rasch 潜变量模型 → 参数估计方法（MLE、EAP、MCMC）→ 计算机自适应测验与大规模题库系统。
- **关键假设**：单维性、局部独立性、单调性、模型正确设定、项目不变性。

## 经典实验

- **Rasch (1960) 丹麦教育测验研究**：Rasch 在阅读测验中提出项目与被试可加性测量模型，奠定 Rasch 测量基础。
- **Lord (1952) 美国军事选拔测验研究**：提出基于正态分布与 Logistic 曲线的项目参数模型，推动 IRT 在美国大规模测验中的应用。

## 评价与争议

- **优势**：
  - 能力与项目参数分离，样本独立性优于 CTT；
  - 可对不同能力水平提供差异化测量精度；
  - 支持自适应测验与等值。
- **争议/反例**：
  - 大样本需求，小样本参数估计不稳定；
  - 单维假设在实际量表中常被违反；
  - 模型拟合检验复杂，易被误用。
- **与相近概念的区别**：CTT 以总分为中心，IRT 以潜变量 θ 为中心；Rasch 模型强调测量结构的可加性，1PL-IRT 更偏向统计拟合。

## 生活实例

- **托福/雅思自适应测验**：根据考生答题表现动态选择下一题难度，即基于 IRT 的计算机自适应测验。
- **医院焦虑抑郁量表（HADS）的精简版开发**：用 IRT 筛选信息量最大的项目，构建短版本量表。

## 考研重点

- **常考题型**：名词解释（IRT、ICC、信息函数）、简答题（IRT 与 CTT 的区别、IRT 基本假设）、选择题（模型参数含义）。
- **易混淆点**：
  - IRT 的"信息"不是日常语义的信息量，而是测量精度；
  - 1PL 不等于 Rasch，虽然公式相似但理论基础不同；
  - 局部独立是"控制 θ 后"独立，不是样本层面的独立。
- **记忆口诀**："潜变量、项目参，ICC 曲线看概率；单维局部加单调，信息函数定精度。"

## 文献来源

- 教材章节：戴海崎《心理与教育测量》第 8 章；漆书青《现代教育与心理测量学原理》第 7–9 章。
- 经典论文：Rasch, G. (1960). *Probabilistic Models for Some Intelligence and Attainment Tests*. Danish Institute for Educational Research.
- 网页/综述：Lord, F. M. (1952). A theory of test scores (Psychometric Monograph No. 7). Psychometric Society.
