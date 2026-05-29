---
type: entity
subtype: benchmark
tags: [reasoning, search, puzzle, llm-evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Mini Crosswords

Mini Crosswords 是一种 5×5 的小型纵横填字游戏(crossword puzzle)任务,常被用作评测 LLM 多步推理与搜索能力的基准。

## 在本 wiki 中的出现

- [[2023-tree-of-thoughts]]:作为该论文用于检验 Tree of Thoughts (ToT) 方法的任务之一。ToT 将 LLM 推理建模为在「思考」树上的搜索(支持前瞻、自评估与回溯),Mini Crosswords 这类需要在大量约束下逐步探索、并在死路上回溯的填词问题,正适合体现树搜索相对于线性 Chain-of-Thought (CoT) 推理的优势。

## 相关

- [[2023-tree-of-thoughts]]
- [[tree-of-thoughts]]
- [[chain-of-thought]]
- [[game-of-24]]
- [[gpt-4]]
