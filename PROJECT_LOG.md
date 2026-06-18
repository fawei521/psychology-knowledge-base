# 心理学知识库项目日志

> 记录本项目的关键进展、决策、踩坑与想法。
> 更新频率：每周一次，关键节点追加。

## 项目背景

这是一个面向**心理学考研复习**的个人知识库。目标是把教材概念、理论、实验，以及个人经验、社会热点事件，结构化地组织起来，让 AI 能够在用户提问时从知识库中精准检索并作答。

核心原则：
- **卡片是给 AI 读的**，用户通过自然语言提问调用。
- **先搭稳概念骨架**，再补充个人经验与时事分析。
- **不追求自动化一步到位**：用户负责提供事件"种子"，AI 负责分析、关联和存储。

---

## 2026-06-12 项目启动与方向确定

### 本周关键工作

1. **开启心理学专家模式**
   - 按 `psychology-expert-mode.md` 约定进入专业回答状态。
   - 读取并加载知识库总规范、概念图、标签索引。

2. **明确知识库的使用方式**
   - 卡片主要给 AI 阅读，用户通过提问调用。
   - 不需要考虑 Markdown 对人的直接可读性。

3. **确定概念卡片最终格式方案**
   - 采用 **完整 YAML frontmatter + 英文概念名文件名 + 语义检索**。
   - 不硬编码复杂关系网，用 `domain` + `tags` + `sqlite-vec` 实现检索。
   - 编号（PSY-GN-XXX）仅作为 `id` 字段保留，用于备忘。

4. **生成并写入 30 张普通心理学概念卡片**
   - 按用户提供的七段式模板填充了 PSY-GN-001 ~ PSY-GN-030。
   - 文件已写入 `E:\psychology-knowledge-base\03-cards\`。

5. **同步到 SQLite 数据库**
   - 运行 `python tools/import_md.py` 完成同步。
   - 修改了 `tools/import_md.py`，使其兼容新模板（无 frontmatter 的七段式卡片）。
   - 中文概念名正确存储在 `name_cn` 字段。

6. **更新索引文件**
   - `04-index/concept-map.md`：新增"普通心理学考研核心概念"簇。
   - `04-index/tag-index.md`：新增通用心理学、社会心理学、认知等标签分类。

### 关键决策

- **不用轻量 frontmatter，用完整 frontmatter**：因为用户不直接看文件，AI 是主要读者，完整 frontmatter 最利于检索和推理。
- **不做复杂关系网**：30 个考研概念大多是平级考点，强行建关系网是过度设计，且容易标错。等知识库更大、真需要推理时再补。
- **个人经验/热点事件采用"种子 + 培育"模式**：用户提供事件线索，AI 负责多视角分析、关联概念、写入知识库。不急于自动化抓取。

### 遇到的问题

1. **新旧模板冲突**
   - 旧卡片有 YAML frontmatter，新模板没有，导致导入脚本第一次运行出错。
   - 解决：修改 `import_md.py` 兼容两种格式。

2. **中文概念名在数据库中显示异常**
   - 第一次导入时把中文概念名写入了 `name` 字段，Bash 终端显示乱码。
   - 解决：确认 UTF-8 字节正确，改为 `name=psy_gn_xxx`（英文标识），`name_cn=中文概念名`。

3. **子 Agent 临时文件位置失控**
   - 某个 Agent 把中间产物写到了 C 盘桌面。
   - 解决：已删除临时文件，后续会严格控制 Agent 输出位置约束。

### 下周计划

1. 把 30 张概念卡片改写成**完整 frontmatter + 英文概念名文件名**。
2. 升级 `tools/import_md.py` 为**增量同步**，避免每次全量重建。
3. 安装配置 `sqlite-vec`，实现语义检索。
4. 设计 `05-observations/` 的模板和录入流程。

### 临时想法

- 未来可以考虑一个"复习模式"：随机抽取一个概念，让用户用费曼学习法复述，AI 对照卡片内容评分。
- 热点事件自动化抓取可以放到项目后期，前期重点是把概念骨架搭稳。

---

## 2026-06-12 上传 GitHub

### 关键工作

- 将本地仓库首次推送到 `https://github.com/fawei521/psychology-knowledge-base`
- 分支：`main`
- 共提交 62 个文件

