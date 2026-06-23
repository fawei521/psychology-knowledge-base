# Claude Code 工作流树型关系图 · 供思维导图生成

> 本文档按「流程 → 阶段 → 规则/脚本调用链」展开，突出规则文件之间的先后顺序和触发关系。
> 不展开卡片、日志等大量内容文件，只关注规则系统的骨架。

---

## 流程一：Claude Code 会话启动流程

```
Claude Code 启动
    │
    ├── 环境就绪
    │   ├── 操作系统 Windows 11 Pro
    │   ├── Shell Git Bash
    │   ├── 工作目录 C:\Users\乏味
    │   └── MCP 服务器连接（context7 / fetch / memory / sequential-thinking）
    │
    ├── SessionStart Hook 触发
    │   └── 运行 rule_hooks.py
    │       ├── 注入 priority-user-messages
    │       └── 注入 rule-toolbox（规则系统触发地图）
    │
    ├── 自建档案自动加载
    │   ├── MEMORY.md（总目录页）
    │   ├── memory-system-guide.md（双轨记忆说明）
    │   ├── installed-skills.md（技能清单）
    │   ├── psychology-expert-mode/index.md（模式入口指针）
    │   └── projects-index.md（项目索引入口）
    │
    ├── claude-mem 检索注入（第二次会话起）
    │
    ├── 项目感知检查
    │   ├── 当前目录有 CLAUDE.md？
    │   │   └── 是 → 自动读取该项目总纲
    │   │       └── 例：E:\psychology-knowledge-base\CLAUDE.md
    │   └── 用户提到具体项目？
    │       └── 是 → 读取 memory/projects/项目名/xxx.md
    │
    └── 启动完成 → 等待用户输入
```

---

## 流程二：用户消息处理流程

```
用户发送新消息
    │
    ├── 触发 priority-user-messages
    │   └── 停下当前工作，优先处理新消息
    │
    ├── 判断用户意图
    │   ├── 明确指令 → 执行 execute-without-confirm
    │   │   └── 听懂直接执行，听不懂才问
    │   │
    │   └── 模糊/风险操作 → 读取 execute-without-confirm
    │       └── 针对具体点提问，不泛泛确认
    │
    ├── 识别是否为模式切换指令
    │   ├── 「开启心理学专家模式」
    │   │   └── 进入流程三：心理学专家模式
    │   ├── 「关闭心理学专家模式」
    │   │   └── 退出模式，恢复普通助手
    │   ├── 「开启跨学科研究搭档模式」
    │   │   └── 进入流程四：研究搭档模式
    │   └── 普通问题 → 继续判断任务类型
    │
    └── 进入对应任务流程
        ├── 写概念卡片 → 流程五：卡片创建
        ├── 批量填充知识库 → 流程六：知识库填充
        ├── 写观察记录 → 流程七：观察记录
        ├── 跑脚本/改工具 → 流程八：工具脚本
        ├── 更新索引 → 流程九：索引维护
        ├── 修改规则文件 → 流程十：规则维护闭环
        ├── 推送到 GitHub → 流程十一：推送备份
        └── 一般问答 → 直接回答
```

---

## 流程三：心理学专家模式进入与运行流程

```
用户说「开启心理学专家模式」
    │
    ├── 读取 meta/psychology-expert-mode.md
    │   ├── 确认身份：心理学研究助手
    │   ├── 语言：大白话解释，学术但不晦涩
    │   ├── 方法：先查知识库 → 再补充外部
    │   └── 知识库调用：查 kb.db / 03-cards/
    │
    ├── 告知用户「已加载心理学专家模式」
    │
    └── 日常心理学问题回答
        ├── 轻量路径
        │   ├── 查 kb.db 数据库
        │   └── 翻 03-cards/ 目录
        │   └── 不读 spec 文件
        │
        └── 特定任务按需加载规范
            ├── 写/改概念卡片 → 04-index/spec-card.md → 流程五
            ├── 批量填充 → 04-index/spec-kb-fill-workflow.md → 流程六
            ├── 写/改观察 → 04-index/spec-observation.md → 流程七
            ├── 同步/归档 → 04-index/spec-archive.md
            ├── 跑脚本/改工具 → 04-index/spec-tools.md → 流程八
            ├── 更新索引 → 04-index/spec-index.md → 流程九
            └── 阶段性自查 → 04-index/spec-maintenance.md

用户说「关闭心理学专家模式」
    │
    └── 退出模式，恢复普通助手状态
        └── 同时退出跨学科研究搭档子模式（如果正在运行）
```

