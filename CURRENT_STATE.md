# 当前状态

> 项目轻量状态看板。
> 历史决策与踩坑见 [`PROJECT_LOG.md`](PROJECT_LOG.md)（索引）和 [`project-logs/`](project-logs/)（按日期归档）。
> 概念簇候选池见 [`04-index/topic-backlog.md`](04-index/topic-backlog.md)（冲刺池）和 [`04-index/topic-pool.md`](04-index/topic-pool.md)（储备池）。

## Sprint 目标

完成概念图自动化和候选池拆分，建立轻量状态看板，进入常规概念簇填充。

## 进行中

无

## 待处理

- [x] 合并/删除 7 个重复 concept 文件（子目录完整版 vs 根目录旧版）
- [ ] 脚本化 `04-index/tag-index.md`
- [ ] 13 个学科子目录写入首页导航卡片
- [ ] Zotero 文献 + `citekeys` 字段填充
- [ ] 分析报告附录路径引用更新（仍引旧 `06-event-cards/`）
- [ ] `03-cards/` 中 `card-*-2026.md` 事件卡迁移到 `05-observations/`
- [ ] 决定是否把 `generate_concept_map.py` 接入 `watch_sync.py`
- [ ] `generate_concept_map.py` 扩展性预案（待卡片数 >500 或单簇 >50 节点时考虑）：
  - 按 `domain` 过滤生成子图；
  - 按核心节点生成单簇图；
  - 大簇折叠/精简输出；
  - 增量更新（只重算 changed cards 涉及的簇）；
  - 用并查集替代 BFS 重构聚类逻辑。

## 远期

- `02-summaries/` 模板和流程优化
- sqlite-vec 语义搜索升级
- 5 张占位符卡片（彩礼事件卡片 11-15）填充

## 最近完成

- 2026-06-21: 概念图自动化脚本 `tools/generate_concept_map.py` + 候选池拆分
- 2026-06-21: 安装全局 pre-commit hook，禁止空 commit/amend
- 2026-06-21: 创建 `CURRENT_STATE.md` 状态看板

## 阻塞/需决策

无

---

## 维护规则

1. **每次工作收尾时更新本文件**：把完成项移到"最近完成"，把新发现的待处理项加入"待处理"。
2. **进入新 sprint 时更新 Sprint 目标**：由用户确认或 AI 提议后写入。
3. **不在这里写历史细节**：具体决策过程、踩坑、数据写入 `PROJECT_LOG.md`。
4. **不在这里写概念簇详情**：候选概念簇只写标题，详情在 `topic-backlog.md` / `topic-pool.md`。
5. **保持轻量**：待处理项超过 10 个时，把低优先级项移回 `topic-pool.md` 或 `PROJECT_LOG.md`。
