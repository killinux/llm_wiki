---
type: concept
subtype: method
tags: [reasoning, planning, llm, mcts, world-model]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Reasoning via Planning (RAP)

Reasoning via Planning (RAP) 是一种把 LLM 推理重新表述为"带世界模型的规划"的方法:它让同一个 LLM 既充当世界模型(预测状态转移)又充当推理智能体,并用 Monte Carlo Tree Search (MCTS) 在推理空间中进行有策略的探索与规划。

## 在本 wiki 中的出现

- [[2023-reasoning-via-planning-rap]]:提出 RAP 的原始工作。RAP 把 LLM 同时当作世界模型(world model)和推理智能体(reasoning agent),用 MCTS 在推理空间里做规划,从而把 LLM 推理重新表述为一种带世界模型的规划过程。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。

## 相关

- [[monte-carlo-tree-search]]
- [[tree-search]]
- [[tree-of-thoughts]]
- [[chain-of-thought]]
- [[llm-planning]]
- [[language-agent-tree-search]]
- [[world-model]]
