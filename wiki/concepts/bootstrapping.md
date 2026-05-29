---
type: concept
subtype: method
tags: [reasoning, self-improvement, fine-tuning, chain-of-thought]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Bootstrapping

Bootstrapping 指模型利用自身生成的数据反复迭代来逐步增强某项能力的自我提升方法,无需依赖大量人工标注。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:STaR 中 bootstrapping 是核心训练范式。模型先用少量 chain-of-thought (CoT) 示例为问题生成推理过程 (rationale),只保留得出正确答案的 rationale;对答错的题目,再用 rationalization(给定正确答案反向补全推理)来获得可用的 rationale。随后用这些自生成的 rationale 微调模型自身,如此反复迭代,从而 bootstrap 出更强的推理能力。

## 相关

- [[chain-of-thought]]
- [[rationalization]]
- [[self-training]]
- [[fine-tuning]]
- [[2022-star-self-taught-reasoner]]
