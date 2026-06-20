---
concept: inferential_statistics
concept_cn: 推断统计
domain: general_psychology
tags: [inferential_statistics, sampling_distribution, standard_error, confidence_interval, hypothesis_testing, 学科/统计与测量, 学科/普通心理学]
citekeys: []
relations:
  - target: "psychological_measurement_basics"
    type: "part-of"
  - target: "descriptive_statistics"
    type: "extends"
---

# 推断统计 / Inferential Statistics

## 定义
推断统计（Inferential Statistics）是指利用样本数据对总体特征进行估计、检验与预测的统计方法，核心任务包括参数估计（点估计与区间估计）与假设检验。

## 核心要点
- 要点1：抽样分布——从同一总体反复抽取相同容量的样本，某一样本统计量（如均值）形成的概率分布；它是推断统计的理论基础。
- 要点2：标准误（Standard Error, SE）——样本统计量的标准差，反映抽样误差大小；均值标准误 SE = σ/√n，样本量越大，标准误越小。
- 要点3：中心极限定理——无论总体分布如何，当样本容量足够大时，样本均值的抽样分布趋近正态分布，使正态理论推断成为可能。
- 要点4：参数估计——点估计用单个数值估计总体参数；区间估计（置信区间）给出总体参数的可能范围。
- 要点5：假设检验——在抽样分布框架下，根据样本数据判断是否拒绝关于总体参数的虚无假设。

## 理论背景
- 提出者/流派：推断统计由 Ronald Fisher、Jerzy Neyman、Egon Pearson 等人在 20 世纪初建立；Fisher 发展显著性检验，Neyman-Pearson 建立假设检验的决策框架。
- 发展脉络：
  - Fisher 显著性检验（p 值）
  - Neyman-Pearson 假设检验（α、β、功效）
  - 贝叶斯推断与频率学派的持续对话
  - 当代：效应量、置信区间与重复实验受到更多重视
- 关键假设：样本是随机抽取的；样本统计量的抽样分布可被建模。

## 经典实验/研究
- **中心极限定理的实验演示**
  - 即使总体分布严重偏态，当 n ≥ 30 时，样本均值的分布仍接近正态
  - 这一性质是许多 t 检验、方差分析与置信区间方法的理论依据
- **Gosset（1908）t 分布**
  - 在小样本且总体标准差未知的情况下，提出用样本标准差估计标准误，并推导 t 分布
  - 使小样本推断成为可能

## 评价与争议
- 优势：使研究者能够从有限样本推断总体，是实验心理学与心理测量的核心工具。
- 争议/反例：
  - p 值滥用与“统计显著”崇拜受到广泛批评；美国统计协会（ASA, 2016）强调不应仅依据 p 值做结论。
  - 置信区间常被误读为“参数有 95% 概率落在区间内”，正确理解是“重复抽样下 95% 的区间会包含参数”。
- 与相近概念的区别：
  - 推断统计以概率为基础，描述统计不涉及概率推断。
  - 标准误 ≠ 标准差：前者衡量统计量稳定性，后者衡量个体分数分散性。

## 生活实例
- 例1：民意调查只访问 1000 人，却能通过抽样分布与置信区间推断全国选民的支持率范围。
- 例2：药物试验通过样本数据判断新药是否显著优于安慰剂，进而推断总体患者的疗效。

## 考研重点
- 常考题型：名词解释（抽样分布、标准误、置信区间、中心极限定理）、简答题（标准误与标准差的区别）、论述题（推断统计与描述统计的关系）。
- 易混淆点：置信区间是区间估计，不是假设检验；标准误随样本量增大而减小。
- 记忆口诀：“抽样分布是基础，标准误看抽样误；点估区间加检验，推断总体有依据。”

## 文献来源
- 教材章节：张厚粲《现代心理与教育统计学》第5–7章；舒华《心理与教育研究中的多因素实验设计》
- 经典论文：Student. (1908). The probable error of a mean. *Biometrika*.; Neyman, J., & Pearson, E. S. (1933). On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society A*.
