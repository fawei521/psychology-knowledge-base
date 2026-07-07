---
concept: item_analysis
concept_cn: 项目分析
domain: psychometrics
tags:
- 学科/统计与测量
- 项目分析
- 项目难度
- 项目区分度
- 选项分析
- 经典测量理论
- 心理测验
citekeys: []
relations:
- target: psychological_measurement_basics
  type: is-a
- target: item_difficulty
  type: part-of
- target: item_discrimination
  type: part-of
- target: distractor_analysis
  type: part-of
- target: classical_test_theory
  type: supports
- target: reliability
  type: supports
- target: validity
  type: supports
---

# 项目分析 / Item Analysis

## 定义

项目分析（Item Analysis）是在心理与教育测量中，通过统计方法对测验题目的质量进行系统评估的过程，主要包括项目难度、项目区分度、选项分析等内容，以决定题目的保留、修改或删除。

## 核心要点

- **目的**：筛选优质题目、淘汰或修改劣质题目，提高测验的信度与效度。
- **主要内容**：
  - **项目难度**：题目难易程度的量化指标；
  - **项目区分度**：题目区分高能力者与低能力者的能力；
  - **选项分析**：检查各选项是否具有合理的诱答功能。
- **理论基础**：经典测量理论（CTT）是最常用的项目分析框架；项目反应理论（IRT）提供更精细的题目参数估计。
- **与测验质量的关系**：区分度高、难度适中的题目有助于提升测验的整体信度和效度。
- **分析流程**：计算难度 → 计算区分度 → 检查选项 → 结合信度（如 Cronbach's α if item deleted）综合决策。

## 理论背景

- **提出者/流派**：项目分析方法伴随经典测量理论（CTT）在 20 世纪上半叶发展起来；Kelley (1939) 提出用上下 27% 分组法计算区分度；Lord (1952) 研究了不同选项数下最佳难度水平。
- **发展脉络**：CTT 项目分析（难度、区分度、选项分析）→ IRT 项目分析（项目特征曲线、题目参数 a/b/c）→ 计算机自适应测验中的实时项目分析。
- **关键假设**：
  - 测验题目为二分计分或多分计分；
  - 样本量足够估计稳定的统计量；
  - 总分能够合理反映被试能力水平。

## 经典实验

- **Lord (1952) *A Theory of Test Scores***：系统研究多项选择题的最优难度，提出 5 选 1 理想难度约为 0.70，4 选 1 约为 0.74，3 选 1 约为 0.77，2 选 1 约为 0.85。
- **Kelley (1939) *The Selection of Upper and Lower Groups for the Validation of Test Items***：论证上下 27% 分组法在正态分布假设下能最大化高低组差异，成为项目区分度计算的经典方法。

## 评价与争议

- **优势**：项目分析提供了客观、可重复的指标，帮助测量者识别问题题目，提升测验质量。
- **争议/反例**：
  - CTT 的项目难度和区分度依赖于特定样本，样本变化时指标也会变化；
  - 仅看难度和区分度可能忽略内容效度，需结合专家评审；
  - 小样本时区分度估计不稳定，容易出现误导性结果。
- **与相近理论的区别**：CTT 项目分析基于总分和样本通过率；IRT 项目分析基于潜在特质 θ 和项目特征曲线，题目参数具有样本不变性。

## 生活实例

- **考研真题分析**：命题组会对每道选择题进行难度和区分度分析，删除区分度过低或被大量高分考生误选的题目。
- **在线学习平台**：MOOC 平台通过项目分析自动识别哪些测验题目过于简单或存在歧义，从而优化题库。

## 考研重点

- **常考题型**：选择题（难度/区分度计算）、简答题（项目分析内容与作用）、综合题（根据数据判断题目质量）。
- **易混淆点**：
  - 难度 P 值越大题目越容易；
  - 区分度 D 值可为负，表示题目质量差或答案有误；
  - 项目分析与测验整体信效度分析不同，前者针对单个题目。
- **记忆口诀**："项目分析三步走，难度区分加选项；P 大题易 D 要正，差题修改或删除。"

## 文献来源

- 教材章节：郑日昌《心理测量学》第 5 章；戴海崎《心理与教育测量》第 6 章。
- 经典论文：Kelley, T. L. (1939). The selection of upper and lower groups for the validation of test items. *Journal of Educational Psychology*, 30(1), 17–24.
- 网页/综述：Assessment Systems. (n.d.). Item Analysis in Psychometrics: A Guide. https://assess.com/item-analysis/
