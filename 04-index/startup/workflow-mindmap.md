---
title: "知识库工作流程 · 思维导图"
type: index
tags: [workflow, guide]
---

# 心理学知识库 · 完整工作流程

```mermaid
mindmap
  root((心理学知识库<br/>工作流程))
    🚀启动加载
      CLAUDE.md<br/>项目规则手册
      MEMORY.md<br/>个人档案索引
      ::_不会自动加载_<br/>项目详细记忆<br/>专家模式
    📥添加内容<br/>四类入口
      01-raw<br/>原始材料
        PDF论文
        网页存档
        ::只存不检索
      02-summaries<br/>结构化摘要
        关键发现
        方法
        涉及概念
      03-cards<br/>概念卡片
        domain 字段
        tags 字段
        ::自动标签依据
      05-observations<br/>观察事件
        current-events<br/>社会热点
        personal-experiences<br/>个人经历
        typical-cases<br/>典型案例
    🏷️自动标签
      auto_tag.py
        概念卡片
          扫描 domain + tags + concept
          对照 13 学科关键词表
          补全 #学科/xxx
        事件文件
          扫描 YAML + 正文前800字
          对照 8 种事件类型关键词表
          ≥2 关键词命中才确认
          补全 #事件类型/xxx
    💾同步数据库
      import_md.py
        增量同步
          对比 mtime + hash
          只处理 新增/修改/删除
        kb.db
          SQLite 数据库
          Markdown 是唯一真相源
    🔍检索查找
      标签筛选
        Obsidian 标签面板
        点 #学科/社会心理学
      反向链接
        打开卡片
        看谁引用了它
      语义搜索
        semantic_search.py
        384维向量匹配
        理解语义不靠关键词
    🔧维护收尾
      更新索引
        concept-map.md
        tag-index.md
        event-classification.md
      写日志
        PROJECT_LOG.md（索引）
        project-logs/YYYY-MM-DD.md
        CURRENT_STATE.md
      git commit
        批量改动前先提交
        阶段性 push 到 GitHub
```

---

## 文字版流程（从上到下）

```
🚀 启动
   ├── 读 CLAUDE.md（项目规则）
   └── 读 MEMORY.md（个人档案）

📥 加内容（选一个入口）
   ├── 原始材料   → 01-raw/
   ├── 结构化摘要  → 02-summaries/
   ├── 概念卡片   → 03-cards/（必须写 domain + tags）
   └── 事件观察   → 05-observations/（三选一子目录）

🏷️ 自动标签
   └── python tools/auto_tag.py --apply
       ├── 概念卡 → 补 #学科/xxx
       └── 事件   → 补 #事件类型/xxx

💾 同步数据库
   └── python tools/import_md.py
       └── 增量同步到 kb.db

🔍 现在可用了
   ├── Obsidian 标签面板筛选
   ├── 反向链接追溯
   └── 语义搜索

🔧 收尾
   ├── 更新索引文件
   ├── 写项目日志
   └── git commit
```