---

## 流程四：跨学科研究搭档模式阶段流程

```
用户说「开启跨学科研究搭档模式」
    │
    ├── 前置检查：已在心理学专家模式中？
    │   └── 否 → 先进入心理学专家模式
    │
    ├── 加载 00-prompts/research-partner-constitution.md（宪法）
    │   ├── 元规则：精神优先于字面、反对表演脚本
    │   ├── 角色：研究搭档，不是老师/学生/秘书
    │   ├── 三条铁律：不编造、不讨好、不放弃追问
    │   ├── 协议体系：严格 / 流动 / 归档
    │   └── 核心工作流：A → B → C → D
    │
    ├── 默认加载两条常驻规则
    │   ├── rules/traps.md（常见陷阱）
    │   └── rules/theory-blacklist.md（理论禁用）
    │
    └── 按阶段推进
        │
        ├── 阶段 A：事实锚定
        │   ├── 加载 rules/stage-a.md
        │   ├── 提供 rules/source-template.md 给用户参考
        │   ├── 用户贴回四层信源
        │   └── AI 联网交叉验证
        │
        ├── 阶段 B：角度速览
        │   ├── 加载 rules/stage-b.md
        │   └── AI 给出多角度快速扫描
        │
        ├── 阶段 C：分轮深入
        │   ├── 加载 rules/stage-c.md
        │   ├── 用户选择方向 / 补充 / 纠正
        │   └── AI + 用户多轮深入
        │
        └── 阶段 D：卡片归档
            ├── 加载 rules/stage-d.md
            ├── 加载 rules/card-template.md
            ├── 加载 rules/output.md
            └── 输出标准化知识卡片

运行时按需加载规则
    │
    ├── 需要元规则补充 → rules/meta.md
    ├── 角色提醒/切换 → rules/role.md
    ├── 具体动作指令 → rules/commands.md
    ├── 切换场景模式 → rules/scenarios.md
    ├── 完整工作流结构 → rules/workflow.md
    └── 测试/验证 → rules/testing.md

协议切换
    │
    ├── 「严格起来」→ 严格协议（默认）
    ├── 「流动起来」→ 流动协议（最小约束）
    └── 「归档」→ 归档协议（生成卡片）

退出
    │
    └── 关闭心理学专家模式时一并退出
```

---

## 流程五：概念卡片创建流程

```
用户要求写/改概念卡片
    │
    ├── 读取 04-index/spec-card.md
    │   ├── YAML 模板（concept / concept_cn / domain / tags / citekeys / relations）
    │   ├── 学科列表
    │   ├── 关系类型表
    │   └── 八段式正文结构
    │
    ├── 查重
    │   ├── 翻 03-cards/ 已有卡片
    │   └── 查 kb.db entities 表
    │
    ├── 确定存放位置
    │   └── 03-cards/{学科编号}-{学科名}/card-{english_concept}.md
    │
    ├── 撰写卡片
    │   ├── frontmatter
    │   └── 八段式正文
    │       ├── 定义
    │       ├── 核心要点
    │       ├── 理论背景
    │       ├── 经典实验
    │       ├── 评价与争议
    │       ├── 生活实例
    │       ├── 考研重点
    │       └── 文献来源
    │
    ├── 保存 .md 文件
    │   └── 触发 PostToolUse hook
    │       ├── format_on_save.py（格式化）
    │       └── verify_on_save.py（验证 frontmatter/链接/实体引用）
    │
    └── 同步数据库
        └── python tools/import_md.py
```

---

## 流程六：知识库批量填充流程

