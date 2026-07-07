---
name: claude-code-startup-workflow
description: Claude Code 会话启动时的完整加载链与工作流程（含心理学专家模式入口）
metadata:
  node_type: memory
  type: reference
  originSessionId: 0f110150-0b4d-491b-8f17-6f33ba643aef
  updated: 2026-06-15
---

# Claude Code 启动工作流 · 完整流程图

> 文字版完整流程图。涵盖每一份文件、每一个分支，从大到小四级展开。

---

## 一、一级流程（顶层六大分支）

```
                        ┌─────────────────────────┐
                        │     Claude Code 启动      │
                        └───────────┬─────────────┘
                                    │
        ┌───────┬───────┬───────┬───┴───┬───────┬───────┐
        ▼       ▼       ▼       ▼       ▼       ▼       ▼
      📌环境  📋档案  🧠记忆  📂项目  🎯模式  🔧技能  ⚡运行
```

---

## 二、二级流程（每个一级分支下的子分支）

```
📌 环境层                      📋 自建档案
├── 操作系统                   ├── 启动时自动加载（4 份）
├── Shell 环境                 └── 触发式按需加载（4 份）
├── 工作目录
└── MCP 服务器                 🧠 记忆系统
                              ├── 自建档案（Markdown）
📂 项目感知                   └── claude-mem（MCP 版）
├── 自动感知（CLAUDE.md）
└── 按需加载（用户提及）       🔧 技能系统
                              ├── 开发核心（7 个）
🎯 模式切换                   ├── 前端/设计（3 个）
├── 普通模式（默认）           ├── 文档（3 个）
├── 心理学专家模式             ├── 记忆/学习（5 个）
│   └── 跨学科研究搭档（子模式）└── 其他（2 个）

⚡ 运行时行为
├── 对话中自动捕获记忆
├── 技能触发（/ 或 AI 判断）
├── 模式指令监听
└── 项目感知触发
```

---

## 三、二级下的完整流程

### 📌 环境层 — 完整流程

```
📌 环境层（启动前就绪，和项目无关）
│
├── 1. 操作系统
│   └── Windows 11 Pro（版本 10.0.26200）
│       └── 平台标识：win32
│
├── 2. Shell 环境
│   └── Git Bash（POSIX sh，非 cmd.exe / PowerShell）
│       ├── Unix 语法：/dev/null 而非 NUL
│       ├── 路径：正斜杠
│       ├── 变量：$VAR 而非 %VAR% 或 $env:VAR
│       └── ⚠️ 已知坑：PowerShell 内联到 bash 会编码崩溃
│           └── 解决：先 Write .ps1 文件 → 再 pwsh -File 执行
│
├── 3. 工作目录
│   ├── 主目录：C:\Users\乏味
│   ├── 附加目录（6 个）：
│   │   ├── D:\桌面
│   │   ├── E:\psychology-knowledge-base
│   │   ├── E:\psychology-knowledge-base\03-cards
│   │   ├── E:\psychology-knowledge-base\04-index
│   │   ├── E:\psychology-knowledge-base\05-observations\typical-cases
│   │   └── E:\psychology-knowledge-base\tools
│   └── ⚠️ Bash 工作目录不持久（每次命令需显式 cd）
│
└── 4. MCP 服务器（4 个，启动时连接）
    ├── context7
    │   └── 功能：查询最新库/框架文档
    │       ├── resolve-library-id → 解析库名到 ID
    │       └── query-docs → 按问题查文档
    ├── fetch
    │   └── 功能：网页抓取（HTTP → Markdown）
    ├── memory
    │   └── 功能：知识图谱 CRUD
    │       ├── create_entities / delete_entities
    │       ├── create_relations / delete_relations
    │       ├── add_observations / delete_observations
    │       ├── search_nodes / open_nodes
    │       └── read_graph
    └── sequential-thinking
        └── 功能：动态反思式问题分析
```

---

### 📋 自建档案 — 完整流程

