#!/usr/bin/env python3
import os, re, glob, collections, json

DIRS = ['sources', 'concepts', 'entities', 'topics']
pages = {}
for d in DIRS:
    for f in glob.glob(f'wiki/{d}/*.md'):
        b = os.path.splitext(os.path.basename(f))[0]
        if b == 'CLAUDE':
            continue
        pages.setdefault(b, []).append(d)
pages_set = set(pages) | {'index'}

# (1) 真正重复的文件页:规范化键相同且都存在
def nk(s):
    return re.sub(r'[-_]', '', s.lower()).rstrip('s')
norm = collections.defaultdict(list)
for slug, dirs in pages.items():
    for d in dirs:
        norm[nk(slug)].append((d, slug))
dups = {k: v for k, v in norm.items() if len(set(v)) > 1}
print("=== (1) 重复文件页(需合并)===")
for k, v in sorted(dups.items()):
    print("  ", " | ".join(f"{d}/{s}" for d, s in sorted(set(v))))

# (2) 悬空链接频次(归一化聚合,仅统计无任何已有页面者)
links = collections.Counter()
for f in glob.glob('wiki/**/*.md', recursive=True):
    if os.path.basename(f) == 'CLAUDE.md':
        continue
    t = open(f, encoding='utf-8').read()
    for m in re.findall(r'\[\[([^\]]+)\]\]', t):
        tgt = m.split('|')[0].split('#')[0].strip()
        if tgt and tgt not in pages_set:
            links[tgt] += 1

existing_norm = set(nk(s) for s in pages)
agg = collections.defaultdict(lambda: {'count': 0, 'variants': []})
for tgt, c in links.items():
    k = nk(tgt)
    if k in existing_norm:
        continue  # 实为变体,已有页面可承接(留待引用自然解析或别名)
    agg[k]['count'] += c
    agg[k]['variants'].append(tgt)
    agg[k].setdefault('canonical', tgt)
    # 选最短 variant 作 canonical
    if len(tgt) < len(agg[k]['canonical']):
        agg[k]['canonical'] = tgt

hubs = sorted(agg.values(), key=lambda x: -x['count'])
print(f"\n=== (2) 真缺页的高频枢纽(top 30,总 {len(hubs)} 组)===")
for h in hubs[:30]:
    print(f"  {h['count']:3d}  {h['canonical']:42s} <- {sorted(set(h['variants']))[:4]}")

top = [h for h in hubs if h['count'] >= 8]
json.dump({'hubs_top': [{'slug': h['canonical'], 'count': h['count'], 'variants': sorted(set(h['variants']))} for h in top]},
          open('.hubs.json', 'w'), ensure_ascii=False, indent=1)
print(f"\n建页阈值>=8 的枢纽数: {len(top)}  -> .hubs.json")
