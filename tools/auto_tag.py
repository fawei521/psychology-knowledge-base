"""
自动标签脚本
- 概念卡片（03-cards/）：根据 domain 字段补全 #学科/xxx 标签
- 事件文件（05-observations/ + 06-event-cards/）：根据内容补全 #事件类型/xxx 标签
用法：
  python tools/auto_tag.py              → 预览，不修改
  python tools/auto_tag.py --apply      → 实际写入
"""

import os, re, sys, yaml

# Ensure UTF-8 output on Windows terminals and other constrained environments
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================
# 学科标签映射（概念卡片用）
# ============================================================
DOMAIN_MAP = [
    # === 中文关键词 ===
    ("学科/普通心理学", ["普通心理学", "感觉", "知觉", "注意", "记忆", "思维", "语言",
                         "意识", "智力", "问题解决", "认知风格", "感觉与知觉"]),
    ("学科/社会心理学", ["社会心理学", "从众", "服从", "偏见", "歧视", "攻击行为",
                         "亲社会", "利他", "人际吸引", "归因", "态度", "群体影响",
                         "认知失调", "社会认知", "自我概念", "性别研究", "政治传播",
                         "群际", "社会认同", "群体极化"]),
    ("学科/人格心理学", ["人格心理学", "人格特质", "人格动力", "人本主义人格",
                         "大五", "自我概念"]),
    ("学科/情绪与动机", ["情绪", "动机", "应激", "压力", "应对"]),
    ("学科/临床与咨询", ["临床心理学", "咨询", "叙事治疗", "接纳承诺", "ACT",
                         "认知解离", "家庭系统治疗", "外化", "元认知", "亲密关系",
                         "依恋理论", "依恋图式", "沟通心理学", "松动结构",
                         "需求与测试", "坚定选择"]),
    ("学科/发展心理学", ["发展心理学", "毕生发展"]),
    ("学科/教育心理学", ["教育心理学", "教学"]),
    ("学科/学习心理学", ["学习理论", "经典条件", "操作条件", "观察学习", "条件反射",
                         "潜伏学习"]),
    ("学科/实验心理学", ["实验心理学", "实验设计", "心理物理", "反应时"]),
    ("学科/生理心理学", ["生理心理学", "神经", "脑机制", "杏仁核", "前额叶",
                         "多巴胺", "HPA", "催产素", "皮质醇"]),
    ("学科/变态心理学", ["变态心理学", "障碍", "焦虑障碍", "心境障碍", "抑郁",
                         "人格障碍", "精神分裂"]),
    ("学科/统计与测量", ["统计", "测量", "心理测量", "量表"]),
    ("学科/基础与进化", ["基础", "概论", "学科定义", "进化心理学", "科学方法"]),

    # === 英文关键词 ===
    ("学科/普通心理学", ["general_psychology", "general", "sensation", "perception",
                         "attention", "memory", "thinking", "language", "consciousness",
                         "intelligence", "cognitive_style", "forgetting"]),
    ("学科/社会心理学", ["social_psychology", "social psychology", "conformity", "obedience",
                         "prejudice", "discrimination", "aggression", "prosocial", "altruism",
                         "interpersonal_attraction", "attribution", "attitude",
                         "group_influence", "cognitive_dissonance", "social_cognitive",
                         "self_concept", "group_polarization"]),
    ("学科/人格心理学", ["personality psychology", "personality", "big_five",
                         "personality_trait", "personality_dynamic", "humanistic_personality",
                         "attachment"]),
    ("学科/情绪与动机", ["emotion psychology", "emotion", "motivation", "stress", "coping"]),
    ("学科/临床与咨询", ["clinical", "counseling", "therapy", "narrative", "ACT"]),
    ("学科/发展心理学", ["developmental"]),
    ("学科/教育心理学", ["educational"]),
    ("学科/学习心理学", ["learning"]),
    ("学科/实验心理学", ["experimental", "psychophysics"]),
    ("学科/生理心理学", ["biological", "neuroscience", "physiological", "brain"]),
    ("学科/变态心理学", ["abnormal", "disorder", "psychopathology"]),
    ("学科/统计与测量", ["statistics", "measurement", "psychometrics"]),
    ("学科/基础与进化", ["evolutionary", "foundations", "definition", "scientific_method"]),
]

