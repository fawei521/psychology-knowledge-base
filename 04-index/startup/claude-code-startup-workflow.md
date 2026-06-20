---
name: claude-code-startup-workflow
description: Claude Code 会话启动时的完整加载链与工作流程（含心理学专家模式入口）
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0f110150-0b4d-491b-8f17-6f33ba643aef
---

# Claude Code 启动工作流 · 思维导图

> 在 Obsidian 中打开此文件，切换到阅读模式即可看到渲染后的思维导图。
> 下面的文字版结构与 Mermaid 内容一致，双保险。

```mermaid
mindmap
  root((Claude Code<br/>启动))
    📌环境层
      Windows 11 + Git Bash
      当前工作目录
        C:\Users\乏味
        E:\psychology-knowledge-base
      MCP 服务器
        context7 文档查询
        fetch 网页抓取
        memory 知识图谱
        sequential-thinking 深度思考
      ::_这三层启动前就绪<br/>不管项目是什么
    📋自建档案<br/>每次自动加载
      MEMORY.md<br/>记忆索引
        ::每次会话第一件事<br/>读这个文件
      user-profile.md
        心理学学生
        编程零基础
        大白话教学
        时间比token贵
      installed-skills.md
        find-skills
        frontend-design
        docx/pptx/xlsx
        自建 win-safe-ps
      lessons-learned.md
        文件上传避坑
        技能安装避坑
        批量操作铁律
        沟通原则
        PowerShell编码
        自动标签经验
      workspace-setup.md
        C盘→E盘迁移
        junction用法
      projects-index.md
        项目列表
        ::不自动加载详情<br/>提到项目时才读
      psychology-expert-mode/index.md
        触发指令
        ::不自动加载详情<br/>说出指令时才加载
    🧠记忆系统<br/>双轨互补
      自建档案_Markdown
        放什么
          用户画像
          项目档案
          经验教训
          环境配置
        特点
          人可以直接看
          不会随对话变化
          每次全量注入索引
      claude-mem_MCP版
        放什么
          临时想法
          对话碎片
          决策过程
        特点
          自动捕获
          只能通过查询接口
          第二次会话起注入
    📂项目感知<br/>按需加载
      当前目录有CLAUDE.md
        自动读取
        项目规则手册
        ::如E盘知识库的<br/>CLAUDE.md
      用户提到某项目
        读 projects/项目名/xxx.md
        项目间互相隔离
      ::_不主动联想<br/>不串项目
    🎯模式切换
      普通模式_默认
        什么模式都没开
        AI正常回答问题
      心理学专家模式
        触发指令
          开启心理学专家模式
        自动加载
          meta/psychology-expert-mode.md
          模式约定与教材
        按需触发
          04-index/spec-card.md
          04-index/spec-observation.md
          04-index/spec-archive.md
          04-index/spec-tools.md
          04-index/spec-index.md
          04-index/spec-maintenance.md
        按需加载
          04-index/concept-map.md
          04-index/tag-index.md
      跨学科研究搭档_子模式
        触发指令
          开启跨学科研究搭档模式
        加载
          research-partner-prompt-v3-optimized.md
        作用
          事件分析协作工作流
    🔧技能系统
      什么时候生效
        用户输入以 / 开头
        或者 AI 判断任务匹配某技能
      举例
        /find-skills → 搜索技能
        /docx → 生成Word
        /frontend-design → UI设计
      ::_技能不会自动运行<br/>需要触发
```

---

## 文字版启动链（从上到下）

```
Claude Code 启动
│
├── 📌 环境层（启动前就绪，和项目无关）
│   ├── Windows 11 + Git Bash
│   ├── 当前工作目录
│   └── MCP 服务器（context7 / fetch / memory / sequential-thinking）
│
├── 📋 自建档案（每次会话自动全量注入）
│   ├── MEMORY.md           ← 第一站，记忆索引
│   ├── user-profile.md     ← 你是谁
│   ├── installed-skills.md ← 装了什么技能
│   ├── lessons-learned.md  ← 踩过的坑
│   ├── workspace-setup.md  ← 盘符规划
│   ├── projects-index.md   ← 项目列表（只读索引，不读详情）
│   └── psychology-expert-mode/index.md ← 模式入口（只读索引，不读详情）
│
├── 🧠 记忆系统（双轨同时运行）
│   ├── 自建档案（Markdown）→ 手动整理，稳定事实
│   └── claude-mem（MCP版）→ 自动捕获，对话碎片
│
├── 📂 项目感知（按需，不自动）
│   ├── 当前目录有 CLAUDE.md → 自动读（如在知识库目录时）
│   └── 用户提到某项目 → 读 projects/项目名/xxx.md
│
├── 🎯 模式（用户说指令才切换）
│   ├── 默认：普通模式
│   ├── "开启心理学专家模式" → 加载知识库规范 + 概念图
│   └── "开启跨学科研究搭档模式" → 加载事件分析工作流
│
└── 🔧 技能（/ 触发或 AI 判断）
    ├── /find-skills
    ├── /frontend-design
    ├── /docx / pptx / xlsx
    └── 自建：win-safe-ps
```
