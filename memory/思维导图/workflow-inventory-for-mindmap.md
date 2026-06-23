# Claude Code 工作流全景图 · 供思维导图生成

> 层级索引。每个节点标明：文件/脚本位置、效用、谁来调取、何时触发。
> 文件位置前缀：
> - `memory/` → `C:/Users/乏味/.claude/projects/C--Users---/memory/`
> - `知识库/` → `E:/psychology-knowledge-base/`

---

## 一、顶层分支

```
                        ┌─────────────────────────┐
                        │     Claude Code 会话      │
                        │   （环境就绪 → 加载规则 → 等待指令） │
                        └───────────┬─────────────┘
                                    │
        ┌───────┬───────┬───────┬───┴───┬───────┬───────┬───────┐
        ▼       ▼       ▼       ▼       ▼       ▼       ▼       ▼
      📌环境  📋档案  🧠记忆  📂项目  🎯模式  🔧技能  ⚙️工具  ⚡运行
```

---

## 二、📌 环境层（启动前就绪）

| 节点 | 说明 | 位置/来源 |
|---|---|---|
| 操作系统 | Windows 11 Pro 10.0.26200 | 系统 |
| Shell | Git Bash（POSIX sh） | 系统 |
| 平台标识 | win32 | Claude Code 注入 |
| 工作目录 | `C:\Users\乏味` 为主；附加目录见下 | Claude Code 注入 |
| 附加目录 | `D:\桌面`、`E:\psychology-knowledge-base` 等 | `settings.local.json` |
| MCP 服务器 | context7 / fetch / memory / sequential-thinking | 启动时连接 |

**环境层规则/陷阱**：
- Bash 工作目录不持久 → 每次 Bash 前显式 `cd`。
- PowerShell 内联到 bash 会编码崩溃 → 先 Write `.ps1`，再 `pwsh -File` 执行。
- 记录文件：`lessons-learned.md`（八、Windows PowerShell 执行问题）。

---

## 三、📋 自建档案层（Markdown 规则系统）

### 3.1 启动时自动加载

| 顺序 | 文件 | 位置 | 效用 | 调取方式 |
|---|---|---|---|---|
| 第 0 站 | `MEMORY.md` | `memory/MEMORY.md` | 总目录页；列出所有档案 + 加载策略 | 每次会话自动注入 |
| 第 1 站 | `memory-system-guide.md` | `memory/memory-system-guide.md` | 双轨记忆系统说明；什么该放自带系统、什么该放自建档案 | 自动加载 |
| 第 2 站 | `installed-skills.md` | `memory/installed-skills.md` | 已装技能清单 20 个 + claude-mem 状态 | 自动加载 |
| 第 3 站 | `psychology-expert-mode/index.md` | `memory/psychology-expert-mode/index.md` | 心理学专家模式入口指针；触发指令 + 项目内规范路径 | 自动加载 |
| 第 4 站 | `projects-index.md` | `memory/projects-index.md` | 项目记忆总索引；只含名称+路径 | 自动加载 |

### 3.2 触发式按需加载（用户指令或异常触发）

| 文件 | 位置 | 效用 | 触发条件 |
|---|---|---|---|
| `rule-toolbox.md` | `memory/rule-toolbox.md` | **规则系统触发地图**；异常/任务该读哪个规则 | 已 hook 自动注入；任何不确定时先查本文件 |
| `priority-user-messages.md` | `memory/priority-user-messages.md` | 收到新消息后停下当前工作、优先回应 | 已 hook 自动注入；用户新消息打断时 |
| `execute-without-confirm.md` | `memory/execute-without-confirm.md` | 听懂后直接执行，听不懂才问 | 用户指令明确时遵循；不确定时读取 |
| `rule-maintenance-loop.md` | `memory/rule-maintenance-loop.md` | 修改规则文件/脚本/钩子后的标准闭环 | 修改规则相关文件时 hook 自动提醒；任务涉及规则系统时读取 |
| `no-repetitive-failed-operations.md` | `memory/no-repetitive-failed-operations.md` | 失败后禁止自动重试；禁用 subagent 做文件扫描 | 同一操作反复失败、token 激增时 |
| `work-principles-systemic-thinking.md` | `memory/work-principles-systemic-thinking.md` | 非琐碎任务的工作原则：分层、循环、显性化 | 复杂任务/流程设计/规则设计时 |
| `lessons-learned.md` | `memory/lessons-learned.md` | 踩坑记录与经验教训 | 涉及编码/脚本/批量操作时 |
| `workspace-setup.md` | `memory/workspace-setup.md` | E 盘工作区约定；junction/npm 迁移经验 | 涉及磁盘/配置迁移时 |
| `user-profile.md` | `memory/user-profile.md` | 用户档案（已陈旧，参考价值有限） | 用户提到身份/偏好时 |
| `psychology-kb-verify-hook.md` | `memory/psychology-kb-verify-hook.md` | 保存后自动验证钩子的配置、触发条件、fallback | 配置/调试 hooks 时；改知识库 .md 文件后 |
| `psychology-knowledge-base-push-script.md` | `memory/psychology-knowledge-base-push-script.md` | 推送到 GitHub 必须使用 `tools/sync_backup.py` | 用户说"推送""备份""同步"时 |
| `claude-code-startup-workflow.md` | `memory/思维导图/claude-code-startup-workflow.md` | 完整流程参考（给人看） | 不需要每次启动读 |
| `research-partner-mode-mindmap.md` | `memory/思维导图/research-partner-mode-mindmap.md` | 跨学科研究搭档模式交互式思维导图 HTML 入口 | 浏览器打开时 |