```
用户要求为知识库填充/编写理论概念卡片
    │
    ├── 读取 04-index/spec-kb-fill-workflow.md
    │
    ├── 步骤 0：批量操作前检查
    │   └── git status + checkpoint commit（如 >5 文件可能改动）
    │
    ├── 步骤 1：确认概念点
    │   ├── 从 04-index/topic-backlog.md 冲刺池选 1 个概念簇
    │   └── 读取 04-index/spec-card.md 确认格式
    │
    ├── 步骤 2：建立层级关系网络
    │   ├── 确定核心框架节点
    │   ├── 列出子主题卡片
    │   ├── 设计关系类型
    │   └── 输出层级规划清单（先给用户看结构）
    │
    ├── 步骤 3：搜索权威来源
    │   ├── 优先 WebSearch
    │   ├── 需要登录/动态页面 → web-access skill（先 check-deps）
    │   └── 多源综合 → deep-research skill
    │
    ├── 步骤 4：填充概念卡片
    │   └── 按 spec-card.md 写多张卡片
    │
    ├── 步骤 5：同步数据库
    │   └── python tools/import_md.py
    │       └── 如关系解析警告 → python tools/rebuild_relations.py --all
    │
    ├── 步骤 6：验证关系网络与标签
    │   ├── SQL 查 relations 表
    │   ├── python tools/auto_tag.py --apply
    │   └── 检查 04-index/concept-map.md
    │
    ├── 步骤 7：生成概念关系图
    │   └── python tools/generate_concept_map.py --apply
    │
    ├── 标记完成
    │   └── 在 04-index/topic-backlog.md 标记「已完成」
    │
    └── 推进规则
        ├── 完成 1 个概念簇后输出摘要
        ├── 自动从冲刺池选下一个概念点
        └── 等待用户指令后再继续
```

---

## 流程七：观察记录创建流程

```
用户要求写/改事件/经验/案例
    │
    ├── 读取 04-index/spec-observation.md
    │   ├── YAML 模板（observation_type / title / event_date / context / behavior / tags / related_entities）
    │   ├── 三种类型：personal_experience / typical_case / current_event
    │   ├── 8 种事件类型关键词表
    │   └── 正文结构
    │
    ├── 确定类型与目录
    │   ├── personal_experience → 05-observations/personal-experiences/
    │   ├── typical_case → 05-observations/typical-cases/
    │   └── current_event → 05-observations/current-events/
    │
    ├── 撰写观察文件
    │   ├── frontmatter
    │   └── 正文
    │       ├── 事件描述
    │       ├── 多视角分析
    │       ├── 可验证的假设
    │       └── 涉及概念（[[card-xxx]]）
    │
    ├── 保存 .md 文件
    │   └── 触发保存验证 hook
    │
    └── 同步数据库
        └── python tools/import_md.py
```

---

## 流程八：工具脚本使用与修改流程

```
用户要求跑脚本/改工具/新增脚本
    │
    ├── 读取 04-index/spec-tools.md
    │
    ├── 常用脚本选择
    │   ├── 同步 Markdown → SQLite → import_md.py
    │   ├── 自动监控同步 → watch_sync.py
    │   ├── 自动补标签 → auto_tag.py
    │   ├── 语义搜索 → semantic_search.py
    │   ├── 生成概念图 → generate_concept_map.py
    │   ├── 重建关系 → rebuild_relations.py
    │   └── 规则加载 → load_rule.py
    │
    ├── 如需加载规则
    │   └── python tools/load_rule.py <namespace> <别名>
    │       ├── namespace: research-partner / psychology-expert-mode / startup-workflow
    │       ├── namespace: memory-rules / kb-specs / kb-tools
    │       └── 别名定义在 tools/rules-registry.yaml
    │
    ├── 修改脚本后同步更新三处
    │   ├── tools/README.md
    │   ├── 04-index/spec-tools.md
    │   └── tools/rules-registry.yaml
    │
    └── 修改 rules-registry.yaml 后
        └── python tools/load_rule.py --verify
```

---

## 流程九：索引维护流程

```
用户要求更新索引
    │
    ├── 读取 04-index/spec-index.md
    │
    ├── 概念关系图
    │   └── python tools/generate_concept_map.py --apply
    │       └── 生成/更新 04-index/concept-map.md
    │
    ├── 标签索引
    │   ├── python tools/auto_tag.py --apply
    │   └── 04-index/tag-index.md（待脚本化，目前按需手动维护）
    │
    └── 事件分类手册
        └── 04-index/event-classification.md（仅在调整分类体系时手动改）
```

---

## 流程十：规则系统修改维护闭环流程

