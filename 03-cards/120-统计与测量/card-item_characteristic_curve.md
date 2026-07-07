---
concept: item_characteristic_curve
concept_cn: 项目特征曲线
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- 项目特征曲线
- ICC
- 难度
- 区分度
citekeys: []
relations:
- target: item_response_theory
  type: part-of
- target: irt_assumptions
  type: supports
- target: one_parameter_logistic_model
  type: applies-to
- target: two_parameter_logistic_model
  type: applies-to
- target: three_parameter_logistic_model
  type: applies-to
- target: item_information_function
  type: supports
---

# 项目特征曲线 / Item Characteristic Curve (ICC)

## 定义

项目特征曲线（Item Characteristic Curve, ICC）是项目反应理论中描述被试潜在能力水平 θ 与答对（或赞同）某项目概率 P(θ) 之间关系的 S 型曲线。

## 核心要点

- **曲线形态**：标准 ICC 为 S 型 Logistic（或正态卵形）曲线，纵轴为作答概率，横轴为能力 θ。
- **难度参数 b**：曲线拐点的 θ 值，b 越大表示项目越难。
- **区分度参数 a**：曲线在拐点处的斜率，a 越大表示项目区分高低能力者越敏锐。
- **猜测参数 c**：曲线下渐近线高度，表示低能力者随机猜对的概率（多见于 3PL）。
- **1PL ICC**：所有项目曲线形状相同，仅位置（难度）不同。
- **2PL ICC**：曲线陡峭程度可不同，项目间区分度可以差异。
- **3PL ICC**：曲线下端被抬高，低能力者也有一定正确概率。

## 理论背景

- **提出者/流派**：ICC 的概念由 Lord 与 Birnbaum 在 20 世纪 50–60 年代发展起来，受生物检定中剂量-反应曲线的启发。
- **发展脉络**：正态卵形模型 → Logistic 模型 → 多级评分模型（GRM、PCM）→ 多维 ICC。
- **关键假设**：单调性、局部独立性、正确模型形式（Logistic 或正态卵形）。

## 经典实验

- **Birnbaum (1968) Logistic 模型化简**：证明 Logistic 函数可很好近似正态卵形 ICC，且计算更简便。
- **SAT 数学项目 ICC 校准**：ETS 在大规模题库中用 ICC 参数筛选和等值题目。

## 评价与争议

- **优势**：
  - 可视化项目在不同能力水平的 functioning；
  - 参数含义清晰，便于题目质量诊断。
- **争议/反例**：
  - 单选猜测题若不用 3PL，ICC 下端会低估低能力者答对概率；
  - 人格/态度项目可能出现非单调 ICC，需要用理想点模型。
- **与相近概念的区别**：ICC 描述单个项目的 θ-P 关系；TCC（测验特征曲线）描述整个测验的期望总分与 θ 的关系。

## 生活实例

- **驾照理论考试题库**：高难度法规题 ICC 拐点靠右，简单常识题拐点靠左；区分度高的题目曲线陡峭。
- **在线学习平台**：根据学生能力推荐题目时，平台内部依赖 ICC 预测答对概率。

## 考研重点

- **常考题型**：名词解释（ICC）、选择题（参数与曲线形态关系）、简答题（如何利用 ICC 评价项目）。
- **易混淆点**：
  - b 是拐点位置，不是正确率 50% 点（3PL 中拐点概率 = (1+c)/2）；
  - a 越大曲线越陡，不代表题目越难；
  - ICC 下方面积无特殊含义。
- **记忆口诀**："S 型曲线 ICC，拐点难度 b 来定；斜率 a 大区分强，c 抬下限防乱蒙。"

## 文献来源

- 教材章节：戴海崎《心理与教育测量》第 8 章；漆书青《现代教育与心理测量学原理》第 7 章。
- 经典论文：Birnbaum, A. (1968). Some latent trait models and their use in inferring an examinee's ability. In F. M. Lord & M. R. Novick, *Statistical Theories of Mental Test Scores* (pp. 397–479). Addison-Wesley.
- 网页/综述：Cogn-IQ. (n.d.). Logistic Model in IRT. https://www.cogn-iq.org/learn/theory/logistic-model/
