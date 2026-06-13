"""
Split research-partner-prompt-v3.1-flexible.md into rule files under rules/.
Uses exact top-level title matching so internal ## headings inside the card
template are not mistaken for new chapters.
"""
import re
from pathlib import Path

src = Path(r"E:\psychology-knowledge-base\00-prompts\research-partner-prompt-v3.1-flexible.md")
rules_dir = Path(r"E:\psychology-knowledge-base\00-prompts\rules")
rules_dir.mkdir(exist_ok=True)

text = src.read_text(encoding="utf-8")

# Remove YAML frontmatter
lines = text.splitlines()
if lines[0].strip() == "---":
    end = lines.index("---", 1)
    body = "\n".join(lines[end + 1 :])
else:
    body = text

# Recognized top-level headings in source order.
# Keys are regex patterns; values are the target filename.
# The first capture group is used as the canonical title.
section_map = [
    (r"前言：为什么需要这个模式？", "meta.md"),
    (r"0\.2 给 AI 的元规则（防止误读）", "meta.md"),
    (r"第一章 角色与关系", "role.md"),
    (r"第二章 整体工作流", "workflow.md"),
    (r"第三章 阶段指南", "stages.md"),
    (r"第四章 输出规范", "output.md"),
    (r"第五章 交互指令集", "commands.md"),
    (r"第六章 场景模式", "scenarios.md"),
    (r"第七章 常见陷阱与避免方法", "traps.md"),
    (r"第八章 知识卡片模板", "card-template.md"),
    (r"第九章 测试与迭代建议", "testing.md"),
    (r"附录 A：理论禁用区", "theory-blacklist.md"),
    (r"附录 B：信源采集提醒模板（用户参考用）", "source-template.md"),
    (r"附录 C：边界与限制", "meta.md"),
]

# Build a single regex that matches any recognized top-level heading at line start.
heading_patterns = [re.escape(pat) if not pat.startswith(r"0\.") else pat for pat, _ in section_map]
pattern = re.compile(
    r"(?m)^## (" + "|".join(heading_patterns) + r")(?=\n|$)"
)

# Split while keeping the headings in the parts.
parts = re.split(pattern, body)
# re.split with one capture group returns: [pre, title1, body1, title2, body2, ...]
files = {}
for i in range(1, len(parts), 2):
    title = parts[i].strip()
    content = parts[i + 1] if i + 1 < len(parts) else ""
    # Find target file by matching title pattern
    target = None
    for pat, fname in section_map:
        if re.fullmatch(pat, title):
            target = fname
            break
    if not target:
        target = "other.md"
    files.setdefault(target, []).append(f"## {title}\n{content}")

# Write merged files
for fname, parts in files.items():
    content = "".join(parts).strip()
    out = rules_dir / fname
    out.write_text(content + "\n", encoding="utf-8")
    print(f"Wrote {out} ({len(content)} chars)")

# Split stages into stage-a/b/c/d
stages_path = rules_dir / "stages.md"
if stages_path.exists():
    stage_text = stages_path.read_text(encoding="utf-8")
    stage_parts = re.split(r"(?=\n### 3\.\d )", "\n" + stage_text)
    stage_files = {
        "3.1": "stage-a.md",
        "3.2": "stage-b.md",
        "3.3": "stage-c.md",
        "3.4": "stage-d.md",
    }
    stage_groups = {}
    for p in stage_parts:
        m = re.search(r"### 3\.(\d)", p)
        if m:
            key = f"3.{m.group(1)}"
            target = stage_files.get(key)
            if target:
                stage_groups.setdefault(target, []).append(p)
    for fname, parts in stage_groups.items():
        content = "".join(parts).strip()
        out = rules_dir / fname
        out.write_text(content + "\n", encoding="utf-8")
        print(f"Wrote {out} ({len(content)} chars)")
    stages_path.unlink()
    print("Removed stages.md")

print("Done.")
