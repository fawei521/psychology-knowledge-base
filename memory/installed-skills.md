---
name: installed-skills
description: "已安装的 Claude Code 技能清单，仅保留\"做自己的软件\"核心技能"
metadata: 
  node_type: memory
  created: 2026-06-11
  last_pruned: 2026-06-12
  type: project
  originSessionId: c794b212-8fb7-4879-aee3-b25dc32336a6
---

## 已安装（精简后）

### 开发核心
| 技能 | 作用 |
|------|------|
| `find-skills` | 搜索和发现 agent skills |
| `skill-creator` | 创建、修改、优化自定义 skill |
| `learn-codebase` | 学习代码库结构和逻辑 |
| `make-plan` | 制定分阶段实施计划 |
| `do` | 用子代理执行计划 |
| `smart-explore` | 代码结构搜索（AST 解析，省 token） |
| `pathfinder` | 代码架构分析，找重复逻辑 |

### 前端/设计
| 技能 | 作用 |
|------|------|
| `frontend-design` | 前端 UI 设计指导 |
| `web-design-guidelines` | 网页设计规范 |
| `design-is` | 用 Dieter Rams 原则审计设计 |

### 文档
| 技能 | 作用 |
|------|------|
| `docx` | 生成 Word 文档 |
| `pptx` | 生成 PPT |
| `xlsx` | 生成 Excel |

### 记忆/学习
| 技能 | 作用 |
|------|------|
| `remembering-conversations` | 搜索过去对话恢复上下文 |
| `self-improvement` | 从错误中学习持续改进 |
| `mem-search` | 搜索 claude-mem 记忆数据库 |
| `knowledge-agent` | 构建知识库并问答 |
| `how-it-works` | 解释 claude-mem 工作原理 |

### 其他
| 技能 | 作用 |
|------|------|
| `web-access` | 网页访问 |
| `win-safe-ps` | Windows PowerShell 安全执行（自建） |

## 已删除（2026-06-12 清理）

| 类型 | 删除的技能 |
|-

## 关于 claude-mem 的状态（2026-06-11 更新）

| 版本 | 状态 | 说明 |
|------|------|------|
| **MCP 版** | ✅ 已内置 | 天生就在我体内，工具列表可见，当前项目数据库为空，待播种 |
| **Skill 版** (`thedotmack/claude-mem`) | ❌ 未启动 | 需要 Bun 运行时，当前环境 SSL 证书验证失败，无法下载安装。Skill 文件已下载到 `~\.agents\skills\`，worker 服务未启动。 |

**结论**：skill 版暂时搁置，但 MCP 版已可用。详见 [[memory-system-guide]] 和 [[lessons-learned]] 中 "claude-mem 的认知纠偏"。
