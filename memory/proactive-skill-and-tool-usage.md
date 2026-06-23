---
name: proactive-skill-and-tool-usage
description: 用户偏好：AI 应主动调用已安装的 agent skills 和 ai-tools，而非等待提醒
metadata:
  node_type: memory
  type: user
  originSessionId: 31b68c45-b8ce-4b4b-a583-44555514a512
---

# AI 工具与工作流使用指南

## 会话摘要（每次自动注入）

**用户偏好**：处理任务时主动检查并调用匹配的能力，而不是直接回答。

**轻量决策顺序**：

1. **非琐碎任务先想 agent-skills slash 命令**：`/spec` → `/plan` → `/build` → `/test` → `/review` → `/ship`。
2. **上下文紧张 / 要省 token / 代码结构分析** → 用 `headroom`。
3. **用户给了 PDF/Word/Excel/PPT/图片/音频/网页** → 用 `markitdown`。
4. **查小红书 / B站 / Twitter / Reddit / YouTube / 招聘 / GitHub** → 用 `agent-reach`。
5. **任意网页 / 登录后页面 / 内部系统 / 一手原始页面** → 用 `web-access` skill。

> 详细规范见下方。复杂任务或不确定时，手动加载本规则全文。

---

## 一、agent-skills：主工作流框架

### slash 命令

| 阶段 | 命令 | 触发场景 |
|------|------|---------|
| 定义 | `/spec` | 新功能、新产品、需要写规格 |
| 规划 | `/plan` | 任务复杂、多文件、需要拆解 |
| 构建 | `/build` | 已有 plan，开始实现 |
| 验证 | `/test` | 写逻辑、修 bug、需要测试 |
| 审查 | `/review` | 改完代码后做五轴审查 |
| 发布 | `/ship` | 准备合并/上线 |
| 简化 | `/code-simplify` | 代码太复杂、需要重构 |
| 性能 | `/webperf` | 前端性能审计 |

### 其他常用 skills

- `debugging-and-error-recovery` — 任何报错/异常
- `source-driven-development` — 查官方文档再实现
- `doubt-driven-development` — 高风险/不熟代码时对抗审查
- `context-engineering` — 上下文质量下降/换任务时
- `security-and-hardening` — 用户输入/认证/数据存储
- `api-and-interface-design` — 设计 API 或模块边界
- `frontend-ui-engineering` — UI 相关改动
- `git-workflow-and-versioning` — 任何代码变更

### 使用原则

- **复杂工程任务**（新功能、重构、多文件改动、bug 修复）：主动建议走 `/spec` → `/plan` → `/build`。
- **简单任务**（单文件小改、查资料、回答概念问题）：可直接处理，不必为了用 skill 而用 skill。
- **优先处理用户意图**，而不是优先展示 skill。

---

## 二、headroom：上下文优化与代码分析

### 路径

`E:\ai-tools\.venv\Scripts\headroom.exe`

### 典型场景

| 场景 | 命令 |
|------|------|
| 启动压缩代理 | `headroom proxy --memory --code-aware --learn` |
| 一次性压缩 messages | Python: `from headroom import compress` |
| 审计 Read 工具流量 | `headroom audit-reads --path ~/.claude/projects/myproj --format json` |
| 代码结构搜索 | `headroom sg -p "fn $NAME($$$ARGS) { $$$BODY }"` |
| 语法感知 diff | `headroom diff old.py new.py --display side-by-side` |
| 代码统计 | `headroom loc [dir]` |

### 使用原则

- 当前先作为 **CLI 工具按需调用**，不接入 MCP。
- memory 模块以后单独评估，暂不使用。
- 与 Claude Code 内置上下文管理互补：内置管理不够用或需要代码感知压缩时，再调用 headroom。

---

## 三、markitdown：文档转 Markdown

### 路径

`E:\ai-tools\.venv\Scripts\markitdown.exe`

### 支持格式

PDF、Word、Excel、PowerPoint、HTML、CSV、Jupyter Notebook、Outlook、ZIP、RSS/Atom、Wikipedia、YouTube、Bing SERP、图片、音频、纯文本。

### 典型用法

