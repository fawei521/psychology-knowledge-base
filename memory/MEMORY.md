# 记忆索引

> 这是我的**长期个人知识库**（自建档案），每次会话自动注入。对话中的碎片信息由自带的 `claude-mem` 系统自动捕获，两者互补。详见 [[memory-system-guide]]。

## 启动时自动加载

> 每次会话必读，不管在哪个目录、做什么任务。

- [双轨记忆系统说明](memory-system-guide.md) — 自带系统 vs 自建档案，什么该放哪儿
- [规则系统工具箱](rule-toolbox.md) — **已 hook 自动注入**：规则触发地图，让 AI 知道何时按需加载规则

## 触发式（不自动加载，按需读取）

> 只在特定情境下按需读取，不随会话启动加载。> 具体触发条件见 [规则系统工具箱](rule-toolbox.md)。

- [优先处理用户新消息](priority-user-messages.md) — 收到新消息后停下当前工作、优先回应（已 hook 自动注入）
- [已装技能](installed-skills.md) — 使用 Claude Code 技能或遇到技能相关问题时读取
- [心理学专家模式索引](psychology-expert-mode/index.md) — 进入心理学专家模式或研究搭档模式前读取
- [项目记忆索引](projects-index.md) — 用户提到具体项目时读取
- [执行指令无需反复确认](execute-without-confirm.md) — 听懂后直接执行，听不懂才问
- [规则系统维护闭环](rule-maintenance-loop.md) — 修改规则文件时的标准流程（修改规则文件时 hook 自动提醒）
- [用户档案](user-profile.md) — 用户提到身份/偏好时按需读取（信息已陈旧，参考价值有限）
- [经验教训 / 错题本](lessons-learned.md) — 涉及编码/脚本/批量操作时按需读取
- [禁止重复失败操作](no-repetitive-failed-operations.md) — **严重错误记录**：失败后不得自动重试，禁用 subagent 做文件扫描
- [工作区约定](workspace-setup.md) — 涉及磁盘/配置迁移时按需读取（迁移已完成，日常用不到）
- [工作原则：系统性思维](work-principles-systemic-thinking.md) — 处理非琐碎任务、设计工作流或规则时按需读取
- [moo 日记仓库](projects/moo-diary/moo-diary.md) — 个人作品/日记仓库，含 momo 导入规则
- [启动工作流图](思维导图\claude-code-startup-workflow.md) — 完整流程参考文档，给人看的，不需要每次启动读
- [研究搭档模式思维导图](思维导图\research-partner-mode-mindmap.md) — 跨学科研究搭档模式交互式思维导图 HTML，浏览器打开
- [心理学知识库保存验证钩子](psychology-kb-verify-hook.md) — 自动触发、生效条件与配置位置
- [psychology-knowledge-base 推送脚本](psychology-knowledge-base-push-script.md) — 推送到 GitHub 时必须使用 `tools/sync_backup.py`