### 3.3 项目专属档案入口

| 项目 | 入口文件 | 触发条件 |
|---|---|---|
| 考研陪伴应用 | `projects/kaoyan-companion/kaoyan-companion.md` | 用户提到该项目 |
| 心理学小程序 | `projects/psychology-miniapp/psychology-miniapp.md` | 用户提到该项目 |
| 心理学资源 | `projects/psychology-resources/psychology-resources.md` | 用户提到该项目 |
| 心理学知识库 | `projects/psychology-kb/psychology-kb-toolstack-plan.md` | 用户提到该项目 |
| 微信读书导出工具 | `projects/weread-exporter/weread-exporter-usage.md` | 用户提到该项目 |
| moo 日记仓库 | `projects/moo-diary/moo-diary.md` | 用户提到该项目 |

---

## 四、🧠 记忆系统层（双轨互补）

### 4.1 轨道 A：自建 Markdown 档案

| 属性 | 说明 |
|---|---|
| 存储 | `C:/Users/乏味/.claude/projects/C--Users---/memory/`（junction 后实际在 E 盘） |
| 格式 | Markdown + YAML frontmatter |
| 擅长 | 稳定事实、项目档案、经验教训、环境配置、模式入口 |
| 注入 | 每次会话全量注入 `MEMORY.md` 索引；4 份必读自动加载；其余按需读取 |
| 维护 | 手动整理，定期复盘后写入 |

### 4.2 轨道 B：claude-mem（MCP 版）

| 属性 | 说明 |
|---|---|
| 存储 | 知识图谱数据库（MCP memory server） |
| 擅长 | 临时想法、对话碎片、决策过程、上下文 |
| 注入 | 第二次会话起按相关性自动检索注入 |
| 维护 | 被动积累；AI 定期复盘后提取精华写入轨道 A |
| 工具前缀 | `mcp__memory__*`（search_nodes / open_nodes / create_entities 等） |

---

## 五、📂 项目感知层

### 5.1 自动感知：CLAUDE.md

| 项目 | CLAUDE.md 位置 | 效用 |
|---|---|---|
| 心理学知识库 | `E:/psychology-knowledge-base/CLAUDE.md` | 项目总纲：目录结构、核心原则、读取规则表、日常流程 |

**触发**：用户 cd 到项目目录时自动读取。

### 5.2 按需加载：projects-index.md

- 用户明确提到某项目名 → 读取 `memory/projects/{项目名}/xxx.md`。
- 项目之间隔离，不串读。

---

## 六、🎯 模式切换层

### 6.1 普通模式（默认）

| 属性 | 说明 |
|---|---|
| 行为 | 正常回答，无额外规则 |
| 加载 | `MEMORY.md` + 4 份必读档案 |

### 6.2 心理学专家模式

