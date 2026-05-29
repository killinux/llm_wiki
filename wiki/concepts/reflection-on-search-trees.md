---
type: concept
subtype: method
tags: [reflection, tree-search, prompting, llm-reasoning, mcts, bfs]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Reflection on Search Trees

Reflection on Search Trees(RoT)是一种让 strong LLM 反思 weak LLM 的历史树搜索经验、将其总结为任务级 guideline 并注入后续 prompt,从而提升基于树搜索的 LLM 推理(如 BFS、MCTS)准确率与搜索效率的方法。

## 在本 wiki 中的出现

- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。

## 相关

- [[tree-search]]
- [[monte-carlo-tree-search]]
- [[self-reflection]]
- [[llm-reasoning]]
- [[guideline-injection]]
