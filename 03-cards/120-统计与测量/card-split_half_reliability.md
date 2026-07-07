---
concept: split_half_reliability
concept_cn: 分半信度
domain: psychometrics
tags:
- 学科/统计与测量
- 分半信度
- 斯皮尔曼-布朗公式
- 内部一致性信度
- 内容取样
- 经典测量理论
citekeys: []
relations:
- target: internal_consistency_reliability
  type: is-a
- target: reliability
  type: is-a
- target: classical_test_theory
  type: part-of
- target: spearman_brown_prophecy_formula
  type: supports
---

# 分半信度 / Split-Half Reliability

## 定义

分半信度（Split-Half Reliability）是指将测验题目分成两半（通常按奇偶题号），计算两半得分之间的相关，再经斯皮尔曼-布朗公式校正后得到的信度估计，用于评估测验内部两半题目的一致性。

## 核心要点

- **操作步骤**：
  1. 将测验按奇偶题号（或前半/后半）分为两半；
  2. 计算每位被试在两半上的得分；
  3. 求两半得分的 Pearson 相关系数 rₕₕ；
  4. 用斯皮尔曼-布朗公式校正：$r_{xx} = \frac{2r_{hh}}{1 + r_{hh}}$。
- **误差来源**：主要控制**内容取样误差**，反映测验两半内容是否测量同一特质。
- **前提条件**：两半测验分数的方差应相等；两半题目在内容、难度上应尽可能等值。
- **与 Cronbach's α 的关系**：α 可视为所有可能分半信度的平均值；分半信度只是其中一种特定分法。
- **分半方式的影响**：奇偶分半通常优于前后分半，可减少疲劳、练习等顺序效应。

## 理论背景

- **提出者/流派**：分半法是经典测量理论（CTT）中最早的内部一致性估计方法之一；Spearman (1910) 和 Brown (1910) 分别提出校正公式，后合称斯皮尔曼-布朗公式。
- **发展脉络**：分半相关 → 斯皮尔曼-布朗校正 → KR-20 → Cronbach's α → 现代结构方程模型中的组合信度。
- **关键假设**：
  - 测验题目可分为两个等值部分；
  - 两半方差相等（tau-equivalent）；
  - 测验只能施测一次，无法计算重测或复本信度。

## 经典实验

- **早期智力测验的分半信度研究**：比奈-西蒙智力量表等早期测验常采用奇偶分半法估计信度，经斯皮尔曼-布朗校正后报告。
- **Rulon (1939) 分半公式比较**：比较不同分半校正公式，指出斯皮尔曼-布朗公式在两半方差相等时效果最佳，否则可使用 Rulon 或 Flanagan 公式。

## 评价与争议

- **优势**：只需一次施测，实施简便，适合课堂测验和小规模研究。
- **争议/反例**：
  - 分半方式不同会导致结果差异；
  - 若两半方差不等，斯皮尔曼-布朗校正会高估或低估信度；
  - 只能反映两半内容的一致性，信息利用率低于 Cronbach's α。
- **与相近概念的区别**：分半信度是内部一致性信度的一种；Cronbach's α 综合了所有可能分半的信息。

## 生活实例

- **课堂测验**：某次小测只能考一次，教师将奇数题和偶数题分别计分，若两半得分高度相关，说明测验内部一致性好。
- **在线问卷平台**：某些平台自动提供奇偶分半信度作为问卷质量的快速指标。

## 考研重点

- **常考题型**：计算题（求分半相关并校正）、选择题（适用条件）、简答题（分半信度与内部一致性信度的关系）。
- **易混淆点**：
  - 分半相关 rₕₕ 会低估整个测验的信度，必须校正；
  - 斯皮尔曼-布朗公式假设两半等值；
  - 分半信度 ≠ 重测信度，前者只需一次施测。
- **记忆口诀**："奇偶两半求相关，斯布公式来校正；r 大题同 r 小异，等值两半才准确。"

## 文献来源

- 教材章节：郑日昌《心理测量学》第 4 章；戴海崎《心理与教育测量》第 4 章。
- 经典论文：Spearman, C. (1910). Correlation calculated from faulty data. *British Journal of Psychology*, 3(3), 271–295.
- 网页/综述：Real Statistics Using Excel. (n.d.). Item analysis basic concepts. https://real-statistics.com/reliability/item-analysis/item-analysis-basic-concepts/