```
📋 自建档案（Markdown 文件，存在 E:\claude-config\projects\C--Users---\memory\）
│
├── 🔵 启动时自动加载（每次会话必读，共 5 份）
│   │
│   ├── ═══ 第 0 站：MEMORY.md（记忆索引）═══
│   │   ├── 角色：最先被读取，是整个系统的"目录页"
│   │   ├── 内容：所有档案的文件清单 + 加载策略
│   │   ├── 分为两区：
│   │   │   ├── 启动时自动加载（4 项）──→ 读完本文件后，依次加载下面 4 份
│   │   │   └── 触发式按需加载（4 项）
│   │   └── ⚠️ 它是"导游"，下面 4 份是被它指路才加载的
│   │
│   ├── ├── 第 1 站：memory-system-guide.md（双轨记忆系统说明）
│   │   │   ├── 加载原因：MEMORY.md 启动区第 1 项
│   │   │   ├── 自带 claude-mem vs 自建 Markdown 的对比
│   │   │   ├── 什么该放哪儿（决策树）
│   │   │   ├── 理想工作流：对话→自动捕获→定期复盘→写入档案
│   │   │   └── 记忆入口化规则：入口文件 + 按需读取
│   │   │
│   │   ├── 第 2 站：installed-skills.md（已装技能清单）
│   │   │   ├── 加载原因：MEMORY.md 启动区第 2 项
│   │   │   ├── 20 个技能分 5 类
│   │   │   ├── 已删除清单（精简历史）
│   │   │   └── claude-mem 状态说明（MCP 版可用 / Skill 版搁置）
│   │   │
│   │   ├── 第 3 站：psychology-expert-mode/index.md（模式入口）
│   │   │   ├── 加载原因：MEMORY.md 启动区第 3 项
│   │   │   ├── 基础模式触发指令："开启心理学专家模式"
│   │   │   ├── 子模式触发指令："开启跨学科研究搭档模式"
│   │   │   └── ⚠️ 只读入口，不加载详情
│   │   │
│   │   └── 第 4 站：projects-index.md（项目索引）
│   │       ├── 加载原因：MEMORY.md 启动区第 4 项
│   │       ├── 5 个项目列表（只含名称 + 路径）
│   │       └── ⚠️ 只读索引，不加载详情
│
└── 🟡 触发式按需加载（不随启动加载，共 4 份）
    │
    ├── user-profile.md（用户档案）
    │   └── 触发：用户提到身份/偏好时（信息已陈旧，参考价值有限）
    │
    ├── lessons-learned.md（经验教训）
    │   ├── 触发：涉及编码/脚本/批量操作时
    │   └── 内容：10 大类教训
    │       ├── 一、文件上传避坑
    │       ├── 二、技能安装避坑
    │       ├── 三、系统命令必须验证
    │       ├── 四、批量操作铁律（先测一个、外部依赖停下、给预估）
    │       ├── 五、沟通原则
    │       ├── 六、沟通铁律（不要瞎猜、时间 > token）
    │       ├── 七、脚本编码问题
    │       ├── 八、PowerShell 执行方案（自建 win-safe-ps）
    │       ├── 九、知识库项目教训（7 条子教训）
    │       └── 十、自动标签与文本匹配教训（4 条子教训）
    │
    ├── workspace-setup.md（工作区约定）
    │   ├── 触发：涉及磁盘/配置迁移时
    │   └── 内容：C→E 盘迁移、junction 用法、npm 配置
    │
    └── claude-code-startup-workflow.md（本文件）
        └── 触发：给人看完整流程时打开，不需要每次启动读
```

---

### 🧠 记忆系统 — 完整流程

```
🧠 记忆系统（双轨互补，同时运行）
│
├── 轨道 A：自建档案（Markdown）
│   ├── 存储位置：E:\claude-config\projects\C--Users---\memory\
│   ├── 格式：Markdown + YAML frontmatter
│   ├── 擅长记：稳定事实、用户画像、项目档案、经验教训、环境配置
│   ├── 特点：
│   │   ├── ✅ 人可以直接打开阅读
│   │   ├── ✅ 不会随对话变化
│   │   └── ✅ 每次会话全量注入索引（MEMORY.md）
│   ├── 注入策略（两层）：
│   │   ├── 自动注入：MEMORY.md + 4 份必读文件（每次会话）
│   │   └── 按需注入：lessons-learned / workspace-setup / user-profile / workflow（触发式）
│   └── 维护：手动整理，定期复盘后写入
│
└── 轨道 B：claude-mem（MCP 版）
    ├── 存储位置：知识图谱数据库（MCP memory server）
    ├── 擅长记：临时想法、对话碎片、决策过程、上下文
    ├── 特点：
    │   ├── ✅ 自动捕获（对话中产生的观察自动入库）
    │   ├── ❌ 人不能直接看（只能通过查询接口）
    │   └── ⚠️ 第二次会话起才注入相关上下文
    ├── 注入策略：按相关性自动检索注入
    └── 维护：被动积累，AI 定期复盘后提取精华写入轨道 A
```

---

### 📂 项目感知 — 完整流程

