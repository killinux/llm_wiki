#!/usr/bin/env python3
"""合并重复文件页(同一概念在 concepts/ 和 entities/ 各一份)。
规则:
- 强制保留 concepts 的核心方法页:见 KEEP_CONCEPTS
- 其余跨目录重复:读 entities 版 frontmatter subtype;若是实体类(model/benchmark/dataset/person/lab/product)→保留 entities,否则保留 concepts
- 同目录单复数变体:保留规范形式(复数)
合并方式:把被删页的「## 在本 wiki 中的出现」条目并入保留页(去重),frontmatter sources 取较大。
可逆(git)。先 --dry 打印计划。"""
import os, re, glob, sys, collections, subprocess

DRY = '--run' not in sys.argv
ENTITY_SUB = {'model', 'benchmark', 'dataset', 'person', 'lab', 'product'}
KEEP_CONCEPTS = {'react', 'reflexion', 'generative-agents', 'chain-of-thought',
                 'monte-carlo-tree-search', 'large-language-models', 'llm-agents',
                 'recommender-systems', 'language-agent-tree-search', 'tree-of-thoughts',
                 'memory-stream'}
# 同目录或跨目录的变体:别名 -> canonical
VARIANT = {
    'diffusion-model': 'diffusion-models',
    'llm-agent': 'llm-agents',
    'recommender-system': 'recommender-systems',
    'recommendation-system': 'recommender-systems',
    'recommendation-systems': 'recommender-systems',
    '2023-multiagent-debate': '2023-multi-agent-debate',
    'react-reasoning-and-acting': 'react',
}

def fpath(slug):
    for d in ['concepts', 'entities', 'sources', 'topics']:
        p = f'wiki/{d}/{slug}.md'
        if os.path.exists(p):
            yield d, p

def subtype(p):
    t = open(p, encoding='utf-8').read()
    m = re.search(r'^subtype:\s*(\S+)', t, re.M)
    return m.group(1) if m else ''

def sources_count(p):
    t = open(p, encoding='utf-8').read()
    m = re.search(r'^sources:\s*(\d+)', t, re.M)
    return int(m.group(1)) if m else 1

def occ_lines(p):
    t = open(p, encoding='utf-8').read()
    return re.findall(r'^- \[\[[^\]]+\]\].*$', t, re.M)

# 找同 slug 跨目录重复
pages = collections.defaultdict(list)
for d in ['concepts', 'entities', 'sources', 'topics']:
    for f in glob.glob(f'wiki/{d}/*.md'):
        b = os.path.splitext(os.path.basename(f))[0]
        if b == 'CLAUDE':
            continue
        pages[b].append(d)

plan = []  # (keep_path, drop_path, slug)
for slug, dirs in pages.items():
    if len(dirs) < 2:
        continue
    if 'concepts' in dirs and 'entities' in dirs:
        cpath, epath = f'wiki/concepts/{slug}.md', f'wiki/entities/{slug}.md'
        if slug in KEEP_CONCEPTS:
            plan.append((cpath, epath, slug))
        elif subtype(epath) in ENTITY_SUB:
            plan.append((epath, cpath, slug))
        else:
            plan.append((cpath, epath, slug))

# 去重(同一 keep/drop 对只处理一次),并跳过不存在的
seen = set()
uniq = []
for keep, drop, slug in plan:
    key = (keep, drop)
    if key in seen:
        continue
    seen.add(key)
    if os.path.exists(keep) and os.path.exists(drop) and keep != drop:
        uniq.append((keep, drop, slug))
plan = uniq

print(f"=== 跨目录同名重复: {len(plan)} 组 ===")
for keep, drop, slug in plan:
    if DRY:
        print(f"  keep {keep.split('/')[1]:9s} drop {drop.split('/')[1]:9s} | {slug}")
    else:
        # 合并 occurrence 行
        kt = open(keep, encoding='utf-8').read()
        keep_occ = set(occ_lines(keep))
        add = [l for l in occ_lines(drop) if l not in keep_occ]
        if add:
            if '## 在本 wiki 中的出现' in kt:
                # 在该小节后插入
                kt = re.sub(r'(## 在本 wiki 中的出现\n)', r'\1' + '\n'.join(add) + '\n', kt, count=1)
            else:
                kt = kt.rstrip() + '\n\n## 在本 wiki 中的出现\n' + '\n'.join(add) + '\n'
        # sources 取较大
        sc = max(sources_count(keep), sources_count(drop))
        kt = re.sub(r'^sources:\s*\d+', f'sources: {sc}', kt, count=1, flags=re.M)
        open(keep, 'w', encoding='utf-8').write(kt)
        subprocess.run(['git', 'rm', '-q', '-f', drop], check=False)

# 变体合并(不同 slug):删别名文件,链接重写在 .rewrite.py 做
print(f"\n=== 变体页(不同 slug,删别名+重写链接)===")
for alias, canon in VARIANT.items():
    apaths = list(fpath(alias))
    cpaths = list(fpath(canon))
    if not apaths or not cpaths:
        print(f"  skip {alias} -> {canon}  (存在性: alias={bool(apaths)} canon={bool(cpaths)})")
        continue
    print(f"  {alias} -> {canon}")
    if not DRY:
        ad, ap = apaths[0]
        cd, cp = cpaths[0]
        ct = open(cp, encoding='utf-8').read()
        cocc = set(occ_lines(cp))
        add = [l for l in occ_lines(ap) if l not in cocc]
        if add:
            if '## 在本 wiki 中的出现' in ct:
                ct = re.sub(r'(## 在本 wiki 中的出现\n)', r'\1' + '\n'.join(add) + '\n', ct, count=1)
            else:
                ct = ct.rstrip() + '\n\n## 在本 wiki 中的出现\n' + '\n'.join(add) + '\n'
            open(cp, 'w', encoding='utf-8').write(ct)
        subprocess.run(['git', 'rm', '-q', '-f', ap], check=False)

print('\n[DRY-RUN] 未改动。加 --run 执行。' if DRY else '\n[已执行]')
