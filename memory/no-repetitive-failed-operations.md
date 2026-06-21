---
name: no-repetitive-failed-operations
description: 操作失败后禁止自动重复尝试，尤其是 subagent 文件系统扫描和外部依赖检查
metadata: 
  node_type: memory
  type: feedback
  severity: critical
  created: 2026-06-20
  originSessionId: f35a9bb9-b26a-43bf-a5e6-3bab55b2c9e8
---

## 事件

2026-06-20，用户要求按 Boris Cherny 方法整理 skills 索引。Explore agent 在读取 `C:\Users\乏味\.claude\skills\deep-research\SKILL.md` 和 `code-review\SKILL.md` 时不存在的路径时反复重试，连续触发十几次 Read 失败；此前 Edge CDP 授权检查也重复运行 4-5 次。用户反馈「半小时没有任何进展」，造成严重 token 浪费。

## 根因

1. **subagent 做文件系统扫描不可控**：Explore agent 看不到「文件不存在就跳过」的约束，进入内部重试循环。
2. **遇到失败默认重试而不是停下报告**：Edge CDP 超时、Read 失败都被当成「再试一次」的信号。
3. **没有充分利用错误信号**：Read 返回文件不存在、Bash exit code 1 都是明确信号，应该立刻切换策略。
4. **把重试交给 agent 而不监控中间步骤**：等用户看到时已经烧了几十次调用。

## 硬性规则

1. **任何工具调用失败后，最多只处理一次**。失败后先向用户报告失败原因和下一步建议，**不自动重试**。
2. **文件系统扫描类任务（列目录、扫文件、确认路径存在）禁止交给 subagent**。使用 `Glob`、`Bash ls`、`Read` 等可直接监控的工具，一次完成。
3. **Read 返回文件不存在时，立刻记录并继续下一个**，禁止再次 Read 同一路径。
4. **外部依赖检查（如浏览器 CDP、Node 版本）失败后，立刻停下来请求用户处理**，不反复 `check-deps`。
5. **使用 subagent 前必须明确约束**：「禁止写文件」「发现缺失即跳过」「禁止重试」「只返回文本不执行」。

## Why

自动重试在不可控环境下不会自行修复问题，只会指数级消耗 token 和用户耐心。用户对时间和 token 都敏感，失败后停下来确认才是真正的效率。

## How to apply

- 听到用户说「又在重复」「怎么还在跑」「亮红灯」时，立刻停止当前 agent/循环，先道歉并报告已发生的重复调用。
- 做索引、归档、扫描类任务时，先用 `Glob` 或 `ls` 拿到真实文件列表，再按需读取。
- 任何「让我再试一次」的冲动都要改为「让我向用户报告并询问是否继续」。

## 相关

- [[lessons-learned]] — 其他批量操作与 agent 约束教训
- [[work-principles-systemic-thinking]] — 处理非琐碎任务时的系统性思维