### 状态

- 本地与远程仓库已关联
- 下阶段工作（增量同步、sqlite-vec、observations 模板）待后续推进

---

## 2026-06-12 增量同步与语义检索完成

### 关键工作

- 重写 `tools/import_md.py` 支持增量同步（基于文件 mtime + hash）
- 更新 `tools/db_init.py` 添加 `sync_log` 扩展字段和 `vec_documents` 向量表
- 安装 `sqlite-vec` 和 `sentence-transformers`（使用 hf-mirror 镜像）
- 新增 `tools/reindex_vectors.py`：为所有文档生成 384 维 embedding
- 新增 `tools/semantic_search.py`：支持自然语言语义检索

### 状态

- 增量同步测试通过：再次运行 `import_md.py` 时 changed files = 0
- 语义搜索测试通过：英文查询 "working memory capacity" 能召回相关概念
- 中文查询在 Bash 终端有编码显示问题，但数据库中存储正确

### 新增工具

- `python tools/import_md.py` — 增量导入 Markdown 到数据库
- `python tools/reindex_vectors.py` — 重建所有向量索引
- `python tools/semantic_search.py "查询文本"` — 语义搜索

### 遇到的问题

1. **sentence-transformers 下载 SSL 证书失败**
   - 解决：在代码中设置 `HF_ENDPOINT=https://hf-mirror.com` 并跳过 SSL 验证

2. **sqlite-vec 向量格式错误**
   - 最初用逗号分隔字符串，sqlite-vec 要求 JSON 数组格式
   - 解决：用 `json.dumps()` 序列化向量

---

## 2026-06-12 Observations 模板与流程完成

### 关键工作

- 新增 `05-observations/_template-observation.md` 模板文件
- 新增示例：`obs-personal-experience-2026-06-05-kaoyan-insomnia-anxiety.md`
- 更新 `CLAUDE.md` v0.1：
  - 添加 observations 正文结构建议
  - 明确测试策略：不写正式测试套件，关键功能手动验证
- 测试：新 observation 成功导入数据库并参与语义搜索

### 测试策略决策

- 当前阶段不写正式测试文件
- 原因：系统仍在快速迭代，测试维护成本高于收益
- 做法：关键功能改完后手动跑一遍验证
- 未来出 bug 时，再针对具体 bug 补回归检查

### 状态

- 概念骨架、增量同步、语义检索、observations 模板均已就绪
- 知识库基本运转流程已打通


---

## 2026-06-14 目录重构、分类手册整合、自动标签系统

### 完成事项

1. **分类手册整合**
   - 将"社会事件心理认知分类手册"精简版写入 `04-index/event-classification.md`
   - 包含 8 类型总览表、决策树、混合事件规则、理论速查、逐类型判断提示
   - 用途：参考工具，非每次加事件的硬性要求

2. **目录架构调整**
   - `03-cards/` 下新建 13 个学科子目录（含 `.gitkeep`），作为学科首页导航入口
   - 概念卡片仍平铺在 `03-cards/`，通过 `#学科/xxx` 标签实现跨学科归属
   - 删除 `06-event-cards/`，事件文件统一归入 `05-observations/` 三个子目录：
     - `current-events/` — 社会热点事件
     - `personal-experiences/` — 个人经历
     - `typical-cases/` — 典型案例深度分析

3. **标签替代子目录**
   - 决策：用 Obsidian 嵌套标签（`#学科/普通心理学`、`#事件类型/威胁-防御`）替代子目录分类
   - 优势：一张卡片可打多学科标签，解决跨学科理论归属问题（如 Bandura 同时属于社会/学习/人格/普通心理学）
   - 一张卡片可打多事件类型标签（如彩礼事件同时是 认同-团结 + 威胁-防御）

4. **自动标签脚本 `tools/auto_tag.py`**
   - 概念卡片：根据 `domain` 字段关键词匹配，自动补全 `#学科/xxx` 标签
   - 事件文件：扫描 `current-events/` + `typical-cases/`，匹配 YAML + 正文前 800 字，≥2 关键词命中才确认
   - 默认 dry-run 模式，需 `--apply` 才实际写入
   - 处理三种 frontmatter 情况：已有 tags / 有 YAML 无 tags / 无 YAML

