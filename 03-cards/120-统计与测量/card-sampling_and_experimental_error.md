---
concept: sampling_and_experimental_error
concept_cn: 抽样与实验误差
domain: psychometrics
tags:
- 学科/统计与测量
- 抽样分布
- 标准误
- 假设检验
- 错误类型
- 统计检验力
- 效应量
- 置信区间
citekeys: []
relations:
- target: inferential_statistics
  type: is-a
- target: sampling_distribution
  type: part-of
- target: standard_error
  type: part-of
- target: type_i_error
  type: part-of
- target: type_ii_error
  type: part-of
- target: statistical_power
  type: part-of
- target: effect_size
  type: part-of
- target: confidence_interval
  type: part-of
---

# 抽样与实验误差 / Sampling and Experimental Error

## 定义

抽样与实验误差是推断统计学中的核心概念簇，指由于从总体中抽取样本而非测量全部个体所引起的样本统计量与总体参数之间的偏差，以及假设检验中因抽样变异导致的决策错误（I 型错误、II 型错误）和控制这些错误的工具（统计检验力、效应量、置信区间）。

## 核心要点

- **抽样误差不可避免**：只要从总体中抽取样本，样本统计量就会围绕总体参数波动，这是统计推断的基本不确定性来源。
- **标准误量化抽样误差**：标准误是样本统计量抽样分布的标准差，反映样本统计量的精确度，样本量越大，标准误越小。
- **两类错误此消彼长**：在样本量固定时，降低 I 型错误率 α 会增加 II 型错误率 β，反之亦然；同时降低两类错误的唯一途径是增加样本量或降低测量误差。
- **统计检验力是正确检测真实效应的概率**：Power = 1 − β，心理学研究通常要求 ≥ 0.80。
- **效应量独立于样本量**：效应量反映处理效应或变量关系的实际大小，是对 p 值的重要补充。
- **置信区间与假设检验等价**：95% 置信区间不包含零假设值时，等价于在 α = 0.05 水平拒绝零假设。

## 理论背景

- **提出者/流派**：Jerzy Neyman 与 Egon Pearson 在 20 世纪 30 年代建立假设检验的形式化框架，明确区分 α、β 与检验力；Jacob Cohen 在 1962–1992 年间大力推广效应量与统计检验力分析。
- **发展脉络**：从经典频率学派推断 → 显著性检验（Fisher）→ Neyman-Pearson 决策框架 → 现代报告规范（效应量 + 置信区间 + 检验力）。
- **关键假设**：
  - 样本为随机抽样或随机分配；
  - 样本统计量的抽样分布可由中心极限定理近似；
  - 显著性水平 α 在数据收集前预先设定。

## 经典实验

- **Cohen (1962) "The Statistical Power of Abnormal-Social Psychological Research"**：回顾《异常与社会心理学杂志》发表的研究，发现平均统计检验力仅约 0.48，首次系统揭示心理学研究功效不足的问题。
- **Sedlmeier & Gigerenzer (1989) "Do Studies of Statistical Power Have an Effect on the Power of Studies?"**：二十多年后重测，发现心理学研究的平均检验力未见显著提升，推动后续功效分析与预注册运动。

## 评价与争议

- **优势**：Neyman-Pearson 框架提供了明确的决策规则；效应量、置信区间和检验力共同克服了单纯依赖 p 值的局限。
- **争议/反例**：
  - p 值操纵（p-hacking）和出版偏倚使 I 型错误被放大；
  - 小样本、低功效研究易得到不可重复结果，是心理学复制危机的重要原因之一；
  - 固定 α = 0.05 被批评为武断。
- **与相近理论的区别**：Fisher 的显著性检验只关注 p 值是否小于 α，不提供备择假设和 β 控制；Neyman-Pearson 框架则同时考虑两类错误和决策规则。

## 生活实例

- **医学检测**：健康人被新冠抗原检测误判为阳性（I 型错误）；感染者未被检测出（II 型错误）。降低 II 型错误需要更高灵敏度或更大样本量。
- **A/B 测试**：产品经理判断新界面是否提升点击率。若实际上无提升却误判为有效，即 I 型错误；若新界面真实有效却未上线，即 II 型错误。

## 考研重点

- **常考题型**：选择题（两类错误关系、功效影响因素）、计算题（标准误、置信区间）、简答题（两类错误与检验力的关系）。
- **易混淆点**：
  - 标准差 vs. 标准误：前者描述原始数据离散，后者描述样本统计量的抽样变异；
  - α + β ≠ 1，二者非互补关系；
  - 统计显著 ≠ 实际重要，必须结合效应量解释。
- **记忆口诀**："α 弃真，β 取伪；功效大，β 小；样本增，误差跑。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 7–8 章；Gravetter & Wallnau《行为科学统计》第 8、11 章。
- 经典论文：Cohen, J. (1962). The statistical power of abnormal-social psychological research. *Journal of Abnormal and Social Psychology*, 65(3), 145–153.
- 网页/综述：Nuzzo, R. (2014). Statistical errors. *Nature*, 506, 150–152.
