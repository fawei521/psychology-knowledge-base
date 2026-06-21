---
name: psychology-kb-toolstack-plan
description: 心理学知识库采用 Obsidian+Zotero+SQLite 工具栈的升级计划
metadata: 
  node_type: memory
  type: project
  originSessionId: 0f110150-0b4d-491b-8f17-6f33ba643aef
---

# 心理学知识库工具栈升级计划

## 背景
当前知识库位于 `E:\psychology-knowledge-base\`，采用 Markdown + YAML Frontmatter + SQLite（kb.db）结构。手动维护分类和索引负担较重，需要引入工具减负。

## 目标工具栈
| 层级 | 工具 |
|---|---|
| 文献管理 | **Zotero** + Better BibTeX |
| 笔记/知识库前端 | **Obsidian** 打开现有 Markdown |
| 数据库 | 继续用 **SQLite (kb.db)** |
| 自动索引 | Python 脚本生成 `tag-index.md` / `concept-map.md` |
| AI 辅助 | Claude 辅助写标签建议和链接发现脚本 |
| 概念图 | Obsidian Graph View 或 CmapTools |

## 执行日志（2026-06-14）

### 已完成
1. Obsidian Vault 配置：`E:\psychology-knowledge-base\`，图谱/反向链接/标签/大纲/属性面板已就位
2. Zotero 安装 + Better BibTeX 安装 + Citation Key 公式设为 `auth.lower + shorttitle(3,3) + year`
3. Obsidian Zotero Integration 插件安装并验证通过
4. 5 张概念卡片（card-intimacy-politicization-2026 等）YAML 新增 `citekeys: []` 字段
5. 建立独立目录：`03-cards/10-social-psychology/`、`20-personality-psychology/` 等（待填充）
6. 项目日志 `C:\Users\乏味\.claude\projects\C--Users---\memory\projects\psychology-kb\psychology-kb-toolstack-plan.md`
7. Zotero Connector 浏览器扩展已安装

### 未完成
- [ ] 往 Zotero 里添加真实文献条目（浏览器扩展卡顿，待后补）
- [ ] 往 citekeys 字段填入实际 citekey
- [ ] 中期：写 Python 脚本自动生成 `04-index/tag-index.md` 和 `04-index/concept-map.md`
- [ ] 远期：引入 sqlite-vec 做语义检索

## 执行步骤
1. ~~**立即**：用 Obsidian Vault 打开 `E:\psychology-knowledge-base\`~~  完成
2. ~~**近期**：安装 Zotero + Better BibTeX，把 source_papers 改为 citekey 格式~~  完成（格式已就位，内容待填充）
3. **中期**：写 Python 脚本自动生成 `04-index/tag-index.md` 和 `04-index/concept-map.md`
4. **远期**：引入 sqlite-vec 做语义检索

## 核心原则
- 不推倒重来，在现有 Markdown+SQLite 基础上叠加工具
- 停止手动维护分类和索引，让链接和脚本自然涌现
- 卡片采用渐进式摘要，不追求一次写完美
- 社会事件分类手册保持轻薄，概念卡片按需调用

## 项目专门经验教训（2026-06-14）

> 这些经验仅适用于本项目的技术栈和目录结构。通用经验见 [[lessons-learned]]。

### 1. Windows Git Bash 中文乱码 ≠ 数据损坏
**现象**：Bash 执行 `python auto_tag.py` 后终端输出中文标签乱码。
**根因**：Windows Git Bash (MSYS) 对 Python stdout 的 UTF-8 中文渲染有问题。
**验证方法**：用 Read 工具逐文件检查实际内容，或用 Python `print(repr(text))` 看原始字节。
**教训**：在 Windows 做中文 Markdown 项目，不要靠终端输出判断正确性，按文件实际内容验证。

### 2. Obsidian 嵌套标签比子目录更适合跨学科分类
**决策过程**：子目录方案（一卡一学科）vs 标签方案（一卡多标签）→ 选标签。
**原因**：许多理论跨多个学科（如 Bandura 的社会认知理论同时属于社会/学习/人格/普通），子目录需要做符号链接或复制，标签只用一行 `tags: [...]`。
**Obsidian 原生支持**：标签面板自动分组 `#学科/社会心理学` → 点即筛选。
**局限**：标签多了以后维护成本会上升，需配合 `auto_tag.py` 自动补标签。

### 3. 本项目的自动标签参数
- 事件匹配范围：YAML 字段 + body 前 800 字
- 事件类型确认阈值：≥2 个不同关键词命中（通用原则见 [[lessons-learned]]）
- 扫描目录：`03-cards/`（概念）、`05-observations/current-events/` + `05-observations/typical-cases/`（事件）

## 当前项目状态（2026-06-14）

- 41 张概念卡片，全部有 `#学科/xxx` 标签
- 5 个事件文件，全部有 `#事件类型/xxx` 标签
- `tools/auto_tag.py` 可对新卡片/事件自动打标签
- 13 个学科子目录已建（.gitkeep），待写首页导航卡片
- `04-index/event-classification.md` 作为分类手册参考
- `06-event-cards/` 已删除，事件统一在 `05-observations/`

## 相关记忆
- [[projects-index]]
- [[psychology-expert-mode-index]]
- [[workspace-setup]]
- [[lessons-learned]]
