---
concept: spearman_brown_prophecy_formula
concept_cn: 斯皮尔曼-布朗公式
domain: psychometrics
tags:
- 学科/统计与测量
- 斯皮尔曼-布朗公式
- 分半信度
- 信度
- 测验长度
- 经典测量理论
citekeys: []
relations:
- target: split_half_reliability
  type: supports
- target: reliability
  type: supports
- target: internal_consistency_reliability
  type: supports
---

# 斯皮尔曼-布朗公式 / Spearman-Brown Prophecy Formula

## 定义

斯皮尔曼-布朗公式（Spearman-Brown Prophecy Formula）是经典测量理论中用于根据现有测验的信度估计测验长度改变后信度的公式，也可用于将由分半相关得到的信度校正为完整测验信度。

## 核心要点

- **基本形式**：$r_{kk} = \frac{K \cdot r_{11}}{1 + (K-1) \cdot r_{11}}$，其中 $r_{11}$ 为原测验信度，K 为测验长度改变的倍数，$r_{kk}$ 为改变后的信度。
- **分半信度校正**：将测验分为两半时，K = 2，公式变为 $r_{xx} = \frac{2r_{hh}}{1 + r_{hh}}$，其中 $r_{hh}$ 为两半得分的相关。
- **预测作用**：可预测增加题目数量（K > 1）后信度的变化；也可预测减少题目数量（K < 1）的影响。
- **假设条件**：新增题目与原题目在内容、难度、区分度上同质；两半分半信度中两半方差相等。
- **实际意义**：信度随测验长度增加而提高，但增长速度递减。

## 理论背景

- **提出者/流派**：Charles Spearman (1910) 和 William Brown (1910) 分别独立提出该公式，后合称为 Spearman-Brown 公式。
- **发展脉络**：分半信度校正 → 测验长度与信度关系研究 → 现代测量中用于样本量规划和测验设计。
- **关键假设**：
  - 题目同质（tau-equivalent）；
  - 新增题目与原题目具有相同统计特性；
  - 被试样本和施测条件不变。

## 经典实验

- **Spearman (1910) 与 Brown (1910)**：两篇论文分别从不同角度推导出同一公式，奠定了测验长度与信度关系的理论基础。
- **测验标准化中的长度设计**：许多标准化测验在编制阶段使用 Spearman-Brown 公式预测不同题目数量下的信度，以确定最终测验长度。

## 评价与争议

- **优势**：形式简洁，便于预测测验加长或缩短后的信度变化；是分半信度校正的标准工具。
- **争议/反例**：
  - 当新增题目质量低于原题目时，实际信度可能低于公式预测；
  - 两半方差不等时，斯皮尔曼-布朗校正会偏离真实信度，此时可用 Rulon 或 Flanagan 公式；
  - 公式假设题目同质，对异质测验（如包含多个分量表）不适用。
- **与相近概念的区别**：Spearman-Brown 公式预测测验长度对信度的影响；Cronbach's α 综合评估现有测验的内部一致性。

## 生活实例

- **测验编制**：若 10 道题的测验信度为 0.60，用公式可预测 20 道题（K=2）时信度约为 0.75。
- **分半校正**：某测验奇偶两半相关为 0.56，经校正后完整测验信度约为 0.72。

## 考研重点

- **常考题型**：计算题（分半相关校正、预测加长后信度）、选择题（公式假设条件）。
- **易混淆点**：
  - K 是长度倍数，不是题目数量；
  - 公式假设新增题目与原题同质；
  - 分半校正时 K = 2。
- **记忆口诀**："斯布公式看长度，分半校正 K 等于二；题增信度会提高，同质假设要牢记。"

## 文献来源

- 教材章节：郑日昌《心理测量学》第 4 章；戴海崎《心理与教育测量》第 4 章。
- 经典论文：Spearman, C. (1910). Correlation calculated from faulty data. *British Journal of Psychology*, 3(3), 271–295.
- 网页/综述：Brown, W. (1910). Some experimental results in the correlation of mental abilities. *British Journal of Psychology*, 3(3), 296–322.
