---
concept: two_parameter_logistic_model
concept_cn: 双参数Logistic模型
domain: psychometrics
tags:
- 学科/统计与测量
- 项目反应理论
- 2PL
- 区分度
- 难度
- 心理测量
citekeys: []
relations:
- target: item_response_theory
  type: is-a
- target: item_characteristic_curve
  type: applies-to
- target: irt_assumptions
  type: supports
- target: one_parameter_logistic_model
  type: extends
- target: three_parameter_logistic_model
  type: extends
- target: item_information_function
  type: supports
---

# 双参数 Logistic 模型 / Two-Parameter Logistic Model (2PL)

## 定义

双参数 Logistic 模型（2PL）是项目反应理论中同时估计项目难度 b 与区分度 a 的 Logistic 模型，是最常用的 IRT 模型之一。

## 核心要点

- **公式**：$P_i(\theta) = \frac{1}{1 + e^{-Da_i(\theta - b_i)}}$，其中 a_i 为区分度，b_i 为难度，D ≈ 1.702。
- **难度参数 b**：ICC 拐点对应的 θ 值，越大表示项目越难。
- **区分度参数 a**：ICC 在拐点处的斜率，a 越大曲线越陡峭，项目区分高低能力者越强；a > 0 保证单调性。
- **模型特点**：
  - 允许不同项目有不同区分度；
  - 不估计猜测参数（c = 0）；
  - 是 1PL 的扩展，也是 3PL 的特例。
- **项目信息函数（2PL）**：$I_i(\theta) = D^2 a_i^2 P_i(\theta) Q_i(\theta)$，在 θ = b 处达到最大。

## 理论背景

- **提出者/流派**：由 Birnbaum（1968）在 Lord 的 IRT 框架下系统提出，作为 1PL 的扩展。
- **发展脉络**：1PL（固定区分度）→ 2PL（释放区分度）→ 3PL（加入猜测）→ 多级评分与多维模型。
- **关键假设**：单维性、局部独立性、单调性、无猜测效应、模型正确设定。

## 经典实验

- **Birnbaum (1968) 2PL 模型推导**：在 Lord & Novick 主编的《Statistical Theories of Mental Test Scores》中系统阐述 2PL 参数估计。
- **GRE 与 SAT 题库校准**：大规模高利害测验常用 2PL 或 3PL 对选择题进行参数估计。

## 评价与争议

- **优势**：
  - 同时估计难度与区分度，拟合能力更强；
  - 项目信息函数与测量精度可直接计算；
  - 广泛应用于题库建设与计算机自适应测验。
- **争议/反例**：
  - 对选择题等存在猜测的题型，低能力者答对概率被低估；
  - 样本量要求较 1PL 更高；
  - 参数估计可能出现非收敛或边界问题。
- **与相近概念的区别**：1PL 假设区分度相同；3PL 在 2PL 基础上加入猜测参数 c；Rasch 模型则不估计区分度且强调数据拟合模型。

## 生活实例

- **研究生入学考试题库**：不同题目区分度不同，2PL 能识别出高质量区分题与低质量题目。
- **心理健康筛查**：PHQ-9 等自评量表条目区分度可用 2PL 估计，筛选最佳条目。

## 考研重点

- **常考题型**：选择题（2PL 参数个数与含义）、简答题（2PL 与 1PL/3PL 比较）、计算题（根据 a、b 判断曲线形态）。
- **易混淆点**：
  - a 影响曲线陡峭程度，不决定难度位置；
  - 2PL 没有猜测参数，对多选题拟合可能不足；
  - 信息函数最大值在 θ = b 处。
- **记忆口诀**："2PL 两个参，a 陡 b 难；无 c 莫猜题，信息顶峰在拐点。"

## 文献来源

- 教材章节：戴海崎《心理与教育测量》第 8 章；漆书青《现代教育与心理测量学原理》第 8 章。
- 经典论文：Birnbaum, A. (1968). Some latent trait models and their use in inferring an examinee's ability. In F. M. Lord & M. R. Novick, *Statistical Theories of Mental Test Scores* (pp. 397–479). Addison-Wesley.
- 网页/综述：Cogn-IQ. (n.d.). Logistic Model in IRT. https://www.cogn-iq.org/learn/theory/logistic-model/
