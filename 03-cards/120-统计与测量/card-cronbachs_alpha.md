---
concept: cronbachs_alpha
concept_cn: 克龙巴赫α系数
domain: psychometrics
tags:
- 学科/统计与测量
- Cronbach's alpha
- 内部一致性信度
- 信度
- 经典测量理论
- 项目分析
citekeys: []
relations:
- target: internal_consistency_reliability
  type: is-a
- target: reliability
  type: is-a
- target: split_half_reliability
  type: extends
- target: item_total_correlation
  type: correlates-with
---

# 克龙巴赫 α 系数 / Cronbach's Alpha

## 定义

克龙巴赫 α 系数（Cronbach's Alpha）是衡量测验内部一致性信度最常用的指标，反映测验各题目之间测量同一特质的程度，可视为所有可能分半信度的平均值。

## 核心要点

- **公式**：$\alpha = \frac{K}{K-1}\left(1 - \frac{\sum_{i=1}^{K} \sigma_i^2}{\sigma_X^2}\right)$，其中 K 为题目数，$\sigma_i^2$ 为各题方差，$\sigma_X^2$ 为总分方差。
- **取值范围**：0 到 1，越接近 1 表示内部一致性越高。
- **评价标准**：
  - α ≥ 0.90：优秀；
  - 0.80–0.89：非常好；
  - 0.70–0.79：可接受；
  - α < 0.70：通常需要修订。
- **适用范围**：多级评分题目；对于二分计分题目，α 等价于 KR-20。
- **与分半信度的关系**：α 是所有可能分半信度的平均值。
- **注意事项**：α 受题目数量影响；α 高不一定表示单维或高效度。

## 理论背景

- **提出者/流派**：Lee J. Cronbach 于 1951 年提出，是对 Kuder-Richardson 公式的推广。
- **发展脉络**：KR-20（二分题）→ Cronbach's α（多级评分）→ McDonald's ω → 结构方程模型中的组合信度。
- **关键假设**：测验题目为 tau-equivalent 或 essentially tau-equivalent；题目之间正向相关。

## 经典实验

- **Cronbach (1951)**：在《Coefficient Alpha and the Internal Structure of Tests》中证明 α 与所有可能分半信度平均值的关系，成为心理测量学引用率最高的论文之一。
- **心理量表标准化研究**：几乎所有现代心理量表（如 SCL-90、大五人格量表）都报告 Cronbach's α 作为基本信度证据。

## 评价与争议

- **优势**：计算简便、适用范围广、与项目-总分相关直接联系。
- **争议/反例**：
  - 题目数量增加会人为提高 α；
  - 多维测验若各维度内部相关高，α 也可能高，造成单维假象；
  - tau-equivalent 假设不满足时，McDonald's ω 更准确。
- **与相近概念的区别**：KR-20 是 α 在二分计分题目上的特例；分半信度只反映一种特定分法的一致性。

## 生活实例

- **问卷质量报告**：学术论文常写 "该量表的 Cronbach's α 为 0.87"，说明量表题目一致性较好。
- **量表修订**：若某题删除后 α 显著提高，说明该题与其他题测量内容不一致，可考虑删除。

## 考研重点

- **常考题型**：名词解释、计算题（根据题目方差和总分方差计算 α）、选择题（α 的影响因素、解释标准）。
- **易混淆点**：
  - α 适用于多级评分，KR-20 适用于二分计分；
  - α 高 ≠ 单维，≠ 高效度；
  - 增加题目数量通常会提高 α。
- **记忆口诀**："克龙阿尔法看一致，零到一之间来评价；七点零上可接受，题目越多越容易高。"

## 文献来源

- 教材章节：郑日昌《心理测量学》第 4 章；戴海崎《心理与教育测量》第 4 章。
- 经典论文：Cronbach, L. J. (1951). Coefficient alpha and the internal structure of tests. *Psychometrika*, 16(3), 297–334.
- 网页/综述：Tavakol, M., & Dennick, R. (2011). Making sense of Cronbach's alpha. *International Journal of Medical Education*, 2, 53–55.