```
📂 项目感知（按需，不主动联想，不串项目）
│
├── 自动感知：当前目录存在 CLAUDE.md
│   ├── 条件：用户 cd 到某项目目录时
│   ├── 行为：自动读取该目录下的 CLAUDE.md
│   ├── 作用：项目规则手册（相当于该项目的 system prompt）
│   └── 示例：
│       └── 用户在 E:\psychology-knowledge-base 时
│           └── 自动读取 E:\psychology-knowledge-base\CLAUDE.md
│               └── 定义知识库的卡片格式、目录结构、导入脚本等规范
│
└── 按需加载：用户明确提到某项目
    ├── 入口文件：projects-index.md（5 个项目）
    ├── 触发条件：用户说出项目名
    ├── 行为：读取 projects/项目名/xxx.md
    └── 项目清单：
        ├── 考研陪伴应用
        │   └── projects/kaoyan-companion/kaoyan-companion.md
        ├── 心理学小程序
        │   └── projects/psychology-miniapp/psychology-miniapp.md
        ├── 心理学资源
        │   └── projects/psychology-resources/psychology-resources.md
        ├── 心理学知识库
        │   └── projects/psychology-kb/psychology-kb-toolstack-plan.md
        └── 微信读书导出工具
            └── projects/weread-exporter/weread-exporter-usage.md
```

---

### 🎯 模式切换 — 完整流程

```
🎯 模式切换（默认普通模式，指令触发切换）
│
├── 默认：普通模式
│   ├── 行为：正常回答，无额外规则
│   └── 加载：仅 MEMORY.md + 4 份必读档案
│
├── 心理学专家模式
│   ├── 触发指令："开启心理学专家模式"
│   ├── 前置条件：无（可在任何目录触发）
│   ├── 进入时自动加载：
│   │   └── E:\psychology-knowledge-base\meta\psychology-expert-mode.md
│   │       ├── 触发条件（专业术语 → 系统查阅）
│   │       ├── AI 身份（心理学研究助手）
│   │       ├── 语言要求（中文、学术但不晦涩）
│   │       ├── 方法要求（先查知识库 → 再补充外部）
│   │       ├── 教材推荐（优先推荐已有卡片）
│   │       └── Skills 使用（xlsx/docx 用于输出）
│   │
│   ├── 日常回答心理学问题（轻量路径）：
│   │   ├── 直接查 kb.db 数据库
│   │   └── 或翻 03-cards/ 目录
│   │   └── ⚠️ 不读任何 spec 文件
│   │
│   └── 特定任务（加载独立规范，共 6 份）：
│       ├── 写卡片       → 04-index/spec-card.md
│       ├── 写观察       → 04-index/spec-observation.md
│       ├── 同步/归档    → 04-index/spec-archive.md
│       ├── 跑脚本       → 04-index/spec-tools.md
│       ├── 更新索引     → 04-index/spec-index.md
│       └── 阶段性自查   → 04-index/spec-maintenance.md
│
│   └── 跨学科研究搭档（子模式，需先进入心理学专家模式）
│       ├── 触发指令："开启跨学科研究搭档模式"
│       ├── 前置条件：必须已在心理学专家模式中
│       ├── 额外加载：
│       │   ├── 常驻规则（始终在前端）：
│       │   │   └── research-partner-constitution.md
│       │   │       ├── 三条铁律：不编造、不讨好、不放弃追问
│       │   │       ├── 协议切换
│       │   │       └── 核心工作流（Stage A→B→C→D）
│       │   │
│       │   └── 按需规则（按阶段/主题读取）：
│       │       └── 工具：python tools/load_rule.py <别名>
│       │           ├── stage-a / stage-b / stage-c / stage-d
│       │           ├── role
│       │           ├── output
│       │           ├── commands
│       │           └── traps
│       │
│       └── 退出：关闭心理学专家模式时，子模式同时退出
```

---

### 🔧 技能系统 — 完整流程

```
🔧 技能系统（/ 触发或 AI 判断匹配，不会自动运行）
│
├── 开发核心（7 个）
│   ├── find-skills           → 搜索和发现 agent skills
│   ├── skill-creator         → 创建、修改、优化自定义 skill
│   ├── learn-codebase        → 学习代码库结构（逐文件阅读）
│   ├── make-plan             → 制定分阶段实施计划 → 通常配合 do 使用
│   ├── do                    → 用子代理执行 make-plan 的计划
│   ├── smart-explore         → AST 解析代码结构（省 token）
│   └── pathfinder            → 代码架构分析，找重复逻辑 → 输出 /make-plan
│
├── 前端/设计（3 个）
│   ├── frontend-design       → UI 设计指导（美学方向、排版）
│   ├── web-design-guidelines → 网页设计规范审查
│   └── design-is             → Dieter Rams 十原则审计 → 输出 /make-plan
│
├── 文档（3 个）
│   ├── docx                  → 生成/编辑 Word 文档
│   ├── pptx                  → 生成/编辑 PPT 幻灯片
│   └── xlsx                  → 生成/编辑 Excel 表格
│
├── 记忆/学习（5 个）
│   ├── remembering-conversations → 搜索过去对话恢复上下文
│   ├── self-improvement          → 从错误中学习，持续改进
│   ├── mem-search                → 搜索 claude-mem 记忆数据库
│   ├── knowledge-agent           → 从观察历史构建知识库并问答
│   └── how-it-works              → 解释 claude-mem 工作原理
│
└── 其他（2 个）
    ├── web-access            → 网页访问（搜索、抓取、登录后操作）
    └── win-safe-ps（自建）    → Windows PowerShell 安全执行
        ├── 位置：C:\Users\乏味\.claude\skills\win-safe-ps\skill.md
        └── 原则：先 Write 到 .ps1 文件 → 再 pwsh -File 执行
```

