---
name: weread-exporter-usage
description: 心理学知识库中的微信读书导出工具位置与用途
metadata: 
  node_type: memory
  type: project
  originSessionId: 5a810ce8-0df8-42c6-9a1b-898f70b9181d
---

# weread-exporter 工具

`E:\psychology-knowledge-base\tools\weread-exporter` 是一个**微信读书导出工具**，用于将微信读书中的读书笔记导出为本地文件，方便整理进心理学知识库。

## 用途

- 导出微信读书中的书籍划线、笔记、书评
- 将导出的内容进一步整理为 `02-summaries/` 或 `03-cards/` 中的知识库条目
- 是心理学知识库的辅助输入工具之一

## 当前状态

- 该目录本身是一个独立的 git 仓库（嵌套仓库）
- 主仓库 `E:\psychology-knowledge-base` 已通过 `.gitignore` 将其排除，避免 submodule 混乱
- 本地保留，不随主仓库一起 push

## 关联

- [[psychology-knowledge-base]]
- [[psychology-resources]]
