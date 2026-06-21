---
name: rule-maintenance-loop
description: 修改规则系统时的标准闭环：先改 rules/，再回写入口/索引，最后记录日志
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ab660333-80f1-4503-b676-3969a97b1cd0
---

# 规则系统维护闭环

**适用场景**：任何涉及修改规则文件（`rules/`、`00-prompts/`、各项目模式规则等）、脚本（`tools/`）或钩子说明（`memory/*.md`）的操作。

**标准流程**：

> **自动提醒**：修改规则相关文件后，Claude Code `PostToolUse` hook 会自动弹出本闭环提醒并运行 `load_rule.py --verify`。收到提醒后，按以下步骤确认即可。

1. **改具体规则 / 脚本 / 钩子**
   - 在 `rules/` 或对应规则目录中修正规则内容。
   - 在 `tools/` 中新增/修改脚本时，同步更新相关说明和索引。
   - 在 `memory/` 中新增/修改钩子说明时，同步更新 `MEMORY.md` 总索引。
   - 不改动按需加载架构本身，除非用户明确要求。

2. **回写入口与索引**
   - 如果规则属于某个模式，更新该模式的入口文件（如 `meta/psychology-expert-mode.md`、`00-prompts/research-partner-constitution.md` 等）。
   - 如果规则属于项目总纲，更新 `CLAUDE.md` 中的读取规则表或相关索引。
   - 如果新增/修改了脚本，同步更新 `tools/README.md` 和 `04-index/spec-tools.md`。
   - 如果新增/修改了记忆库钩子说明，同步更新 `MEMORY.md` 中的触发式索引。
   - 确保入口文件中的别名表、规则索引、触发条件与 `rules/` 一致。

3. **同步 `tools/rules-registry.yaml`（如适用）**
   - 新增/删除/重命名规则文件时，同步更新对应 namespace 的 `aliases`。
   - 新增/删除/重命名脚本时，同步更新 `kb-tools` namespace 的 `aliases`。
   - 新增/删除/重命名记忆库钩子说明时，同步更新 `memory-rules` namespace 的 `aliases`。
   - 若改动影响多个规则集，检查所有 namespace 的一致性。
   - `tools/load_rule.py` 本身不再硬编码别名，只读取注册表。

4. **记录到项目日志**
   - 在对应项目的 `PROJECT_LOG.md` 中简要说明：改了什么、为什么、影响哪些调用链。

**原则**：
- `rules/` 负责规则内容。
- `tools/` 负责脚本实现。
- `memory/` 负责钩子说明与触发式入口。
- 入口文件（CLAUDE.md / 模式入口 / MEMORY.md / README.md / spec-*.md）负责索引和调用说明。
- `tools/rules-registry.yaml` 负责确定性加载。
- 五者必须同步，不能只改一边。

**Why:** 规则系统容易出现"改了具体规则但入口索引没更新"的悬空问题，导致 AI 不知道该读哪个文件。

**How to apply:** 每次用户要求检查/优化/修正规则系统时，先读取本文件，然后按流程执行。

**相关记忆**
- [[work-principles-systemic-thinking]] — 处理非琐碎任务、设计工作流或规则时按需读取
- [[lessons-learned]] — 编码/脚本/批量操作经验教训
- [[priority-user-messages]] — 收到新消息后优先处理用户指示