```
修改规则相关文件
    │
    ├── 触发 PostToolUse(Edit|Write) hook
    │   └── 运行 rule_hooks.py
    │       ├── 判断是否为规则文件
    │       │   └── 00-prompts/rules/、meta/、04-index/spec-、tools/rules-registry.yaml
    │       │       memory/rule-maintenance-loop.md、memory/priority-user-messages.md 等
    │       │
    │       ├── 弹出「规则维护闭环提醒」
    │       └── 运行 python tools/load_rule.py --verify
    │
    ├── 读取 memory/rule-maintenance-loop.md
    │
    ├── 步骤 1：改具体规则/脚本/钩子
    │   ├── rules/ 下修正规则内容
    │   ├── tools/ 下新增/修改脚本
    │   └── memory/ 下新增/修改钩子说明
    │
    ├── 步骤 2：回写入口与索引
    │   ├── 模式规则 → 更新模式入口文件
    │   ├── 项目总纲 → 更新 CLAUDE.md 读取规则表
    │   ├── 脚本 → 更新 tools/README.md + 04-index/spec-tools.md
    │   └── 记忆库钩子 → 更新 MEMORY.md 触发式索引
    │
    ├── 步骤 3：同步 tools/rules-registry.yaml
    │   ├── 新增/删除/重命名规则文件 → 更新对应 namespace 的 aliases
    │   ├── 新增/删除/重命名脚本 → 更新 kb-tools namespace
    │   └── 新增/删除/重命名记忆库钩子 → 更新 memory-rules namespace
    │
    ├── 步骤 4：运行 python tools/load_rule.py --verify
    │   └── 检查：缺失文件 / 未注册文件 / 别名冲突 / 重复注册
    │
    └── 步骤 5：记录到项目日志
        ├── PROJECT_LOG.md 索引
        └── project-logs/YYYY-MM-DD.md 归档
```

---

## 流程十一：保存后自动验证流程

```
修改知识库/日记的 .md 文件
    │
    ├── 触发 PostToolUse(Edit|Write) hook
    │   └── settings.json 中配置的 hooks 生效
    │
    ├── format_on_save.py 运行
    │   └── 按 format_profiles.yaml 格式化 Markdown
    │
    ├── verify_on_save.py 运行
    │   ├── 按 verify_profiles.yaml 检查
    │   ├── 检查必填 frontmatter
    │   ├── 检查内部 [[card-xxx]] / [[summary-xxx]] 链接
    │   └── 检查 frontmatter 中的实体引用
    │
    └── 发现问题 → systemMessage 蓝色警告
        无问题 → 静默通过

Hook 未启用时的 fallback
    │
    ├── python tools/load_rule.py --verify
    ├── python tools/check_rule_refs.py（如存在）
    └── SQL 查询 relations 表验证关系网络
```

---

## 流程十二：推送到 GitHub 流程

```
用户说「推送 psychology-knowledge-base」或「备份 memory 和 me-me」
    │
    ├── 读取 memory/psychology-knowledge-base-push-script.md
    │
    ├── 执行标准命令
    │   └── cd /e/psychology-knowledge-base
    │       └── python tools/sync_backup.py --push
    │
    ├── 脚本行为
    │   ├── 复制 memory/ → 知识库/memory/
    │   ├── 复制 E:/me me → 知识库/me-me/
    │   ├── 排除 原文件 / 原始备份 / 图片视频音频
    │   ├── git add -A
    │   ├── git commit
    │   └── git push
    │
    └── 可选清理
        └── python tools/sync_backup.py --push --clean
```

---

## 流程十三：异常处理流程

```
运行中遇到异常
    │
    ├── 同一操作反复失败 ≥2 次
    │   └── 读取 memory/no-repetitive-failed-operations.md
    │       ├── 最多只处理一次失败
    │       ├── 禁止 subagent 做文件系统扫描
    │       ├── Read 失败立刻跳过
    │       └── 外部依赖失败立刻停下报告用户
    │
    ├── 用户新消息打断当前任务
    │   └── 读取 memory/priority-user-messages.md
    │       └── 完成当前工具调用后切换新消息
    │
    ├── 不确定要不要确认
    │   └── 读取 memory/execute-without-confirm.md
    │       └── 听懂直接执行，听不懂才问
    │
    ├── 复杂任务/流程设计
    │   └── 读取 memory/work-principles-systemic-thinking.md
    │       └── 分层、循环、显性化
    │
    └── 工具/脚本行为异常
        ├── 读 memory/lessons-learned.md
        └── 跑 python tools/load_rule.py --verify
```