5. **标签写入结果**
   - 41 张概念卡片全部写入 `#学科/xxx` 标签
   - 4 个事件文件写入 `#事件类型/xxx` 标签：
     - 碳水脸事件 → 认同-团结 + 权力-支配
     - 碳水脸分析报告 v1.2 → 同上
     - 明星塌房群体极化 → 认同-团结
     - 彩礼事件分析 v1.1 → 认同-团结 + 威胁-防御

### 踩坑与教训

| # | 问题 | 教训 | 类型 |
|---|---|---|---|
| 1 | 初版事件标签匹配全文，分析文本讨论所有类型，每个事件被标 6-8 种 | **匹配范围必须限缩**：只扫 YAML 字段 + body 前 800 字 | 普遍 |
| 2 | `patch_tags` 只处理"已有 tags 行"的情况，彩礼事件无 YAML frontmatter 且体内有 YAML 代码块，正则匹配出错 | **文本处理要覆盖三种情况**：有 tags / 有 YAML 无 tags / 无 YAML | 普遍 |
| 3 | auto_tag.py 头部注释写 `06-event-cards/`，但目录已删除、代码已改为 `typical-cases/` | **改代码时同步更新注释**，否则文档是谎言 | 普遍 |
| 4 | 分析报告 v1.2 附录仍引用 `06-event-cards/` 路径 | **删目录后 grep 残留引用**，不能只删目录本身 | 项目 |
| 5 | 大规模改 41 张卡片标签前没有 git commit | **批量修改前先打 commit**，方便回滚 | 普遍 |
| 6 | Windows Git Bash 终端中文乱码，只能靠 Read 工具逐文件验证 | **中文项目在 Windows 下验证按文件内容而非终端输出** | 项目 |

### 当前架构总览

```
psychology-knowledge-base/
├── 03-cards/                  ← 概念卡片（平铺，用标签分类）
│   ├── 10-普通心理学/...      ← 13 个学科子目录（首页导航，各含 .gitkeep）
│   └── card-*.md              ← 41 张概念卡片（#学科/xxx 标签）
├── 04-index/
│   ├── concept-map.md
│   ├── tag-index.md
│   └── event-classification.md ← 社会事件分类手册（8 类型）
├── 05-observations/
│   ├── current-events/        ← 社会热点 + 分析报告
│   ├── personal-experiences/  ← 个人经历
│   └── typical-cases/         ← 典型案例深度分析
├── tools/
│   ├── auto_tag.py            ← 自动标签（新卡/新事件用的核心工具）
│   ├── import_md.py           ← 增量导入数据库
│   ├── semantic_search.py     ← 语义检索
│   └── ...
└── PROJECT_LOG.md             ← 本文件
```

### 日常使用流程

```
加新概念卡片 → 写 domain 字段        → python tools/auto_tag.py --apply → 学科标签自动补
加新社会事件 → 写 YAML + 正文描述    → python tools/auto_tag.py --apply → 事件类型自动补
找某学科卡片 → Obsidian 标签面板点 #学科/社会心理学
找某类型事件 → Obsidian 标签面板点 #事件类型/不公-愤怒
```

### 待处理

- 13 个学科子目录写入首页导航卡片
- 5 张占位符卡片（彩礼事件卡片 11-15）填充内容
- Zotero 文献条目 + concept card 的 `citekeys` 字段
- 脚本：自动生成 `04-index/tag-index.md` 和 `04-index/concept-map.md`
- 分析报告 v1.2 附录路径引用更新

---

## 2026-06-15 Claude Code 启动链优化 + 技术规范拆分

### 完成事项

1. **MEMORY.md 加载策略分级**
   - 拆分为「启动时自动加载」（5 个）和「触发式」（3 个）
   - `user-profile.md`、`lessons-learned.md`、`workspace-setup.md` 改为触发式
   - 新增 `claude-code-startup-workflow.md` 记录完整 6 层加载链

2. **CLAUDE.md 重写为项目总纲**
   - 只保留项目是什么、核心原则、目录一览、读取规则表、日常流程
   - 技术规范全部移到 `04-index/spec-*.md`
   - 读取规则表：用户任务 → 精确文件，不再需要 AI 自己判断读哪节

