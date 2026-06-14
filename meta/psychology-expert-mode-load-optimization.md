---
name: psychology-expert-mode-load-optimization
description: 心理学专家模式知识库读取策略优化为只读行为约定，技术规范按需触发
metadata:
  type: feedback
---

心理学专家模式开启时，不必一次性读取全部知识库索引文件。2026-06-13 用户反馈：全读太麻烦，而且知识库会越来越大。

**Why：**
- `concept-map.md` 和 `tag-index.md` 通常只在回答具体概念/标签相关问题时才需要。
- 进入模式时只确认总规范即可，避免浪费上下文。
- 后续知识库膨胀后，全读成本会越来越高。

**How to apply：**
- 触发「开启心理学专家模式」后，只自动读取 `E:\psychology-knowledge-base\meta\psychology-expert-mode.md`。技术规范按任务触发 `04-index/spec-*.md`。
- `04-index/concept-map.md` 和 `04-index/tag-index.md` 改为按需读取（例如用户问到概念关系或标签检索时）。
- 不要把当前文本框的会话上下文误当成长期记忆来推销，用户会觉得这是理所当然的。
