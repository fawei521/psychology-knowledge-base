from pathlib import Path
import re

cards_dir = Path('03-cards')

mapping = {
    'PSY-GN-001': ('sensation_and_perception', '感觉与知觉', '普通心理学', ['sensation', 'perception', 'psychophysics']),
    'PSY-GN-002': ('attention', '注意', '普通心理学', ['attention', 'selective_attention', 'divided_attention', 'filter_model']),
    'PSY-GN-003': ('three_stage_memory_model', '记忆的三级模型', '普通心理学', ['memory', 'sensory_memory', 'short_term_memory', 'long_term_memory', 'encoding', 'retrieval']),
    'PSY-GN-004': ('working_memory', '工作记忆', '普通心理学', ['memory', 'working_memory', 'phonological_loop', 'visuospatial_sketchpad', 'central_executive']),
    'PSY-GN-005': ('forgetting_theories', '遗忘理论', '普通心理学', ['memory', 'forgetting', 'decay', 'interference', 'repression', 'retrieval_failure']),
    'PSY-GN-006': ('thinking_and_problem_solving', '思维与问题解决', '普通心理学', ['thinking', 'problem_solving', 'heuristic', 'algorithm', 'mental_set', 'functional_fixedness']),
    'PSY-GN-007': ('language', '语言', '普通心理学', ['language', 'brocas_area', 'wernickes_area', 'language_acquisition', 'critical_period', 'lad']),
    'PSY-GN-008': ('motivation_theories', '动机理论', '普通心理学', ['motivation', 'maslow', 'hierarchy_of_needs', 'drive_theory', 'incentive_theory', 'self_efficacy']),
    'PSY-GN-009': ('emotion_theories', '情绪理论', '普通心理学', ['emotion', 'james_lange_theory', 'cannon_bard_theory', 'schachter_singer_theory', 'lazarus', 'cognitive_appraisal']),
    'PSY-GN-010': ('emotion_regulation', '情绪调节', '普通心理学', ['emotion', 'emotion_regulation', 'cognitive_reappraisal', 'expressive_suppression', 'gross_process_model']),
    'PSY-GN-011': ('intelligence_theories', '智力理论', '普通心理学', ['intelligence', 'fluid_intelligence', 'crystallized_intelligence', 'multiple_intelligences', 'triarchic_theory', 'pass_model']),
    'PSY-GN-012': ('learning_theories', '学习理论', '普通心理学', ['learning', 'classical_conditioning', 'operant_conditioning', 'observational_learning', 'latent_learning']),
    'PSY-GN-013': ('cognitive_styles', '认知风格', '普通心理学', ['cognitive_style', 'field_independence', 'field_dependence', 'reflective_impulsive', 'deep_processing']),
    'PSY-GN-014': ('consciousness_and_sleep', '意识与睡眠', '普通心理学', ['consciousness', 'sleep', 'rem_sleep', 'nrem_sleep', 'hypnosis']),
    'PSY-GN-015': ('personality_trait_theories', '人格特质理论', '普通心理学', ['personality', 'big_five', 'eysenck', 'traits', 'person_situation_debate']),
    'PSY-GN-016': ('personality_dynamic_theories', '人格动力理论', '普通心理学', ['personality', 'psychoanalysis', 'freud', 'defense_mechanisms', 'jung', 'collective_unconscious']),
    'PSY-GN-017': ('humanistic_personality', '人本主义人格', '普通心理学', ['personality', 'humanistic', 'rogers', 'maslow', 'self_actualization', 'unconditional_positive_regard']),
    'PSY-GN-018': ('social_cognitive_theory', '社会认知理论', '普通心理学', ['personality', 'bandura', 'self_efficacy', 'observational_learning', 'reciprocal_determinism']),
    'PSY-GN-019': ('stress_and_coping', '应激与应对', '普通心理学', ['stress', 'coping', 'lazarus', 'resilience', 'primary_appraisal', 'secondary_appraisal']),
    'PSY-GN-020': ('cognitive_dissonance', '认知失调', '社会心理学', ['attitude', 'cognitive_dissonance', 'festinger', 'overjustification_effect']),
    'PSY-GN-021': ('attribution_theory', '归因理论', '社会心理学', ['attribution', 'fundamental_attribution_error', 'self_serving_bias', 'weiner', 'kelley']),
    'PSY-GN-022': ('attitude_formation_and_change', '态度形成与改变', '社会心理学', ['attitude', 'balance_theory', 'elm', 'persuasion', 'central_route', 'peripheral_route']),
    'PSY-GN-023': ('conformity', '从众', '社会心理学', ['conformity', 'asch', 'normative_influence', 'informational_influence']),
    'PSY-GN-024': ('obedience', '服从', '社会心理学', ['obedience', 'milgram', 'authority']),
    'PSY-GN-025': ('group_influence', '群体影响', '社会心理学', ['group_influence', 'social_facilitation', 'social_loafing', 'deindividuation', 'group_polarization', 'groupthink']),
    'PSY-GN-026': ('prejudice_and_discrimination', '偏见与歧视', '社会心理学', ['prejudice', 'discrimination', 'stereotype', 'in_group_bias', 'out_group_homogeneity']),
    'PSY-GN-027': ('aggression', '攻击行为', '社会心理学', ['aggression', 'frustration_aggression_hypothesis', 'social_learning', 'media_violence', 'gam']),
    'PSY-GN-028': ('prosocial_behavior', '亲社会行为', '社会心理学', ['prosocial_behavior', 'altruism', 'bystander_effect', 'diffusion_of_responsibility', 'reciprocity_norm']),
    'PSY-GN-029': ('interpersonal_attraction', '人际吸引', '社会心理学', ['interpersonal_attraction', 'proximity', 'similarity', 'physical_attractiveness', 'reciprocal_liking']),
    'PSY-GN-030': ('self_concept', '自我概念', '普通心理学 / 社会心理学', ['self_concept', 'self_schema', 'self_esteem', 'self_verification', 'self_enhancement', 'self_handicapping']),
}