| 项目 | 说明 |
|---|---|
| **开启指令** | 用户明确说出「开启心理学专家模式」 |
| **关闭指令** | 用户明确说出「关闭心理学专家模式」 |
| **加载文件** | `知识库/meta/psychology-expert-mode.md` |
| **日常回答** | 直接查 `kb.db` 或翻 `03-cards/`，不读 spec |
| **写卡片** | 读 `知识库/04-index/spec-card.md` |
| **写观察** | 读 `知识库/04-index/spec-observation.md` |
| **批量填充** | 读 `知识库/04-index/spec-kb-fill-workflow.md` |
| **跑脚本/改工具** | 读 `知识库/04-index/spec-tools.md` |
| **更新索引** | 读 `知识库/04-index/spec-index.md` |
| **阶段性自查** | 读 `知识库/04-index/spec-maintenance.md` |
| **同步/归档** | 读 `知识库/04-index/spec-archive.md` |

### 6.3 跨学科研究搭档模式（子模式）

| 项目 | 说明 |
|---|---|
| **进入条件** | 必须已在心理学专家模式中 |
| **开启指令** | 用户说「开启跨学科研究搭档模式」或讨论社会事件/时事分析 |
| **常驻加载** | `知识库/00-prompts/research-partner-constitution.md` |
| **阶段规则** | `00-prompts/rules/stage-a.md` 到 `stage-d.md` |
| **别名加载** | `python tools/load_rule.py <别名>` |
| **退出** | 关闭心理学专家模式时同时退出 |

### 6.4 研究搭档模式规则文件索引

| 文件 | 位置 | 效用 | 别名 |
|---|---|---|---|
| `research-partner-constitution.md` | `知识库/00-prompts/research-partner-constitution.md` | 宪法；三条铁律、协议体系、核心工作流 | `constitution` / `宪法` |
| `rules/traps.md` | `知识库/00-prompts/rules/traps.md` | 常见陷阱 | `traps` / `陷阱` |
| `rules/theory-blacklist.md` | `知识库/00-prompts/rules/theory-blacklist.md` | 严禁作为科学解释使用的概念 | `theory-blacklist` / `理论禁用` |
| `rules/meta.md` | `知识库/00-prompts/rules/meta.md` | 前言、元规则补充 | `meta` / `前言` / `元规则` |
| `rules/role.md` | `知识库/00-prompts/rules/role.md` | 角色提醒 | `role` / `角色` |
| `rules/commands.md` | `知识库/00-prompts/rules/commands.md` | 具体动作指令含义 | `commands` / `指令` |
| `rules/scenarios.md` | `知识库/00-prompts/rules/scenarios.md` | 日常/讲课/诊断/考研场景 | `scenarios` / `场景` |
| `rules/workflow.md` | `知识库/00-prompts/rules/workflow.md` | 完整工作流结构 | `workflow` / `工作流` |
| `rules/stage-a.md` | `知识库/00-prompts/rules/stage-a.md` | 阶段 A：事实锚定 | `stage-a` / `事实锚定` |
| `rules/stage-b.md` | `知识库/00-prompts/rules/stage-b.md` | 阶段 B：角度速览 | `stage-b` / `角度速览` |
| `rules/stage-c.md` | `知识库/00-prompts/rules/stage-c.md` | 阶段 C：分轮深入 | `stage-c` / `分轮深入` |
| `rules/stage-d.md` | `知识库/00-prompts/rules/stage-d.md` | 阶段 D：卡片归档 | `stage-d` / `卡片归档` |
| `rules/card-template.md` | `知识库/00-prompts/rules/card-template.md` | 归档卡片模板 | `card-template` / `卡片模板` |
| `rules/output.md` | `知识库/00-prompts/rules/output.md` | 输出约束 | `output` / `输出` |
| `rules/source-template.md` | `知识库/00-prompts/rules/source-template.md` | 四层信源模板 | `source-template` / `信源` |
| `rules/testing.md` | `知识库/00-prompts/rules/testing.md` | 测试规则 | `testing` / `测试` |

---

## 七、🔧 技能系统层

### 7.1 开发核心（7 个）

| 技能 | 效用 | 触发 |
|---|---|---|
| `find-skills` | 搜索和发现 agent skills | 用户输入 `/find-skills` 或找技能 |
| `skill-creator` | 创建、修改、优化自定义 skill | 用户输入 `/skill-creator` |
| `learn-codebase` | 学习代码库结构（逐文件阅读） | 用户输入 `/learn-codebase` |
| `make-plan` | 制定分阶段实施计划 | 用户输入 `/make-plan` |
| `do` | 用子代理执行计划 | 用户输入 `/do` |
| `smart-explore` | AST 解析代码结构（省 token） | 用户输入 `/smart-explore` |
| `pathfinder` | 代码架构分析，找重复逻辑 | 用户输入 `/pathfinder` |