# ============================================================
# 事件类型标签映射（社会事件用，来自分类手册 8 种类型）
# ============================================================
EVENT_TYPE_MAP = [
    ("事件类型/威胁-防御", ["害怕", "恐惧", "焦虑", "安全感", "风险", "不安全",
                            "威胁", "恐慌", "怎么办", "万一", "安全焦虑"]),
    ("事件类型/不公-愤怒", ["不公平", "凭什么", "双标", "愤怒", "义愤", "不公",
                            "公正", "剥夺", "特权", "严惩", "公道", "太黑"]),
    ("事件类型/道德-厌恶", ["恶心", "底线", "畜生", "不是人", "玷污", "突破底线",
                            "道德", "肮脏", "洁净", "污染"]),
    ("事件类型/共情-利他", ["心疼", "看哭了", "可怜", "帮助", "捐款", "同情",
                            "受苦", "怜悯", "感动", "共情"]),
    ("事件类型/认同-团结", ["我们", "他们", "群体", "身份", "认同", "归属",
                            "团结", "一致对外", "丢人", "争光", "XX人",
                            "性别", "男女", "男性", "女性", "阶层", "阶级",
                            "极化", "粉丝", "阵营", "立场"]),
    ("事件类型/失调-困惑", ["不信", "反转", "到底怎么回事", "矛盾", "困惑",
                            "细思极恐", "让子弹飞", "不确定", "怀疑", "罗生门"]),
    ("事件类型/权力-支配", ["压迫", "反抗", "权贵", "底层", "欺负", "支配",
                            "仗势欺人", "跪久了", "无力", "屈辱", "控制",
                            "强弱", "阶层", "鄙视链"]),
    ("事件类型/新奇-探索", ["居然", "吃瓜", "活久见", "求科普", "新奇", "惊讶",
                            "好奇", "有趣", "梗", "娱乐"]),
]


# ============================================================
# 工具函数
# ============================================================
def parse_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}, content
    try:
        return yaml.safe_load(m.group(1)) or {}, content
    except yaml.YAMLError:
        return {}, content


def match_keywords(text, mapping):
    """在 text 中匹配 mapping（tag, [keywords]），返回命中的 tag 列表"""
    hits = []
    seen = set()
    for tag, keywords in mapping:
        if tag in seen:
            continue
        for kw in keywords:
            if kw.lower() in text.lower():
                hits.append(tag)
                seen.add(tag)
                break
    return hits


def _yaml_str(value):
    """将单个 tag 格式化为 YAML 字符串：必要时加单引号"""
    if re.match(r"^[A-Za-z0-9_]+$", value):
        return value
    return f"'{value}'"


def _format_tags_inline(tags):
    return "tags: [" + ", ".join(_yaml_str(t) for t in tags) + "]"


def _format_tags_list(tags):
    lines = ["tags:"]
    for t in tags:
        lines.append(f"- {_yaml_str(t)}")
    return "\n".join(lines)


def patch_tags(filepath, content, existing_tags, new_tags, dry_run):
    """给文件的 YAML tags 数组追加新标签，保持原格式（inline 或 list）"""
    if dry_run:
        return False

    # 合并并去重，保持顺序
    seen = set()
    all_tags = []
    for t in existing_tags + new_tags:
        if t not in seen:
            all_tags.append(t)
            seen.add(t)

    # 情况1：已有 inline tags: [...] 行 → 替换整行
    if re.search(r"^tags:\s*\[.*?\]", content, flags=re.MULTILINE):
        new_content = re.sub(
            r"^tags:\s*\[.*?\]",
            _format_tags_inline(all_tags),
            content,
            flags=re.MULTILINE,
        )
    # 情况2：已有多行 tags 列表 → 替换整个 tags 块
    elif re.search(r"^tags:\s*\n(?:\s*-\s*.*?\n)+", content, flags=re.MULTILINE):
        new_content = re.sub(
            r"^tags:\s*\n(?:\s*-\s*.*?\n)+",
            _format_tags_list(all_tags) + "\n",
            content,
            flags=re.MULTILINE,
        )
    # 情况3：有 YAML frontmatter 但没有 tags 行 → 在 frontmatter 末尾加 inline tags
    elif content.startswith("---"):
        new_content = re.sub(
            r"(\n---)",
            f"\n{_format_tags_inline(all_tags)}\\1",
            content,
            count=1,
        )
    # 情况4：没有 YAML frontmatter → 新建一个
    else:
        new_content = f"---\n{_format_tags_inline(all_tags)}\n---\n\n{content}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


