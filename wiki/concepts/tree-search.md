---
type: concept
subtype: method
tags: [reasoning, search, planning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Tree Search

Tree Search 是一类在树状结构的状态空间中通过分支扩展、评估与回溯来寻找解的搜索方法,在 LLM 中常被用来把推理过程组织为可探索、可前瞻、可回退的树。

## 在本 wiki 中的出现

- [[2023-tree-of-thoughts]]:将 LLM 推理建模为在「思考」(thought)树上的 Tree Search。每个节点是一段中间思考,模型可以进行前瞻(lookahead)、自评估(self-evaluation)候选分支的优劣,并在死路时回溯(backtracking)到更有希望的分支。借助这种搜索,在 24 点(Game of 24)任务上把 GPT-4 的成功率从 CoT 的 4% 提升到 74%。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。

## 相关

- [[tree-of-thoughts]]:基于 Tree Search 的具体 LLM 推理框架。
- [[monte-carlo-tree-search]]:Tree Search 的一种经典实例,以采样模拟指导分支选择。
- [[language-agent-tree-search]]:将 Tree Search 与 LLM agent 结合的方法。
- [[chain-of-thought]]:线性的推理范式,Tree Search 是其向树状搜索的扩展。
- [[self-consistency]]:对多条推理路径采样并投票,与树状探索思路相关。
- [[llm-planning]]:Tree Search 常作为 LLM 规划中的搜索机制。
- [[react]]:推理-行动交替范式,可与 Tree Search 组合。