### 7.2 前端/设计（3 个）

| 技能 | 效用 | 触发 |
|---|---|---|
| `frontend-design` | UI 设计指导 | `/frontend-design` |
| `web-design-guidelines` | 网页设计规范审查 | `/web-design-guidelines` |
| `design-is` | Dieter Rams 十原则审计 | `/design-is` |

### 7.3 文档（3 个）

| 技能 | 效用 | 触发 |
|---|---|---|
| `docx` | 生成/编辑 Word | `/docx` |
| `pptx` | 生成/编辑 PPT | `/pptx` |
| `xlsx` | 生成/编辑 Excel | `/xlsx` |

### 7.4 记忆/学习（5 个）

| 技能 | 效用 | 触发 |
|---|---|---|
| `remembering-conversations` | 搜索过去对话 | `/remembering-conversations` |
| `self-improvement` | 从错误中学习 | `/self-improvement` |
| `mem-search` | 搜索 claude-mem | `/mem-search` |
| `knowledge-agent` | 构建知识库并问答 | `/knowledge-agent` |
| `how-it-works` | 解释 claude-mem 工作原理 | `/how-it-works` |

### 7.5 其他（2 个）

| 技能 | 效用 | 触发 |
|---|---|---|
| `web-access` | 网页访问（搜索、抓取、登录后操作） | `/web-access` |
| `win-safe-ps` | Windows PowerShell 安全执行（自建） | `/win-safe-ps` |

### 7.6 专家模式专属技能

| 技能 | 效用 | 使用场景 |
|---|---|---|
| `literature-review` | 心理学文献综述 | 仅在心理学专家模式下使用 |
| `web-access` / `deep-research` / `knowledge-agent` / `smart-explore` | 深度研究/网页访问 | 仅在心理学专家模式下主动使用 |

---

## 八、⚙️ 工具/脚本层

### 8.1 心理学知识库核心脚本

| 脚本 | 位置 | 效用 | 常用命令 | 触发场景 |
|---|---|---|---|---|
| `import_md.py` | `知识库/tools/import_md.py` | Markdown → SQLite 同步（两阶段：先实体后关系） | `python tools/import_md.py` | 写完卡片/观察后同步数据库 |
| `watch_sync.py` | `知识库/tools/watch_sync.py` | 监控 .md 变化自动调用 `import_md.py` | `python tools/watch_sync.py` | 长期编辑时后台同步 |
| `auto_tag.py` | `知识库/tools/auto_tag.py` | 自动补全学科/事件标签 | `python tools/auto_tag.py --apply` | 批量卡片/观察后补标签 |
| `db_init.py` | `知识库/tools/db_init.py` | 初始化数据库（会清空） | `python tools/db_init.py` | 重建空库 |
| `query.py` | `知识库/tools/query.py` | 命令行查询数据库 | `python tools/query.py "SQL"` | 快速验证数据 |
| `semantic_search.py` | `知识库/tools/semantic_search.py` | 384 维向量语义搜索 | `python tools/semantic_search.py "查询"` | 语义检索 |
| `reindex_vectors.py` | `知识库/tools/reindex_vectors.py` | 重建向量索引 | `python tools/reindex_vectors.py` | 向量异常时 |
| `generate_concept_map.py` | `知识库/tools/generate_concept_map.py` | 从 relations 生成概念图 | `python tools/generate_concept_map.py --apply` | 主题完成后生成索引 |
| `rebuild_relations.py` | `知识库/tools/rebuild_relations.py` | 从 frontmatter 重建关系 | `python tools/rebuild_relations.py --all` | 关系解析异常时 |
| `load_rule.py` | `知识库/tools/load_rule.py` | 通用规则加载器 | `python tools/load_rule.py <namespace> <别名>` | 按别名加载规则 |
| `check_rule_refs.py` | `知识库/tools/check_rule_refs.py` | 扫描规则文件硬编码引用 | `python tools/check_rule_refs.py` | 检查断裂引用 |
| `sync_backup.py` | `知识库/tools/sync_backup.py` | 推送 memory + me-me 到 GitHub | `python tools/sync_backup.py --push` | 用户说推送/备份/同步 |

### 8.2 历史/谨慎使用脚本

| 脚本 | 位置 | 效用 | 备注 |
|---|---|---|---|
| `rewrite_cards.py` | `知识库/tools/rewrite_cards.py` | 批量重写卡片 | 历史脚本，谨慎使用 |
| `split_rules.py` | `知识库/tools/split_rules.py` | 拆分规则文件 | 仅在规则结构大改时考虑 |