domain_map = {
    '普通心理学': 'general_psychology',
    '社会心理学': 'social_psychology',
    '普通心理学 / 社会心理学': 'general_psychology, social_psychology',
}

for old_file in sorted(cards_dir.glob('card-psy-gn-*.md')):
    content = old_file.read_text(encoding='utf-8')
    lines = content.strip().split('\n')

    number = ''
    for line in lines[:5]:
        m = re.match(r'^#\s*卡片编号：\s*(.+)$', line)
        if m:
            number = m.group(1).strip()
            break

    if number not in mapping:
        print(f"Skip {old_file.name}: unknown number {number}")
        continue

    concept, concept_cn, domain_cn, tags = mapping[number]
    domain = domain_map.get(domain_cn, domain_cn)

    body_lines = []
    for line in lines:
        if re.match(r'^#\s*(卡片编号|概念名称|所属学科|相关概念)：', line):
            continue
        body_lines.append(line)

    while body_lines and body_lines[0].strip() == '':
        body_lines.pop(0)

    new_body = '\n'.join(body_lines)
    new_body = re.sub(r'^## 一、定义$', '## 定义', new_body, flags=re.MULTILINE)
    new_body = re.sub(r'^## 二、核心要点$', '## 核心要点', new_body, flags=re.MULTILINE)
    new_body = re.sub(r'^## 三、理论背景$', '## 理论背景', new_body, flags=re.MULTILINE)
    new_body = re.sub(r'^## 四、生活实例$', '## 生活实例', new_body, flags=re.MULTILINE)
    new_body = re.sub(r'^## 五、社会热点关联（预留，待填充）$', '## 社会热点关联', new_body, flags=re.MULTILINE)
    new_body = re.sub(r'^## 六、考研重点$', '## 考研重点', new_body, flags=re.MULTILINE)
    new_body = re.sub(r'^## 七、文献来源$', '## 文献来源', new_body, flags=re.MULTILINE)

    title_en = ' '.join(word.capitalize() for word in concept.split('_'))
    frontmatter = f"""---
concept: {concept}
concept_cn: {concept_cn}
domain: {domain}
tags: {tags}
---

# {concept_cn} / {title_en}

"""

    new_content = frontmatter + new_body

    new_file = cards_dir / f'card-{concept}.md'
    new_file.write_text(new_content, encoding='utf-8')
    old_file.unlink()
    print(f"Rewrote {old_file.name} -> {new_file.name}")

print("Done.")
