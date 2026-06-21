---
name: workspace-setup
description: E 盘工作区约定，C 盘迁移经验，junction 与 npm 配置
metadata: 
  node_type: memory
  created: 2026-06-11
  type: project
  originSessionId: c794b212-8fb7-4879-aee3-b25dc32336a6
---

## 核心约定

**以后所有工作、项目、配置都放到 E 盘。**

## 2026-06-11 教训

### junction 自以为成功了，实际没生效

用户执行了 `mklink /J`，我没验证就断言成功。后来发现 `C:\Users\乏味\.claude` 仍是真实文件夹，E 盘 `claude-config` 成了独立孤儿目录。

**根因**：执行时 Claude 可能在运行，文件被占用导致命令部分失败。我没有检查返回值，也没有用 `Get-Item` 验证 Attributes 是否为 `Directory, ReparsePoint`。

**以后执行系统命令后必须验证**：
```powershell
Get-Item "路径" | Select-Object Attributes, Target
# junction 应该显示 Target = 目标路径
```

### npm 迁移教训

改 `prefix` 配置后，**旧全局包不会自动搬过去**。必须手动把旧目录的 `.cmd`、`.ps1`、`node_modules` 复制到新目录，否则全局命令找不到。

## 当前状态

| 项目 | 状态 | 备注 |
|------|------|------|
| npm | ✅ 已正常迁移到 E 盘 | 全局包已手动搬运 |
| Claude 配置 | ✅ 已生效 | junction 已生效，`C:\Users\乏味\.claude\projects\C--Users---` 与 `E:\claude-config\projects\C--Users---` 指向同一 inode |

## 重要提醒

`C:\Users\乏味\.claude\projects\C--Users---` 和 `E:\claude-config\projects\C--Users---` **是同一个目录的两个路径别名**，其下文件（包括 memory 目录）inode 相同。不要重复检查两个路径是否一致，也不要把它们当成两份副本。

**Why:** 之前每次出现 E 盘路径都重新 `ls -i` 验证，浪费步骤；记录下来后直接按同一位置处理。

**How to apply:** 操作 memory 文件时优先用 Claude Code 环境给出的路径（当前多为 C 盘），遇到 `E:\claude-config\projects\C--Users---` 时知道它就是 C 盘同目录，无需再次比对 inode。

## 默认落盘规则

> 核心约定「所有工作、项目、配置都放 E 盘」仍然有效。由于 Claude Code 当前 Primary working directory 是 `C:\Users\乏味`，不能依赖默认路径自动进 E 盘，因此显式约定如下：

1. **用户未指定路径时**，新建项目/文件优先落到 `E:\projects\`；如果该目录不存在，先创建它。
2. **已有项目**（如 `E:\psychology-knowledge-base`、`E:\me me\moo`）继续在其原目录下操作。
3. **临时文件、一次性输出**（如下载缓存、中间产物）可以放在系统临时目录或当前工作区，完成后清理。
4. **memory 文件**仍按原有路径 `C:\Users\乏味\.claude\projects\C--Users---\memory\`（实际在 E 盘 junction 后）读写。

**Why:** 不改 VSCode 工作区的情况下，避免无意识地把新项目/文件堆积到 C 盘用户目录。

**How to apply:** 每次写新文件或创建新项目前，先判断用户是否给了明确路径；没有就默认用 `E:\projects\<name>`。
