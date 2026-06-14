# spec-maintenance.md — 维护机制

> **触发条件**：AI 完成阶段性工作后自查；用户提到维护/更新/同步时读取
> 本文件独立自足，不需要跨文件引用。

---

## 更新追溯表

> 修改了什么东西后，该同步更新哪些文件？避免改一处漏一处。

| 你改了什么 | 必须同步更新 |
|-----------|-------------|
| 目录结构、新增/删除目录 | `CLAUDE.md`（目录一览） + `04-index/spec-archive.md` |
| 卡片/观察的 YAML 模板、字段定义 | `04-index/spec-card.md` / `04-index/spec-observation.md` + `_template-*.md` |
| 工具脚本（新增/删除/改名/改参数） | `04-index/spec-tools.md` |
| 学科列表、事件类型、关系类型 | 对应 spec-*.md + `auto_tag.py` 关键词表（如有） |
| 项目核心原则、日常流程 | `CLAUDE.md` |
| 模式约定、触发条件 | `meta/psychology-expert-mode.md` |
| 子模式规则 | `00-prompts/` 对应文件 + `psychology-expert-mode/index.md` |
| 完成阶段性工作 | `PROJECT_LOG.md` + `CURRENT_STATE.md` |
| 个人档案（身份/偏好/环境） | `memory/user-profile.md` |

## 检查清单（每次阶段性完成后跑一遍）

- [ ] `grep -r "old-name"` 搜全仓库，确保没有残留引用（注释、附录、索引也要查）
- [ ] 改了 >5 个文件 → 之前打 commit 了吗？
- [ ] 跑过 `import_md.py` 同步数据库了吗？
- [ ] 更新了 `PROJECT_LOG.md` 吗？
- [ ] 如果有新概念/新事件 → 更新了 `04-index/` 下的索引文件吗？

## 陈旧内容审查（每月一次）

- 打开 `MEMORY.md`，逐条问自己：这个文件还对我有用吗？
- `user-profile.md`、`lessons-learned.md`、`workspace-setup.md` 这三个触发式文件最容易过时
- 信息已经体现在别处或不再适用 → 直接删
- 需要保留但更新 → 当场改
