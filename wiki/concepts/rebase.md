---
type: concept
subtype: method
tags: [inference-scaling, tree-search, reasoning, compute-optimal]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# REBASE

REBASE(REward BAlanced SEarch)是一种新型树搜索算法,用奖励模型对候选节点进行平衡式扩展,在固定推理算力下高效地权衡探索与利用,以提升大语言模型的推理表现。

## 在本 wiki 中的出现

- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 即可达到 34B 水平)。

## 相关

- [[inference-scaling-laws]]
- [[compute-optimal-inference]]
- [[tree-search]]
- [[reward-model]]
