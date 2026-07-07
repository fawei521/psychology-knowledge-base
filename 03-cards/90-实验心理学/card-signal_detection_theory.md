---
concept: signal_detection_theory
concept_cn: 信号检测论
domain: experimental_psychology
tags: [experimental_psychology, psychophysics, decision_making, perception, cognitive_modeling]
relations:
  - target: psychophysical_methods
    type: extends
  - target: method_of_limits
    type: contrasts
  - target: method_of_adjustment
    type: contrasts
  - target: method_of_constant_stimuli
    type: contrasts
---

# 信号检测论 / Signal Detection Theory

## 定义
信号检测论（signal detection theory, SDT）是一种将感知过程分解为**感受性（sensitivity）**与**反应偏好/判断标准（response bias/criterion）**的数学模型，最初源于雷达与通信工程，后被 Green & Swets 引入心理物理学。

## 核心要点
- 由 **Green & Swets（1966）** 系统化引入心理学。
- 基本假设：
  - 感觉证据是连续变量，来自噪声（N）分布与信号+噪声（S+N）分布。
  - 两分布通常假设为等方差正态分布。
  - 被试设定一个决策标准（criterion），将证据分为“有信号”与“无信号”。
- 四种结果：
  - **击中（Hit）**：信号存在，报告“有”。
  - **漏报（Miss）**：信号存在，报告“无”。
  - **虚报（False Alarm）**：信号不存在，报告“有”。
  - **正确拒斥（Correct Rejection）**：信号不存在，报告“无”。
- 核心指标：
  - **d'（d-prime）**：感受性指数，d' = Z(击中率) − Z(虚报率)。
  - **β（beta）**：似然比标准，β = p(x|S)/p(x|N) 在标准处取值。
  - **c**：标准位置，c = −0.5[Z(击中率) + Z(虚报率)]。
- ROC 曲线：以虚报率为横轴、击中率为纵轴，描绘不同标准下的表现，曲线下面积反映感受性。

## 理论背景
- 传统心理物理学将阈限视为固定界限，无法解释动机、期望、奖励对反应的影响。
- SDT 用决策标准替代固定阈限，将感觉过程与决策过程分离。
- 现代应用包括记忆再认、医学诊断、目击者证词、机器学习分类、神经影像决策研究。

## 经典实验
- **听觉检测实验**：在噪声背景中随机呈现弱信号，改变信号先验概率或奖励结构，观察 d' 与 β/c 的变化。
- **再认记忆实验**：区分“记得”与“知道”反应，发现熟悉感与回忆可用 d' 分离。
- **医学影像判读**：放射科医生检测 X 光片中的肿瘤，用 SDT 评估诊断敏感性（d'）与保守/宽松倾向（c）。

## 评价与争议
- **优势**：
  - 分离感受性与反应偏好，克服传统阈限方法的混淆。
  - 数学严谨，可跨任务、跨被试比较。
  - ROC 分析提供不依赖单一标准的敏感性指标。
- **批评**：
  - 等方差正态分布假设在某些情境下不成立。
  - 实验设计需同时操纵信号与噪声试次，否则无法估计 d'。
  - β 与 c 作为标准指标各有适用场景，β 对极端概率不稳定。
- **与传统心理物理学方法的关系**：SDT 不是阈限测量法，而是决策模型；可与传统方法结合，也可独立使用。

## 生活实例
- 机场安检员判断行李图像中是否有违禁品：其“严格”或“宽松”标准影响虚报与漏报。
- 手机面部识别在光线差时降低标准以提高解锁率，但增加误识风险。
- 考试选择题“不确定时是否猜答案”涉及 SAT 与反应偏好。

## 考研重点
- **常考题型**：名词解释“信号检测论/d'/β/ROC 曲线”；计算 d' 与 β；简答 SDT 与传统心理物理法的区别。
- **易混淆点**：
  - d' 只反映感受性，不受标准影响；β/c 反映反应偏好。
  - 击中率、虚报率必须基于信号试次与噪声试次分别计算。
  - ROC 曲线越凸向左上角，感受性越高。
- **记忆口诀**：
  - “噪声信号两分布，标准一划分四区；d' 感度 β 偏好，ROC 曲线定高低。”

## 文献来源
- Green, D. M., & Swets, J. A. (1966). *Signal Detection Theory and Psychophysics*. Wiley.
- Macmillan, N. A., & Creelman, C. D. (2005). *Detection Theory: A User's Guide* (2nd ed.). Lawrence Erlbaum.
- Swets, J. A., Tanner, W. P., Jr., & Birdsall, T. G. (1961). Decision processes in perception. *Psychological Review, 68*(5), 301–340.
- 郭秀艳, 杨治良. (2019). 《实验心理学》（第2版）. 人民教育出版社.
- 朱滢. (2016). 《实验心理学》（第4版）. 北京大学出版社.
