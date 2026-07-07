---
concept: irt_assumptions
concept_cn: IRT基本假设
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- IRT假设
- 单维性
- 局部独立性
- 心理测量
citekeys: []
relations:
- target: item_response_theory
  type: part-of
- target: item_characteristic_curve
  type: supports
- target: one_parameter_logistic_model
  type: supports
- target: two_parameter_logistic_model
  type: supports
- target: three_parameter_logistic_model
  type: supports
- target: item_information_function
  type: supports
---

# IRT 基本假设 / IRT Assumptions

## 定义

IRT 基本假设是指应用项目反应理论模型前需要满足的一系列前提条件，主要包括单维性、局部独立性、单调性、项目不变性和正确模型设定。

## 核心要点

- **单维性（Unidimensionality）**：测验只测量一个主导的潜在特质 θ；可用因素分析或 Stout 检验评估。
- **局部独立性（Local Independence）**：在控制了 θ 之后，被试对不同项目的作答相互独立；常用 Q₃ 统计量检验。
- **单调性（Monotonicity）**：项目作答概率随能力水平单调递增；ICC 应为非递减曲线。
- **项目不变性（Item Invariance）**：项目参数在不同样本（同一 θ 水平）中保持稳定；若不稳定则可能存在项目功能差异（DIF）。
- **正确模型设定（Correct Model Specification）**：所选模型（1PL/2PL/3PL）应能合理拟合数据。
- **非速度性（Non-speededness）**：测验应让被试有足够时间作答，避免速度因素干扰。

## 理论背景

- **提出者/流派**：假设体系由 Rasch、Lord 与 Novick 等人在建立潜变量测量模型时逐步明确。
- **发展脉络**：CTT 对假设要求较宽松 → IRT 提出严格假设 → 假设检验方法（Q₃、因素分析、DIF）不断发展 → 多维 IRT 用于放松单维假设。
- **关键假设**：单维性与局部独立性是 IRT 最核心的两条假设，被形容为"同一枚硬币的两面"。

## 经典实验

- **Yen (1984) Q₃ 统计量研究**：提出用项目残差相关检验局部独立性，成为 IRT 假设检验的经典工具。
- **Chen & Thissen (1997) LDG2 指数**：提出局部依赖 G² 指数，用于检测项目对之间的局部依赖。

## 评价与争议

- **优势**：明确假设使模型可检验，参数估计具有样本独立性。
- **争议/反例**：
  - 实际量表常为多维度，严格单维难以满足；
  - 局部独立性常被忽视，约 36% 的研究未报告检验；
  - 模型误用会导致参数估计偏差。
- **与相近概念的区别**：CTT 假设较少且多为隐含；IRT 将假设显性化并发展专门检验方法。

## 生活实例

- **人格量表中的多维问题**：若量表同时测量外向性与宜人性，就不满足单维性，直接应用单维 IRT 会出错。
- **阅读理解题组**：同一篇文章的若干题目可能因共享背景材料而产生局部依赖，需要检验或采用题组模型。

## 考研重点

- **常考题型**：简答题（IRT 的基本假设有哪些）、选择题（单维性/局部独立性的含义）。
- **易混淆点**：
  - 局部独立不是样本独立，而是控制 θ 后的条件独立；
  - 单维性不等于题目内容完全相同；
  - 单调性 ICC 可以平坦但不能下降。
- **记忆口诀**："单维局部单调性，不变模型要设定；Q三因子来检验，违反就用多维行。"

## 文献来源

- 教材章节：漆书青《现代教育与心理测量学原理》第 8 章；戴海崎《心理与教育测量》第 8 章。
- 经典论文：Yen, W. M. (1984). Effects of local item dependence on the fit and equating performance of the three-parameter logistic model. *Applied Psychological Measurement*, 8(2), 125–145.
- 网页/综述：Cogn-IQ. (n.d.). Unidimensionality in IRT. https://www.cogn-iq.org/learn/theory/unidimensionality/
