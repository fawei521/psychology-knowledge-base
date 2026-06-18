---
name: spec-kb-fill-workflow
description: 心理学专家模式下为知识库填充概念卡片的标准工作流与操作规范
metadata:
  node_type: spec
  type: reference
  updated: 2026-06-18
---

# 心理学知识库填充工作流

> 触发条件：用户在心理学专家模式下要求为知识库填充理论概念卡片。

## 标准工作流

1. **确认概念点**
   - 用户从候选池中选择一个**具体概念点/理论簇**（如「记忆」「浪漫爱情」「认知发展」）。
   - 读取 `04-index/spec-card.md` 确认卡片规范。
   - 查看 `03-cards/` 中已有的相关卡片，避免重复。

2. **建立分类层级关系网络（必须先输出清单，再搜索写卡）**
   - 确定该概念点的**核心框架节点**（如记忆的 `three_stage_memory_model`、浪漫爱情的 `romantic_love`）。
   - 列出子主题卡片，并设计它们与核心节点、彼此之间的关系类型：`is-a` / `part-of` / `causes` / `extends` / `applies-to` / `supports` / `correlates-with` / `contrasts`。
   - **输出层级规划清单**：在写卡前以文本形式明确核心节点、子卡片列表、关系类型，避免边写边补结构。
   - 关系目标统一使用 `concept` 字段的值（不要带 `card-` 前缀）。
   - 若子卡片文件名按字母排序会先于核心节点导入，可通过以下方式之一避免关系解析失败：
     - 让核心节点文件名排在前面（如核心节点用 `card-core-xxx` 前缀）；
     - 导入后再运行一次关系重建脚本验证并补全。

3. **搜索权威来源**
   - 优先使用系统自带 **WebSearch** 工具搜索教材、Noba Project、OpenStax Psychology、学术综述、经典论文。
   - 对于需要登录、动态页面或反爬站点的内容，才启用 `web-access` skill；使用前必须先运行 `node "C:/Users/乏味/.claude/skills/web-access/scripts/check-deps.mjs"` 检查 Node.js 22+ 和 CDP 环境。
   - 每个概念需确认：定义、代表人物、经典实验、核心观点、评价/争议、考研常见考法。

4. **填充概念卡片**
   - 文件名：`card-{english_concept}.md`，多词用下划线。
   - YAML frontmatter：`concept`、`concept_cn`、`domain`、`tags`、`relations`。
   - 正文结构沿用 `spec-card.md` 推荐的八段式格式：定义、核心要点、理论背景、经典实验、评价与争议、生活实例、考研重点、文献来源。
   - 每个主题尽量一次性把核心理论全部覆盖，然后进入下一个主题。

5. **同步到 kb.db**
   - 运行：`python tools/import_md.py`
   - 该脚本会基于文件 hash 做增量同步，自动生成 embedding 并更新向量索引。
   - 导入顺序按**文件名排序**，因此关系目标若尚未存在，第一次导入可能无法解析。处理办法：
     - 若核心节点文件名排在子卡片之后，第一次导入后目标节点已存在，第二次运行 `import_md.py` 会重新解析 changed files 的关系；
     - 更稳妥的做法是导入后执行 SQL 验证，发现缺失时运行关系重建脚本（删除该概念簇内部旧关系，按 frontmatter 重新插入）。

6. **验证关系网络**
   - 用 SQL 查询 `relations` 表，确认同一主题内的卡片关系完整。
   - 若关系缺失，使用批量脚本根据 frontmatter 重建关系网络（删除该主题内部旧关系后重新插入）。

## 卡片内容要点

- 定义要精确，一句话说清概念是什么。
- 核心要点 3–5 条，避免堆砌。
- 代表人物和经典实验必须标注年份和关键操作。
- 评价维度包含：优势、争议/反例、与相近理论的区别。
- 考研重点包含：常考题型、易混淆点、记忆口诀。
- 文献来源优先引用教材章节和经典论文，网页来源作为补充。

## 工具选择

| 场景 | 工具 |
|---|---|
| 查教材/百科/综述/经典论文 | **WebSearch** |
| 需要登录、动态渲染、反爬站点 | **web-access skill**（需先 check-deps） |
| 批量搜索 + 事实核查 + 多源综合 | **deep-research skill** |
| 整理已有知识、建知识库结构 | **knowledge-agent skill** |

## 注意事项

- `web-access` skill 调用本身不会自动执行搜索，需要按 skill 指引先启动 CDP proxy。
- `import_md.py` 的关系解析依赖导入顺序；批量更新关系后建议手动重建该主题内部关系网络。
- 同一主题内卡片的关系网络应在填充具体卡片前确定，减少后续全改成本。
- 不要为每个卡片单独问用户确认格式，先按规范写，完成后统一展示。

## 已完成的主题示例

- **记忆**（2026-06-18）：12 张卡片，23 条关系，核心节点 `three_stage_memory_model`。

## 主题完成验收

确认一个概念点填充完成前，逐项检查：

1. **层级规划已输出**：核心节点、子卡片、关系类型在写卡前已明确。
2. **卡片覆盖完整**：该概念点的核心理论、关键概念、经典实验已全部写成卡片。
3. **关系网络建立**：核心节点与子节点之间关系清晰，用 SQL 查询 `relations` 表可验证。
   ```sql
   SELECT e1.name AS source, e2.name AS target, r.relation_type AS type
   FROM relations r
   JOIN entities e1 ON r.from_id = e1.id
   JOIN entities e2 ON r.to_id = e2.id
   WHERE e1.name IN ('concept_a', 'concept_b', ...);
   ```
4. **数据库已同步**：运行过 `python tools/import_md.py` 且无报错。
5. **标签已补全且无重复字段**：运行过 `python tools/auto_tag.py --apply`，并检查没有生成第二个 `tags:` 行。
6. **索引文件已更新**：`04-index/concept-map.md` 和 `04-index/tag-index.md` 已手动补充（或脚本已生成）。
7. **候选池已标记**：在 `04-index/topic-backlog.md` 中标记该概念点为「已完成」。
8. **已 git commit**：批量改动打检查点。

> **PROJECT_LOG 记录原则**：只记录通用流程改进、架构决策、可复用的踩坑教训，不记录具体填了哪个概念点（由 `topic-backlog.md` 负责）。

## 选择下一个概念点

候选池统一维护在 `04-index/topic-backlog.md`（如不存在则创建）。候选粒度是**具体概念点**（如「记忆」「认知发展」「焦虑障碍」），而不是宽泛学科（如「发展心理学」）。流程：

1. **展示候选**：从 `topic-backlog.md` 中列出 3-5 个未完成的候选概念点，每个附一句话说明重要性与考研关联。
2. **用户选择**：等待用户明确选择其中一个概念点。
3. **开始工作流**：回到本规范第 1 步「确认主题」。
4. **标记完成**：概念点填充并验收完成后，在 `topic-backlog.md` 中标记为「已完成」。流程改进、工具 bug、架构决策等通用经验才写入 `PROJECT_LOG.md`。
