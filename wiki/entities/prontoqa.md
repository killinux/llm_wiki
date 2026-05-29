---
type: entity
subtype: benchmark
tags: [reasoning, logical-reasoning, qa, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# PrOntoQA

PrOntoQA 是一个用于评估 LLM 多步逻辑推理能力的合成问答基准,它通过本体(ontology)生成可控的演绎推理链,从而能够逐步验证模型推理过程的正确性。

## 在本 wiki 中的出现

- [[2023-reasoning-via-planning-rap]]:RAP 把 LLM 同时当作世界模型和推理智能体,用 MCTS 在推理空间里做规划,将 LLM 推理重新表述为带世界模型的规划。PrOntoQA 在其中作为逻辑推理任务的评测基准之一,用于检验这种"规划式推理"方法的效果。

## 相关

- [[2023-reasoning-via-planning-rap]]
- [[monte-carlo-tree-search|mcts]]
- [[world-model]]
- [[logical-reasoning]]
- [[chain-of-thought]]
