---
concept: reliability
concept_cn: 信度
domain: general_psychology
tags: [reliability, test_retest, split_half, cronbach_alpha, internal_consistency, 学科/统计与测量, 学科/普通心理学]
citekeys: []
relations:
  - target: "psychological_measurement_basics"
    type: "part-of"
  - target: "validity"
    type: "supports"
---

# 信度 / Reliability

## 定义
信度（Reliability）是指测量工具所得分数的一致性、稳定性与可重复性程度；信度是效度的必要条件，但不是充分条件。

## 核心要点
- 要点1：再测信度（Test-Retest Reliability）——同一测验在不同时间对同一群体施测两次，计算两次分数的相关；适用于较稳定的特质。
- 要点2：复本信度（Parallel-Forms Reliability）——使用两个等值测验版本同时或间隔施测，考察形式等价性。
- 要点3：内部一致性信度——反映测验内部条目测量同一特质的程度，常用分半信度（Split-Half）与 Cronbach's α 系数。
- 要点4：评分者信度（Inter-Rater Reliability）——多个评分者对同一反应评分的一致性，常用 Cohen's κ 或组内相关系数 ICC。
- 要点5：信度系数解释——通常 α ≥ .70 为可接受，≥ .80 为良好，≥ .90 为高信度；但过高可能提示条目冗余。

## 理论背景
- 提出者/流派：经典测量理论（Classical Test Theory, CTT）中，Spearman 提出真分数模型 X = T + E；Cronbach（1951）提出 α 系数。
- 发展脉络：真分数模型 → 信度类型细分（再测、复本、内部一致性、评分者） → 概化理论（GT） → 项目反应理论（IRT）中的信息函数。
- 关键假设：测量分数由真分数与误差组成；随机误差降低信度，系统误差降低效度。

## 经典实验/研究
- **Cronbach（1951）α 系数**
  - 提出 α 系数作为内部一致性的指标
  - 数学上等价于所有可能分半信度的平均值（经 Spearman-Brown 校正）
  - 公式：α = (k / (k−1)) × (1 − Σσ²_items / σ²_total)
- **Spearman-Brown 校正公式**
  - 用于将分半信度校正为全长度测验的估计信度
  - 公式：r_SB = 2r_h / (1 + r_h)

## 评价与争议
- 优势：信度是测验质量最基础、最易量化的指标；α 系数计算简便，应用广泛。
- 争议/反例：
  - α 高不一定代表单维结构；测验若包含多个相关维度，α 可能虚高。
  - “信度高就有效度高”是常见误解；一个稳定地测量错误特质的工具可以信度高但效度低。
  - 再测信度受时间间隔、练习效应、被试记忆等因素影响。
- 与相近概念的区别：
  - 信度 ≠ 效度：信度回答“测得稳不稳”，效度回答“测得对不对”。
  - 内部一致性 ≠ 同质性：前者是信度指标，后者是结构特征。

## 生活实例
- 例1：体重秤每次站上显示不同数字，说明信度低；若稳定显示同一错误数值，则信度高但效度低。
- 例2：某人格量表间隔两周重测，相关系数 .85，说明该量表具有较高的时间稳定性。

## 考研重点
- 常考题型：名词解释（信度、再测信度、分半信度、Cronbach's α）、简答题（信度的类型及估计方法）、论述题（信度与效度的关系）。
- 易混淆点：再测信度 vs 复本信度；分半信度需 Spearman-Brown 校正；α 高 ≠ 单维。
- 记忆口诀：“信度稳定可重复，再测复本分半齐；Cronbach α 最常用，Spearman-Brown 来校正。”

## 文献来源
- 教材章节：戴海崎《心理与教育测量》第4章；郑日昌《心理测量学》信度章节
- 经典论文：Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*.; Spearman, C. (1910). Correlation calculated from faulty data. *British Journal of Psychology*.