3. **技术规范从单文件拆分为 6 个独立文件**
   - 根目录 `index.md` 删除
   - `04-index/spec-card.md` — 概念卡片规范
   - `04-index/spec-observation.md` — 观察记录规范
   - `04-index/spec-archive.md` — 归档与同步规范
   - `04-index/spec-tools.md` — 工具脚本规范
   - `04-index/spec-index.md` — 索引维护规范
   - `04-index/spec-maintenance.md` — 维护机制（更新追溯表 + 检查清单 + 月度审查）
   - 优势：按任务精确触发，不再在一大张文件里找小节

4. **心理学专家模式入口重构**
   - `psychology-expert-mode/index.md` 拆清层次：基础模式触发 → 行为约定 → 按需规范 → 子模式
   - 子模式（跨学科研究搭档）明确标注嵌套在专家模式之下
   - `meta/psychology-expert-mode.md` 不再自动加载 `index.md`，改为按任务触发 `spec-*.md`

5. **启动树形图更新**
   - `claude-startup-tree.html`：2 次重写，修复 JS 语法错误、深色模式配色、BOM 编码
   - 树数据更新为新加载结构：触发式文件标记为紫色、子模式嵌套展示
   - 新增缩放/平移/双击重置交互

### 踩坑与教训

| # | 问题 | 教训 | 类型 |
|---|---|---|---|
| 1 | 树形图 HTML 在 Windows 下打开空白（3 次 debug） | SVG 需 `width:100vw;height:100vh` CSS；JS 避免重复声明；Windows 需要 UTF-8 BOM | 项目 |
| 2 | CLAUDE.md 加了"一屏以内"硬约束 | 用户反馈：可用性第一，不用硬凑一屏 | 普遍 |
| 3 | 拆分后 Obsidian workspace.json 残留旧 `index.md` 引用 | 删文件后检查 IDE 缓存文件 | 项目 |

### 待处理

- 概念关系图和思维导图（用户说"不急，等我指令"）
- `04-index/` 下的 HTML 思维导图文件后续整理

---

## 2026-06-18 概念簇填充工作流优化

### 背景

以「浪漫爱情」概念簇为试点，跑了一遍完整的知识库填充流程，发现流程规范中有几处需要固化到规则里。

### 关键决策

1. **候选池粒度下沉到「具体概念点/理论簇」**
   - 原候选池是「发展心理学」「异常心理学」等学科级主题，范围过大、难以落地。
   - 改为「记忆」「浪漫爱情」「认知发展」等具体概念簇，`topic-backlog.md` 中维护。

2. **填充前必须先做层级规划**
   - 明确核心节点、子卡片、关系类型后，再开始搜索和写卡。
   - 避免边写边补结构，导致关系网络遗漏或反复修改。

3. **关系解析失败的处理方式**
   - `import_md.py` 按文件名排序导入，若核心节点文件名排在子卡片之后，第一次导入时关系目标可能不存在。
   - 规范中明确：导入后必须验证 `relations` 表，缺失时手动重建该概念簇内部关系。

### 发现的问题

1. **`auto_tag.py` 会追加重复 `tags:` 字段**
   - 脚本在文件末尾追加新的 `tags: [...]` 行，而不是修改已有 tags 列表，导致 frontmatter 重复。
   - 需要修复脚本或在 `--apply` 后人工检查。

2. **PROJECT_LOG 不应记录具体填充了哪个概念簇**
   - 具体完成情况由 `topic-backlog.md` 负责；PROJECT_LOG 只记录通用流程改进和架构决策。

### 已更新的规则文件

- `04-index/spec-kb-fill-workflow.md`：候选池粒度、层级规划前置、导入后关系验证、验收 checklist。
- `04-index/spec-tools.md`：记录 `auto_tag.py` 的已知问题与检查方法；新增 `watch_sync.py` 使用说明。
- `04-index/spec-maintenance.md`：新增概念簇填充完成 checklist；同步检查项纳入 `watch_sync.py`。
- `tools/auto_tag.py`：修复为合并 tags 而非追加（已完成）。
- `tools/watch_sync.py`：新增 Markdown 自动同步脚本，保存 .md 后自动调用 `import_md.py`。

### 待处理

- 跑通一次新规范下的完整填充，验证流程是否顺畅。
- 长期运行 `watch_sync.py` 的实际稳定性观察。