```bash
markitdown input.pdf -o output.md
markitdown input.docx -o output.md
markitdown input.csv -o output.md
```

### 使用原则

- 用户给文档/文件要处理时，直接调用 markitdown 转换。
- 管道用法：`cat input.pdf | markitdown`。

---

## 四、agent-reach：外部调研路由器

### 路径

`E:\ai-tools\.venv\Scripts\agent-reach.exe`

### 平台矩阵

| 分类 | 平台 | 后端 | 是否需要配置 |
|------|------|------|-------------|
| search | Exa 语义搜索 | mcporter + Exa MCP | 需装 mcporter |
| social | Twitter/X | twitter-cli / OpenCLI / bird | 需登录 Cookie |
| social | 小红书 | OpenCLI / xiaohongshu-mcp / xhs-cli | 桌面复用 Chrome 登录态 |
| social | B站 | bili-cli / OpenCLI / 搜索 API | 搜索 API 零配置 |
| social | Reddit | OpenCLI / rdt-cli | 必须登录 |
| social | V2EX | V2EX API | 公开 API，大陆可能需代理 |
| career | LinkedIn | linkedin-scraper-mcp / Jina Reader | Jina 可读公开页 |
| dev | GitHub | gh CLI | 需装 gh CLI |
| web | 任意网页 | Jina Reader | 完全零配置 |
| web | RSS/Atom | feedparser | 需装 feedparser |
| video | YouTube | yt-dlp | 需装 yt-dlp |
| video | 小宇宙播客 | groq-whisper + ffmpeg | 需 ffmpeg + Groq key |
| finance | 雪球 | Xueqiu API | 需登录 Cookie |

### 常用命令

```bash
agent-reach doctor --json          # 体检，看哪些通道可用
agent-reach setup                  # 交互配置向导
agent-reach configure --from-browser chrome  # 从浏览器提取 Cookie
agent-reach install --channels twitter,xiaohongshu,reddit,bilibili,all
```

### 使用原则

- 涉及 agent-reach 支持的 13 个平台时，优先用它。
- 零配置下只有 web (Jina Reader)、RSS、B站搜索可用，其他需安装后端+配置。
- 需要任意网页/登录后页面/内部系统时，回退到 `web-access` skill。

---

## 五、web-access：浏览器级兜底

### 触发方式

用户要求搜索/抓取/访问网页/操作浏览器/登录后操作等任何联网任务。

### 能力

- 通过 CDP 直连本地 Chrome/Edge
- 复用浏览器登录态
- 支持任意网站、动态渲染、复杂交互、截图

### 使用原则

- agent-reach 不覆盖的场景，或需要登录态/复杂交互的页面，用 web-access。
- 与 agent-reach 互补：agent-reach 优先用于已知平台，web-access 兜底任意网页。

---

## 六、综合调用决策表

| 用户意图 | 首选能力 |
|---------|---------|
| 新功能/复杂改动/修 bug | `/spec` → `/plan` → `/build` / `/test` |
| 代码审查/简化/性能审计 | `/review` / `/code-simplify` / `/webperf` |
| 上下文快满、要省 token、代码结构分析 | `headroom` |
| 给了 PDF/Word/Excel/PPT/图片/音频 | `markitdown` |
| 查小红书/B站/Twitter/Reddit/YouTube/招聘/GitHub | `agent-reach` |
| 查任意网页/登录后页面/内部系统 | `web-access` |
| 不确定该用什么 | `/plan` 或 `using-agent-skills` |

---

## 不要做的事

- 不要等用户说“用 /plan”才用。
- 不要凭直觉直接实现，跳过思考匹配能力的过程。
- 不要为了用 skill 而用 skill，简单任务直接处理。
- 不要说“你可以用 /xxx”，而是直接调用或说“我先用 /xxx 处理”。

---

**Why:** 用户希望 AI 能主动利用已安装的 workflow skills 和 CLI 工具，而不是把认知负担留给用户。

**How to apply:** 每次收到请求后，先快速扫描意图是否匹配某个 skill 或工具；如果匹配，优先调用而不是直接回答。复杂任务时手动加载本规则全文查看详细规范。