---

## 流程十四：规则加载器调用链

```
python tools/load_rule.py <namespace> <别名>
    │
    ├── 读取 tools/rules-registry.yaml
    │   ├── global_aliases（全局别名）
    │   └── namespaces（各规则集）
    │       ├── research-partner
    │       ├── psychology-expert-mode
    │       ├── startup-workflow
    │       ├── memory-rules
    │       ├── kb-specs
    │       └── kb-tools
    │
    ├── 解析 namespace + alias → 文件路径
    │
    └── 输出规则文件内容

python tools/load_rule.py --list
    └── 列出所有可用 namespace + alias

python tools/load_rule.py --verify
    ├── 检查别名指向文件是否存在
    ├── 检查 base_dir 下未注册文件
    ├── 检查跨 namespace 别名冲突
    └── 检查同一文件重复注册
```

---

## 流程十五：双轨记忆系统工作流

```
对话中产生信息
    │
    ├── 临时/碎片/动态信息
    │   └── 自动进入 claude-mem（MCP memory server）
    │       ├── create_entities
    │       ├── create_relations
    │       ├── add_observations
    │       └── search_nodes / open_nodes
    │
    └── 稳定/长期/事实信息
        └── 等待 AI 定期复盘
            ├── 提取精华
            ├── 写入 Markdown 档案
            │   └── memory/*.md
            ├── 更新 MEMORY.md 索引
            └── 下次会话自动注入
```

---

## 关键规则调用关系总图

```
MEMORY.md（入口）
    │
    ├── 自动加载链
    │   ├── memory-system-guide.md
    │   ├── installed-skills.md
    │   ├── psychology-expert-mode/index.md
    │   │   └── 触发 → 知识库/meta/psychology-expert-mode.md
    │   │       ├── 日常回答 → 查 kb.db / 03-cards/
    │   │       └── 特定任务 → 04-index/spec-*.md
    │   │           ├── 写卡片 → spec-card.md
    │   │           ├── 批量填充 → spec-kb-fill-workflow.md
    │   │           ├── 写观察 → spec-observation.md
    │   │           ├── 跑脚本 → spec-tools.md
    │   │           ├── 更新索引 → spec-index.md
    │   │           ├── 阶段性自查 → spec-maintenance.md
    │   │           └── 同步归档 → spec-archive.md
    │   │
    │   │       └── 子模式触发 → 00-prompts/research-partner-constitution.md
    │   │           ├── 阶段 A → rules/stage-a.md + source-template.md
    │   │           ├── 阶段 B → rules/stage-b.md
    │   │           ├── 阶段 C → rules/stage-c.md
    │   │           └── 阶段 D → rules/stage-d.md + card-template.md + output.md
    │   │
    │   └── projects-index.md
    │       └── 触发 → memory/projects/{项目名}/*.md
    │
    └── 按需加载链
        ├── rule-toolbox.md（规则地图）
        │   └── 指向以下规则
        ├── priority-user-messages.md
        ├── execute-without-confirm.md
        ├── rule-maintenance-loop.md
        ├── no-repetitive-failed-operations.md
        ├── work-principles-systemic-thinking.md
        ├── lessons-learned.md
        ├── workspace-setup.md
        ├── psychology-kb-verify-hook.md
        └── psychology-knowledge-base-push-script.md

规则加载器核心
    │
    ├── tools/load_rule.py
    │   └── 读取 tools/rules-registry.yaml
    │       ├── 所有规则的 namespace + alias 映射
    │       └── python tools/load_rule.py --verify 检查完整性
    │
    └── 修改规则后触发
        └── rule_hooks.py（SessionStart / PostToolUse hook）
            ├── 注入规则包
            └── 提醒维护闭环 + 自动 verify
```

---

## 文件位置速查

| 符号 | 实际路径 |
|---|---|
| `memory/` | `C:/Users/乏味/.claude/projects/C--Users---/memory/` |
| `知识库/` | `E:/psychology-knowledge-base/` |
| `hooks/` | `C:/Users/乏味/.claude/hooks/` |

---

*生成时间：2026-06-21*
*用途：交给 agent 按流程树生成思维导图，强调规则文件之间的调用顺序*
