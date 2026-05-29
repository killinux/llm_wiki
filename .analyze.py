#!/usr/bin/env python3
"""分析悬空链接:区分(A)可归一化到已有页面的别名变体 vs (B)真正缺页的高频枢纽概念。
输出 rewrite map(别名->canonical)与 归一化后仍悬空的高频清单。"""
import os, re, glob, collections, json

DIRS = ['sources', 'concepts', 'entities', 'topics']

# 已有页面 slug -> (dir, slug)
pages = {}
for d in DIRS:
    for f in glob.glob(f'wiki/{d}/*.md'):
        b = os.path.splitext(os.path.basename(f))[0]
        if b == 'CLAUDE':
            continue
        pages[b] = d
pages_set = set(pages) | {'index'}

def norm(s):
    s = s.lower().strip()
    s = re.sub(r'[-_\s]+', '', s)
    s = re.sub(r's$', '', s)          # 去尾复数
    s = s.replace('llms', 'llm').replace('agents', 'agent')
    return s

# 已有页面的规范化键 -> canonical slug(优先 concepts/entities 中较短者)
normmap = {}
for slug, d in pages.items():
    k = norm(slug)
    if k not in normmap or len(slug) < len(normmap[k]):
        normmap[k] = slug

# 收集所有链接引用
links = collections.Counter()
for f in glob.glob('wiki/**/*.md', recursive=True):
    if os.path.basename(f) == 'CLAUDE.md':
        continue
    t = open(f, encoding='utf-8').read()
    for m in re.findall(r'\[\[([^\]]+)\]\]', t):
        tgt = m.split('|')[0].split('#')[0].strip()
        if tgt:
            links[tgt] += 1

# 手工同义词归并(指向同一 canonical 概念)
SYNONYMS = {
    'recommendation-system': 'recommender-systems',
    'recommendation-systems': 'recommender-systems',
    'recommender-system': 'recommender-systems',
    'recsys': 'recommender-systems',
    'llm-agent': 'llm-agents',
    'large-language-model': 'large-language-models',
    'large-language-models': 'large-language-models',
    'llm': 'large-language-models',
    'llms': 'large-language-models',
    'multi-agent-system': 'multi-agent-systems',
    'multi-agent': 'multi-agent-systems',
    'multiagent-debate': 'multi-agent-debate',
    'diffusion-model': 'diffusion-models',
    'chain-of-thought-prompting': 'chain-of-thought',
    'cot': 'chain-of-thought',
    'mcts': 'monte-carlo-tree-search',
    'rlhf': 'reinforcement-learning-from-human-feedback',
    'reinforcement-learning-from-human-feedback': 'reinforcement-learning-from-human-feedback',
    'recommendation-debiasing': 'debiasing-recommendation',
    'recommendation-systems': 'recommender-systems',
    'agent-based-models': 'generative-agent-based-modeling',
}

rewrite = {}      # alias -> canonical(已存在页面)
still_missing = collections.Counter()
for tgt, c in links.items():
    if tgt in pages_set:
        continue  # 已解析
    # 1) 手工同义
    cand = SYNONYMS.get(tgt)
    if cand and cand in pages_set:
        rewrite[tgt] = cand; continue
    # 2) 规范化匹配已有页面
    k = norm(tgt)
    if k in normmap:
        rewrite[tgt] = normmap[k]; continue
    # 3) 经同义再规范化
    if cand:
        k2 = norm(cand)
        if k2 in normmap:
            rewrite[tgt] = normmap[k2]; continue
    still_missing[tgt] += c

# 把"归一化后仍缺、但多个别名指向同一规范键"聚合成建页候选
group = collections.defaultdict(lambda: {'count': 0, 'aliases': []})
for tgt, c in still_missing.items():
    cand = SYNONYMS.get(tgt, tgt)
    k = norm(cand)
    group[k]['count'] += c
    group[k]['aliases'].append(tgt)
    group[k]['canonical'] = cand

print(f"页面总数: {len(pages_set)}")
print(f"悬空 target: {len(still_missing)+len(rewrite)} -> 可重写(映射到已有页): {len(rewrite)}; 归一化后仍缺: {len(still_missing)}")
print(f"\n=== 可重写别名 sample(共 {len(rewrite)})===")
for a, c in sorted(rewrite.items())[:20]:
    print(f"  {a} -> {c}")

# 建页候选:按聚合后引用次数排序,>=5 次建页
cand_pages = sorted(group.items(), key=lambda x: -x[1]['count'])
print(f"\n=== 建页候选(归一化聚合后 >=5 次)===")
hubs = []
for k, info in cand_pages:
    if info['count'] >= 5:
        hubs.append(info)
        print(f"  {info['count']:3d}  {info['canonical']}   <- {info['aliases'][:5]}")
print(f"\n建页候选总数(>=5): {len(hubs)}")

json.dump({'rewrite': rewrite, 'hubs': hubs}, open('.lint_plan.json', 'w'), ensure_ascii=False, indent=1)
print("\n已写 .lint_plan.json")
