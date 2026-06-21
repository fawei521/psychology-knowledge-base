---
name: psychology-kb-verify-hook
description: 保存后自动验证钩子的触发方式、覆盖范围、生效条件与手动启用步骤
metadata:
  node_type: memory
  type: project
  originSessionId: 31c9fbde-3f6b-47e3-a718-badc7b6fc7df
  updated: 2026-06-20
---

保存后验证钩子由 Claude Code 的 `PostToolUse` 事件自动触发，但**不会自动启用**——必须先把钩子脚本注册到 `settings.json` 中。

## 已部署的脚本

| 脚本 | 作用 | 路径 |
|---|---|---|
| `verify_on_save.py` | 保存后检查 frontmatter、链接、实体引用 | `C:/Users/乏味/.claude/hooks/verify_on_save.py` |
| `format_on_save.py` | 保存后格式化 Markdown | `C:/Users/乏味/.claude/hooks/format_on_save.py` |
| `rule_hooks.py` | SessionStart 注入规则；保存规则文件后运行 `--verify` | `C:/Users/乏味/.claude/hooks/rule_hooks.py` |

配置文件：
- `verify_profiles.yaml` —— `verify_on_save.py` 的检查规则
- `format_profiles.yaml` —— `format_on_save.py` 的格式化规则

## 启用方法（必须手动）

在全局 `C:/Users/乏味/.claude/settings.json` 中新增 `hooks` 字段（**注意必须使用 Claude Code 官方格式**）：

```json
{
  "env": { ... },
  "permissions": { ... },
  "effortLevel": "xhigh",
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python C:/Users/乏味/.claude/hooks/rule_hooks.py"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python C:/Users/乏味/.claude/hooks/format_on_save.py"
          },
          {
            "type": "command",
            "command": "python C:/Users/乏味/.claude/hooks/verify_on_save.py"
          },
          {
            "type": "command",
            "command": "python C:/Users/乏味/.claude/hooks/rule_hooks.py"
          }
        ]
      }
    ]
  }
}
```

**格式要点**（易错）：
- `SessionStart` 和 `PostToolUse` 的值是**对象数组**，不是字符串数组。
- `PostToolUse` 下用 `matcher` 字段匹配工具名，如 `"Edit|Write"`，**不能**写成 `PostToolUse:Write` 或 `PostToolUse:Edit`。
- 每个 hook 条目必须是 `{ "type": "command", "command": "..." }` 对象，不能直接写脚本路径字符串。

**错误示例**（会导致 Settings Error）：
```json
"PostToolUse:Write": ["C:/Users/乏味/.claude/hooks/verify_on_save.py"]
```

## 重载配置

修改 `settings.json` 后，必须让 Claude Code 重新加载配置：

1. 在 Claude Code 中输入 `/hooks` 打开 hooks 面板，系统会自动加载；或
2. 完全退出并重启 Claude Code。

只保存文件不重启，钩子不会生效。

## 自动触发条件

配置生效后，只要 Claude Code 写/改以下目录的 `.md` 文件，就会自动运行验证：

- `E:/psychology-knowledge-base/03-cards/`（概念卡片）
- `E:/psychology-knowledge-base/05-observations/`（观察记录）
- `E:/psychology-knowledge-base/02-summaries/`（文献摘要）
- `E:/psychology-knowledge-base/04-index/`（索引文件）
- `E:/me me/moo/日记/`（日记文件）

## 行为说明

- 只检查、不修改文件。
- 发现问题时弹 `systemMessage` 蓝色警告。
- 无问题时静默通过。

## 检查内容

- 必填 frontmatter 字段（仅对卡片/观察生效，摘要/索引/日记不强制）
- 内部 `[[card-...]]` / `[[summary-...]]` 链接是否指向真实文件
- frontmatter 中的实体引用（如 `related_entities`、`concepts`、`relations[*].target`）是否指向存在的卡片/摘要

## 如果 hook 未启用（故障 fallback）

当 `settings.json` 没有正确配置 hook 时，AI 必须在完成写卡/改卡/改索引后**手动运行等效检查**：

```bash
# 1. 规则系统完整性（改规则文件后）
python E:/psychology-knowledge-base/tools/load_rule.py --verify

# 2. 概念图/索引链接检查（改 04-index 后）
python E:/psychology-knowledge-base/tools/check_rule_refs.py 2>/dev/null || echo "check_rule_refs.py 不存在，跳过"

# 3. 关系网络验证（导入新卡片后）
cd /e/psychology-knowledge-base
python -c "
import sqlite3
conn = sqlite3.connect('kb.db')
c = conn.cursor()
c.execute('''SELECT e1.name, e2.name, r.relation_type FROM relations r
JOIN entities e1 ON r.from_id = e1.id
JOIN entities e2 ON r.to_id = e2.id
LIMIT 20''')
for row in c.fetchall(): print(row)
"
```

**Why:** 避免依赖 AI 记忆规则，把“链接是否断裂、必填 frontmatter 是否缺失、实体引用是否有效”这类廉价但易漏的校验交给确定性脚本；同时保留手动 fallback，防止 hook 失效时检查遗漏。

**How to apply:**
- 正常情况：保存上述目录的 `.md` 文件后，等待 Claude Code 自动弹出蓝色警告。
- 如果未弹出警告，说明 hook 可能未生效，此时按上述 fallback 手动检查。
- 如需调整检查规则，改 `verify_profiles.yaml` 或 `format_profiles.yaml` 后重载 `/hooks`。