### 8.3 规则加载器注册表

| 文件 | 位置 | 效用 |
|---|---|---|
| `rules-registry.yaml` | `知识库/tools/rules-registry.yaml` | `load_rule.py` 的别名与 namespace 注册表；新增/删除/重命名规则或脚本时必须同步 |

### 8.4 Claude Code Hooks 脚本

| 脚本 | 位置 | 效用 | 触发条件 |
|---|---|---|---|
| `rule_hooks.py` | `C:/Users/乏味/.claude/hooks/rule_hooks.py` | SessionStart 注入规则包；PostToolUse 修改规则文件后提醒维护闭环并运行 `--verify` | `settings.json` 配置后自动触发 |
| `verify_on_save.py` | `C:/Users/乏味/.claude/hooks/verify_on_save.py` | 保存后检查 frontmatter、链接、实体引用 | 修改知识库/日记 .md 后 |
| `format_on_save.py` | `C:/Users/乏味/.claude/hooks/format_on_save.py` | 保存后格式化 Markdown | 同上 |
| `verify_profiles.yaml` | `C:/Users/乏味/.claude/hooks/verify_profiles.yaml` | `verify_on_save.py` 的检查规则配置 | 配置文件 |
| `format_profiles.yaml` | `C:/Users/乏味/.claude/hooks/format_profiles.yaml` | `format_on_save.py` 的格式化规则配置 | 配置文件 |

### 8.5 配置：settings.json 中的 hooks

| Hook | 事件 | 执行脚本 | 说明 |
|---|---|---|---|
| `SessionStart` | 会话开始 | `rule_hooks.py` | 注入 `priority-user-messages` + `rule-toolbox` |
| `PostToolUse(Edit\|Write)` | 写/改文件后 | `format_on_save.py` + `verify_on_save.py` + `rule_hooks.py` | 格式化、验证、维护提醒 |

**注意**：`settings.json` 中 `hooks` 字段必须按官方格式配置，保存后需 `/hooks` 或重启生效。

---

## 九、⚡ 运行时行为层

| 行为 | 说明 |
|---|---|
| 对话中自动捕获记忆 | `claude-mem` 自动写入知识图谱（实体、关系、观察） |
| 技能触发 | 用户 `/` 开头或 AI 判断任务匹配技能描述 |
| 模式指令监听 | 监听「开启/关闭心理学专家模式」「开启跨学科研究搭档模式」 |
| 项目感知触发 | cd 到项目目录自动读 `CLAUDE.md`；用户提到项目名读 `projects-index` |
| 规则文件修改后 | `rule_hooks.py` 自动提醒维护闭环并运行 `load_rule.py --verify` |
| 保存知识库 .md 后 | `verify_on_save.py` + `format_on_save.py` 自动检查/格式化 |

---

## 十、📋 关键任务 → 规则/脚本速查表

| 任务 | 先读规则 | 再执行脚本 |
|---|---|---|
| 写/改概念卡片 | `知识库/04-index/spec-card.md` | `python tools/import_md.py` |
| 批量填充知识库 | `知识库/04-index/spec-kb-fill-workflow.md` | `import_md.py` → `auto_tag.py --apply` → `generate_concept_map.py --apply` |
| 写/改观察记录 | `知识库/04-index/spec-observation.md` | `python tools/import_md.py` |
| 同步数据库/归档 | `知识库/04-index/spec-archive.md` | `python tools/import_md.py` |
| 跑脚本/改工具 | `知识库/04-index/spec-tools.md` | 按需 |
| 更新概念图/索引 | `知识库/04-index/spec-index.md` | `python tools/generate_concept_map.py --apply` |
| 阶段性自查 | `知识库/04-index/spec-maintenance.md` | 按 checklist |
| 推送 GitHub | `memory/psychology-knowledge-base-push-script.md` | `python tools/sync_backup.py --push` |
| 进入心理学专家模式 | `知识库/meta/psychology-expert-mode.md` | — |
| 进入研究搭档模式 | `知识库/00-prompts/research-partner-constitution.md` | `python tools/load_rule.py <别名>` |
| 修改规则文件 | `memory/rule-maintenance-loop.md` | `python tools/load_rule.py --verify` |
| 同一操作反复失败 | `memory/no-repetitive-failed-operations.md` | 停下报告 |