---

### ⚡ 运行时行为 — 完整流程

```
⚡ 运行时行为（启动后的动态过程）
│
├── 对话中自动捕获记忆
│   ├── claude-mem 自动将对话碎片写入知识图谱
│   ├── 事件类型：实体创建、关系建立、观察追加
│   └── 下个会话起自动注入相关上下文
│
├── 技能触发判断
│   ├── 方式 A：用户输入以 / 开头
│   │   └── 如 /docx、/find-skills、/make-plan
│   ├── 方式 B：AI 判断任务匹配某技能描述
│   │   └── 如用户说"生成一个 Word 报告" → 触发 docx
│   └── ⚠️ 技能不自动运行，必须触发
│
├── 模式指令监听
│   ├── 持续监听关键词：
│   │   ├── "开启心理学专家模式"
│   │   └── "开启跨学科研究搭档模式"
│   └── 匹配后执行对应加载流程
│
└── 项目感知触发
    ├── 用户 cd 到新目录 → 检查是否有 CLAUDE.md → 有则自动读
    └── 用户提到项目名 → 查 projects-index.md → 读对应项目文件
```

---

## 四、全貌总图（一级 + 二级合并视角）

```
                        ┌─────────────────────────────────┐
                        │        Claude Code 启动           │
                        │   Windows 11 + Git Bash + 4 MCP   │
                        └───────────────┬───────────────────┘
                                        │
        ┌───────────┬───────────┬───────┼───────┬───────────┬───────────┐
        ▼           ▼           ▼       ▼       ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │ 📌 环境  │ │ 📋 档案  │ │ 🧠 记忆  │ │ 📂 项目  │ │ 🎯 模式  │ │ 🔧 技能  │
   └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
        │           │           │           │           │           │
   ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐
   │Win11    │ │自动加载  │ │Markdown │ │自动感知  │ │普通模式  │ │开发 7个  │
   │Git Bash │ │ 4份必读  │ │手动整理  │ │CLAUDE.md │ │(默认)   │ │设计 3个  │
   │4个目录  │ │         │ │         │ │         │ │         │ │文档 3个  │
   │4个MCP   │ │按需加载  │ │MCP版    │ │按需加载  │ │心理学    │ │记忆 5个  │
   │         │ │ 4份触发  │ │自动捕获  │ │5个项目   │ │专家模式  │ │其他 2个  │
   └─────────┘ └─────────┘ └─────────┘ └─────────┘ │└─跨学科  │ └─────────┘
                                                     │  子模式  │
                                                     └─────────┘
```

---

## 五、加载时序

```
t=0  环境就绪（OS + Shell + MCP 连接）
     │
t=1  自建档案注入
     │  MEMORY.md → memory-system-guide → installed-skills
     │  → psychology-expert-mode/index → projects-index
     │
t=2  记忆系统注入（claude-mem 检索相关上下文，第二次会话起生效）
     │
t=3  项目感知（检查当前目录 CLAUDE.md，有则自动读）
     │
t=4  ─── 启动完成，等待用户输入 ───
     │
t=5  运行时（持续循环）
     ├── 模式指令监听 → 匹配则加载对应模式
     ├── 技能触发判断 → / 开头或 AI 匹配
     ├── 项目感知触发 → 用户提及或 cd 目录
     └── 自动记忆捕获 → claude-mem 写入知识图谱
```

---

## 六、关键设计原则

| 原则 | 说明 |
|------|------|
| **入口化** | 索引文件只放触发方式，详情不随启动加载 |
| **隔离性** | 项目之间不串，模式之间不串，读到 A 不看 B |
| **按需加载** | 启动只加载 4 份必读，其余触发时才读 |
| **双轨互补** | Markdown 记稳定事实，claude-mem 记对话碎片 |
| **技能被动** | 技能不自动运行，必须 / 触发或 AI 判断匹配 |
| **时间 > token** | 能直接跑命令验证的，不要中途停下来问用户 |
