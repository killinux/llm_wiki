---
type: concept
subtype: method
tags: [reasoning, prompting, search, planning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 11
---

# Tree of Thoughts

Tree of Thoughts(ToT)是一种 LLM 推理方法,它把问题求解建模为在「思考(thought)」组成的树上的搜索,让模型生成多条候选推理路径、对中间状态做自评估,并通过前瞻(lookahead)与回溯(backtracking)来选择更优的解。

## 在本 wiki 中的出现

- [[2023-tree-of-thoughts]]:ToT 的提出论文。将 LLM 推理建模为在「思考」树上的搜索,支持前瞻、自评估与回溯。在 Game of 24 任务上,把 GPT-4 的成功率从 Chain-of-Thought 的 4% 提升到 74%。
- [[2022-chain-of-thought]]:ToT 的直接前身与对比基线。Chain-of-Thought prompting 在 few-shot 示例中加入中间推理步骤,显著提升大模型的多步推理能力,且该增益随模型规模涌现(PaLM 540B 在 GSM8K 达 57%)。ToT 把 CoT 的单条线性推理链扩展为可分支、可搜索的树。
- [[2023-reasoning-via-planning-rap]]:与 ToT 思路相近的同期工作。RAP 把 LLM 同时当作世界模型(world model)和推理智能体,用 MCTS 在推理空间里做规划,把 LLM 推理重新表述为带世界模型的规划——与 ToT 同属「把推理当作搜索 / 规划」的范式。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。
- [[2024-rethinkmcts]]:一个面向代码生成的思路搜索框架,用 MCTS 探索写代码的推理过程,并通过 rethink 机制利用块级代码执行反馈直接精炼搜索树中的错误思路。
- [[2024-multi-agent-tot-validator]]:将 Tree-of-Thoughts 与多智能体推理结合,新增 Thought Validator agent 过滤无效推理分支后再共识投票,在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。

## 相关

- [[chain-of-thought]]
- [[monte-carlo-tree-search]]
- [[language-agent-tree-search]]
- [[2023-reasoning-via-planning-rap]]
- [[self-evaluation]]
- [[prompt-engineering]]
