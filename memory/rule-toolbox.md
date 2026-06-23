---
name: rule-toolbox
description: 规则系统触发地图：开局必读，AI 遇到异常或任务时按场景调取规则，不凭记忆
metadata: 
  node_type: memory
  type: reference
  originSessionId: 63872cec-2633-442c-85ef-54a832599efd
---

# 规则系统触发地图

**核心原则**：规则文件很多，AI 不能凭记忆判断该读哪个。**遇到非琐碎任务，先检查是否有匹配的 skill/headroom/markitdown/agent-reach等工具。**遇到异常或任务时，先查本表，再按别名加载规则。** 本规则系统通过 `~/.claude/hooks/rule_hooks.py` 全局生效，所有 Claude Code 会话都会自动注入核心规则并监听规则文件改动。

---

## ⚠️ 异常触发（遇到就停，先读规则）

> 出现以下情况时，**立即停止当前操作**，按表读取对应规则，不要凭直觉继续。

| 异常场景 | 识别信号 | 立即读取规则 |
|---------|---------|------------|
| 同一操作反复失败 | 同样错误出现 ≥2 次、换方法仍失败、token 消耗激增 | `memory-rules/no-repetitive-failed` |
| 用户新消息打断 | 用户发了新消息，而当前任务还没完成 | `memory-rules/priority-user-messages`（已注入） |
| 不确定要不要确认 | 用户指令模糊、涉及删除/覆盖/对外发布 | `memory-rules/execute-without-confirm` |
| 复杂任务/流程设计 | 要设计工作流、规则、批量操作、多文件改动 | `memory-rules/work-principles` |
| 修改规则文件 | 改动了 `rules/`、`00-prompts/`、`memory/`、`tools/rules-registry.yaml` | `memory-rules/rule-maintenance` |
| 工具/脚本行为异常 | `load_rule.py`、import、verify 报错 | `kb-tools/readme` + `kb-specs/spec-tools` |

---

## 📋 任务触发（做之前先读规则）

| 任务场景 | 读取规则 |
|---------|---------|
| 用户提到「知识库」/项目总纲 | `python load_rule.py 知识库` |
| 写/改概念卡片 | `python load_rule.py 写卡片`（即 `kb-specs/spec-card`） |
| 批量填充知识库/为主题填充理论卡片 | `python load_rule.py 填充概念卡片`（即 `kb-specs/kb-fill-workflow`） |
| 写/改事件/经验/案例 | `kb-specs/spec-observation` |
| 跑脚本、改工具、新增脚本 | `kb-specs/spec-tools` + `kb-tools/readme` |
| 更新索引/概念图/标签索引 | `kb-specs/spec-index` |
| 项目阶段性自查/维护 | `kb-specs/spec-maintenance` |
| 推送 psychology-knowledge-base 到 GitHub | `kb-tools/sync-backup`（即 `tools/sync_backup.py --push`） |
| 进入心理学专家模式 | `psychology-expert-mode/main` |
| 进入跨学科研究搭档模式 | `research-partner/constitution` |
| 选择/调用 agent skills 或 AI 工具（headroom、markitdown、agent-reach、web-access）| `memory-rules/proactive-skill-usage` |
|选择/调用skills工具| `memory-rules/installed-skills.md` |

---

## 🔧 规则加载命令

```bash
python E:/psychology-knowledge-base/tools/load_rule.py <namespace> <alias>
```

**常用 namespace**：
- `memory-rules` — 记忆库中的行为规则与工具说明
- `kb-specs` — 心理学知识库规范
- `kb-tools` — 工具脚本说明
- `psychology-expert-mode` — 心理学专家模式
- `research-partner` — 跨学科研究搭档模式

**列出全部规则**：
```bash
python E:/psychology-knowledge-base/tools/load_rule.py --list
```

**校验注册表完整性**：
```bash
python E:/psychology-knowledge-base/tools/load_rule.py --verify
```

---

## 🤖 已自动化的 hooks

- **SessionStart**：自动注入 `priority-user-messages` + 本触发地图。
- **PostToolUse(Write|Edit)**：修改规则相关文件后，自动提醒维护闭环并运行 `--verify`。
- **保存后验证/格式化（当前未自动启用）**：`C:/Users/乏味/.claude/hooks/format_on_save.py` 与 `verify_on_save.py` 是 Claude Code `PostToolUse` Hook 脚本，设计为在每次 Write/Edit 后由 Claude Code 自动调用。它们通过 stdin 读取工具调用的 JSON payload，**直接手动运行不会生效**（stdin 为空即退出）。
  - 当前 `settings.json` 只注册了 `rule_hooks.py`，这两个脚本**未启用**。
  - 如需启用，需将其加入 `settings.json` 的 `hooks.PostToolUse` 配置；在此之前，写/改 `03-cards/`、`05-observations/`、`02-summaries/`、`04-index/`、`me-me/moo/日记/` 下的 `.md` 文件后，应自行检查格式与 frontmatter 完整性。

---

## 使用口诀

> **遇事不决查地图，异常先停再读规；任务开始先读规，不要凭记忆硬推。**
