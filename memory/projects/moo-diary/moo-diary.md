---
name: moo-diary
description: E:\me me\moo 个人作品仓库，现为日记库，使用 CLAUDE.md 规范 moo 导入
metadata: 
  node_type: memory
  type: project
  originSessionId: bf316678-ecf5-4efb-9b92-d93fce281ef0
---

`E:\moo` 是用户的个人作品仓库，目前主要存放日记。该目录也是 Obsidian 库，日记统一放在 `日记/` 下。

关键约定：
- momo TXT 导出只导入文字，不处理图片。
- 单篇单文件，文件名 `YYYY-MM-DD 标题.md`。
- 固定 frontmatter：`title`、`date`、`weather`、`mood`、`activity`。
- 空标题用正文第一行补全；同名同日期加 `(2)` 等后缀。
- 不要覆盖已有文件，不改动原始 `Moo-TXT-*` 导出文件夹。
- 仓库根目录有 `CLAUDE.md` 记录完整规则。

**Why:** 这些规则来自用户本次整理 momo 日记时的明确决策，写成规则后可避免下次导入时重复确认、误改旧文件或误插图片。

**How to apply:** 每次用户提到“momo 导入 / 日记整理 / moo 仓库”时，先读取 `E:\moo\CLAUDE.md`，再按规则操作。
