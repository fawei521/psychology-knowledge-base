---
concept: three_parameter_logistic_model
concept_cn: 三参数Logistic模型
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- 3PL
- 猜测参数
- 难度
- 区分度
citekeys: []
relations:
- target: item_response_theory
  type: is-a
- target: item_characteristic_curve
  type: applies-to
- target: irt_assumptions
  type: supports
- target: two_parameter_logistic_model
  type: extends
- target: item_information_function
  type: supports
---

# 三参数 Logistic 模型 / Three-Parameter Logistic Model (3PL)

## 定义

三参数 Logistic 模型（3PL）在项目反应理论的双参数模型基础上增加猜测参数 c，用于描述低能力者因随机猜测而答对项目的概率。

## 核心要点

- **公式**：$P_i(\theta) = c_i + \frac{1 - c_i}{1 + e^{-Da_i(\theta - b_i)}}$，其中 a_i 为区分度，b_i 为难度，c_i 为猜测参数，D ≈ 1.702。
- **猜测参数 c**：表示能力极低者答对项目的概率，通常等于选择题选项数的倒数（如四选题 c ≈ 0.25）。
- **ICC 特征**：曲线下渐近线位于 c，低能力者答对概率不会趋近于 0。
- **拐点概率**：ICC 拐点处的答对概率为 $\frac{1+c}{2}$，不再像 1PL/2PL 那样等于 0.5。
- **适用场景**：多项选择题、高利害大规模考试（如 SAT、GRE、高考）。
- **参数估计挑战**：c 的估计需要较大样本，小样本中容易出现边界估计或收敛问题。

## 理论背景

- **提出者/流派**：3PL 由 Birnbaum（1968）在 Lord 的 IRT 框架下提出，用于处理多项选择题中的随机猜测。
- **发展脉络**：1PL → 2PL → 3PL → 多级评分模型与题组模型（testlet model）。
- **关键假设**：在 2PL 假设基础上，增加"低能力者存在非零猜测概率"的假设；仍要求单维性、局部独立性与单调性。

## 经典实验

- **Birnbaum (1968) 3PL 推导与应用**：在经典教材中证明 3PL 能更好拟合多项选择测验数据。
- **SAT 数学部分项目校准**：College Board 使用 3PL 估计题目参数，并据此进行等值与题库管理。

## 评价与争议

- **优势**：
  - 能处理多项选择题的随机猜测；
  - 对低能力被试的能力估计更准确。
- **争议/反例**：
  - c 参数估计不稳定，尤其在小样本中；
  - 增加参数后模型更复杂，拟合检验更困难；
  - "成功猜测" 是否真正随机存在争议。
- **与相近概念的区别**：3PL 是 2PL 的扩展；1PL/2PL 假设 c=0；Rasch 模型完全不考虑猜测。

## 生活实例

- **驾照理论考试**：四选一题目即使完全不会也有一定概率猜对，3PL 中的 c 参数可表示这种猜测概率。
- **高考英语阅读理解**：选项含干扰项，低能力考生仍可能蒙对部分题目，3PL 更合适。

## 考研重点

- **常考题型**：选择题（3PL 参数个数、公式）、简答题（3PL 与 2PL 的区别、何时使用 3PL）。
- **易混淆点**：
  - c 不是"正确率"，而是极低能力者的答对概率；
  - 3PL 拐点概率是 (1+c)/2，不是 0.5；
  - c 越大，曲线整体抬高，但不影响 b 的位置。
- **记忆口诀**："3PL 三个参，a 陡 b 难 c 抬高；多选题里有蒙对，拐点概率一加 c 除以二。"

## 文献来源

- 教材章节：戴海崎《心理与教育测量》第 8 章；漆书青《现代教育与心理测量学原理》第 8 章。
- 经典论文：Birnbaum, A. (1968). Some latent trait models and their use in inferring an examinee's ability. In F. M. Lord & M. R. Novick, *Statistical Theories of Mental Test Scores* (pp. 397–479). Addison-Wesley.
- 网页/综述：Cogn-IQ. (n.d.). Logistic Model in IRT. https://www.cogn-iq.org/learn/theory/logistic-model/