---

## 十一、📁 关键文件总索引

### 记忆库（`memory/`）

| 文件 | 类型 | 作用 |
|---|---|---|
| `MEMORY.md` | 索引 | 总目录页 |
| `rule-toolbox.md` | 触发地图 | 规则系统入口地图 |
| `memory-system-guide.md` | 参考 | 双轨记忆系统说明 |
| `installed-skills.md` | 参考 | 已装技能清单 |
| `priority-user-messages.md` | 反馈 | 优先处理新消息 |
| `execute-without-confirm.md` | 反馈 | 听懂即执行 |
| `rule-maintenance-loop.md` | 反馈 | 修改规则标准流程 |
| `no-repetitive-failed-operations.md` | 反馈 | 禁止重复失败操作 |
| `work-principles-systemic-thinking.md` | 反馈 | 系统性思维工作原则 |
| `lessons-learned.md` | 反馈 | 经验教训 |
| `workspace-setup.md` | 项目 | 工作区约定 |
| `projects-index.md` | 参考 | 项目索引 |
| `psychology-expert-mode/index.md` | 参考 | 心理学专家模式入口 |
| `psychology-kb-verify-hook.md` | 项目 | 保存验证钩子说明 |
| `psychology-knowledge-base-push-script.md` | 项目 | 推送脚本说明 |
| `user-profile.md` | 用户 | 用户档案 |
| `思维导图/claude-code-startup-workflow.md` | 参考 | 启动流程参考 |
| `思维导图/research-partner-mode-mindmap.md` | 参考 | 研究搭档导图入口 |

### 心理学知识库项目内

| 文件 | 类型 | 作用 |
|---|---|---|
| `CLAUDE.md` | 总纲 | 项目规则手册 |
| `04-index/spec-card.md` | 规范 | 概念卡片规范 |
| `04-index/spec-observation.md` | 规范 | 观察记录规范 |
| `04-index/spec-kb-fill-workflow.md` | 规范 | 知识库填充工作流 |
| `04-index/spec-tools.md` | 规范 | 工具脚本规范 |
| `04-index/spec-index.md` | 规范 | 索引维护规范 |
| `04-index/spec-maintenance.md` | 规范 | 维护机制 |
| `04-index/spec-archive.md` | 规范 | 归档与同步规范 |
| `04-index/concept-map.md` | 索引 | 概念关系图（脚本生成） |
| `04-index/tag-index.md` | 索引 | 标签索引 |
| `04-index/event-classification.md` | 索引 | 事件分类手册 |
| `04-index/topic-pool.md` | 索引 | 主题储备池 |
| `04-index/topic-backlog.md` | 索引 | 主题待办/冲刺池 |
| `meta/psychology-expert-mode.md` | 模式 | 心理学专家模式行为约定 |
| `meta/psychology-textbook-recommendations.md` | 参考 | 教材推荐 |
| `00-prompts/research-partner-constitution.md` | 模式 | 研究搭档宪法 |
| `00-prompts/rules/*.md` | 规则 | 研究搭档子规则 |
| `tools/load_rule.py` | 脚本 | 规则加载器 |
| `tools/rules-registry.yaml` | 配置 | 规则别名注册表 |
| `tools/README.md` | 索引 | 脚本目录索引 |
| `tools/import_md.py` | 脚本 | Markdown → SQLite |
| `tools/sync_backup.py` | 脚本 | 推送到 GitHub |
| `PROJECT_LOG.md` | 日志 | 项目日志索引 |
| `CURRENT_STATE.md` | 状态 | 当前状态 + 待办 |

---

## 十二、🧩 设计原则

| 原则 | 说明 |
|---|---|
| **入口化** | 索引文件只放触发方式，详情不随启动加载 |
| **隔离性** | 项目之间不串，模式之间不串，读到 A 不看 B |
| **按需加载** | 启动只加载 4 份必读，其余触发时才读 |
| **双轨互补** | Markdown 记稳定事实，claude-mem 记对话碎片 |
| **技能被动** | 技能不自动运行，必须 `/` 触发或 AI 判断匹配 |
| **时间 > token** | 能直接跑命令验证的，不要中途停下来问用户 |
| **规则五处同步** | 改规则时同步 `rules/`、`tools/`、`memory/`、入口文件、`rules-registry.yaml` |

---

*生成时间：2026-06-21*
*用途：交给 agent 生成交互式思维导图*
