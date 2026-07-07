---
concept: effect_size
concept_cn: 效应量
domain: psychometrics
tags:
- 学科/统计与测量
- 效应量
- Cohen's d
- eta squared
- 元分析
- 实际意义
- p值
citekeys: []
relations:
- target: sampling_and_experimental_error
  type: part-of
- target: statistical_power
  type: correlates-with
- target: meta_analysis
  type: supports
- target: p_value
  type: contrasts
- target: confidence_interval
  type: correlates-with
---

# 效应量 / Effect Size

## 定义

效应量（Effect Size）是衡量处理效应、组间差异或变量关系强度的标准化指标，它反映现象的实际大小，独立于样本量。

## 核心要点

- **独立于样本量**：与 p 值不同，效应量不受样本量大小直接影响；大样本可能使极小效应统计显著，但效应量仍很小。
- **常用指标**：
  - **Cohen's d**：两组均值差异的标准化指标，小/中/大效应通常分别为 0.20、0.50、0.80；
  - **η²（Eta squared）**：方差分析中解释方差的比例，小/中/大效应通常分别为 0.01、0.06、0.14；
  - **r（相关系数）**：相关研究中的效应量，小/中/大效应通常分别为 0.10、0.30、0.50；
  - **R²（决定系数）**：回归中自变量解释因变量方差的比例；
  - **Cramer's V / φ**：分类变量关联强度指标。
- **实际意义**：效应量回答 "效应有多大"，p 值只回答 "效应是否存在"。
- **在元分析中的作用**：效应量是跨研究汇总和比较的基础单位。

## 理论背景

- **提出者/流派**：Jacob Cohen 是效应量在心理学中系统应用的主要推动者，他在 1969 年的著作中提出 Cohen's d 等标准化指标。
- **发展脉络**：早期研究仅报告显著性 → Cohen 强调效应量 → 美国心理学会（APA）第 5 版 Publication Manual (2001) 要求报告效应量 → 现代开放科学运动强调效应量 + 置信区间 + 检验力。
- **关键假设**：
  - 效应量指标需与研究设计和测量尺度匹配；
  - 小/中/大效应的 Cohen 经验标准仅作参考，实际解释需结合领域背景。

## 经典实验

- **Rosenthal & Rubin (1982) "Binomial Effect Size Display"**：提出用简单比例差异呈现效应量，使非专业读者也能理解 r = 0.30 等指标的实践意义。
- **Many Labs 项目**：大规模重复实验显示许多经典心理学效应的效应量比原研究小，但仍有统计学意义，凸显仅看 p 值的不足。

## 评价与争议

- **优势**：
  - 提供处理效应的实际大小，弥补 p 值的局限；
  - 便于跨研究、跨测量工具比较；
  - 是元分析的标准化输入。
- **争议/反例**：
  - Cohen 的 0.2/0.5/0.8 标准被批评为脱离具体领域，某些领域中小效应可能非常重要（如公共卫生干预）；
  - 过度追求大效应可能导致发表偏倚；
  - 不同效应量指标之间换算复杂，解释需谨慎。
- **与相近概念的区别**：p 值反映数据与零假设的不一致程度，受样本量影响；效应量反映实际效应强度，不受样本量直接影响。

## 生活实例

- **教育干预**：某学习方法使学生成绩提高 5 分。若 Cohen's d = 0.10，则实际效应很小；若 d = 0.80，则干预效果显著且值得推广。
- **医学治疗**：一种新药使康复率从 50% 提高到 60%，其效应量可能中等，但如果涉及数百万患者，实际公共健康意义巨大。

## 考研重点

- **常考题型**：选择题（Cohen's d 大小判断）、简答题（效应量与 p 值的区别）、计算题（根据均值、标准差计算 Cohen's d）。
- **易混淆点**：
  - 统计显著 ≠ 实际重要，大样本下 p < .05 可能对应极小效应；
  - η² 与偏 η²（partial eta squared）在多重自变量时不同；
  - 效应量的解释标准因领域而异。
- **记忆口诀**："p 值看是否，效应量看多大；Cohen d 零点二五八，小中大要记牢。"

## 文献来源

- 教材章节：张厚粲《现代心理与教育统计学》第 8、10 章；Gravetter & Wallnau《行为科学统计》第 8 章。
- 经典论文：Cohen, J. (1969). *Statistical Power Analysis for the Behavioral Sciences*. Academic Press.
- 网页/综述：Lakens, D. (2013). Calculating and reporting effect sizes to facilitate cumulative science: A practical primer for t-tests and ANOVAs. *Frontiers in Psychology*, 4, 863.
