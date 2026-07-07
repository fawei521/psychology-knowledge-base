---
concept: test_information_function
concept_cn: 测验信息函数
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- 测验信息函数
- TIF
- 测量精度
- 心理测量
citekeys: []
relations:
- target: item_response_theory
  type: part-of
- target: item_information_function
  type: is-a
- target: standard_error
  type: correlates-with
- target: test_equating
  type: supports
---

# 测验信息函数 / Test Information Function (TIF)

## 定义

测验信息函数（Test Information Function, TIF）表示整个测验在不同潜在能力水平 θ 上所提供的总测量信息量，是项目信息函数的聚合。

## 核心要点

- **可加性**：在单维 IRT 中，$T(\theta) = \sum_{i=1}^{n} I_i(\theta)$，即 TIF 等于所有项目信息函数之和。
- **与标准误差的关系**：$SE(\theta) = \frac{1}{\sqrt{T(\theta)}}$；TIF 越大，该 θ 水平的能力估计标准误越小，越精确。
- **函数形态**：TIF 随 θ 变化而变化，反映测验在不同能力区间的测量精度分布。
- **应用价值**：
  - 评估测验对特定能力群体的测量精度；
  - 指导测验长度与项目选择；
  - 计算机自适应测验（CAT）中用于选题与终止规则。
- **峰值位置**：TIF 峰值所在的能力区间，是测验测量最精确的区域。

## 理论背景

- **提出者/流派**：TIF 由 Lord 在 IRT 框架下系统提出，是项目信息函数的自然扩展。
- **发展脉络**：项目信息函数 → 测验信息函数 → 信息函数在 CAT 与测验等值中的应用。
- **关键假设**：单维性、局部独立性、项目参数已准确估计；多维 IRT 中 TIF 不再是简单相加。

## 经典实验

- **Lord (1980) 测验信息函数研究**：证明 TIF 与 θ 估计标准误的倒数关系，奠定 IRT 精度评估基础。
- **CAT 早期实现研究**：Weiss 与 Kingsbury (1984) 使用信息函数最大化原则开发自适应测验系统。

## 评价与争议

- **优势**：
  - 直观展示测验在能力全量尺上的精度分布；
  - 可用于比较不同测验或测验形式的测量效能；
  - 支持 CAT 与等值决策。
- **争议/反例**：
  - 单维 IRT 中 TIF 才有简单可加性；
  - 信息函数对模型假设和参数估计误差敏感；
  - 高 TIF 不一定意味着测验内容覆盖全面。
- **与相近概念的区别**：TIF 是整个测验的信息；IIF 是单个项目的信息；CTT 信度是一个总体指标，不随 θ 变化。

## 生活实例

- **高难度资格考试**：若 TIF 峰值集中在高分段，说明测验对高水平考生的区分能力更强。
- **抑郁症筛查量表**：若 TIF 在中等抑郁水平最高，说明量表对轻中度患者的筛查最敏感。

## 考研重点

- **常考题型**：名词解释（测验信息函数）、选择题（TIF 与 SE 的关系）、简答题（TIF 的意义与计算）。
- **易混淆点**：
  - TIF 不是单一数值，而是 θ 的函数；
  - TIF 与 SE 成反比关系，不是正比；
  - 多维 IRT 中 TIF 不等于项目信息函数之和。
- **记忆口诀**："TIF 汇总项目精，相加得到总量程；开方取倒数求 SE，峰值区域测最灵。"

## 文献来源

- 教材章节：戴海崎《心理与教育测量》第 8 章；漆书青《现代教育与心理测量学原理》第 9 章。
- 经典论文：Lord, F. M. (1980). *Applications of Item Response Theory to Practical Testing Problems*. Lawrence Erlbaum.
- 网页/综述：Koolearn. (2024). 2025心理学考研知识梳理：项目信息函数与测验信息函数. https://kaoyan.koolearn.com/20240823/1745076.html
