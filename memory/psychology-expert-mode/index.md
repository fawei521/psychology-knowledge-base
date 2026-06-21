---
name: psychology-expert-mode-index
description: 心理学专家模式入口指针，详细规则见项目内部 meta/psychology-expert-mode.md
metadata: 
  node_type: memory
  type: reference
  originSessionId: c18f998c-4324-49c5-a1af-c7e99e647c15
  updated: 2026-06-18
---

# 心理学专家模式索引

这是入口指针。完整规则、行为约定、教材推荐、skills 使用说明都在项目内部文件中，不在 memory 里重复。

## 触发指令

- **开启**：用户明确说出「开启心理学专家模式」
- **关闭**：用户明确说出「关闭心理学专家模式」

## 项目内部规范（按需读取）

> 快速查看规则：运行 `python E:\psychology-knowledge-base\tools\load_rule.py <namespace> <别名>`，或用 `--list` 查看所有别名。常用 namespace：`research-partner`、`psychology-expert-mode`、`startup-workflow`、`memory-rules`、`kb-specs`、`kb-tools`。

| 规范类型 | 读取文件 |
|---|---|
| 项目总纲与 spec 索引 | `E:\psychology-knowledge-base\CLAUDE.md` |
| 心理学专家模式行为约定 | `E:\psychology-knowledge-base\meta\psychology-expert-mode.md` |
| 跨学科研究搭档子模式 | `E:\psychology-knowledge-base\00-prompts\research-partner-constitution.md` |

## 为什么不在这里重复内容

模式资料属于项目专属规范，应随项目文件走。memory 里只保留入口指针，避免项目内部规范更新后 memory 中的副本过时。

**相关记忆**
- [[memory-system-guide]] — 双轨记忆系统与入口化规则
- [[projects-index]] — 项目记忆索引
