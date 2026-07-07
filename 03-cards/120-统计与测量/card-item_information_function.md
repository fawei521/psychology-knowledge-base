---
concept: item_information_function
concept_cn: 项目信息函数
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- 项目信息函数
- IIF
- 测量精度
- 信息函数
citekeys: []
relations:
- target: item_response_theory
  type: part-of
- target: test_information_function
  type: part-of
- target: item_characteristic_curve
  type: supports
- target: one_parameter_logistic_model
  type: applies-to
- target: two_parameter_logistic_model
  type: applies-to
- target: three_parameter_logistic_model
  type: applies-to
- target: standard_error
  type: correlates-with
---

# 项目信息函数 / Item Information Function (IIF)

## 定义

项目信息函数（Item Information Function, IIF）描述单个项目在不同潜在能力水平 θ 上提供的测量信息量；信息量越大，该 θ 水平上的能力估计越精确。

## 核心要点

- **信息即精度**：IRT 中的"信息"不是日常语义的信息量，而是 Fisher 信息量，反映参数估计的精确程度。
- **2PL 公式**：$I_i(\theta) = D^2 a_i^2 P_i(\theta) Q_i(\theta)$，其中 a_i 为区分度，P 为答对概率，Q = 1-P。
- **一般公式**：$I_i(\theta) = \frac{[P_i'(\theta)]^2}{P_i(\theta)Q_i(\theta)}$，适用于各种 IRT 模型。
- **最大值位置**：对于 1PL/2PL，IIF 在 θ = b（难度参数）处最大；3PL 中最大值位置略有偏移。
- **影响因素**：
  - 区分度 a 越大，信息量越大；
  - 难度 b 决定信息量峰值出现的位置；
  - 猜测参数 c 会降低整体信息量。
- **可加性**：在单维 IRT 中，测验信息函数等于所有项目信息函数之和。

## 理论背景

- **提出者/流派**：信息函数概念源自 Fisher 信息，Lord 与 Birnbaum 将其引入 IRT 框架。
- **发展脉络**：Fisher 信息 → IRT 项目信息函数 → 测验信息函数 → 计算机自适应测验中的项目选择规则。
- **关键假设**：局部独立性、正确模型设定、项目参数已知或可精确估计。

## 经典实验

- **Lord (1980) 信息函数与测量精度研究**：系统证明测验信息函数与能力估计标准误差的关系。
- **计算机自适应测验（CAT）早期研究**：利用项目信息函数最大化规则动态选择题目（如 Lord, 1971）。

## 评价与争议

- **优势**：
  - 可量化项目在不同能力水平的测量贡献；
  - 指导题库建设与 CAT 选题；
  - 与标准误差直接挂钩，便于解释。
- **争议/反例**：
  - 信息函数依赖模型假设，模型误设时不可靠；
  - 多维 IRT 中信息函数不再简单可加；
  - 小样本参数估计误差会传递到信息函数。
- **与相近概念的区别**：IIF 针对单个项目；TIF 针对整个测验；CTT 中对应概念为测量标准误与信度。

## 生活实例

- **自适应考试选题**：当考生能力处于中等水平时，系统优先选择难度中等、区分度高的题目，使其 IIF 峰值落在考生 θ 附近。
- **量表精简**：保留信息量大且覆盖不同能力范围的题目，删除信息量低或高度重复的条目。

## 考研重点

- **常考题型**：名词解释（项目信息函数）、选择题（信息最大值位置、影响因素）、简答题（IIF 与 TIF 的关系）。
- **易混淆点**：
  - 信息函数是 θ 的函数，不是常数；
  - 信息最大处标准误差最小（SE = 1/√I）；
  - 3PL 中信息最大值不严格等于 b。
- **记忆口诀**："信息就是精度高，a 大峰高 b 定焦；TIF 相加得总量，开方取倒是 SE。"

## 文献来源

- 教材章节：戴海崎《心理与教育测量》第 8 章；漆书青《现代教育与心理测量学原理》第 9 章。
- 经典论文：Lord, F. M. (1980). *Applications of Item Response Theory to Practical Testing Problems*. Lawrence Erlbaum.
- 网页/综述：Koolearn. (2024). 2025心理学考研知识梳理：项目信息函数与测验信息函数. https://kaoyan.koolearn.com/20240823/1745076.html
