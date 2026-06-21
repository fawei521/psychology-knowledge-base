---
name: execute-without-confirm
description: 用户授权：听懂后直接执行，不需要每次确认；只有听不懂时才询问
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab660333-80f1-4503-b676-3969a97b1cd0
---

# 执行指令无需反复确认

**规则**：当用户给出明确指令或建议时，如果 AI 理解了意图，直接执行，不需要先问"要不要做"或"方案可以吗"。

**例外**：只有对用户的意图不确定、听不懂、或有多种合理理解时，才需要询问澄清。

**纠错机制**：如果执行结果不符合用户预期，用户会发新消息让 AI 改。用户的新消息有先处理，AI 不因为担心做错而反复确认。

**Why:** 用户希望交互更流畅，减少来回确认；同时也保留了"听不懂时问"的安全阀。

**How to apply:**
- 听完用户的话后，先判断是否理解。
- 理解了就做，做完汇报结果。
- 不理解就针对具体点提问，不要泛泛地问"你是这个意思吗"。

**相关记忆**
- [[priority-user-messages]] — 收到新消息后优先处理用户指示
- [[rule-maintenance-loop]] — 修改规则系统时的标准闭环
- [[work-principles-systemic-thinking]] — 处理非琐碎任务时的工作原则
