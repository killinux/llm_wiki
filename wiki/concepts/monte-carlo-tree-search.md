---
type: concept
subtype: method
tags: [search, planning, reasoning, rl]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Monte-Carlo Tree Search

Monte-Carlo Tree Search (MCTS) 是一种启发式搜索算法,通过反复执行选择 (selection) → 扩展 (expansion) → 评估/模拟 (simulation) → 回传 (backpropagation) 四个步骤,在搜索树中以随机采样增量地构建并评估节点,并平衡探索与利用(经典做法为 UCB/UCT),从而在大型决策空间中逼近高回报的策略。因博弈系统(如 AlphaGo)而闻名。

## 在本 wiki 中的出现

- [[2023-reasoning-via-planning-rap]]:RAP 把 LLM 同时当作世界模型 (world model) 和推理智能体 (reasoning agent),用 MCTS 在巨大的推理空间里做有策略的规划,在世界模型与任务专属奖励的引导下平衡探索与利用,从而把 LLM 推理重新表述为带世界模型的规划问题。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM 用学习的 value function 实现 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。

## 相关

- [[tree-search]]:MCTS 是 Tree Search 的一种经典实例,以采样模拟指导分支选择。
- [[tree-of-thoughts]]:同样把推理建模为树上的搜索,但通常无显式世界模型与回传。
- [[language-agent-tree-search]]:将 MCTS 与 LLM agent(行动 + 反思)结合。
- [[llm-planning]]:MCTS 常作为 LLM 规划中的搜索/规划机制。
- [[reinforcement-learning]]:MCTS 与 RL 共享探索-利用、价值估计等思想。
- [[test-time-compute]]:以搜索增加推理期算力来提升推理质量。
