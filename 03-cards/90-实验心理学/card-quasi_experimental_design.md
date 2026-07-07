---
concept: quasi_experimental_design
concept_cn: 准实验设计
domain: experimental_psychology
tags: [experimental_psychology, research_methods, causal_inference, field_research]
relations:
  - target: advanced_experimental_design
    type: part-of
  - target: single_subject_design
    type: contrasts
  - target: ecological_validity
    type: correlates-with
---

# 准实验设计 / Quasi-Experimental Design

## 定义
准实验设计（quasi-experimental design）是一种对自变量进行操纵但未对被试进行随机分组的研究设计，常用于真实教育、临床、社区或政策情境中，以在随机分配不可行时尽量推断因果关系。

## 核心要点
- 与真实验的根本区别：**无随机分配**。
- 常见类型：
  - **非等组前后测设计（Nonequivalent Control Group Design）**：
    - 实验组：O₁ X O₂；对照组：O₃ — O₄。
    - 主要威胁：选择偏差、选择×成熟交互、回归假象。
  - **中断时间序列设计（Interrupted Time-Series Design）**：
    - 对同一群体在干预前后进行多次测量：O₁ O₂ O₃ O₄ X O₅ O₆ O₇ O₈。
    - 优势：可观察趋势变化，控制部分历史威胁。
  - **非等组中断时间序列设计**：结合上述两者，因果推断力更强。
  - **回归-间断设计（Regression Discontinuity Design, RDD）**：按临界值分配干预，利用断点两侧比较。
- 威胁控制策略：增加非等组因变量、切换复制、统计协变量控制、双重差分（DID）等。

## 理论背景
- **Campbell & Stanley（1966）** 在《Experimental and Quasi-Experimental Designs for Research》中首次系统提出准实验设计框架。
- **Cook & Campbell（1979）** 扩展效度威胁清单与统计分析方法。
- 现代发展：倾向得分匹配（PSM）、双重差分、合成控制法、RDD 等因果推断工具。

## 经典实验
- **Campbell 的康涅狄格交通安全法评估（1960s）**：使用中断时间序列设计评估交通法规变化对事故率的影响。
- **教育干预评估**：学校无法随机分班时，采用非等组前后测或 RDD 评估新课程效果。

## 评价与争议
- **优势**：
  - 可在真实情境中进行因果推断，外部效度高。
  - 伦理与实践上更易实施，尤其涉及既有群体或政策。
- **局限**：
  - 内部效度低于真实验，选择偏差是最核心威胁。
  - 需要更多测量点、对照组与统计控制来弥补随机化缺失。
- **与单被试设计的区别**：准实验通常关注群体层面的平均效应；单被试设计关注个体时间序列。
- **与真实验的区别**：真实验通过随机分配确立组间等价；准实验依赖设计与统计控制。

## 生活实例
- 评估某城市限行政策对空气质量的影响，无法随机让某些城市限行而另一些不限行。
- 医院评估新护理流程效果，按科室而非随机分配实施。

## 考研重点
- **常考题型**：名词解释“准实验设计”；简答非等组前后测、中断时间序列设计及其主要威胁；比较真实验与准实验。
- **易混淆点**：
  - 准实验可以有自变量操纵，只是缺乏随机分配。
  - 中断时间序列设计需要干预前足够多测量点以建立基线趋势。
- **记忆口诀**：
  - “非随机分准实验，非等组与时间序列；选择偏差是大敌，RDD 断点找因果。”

## 文献来源
- Campbell, D. T., & Stanley, J. C. (1966). *Experimental and Quasi-Experimental Designs for Research*. Rand McNally.
- Cook, T. D., & Campbell, D. T. (1979). *Quasi-Experimentation: Design & Analysis Issues for Field Settings*. Houghton Mifflin.
- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*. Houghton Mifflin.
- 郭秀艳, 杨治良. (2019). 《实验心理学》（第2版）. 人民教育出版社.