# ============================================================
# 主逻辑
# ============================================================
def process_cards(dry_run):
    """处理 03-cards/ 及其子目录下的概念卡片"""
    cards_dir = os.path.join(BASE, "03-cards")
    updated, unchanged = 0, 0

    for root, dirs, files in os.walk(cards_dir):
        # 跳过非学科子目录中的模板或 README
        for filename in sorted(files):
            if not (filename.startswith("card-") and filename.endswith(".md")):
                continue
            filepath = os.path.join(root, filename)
        meta, content = parse_frontmatter(filepath)
        if not meta:
            continue

        domain = meta.get("domain", "") or ""
        tags = meta.get("tags", []) or []
        concept = meta.get("concept", "") or ""
        concept_cn = meta.get("concept_cn", "") or ""
        text = f"{concept} {concept_cn} {domain} {' '.join(tags)}"

        suggestion = match_keywords(text, DOMAIN_MAP)
        new_tags = [t for t in suggestion if t not in tags]

        if not new_tags:
            unchanged += 1
            continue

        print(f"[概念] {filename}")
        print(f"  现有: {tags}")
        print(f"  +{new_tags}")
        patch_tags(filepath, content, tags, new_tags, dry_run)
        updated += 1

    return updated, unchanged


def process_events(dry_run):
    """处理事件文件：只扫 current-events/ 和 event-cards/，匹配 YAML + 前 800 字"""
    dirs = [
        os.path.join(BASE, "05-observations", "current-events"),
        os.path.join(BASE, "05-observations", "typical-cases"),
    ]
    updated, unchanged = 0, 0

    for d in dirs:
        if not os.path.isdir(d):
            continue
        for filename in sorted(os.listdir(d)):
            if not filename.endswith(".md"):
                continue
            filepath = os.path.join(d, filename)
            if "_template" in filename or "README" in filename:
                continue

            meta, content = parse_frontmatter(filepath)
            tags = meta.get("tags", []) or []

            # 只取 YAML 描述字段 + body 前 800 字（事件摘要，不是分析）
            context = meta.get("context", "") or ""
            title = meta.get("title", "") or ""
            body = re.sub(r"^---.*?\n---\n", "", content, flags=re.DOTALL)
            snippet = body[:800]
            text = f"{title} {context} {snippet}"

            suggestion = match_keywords(text, EVENT_TYPE_MAP)
            # 过滤：每种类型至少命中 2 个关键词才算
            filtered = []
            for tag, keywords in EVENT_TYPE_MAP:
                if tag in suggestion:
                    hits = sum(1 for kw in keywords if kw.lower() in text.lower())
                    if hits >= 2:
                        filtered.append(tag)

            new_tags = [t for t in filtered if t not in tags]

            if not new_tags:
                unchanged += 1
                continue

            rel_path = os.path.relpath(filepath, BASE)
            print(f"[事件] {rel_path}")
            print(f"  现有: {tags}")
            print(f"  +{new_tags}")
            patch_tags(filepath, content, tags, new_tags, dry_run)
            updated += 1

    return updated, unchanged


def main():
    dry_run = "--apply" not in sys.argv
    mode = "[DRY RUN] 预览模式" if dry_run else "[APPLY] 写入模式"
    print(f"{mode}\n")

    print("=== 概念卡片（学科标签）===")
    c_up, c_un = process_cards(dry_run)

    print("\n=== 事件文件（事件类型标签）===")
    e_up, e_un = process_events(dry_run)

    print(f"\n概念卡片: 更新 {c_up}  不变 {c_un}")
    print(f"事件文件: 更新 {e_up}  不变 {e_un}")
    if dry_run:
        print("\n这是预览。要实际修改请运行: python tools/auto_tag.py --apply")


if __name__ == "__main__":
    main()
