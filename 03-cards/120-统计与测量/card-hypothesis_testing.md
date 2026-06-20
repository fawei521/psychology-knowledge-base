---
concept: hypothesis_testing
concept_cn: 假设检验
domain: general_psychology
tags: [hypothesis_testing, null_hypothesis, type_i_error, type_ii_error, p_value, statistical_power, 学科/统计与测量, 学科/普通心理学]
citekeys: []
relations:
  - target: "inferential_statistics"
    type: "is-a"
---

# 假设检验 / Hypothesis Testing

## 定义
假设检验（Hypothesis Testing）是在抽样分布框架下，根据样本数据对关于总体参数的假设做出拒绝或保留决策的统计推断方法。

## 核心要点
- 要点1：虚无假设与备择假设——H₀ 通常表示“无效应/无差异”，H₁ 表示研究者希望证实的效应或差异。
- 要点2：显著性水平 α——事先设定的犯 Type I 错误（弃真）的概率阈值，心理学中通常取 .05。
- 要点3：p 值——在 H₀ 为真的前提下，观察到当前样本结果或更极端结果的概率；p < α 时拒绝 H₀。
- 要点4：两类错误——Type I 错误（α）：H₀ 真却拒绝；Type II 错误（β）：H₀ 假却未拒绝；统计功效 power = 1 − β。
- 要点5：决策逻辑——假设检验是反证法思路：若样本结果在 H₀ 下极不可能，则怀疑 H₀。

## 理论背景
- 提出者/流派：Ronald Fisher 提出显著性检验与 p 值；Jerzy Neyman 与 Egon Pearson 建立包含 H₀/H₁、α、β 的决策框架。
- 发展脉络：
  - Fisher：p 值作为反对 H₀ 的证据强度
  - Neyman-Pearson：长期错误率控制与最优检验
  - 当代：强调效应量、置信区间、先验注册与重复实验
- 关键假设：样本随机；检验统计量在 H₀ 下的抽样分布已知；模型假设（如正态性、方差齐性）基本满足。

## 经典实验/研究
- **Fisher 女士品茶实验（1935）**
  - 设计：一位女士声称能分辨奶茶中先加奶还是先加茶；Fisher 设计 8 杯饮品，4 杯先奶、4 杯先茶
  - 推理：若她只是随机猜测，8 杯全对的概率为 1/70 ≈ .014；观察到全对结果后拒绝“她只是猜测”的 H₀
  - 意义：展示了显著性检验的基本逻辑
- **Neyman-Pearson 引理**
  - 证明：在简单假设下，似然比检验是在给定 α 下功效最大的检验
  - 奠定了最优假设检验的理论基础

## 评价与争议
- 优势：为科学实验提供了一套系统的决策规则；使研究结果可量化、可比较。
- 争议/反例：
  - p 值不能衡量 H₀ 为真的概率，也不能单独衡量效应大小。
  - “p < .05 即显著”的机械使用导致可重复性危机；ASA 建议结合效应量、置信区间与实质意义。
  - 小样本、低功效研究容易得到不稳定的显著结果。
- 与相近概念的区别：
  - 显著性检验（Fisher）与假设检验（Neyman-Pearson）在哲学上不同，但实务中常被混用。
  - 统计显著 ≠ 实际重要：大样本下微小效应也可显著。

## 生活实例
- 例1：新药审批中，H₀ 为“新药与安慰剂无差异”；若试验显示 p < .05 且效应量足够大，才认为新药有效。
- 例2：法庭审判中，“无罪推定”类似 H₀，需有足够证据（超越合理怀疑）才能拒绝它。

## 考研重点
- 常考题型：名词解释（虚无假设、备择假设、Type I/II 错误、统计功效、p 值）、简答题（两类错误的关系）、论述题（假设检验的基本步骤与逻辑）。
- 易混淆点：p 值不是 H₀ 为真的概率；α 是事前阈值，p 是事后概率；power 受样本量、效应量、α 影响。
- 记忆口诀：“虚无假设要推翻，显著水平先定好；p小拒绝别乱跑，效应量大才可靠。”

## 文献来源
- 教材章节：张厚粲《现代心理与教育统计学》第8章；甘怡群《心理与行为科学统计》假设检验部分
- 经典论文：Fisher, R. A. (1935). *The design of experiments*.; Neyman, J., & Pearson, E. S. (1933). On the problem of the most efficient tests of statistical hypotheses. *Philosophical Transactions of the Royal Society A*.; Wasserstein, R. L., & Lazar, N. A. (2016). The ASA statement on p-values. *The American Statistician*.
