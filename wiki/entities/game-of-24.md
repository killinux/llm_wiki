---
type: entity
subtype: benchmark
tags: [reasoning, math, search, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Game of 24

Game of 24(24 点)是一项数学推理游戏:给定 4 个数字,通过加减乘除四则运算将它们组合得到结果 24,常被用作评测 LLM 多步推理与搜索能力的 benchmark。

## 在本 wiki 中的出现
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[tree-search]]
- [[value-function]]
- [[reasoning]]
- [[alphazero]]

- [[2023-tree-of-thoughts]]:将其用作核心评测任务之一。该工作把 LLM 推理建模为在「思考」树(tree of thoughts)上的搜索,支持前瞻、自评估与回溯,在 Game of 24 上把 GPT-4 的成功率从 Chain-of-Thought(CoT)的 4% 提升到 74%。

## 相关

- [[tree-of-thoughts]]
- [[chain-of-thought]]
- [[gpt-4]]
- [[llm-reasoning]]
- [[search]]
