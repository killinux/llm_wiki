---
type: concept
subtype: method
tags: [reasoning, inference, scaling, multi-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Test-Time Scaling

Test-Time Scaling 指在推理阶段(而非训练阶段)投入更多计算来提升模型表现的一类方法,例如让模型生成更多中间推理、进行多次采样或多轮交互,从而以额外的推理算力换取更高的答案质量。

## 在本 wiki 中的出现

- [[2023-multiagent-debate]]:将 Test-Time Scaling 体现为"多智能体辩论"——在推理时实例化多个 LLM,让它们经过多轮辩论、互相批评并修正彼此的答案。这种推理期的额外计算显著提升了表现:在推理任务上 GSM8K 从 77% 提升到 85%,在事实性任务上 MMLU 从 63.9% 提升到 71.1%。它体现了通过增加推理时交互轮次与模型实例数(即扩展 test-time compute)来提升结果质量的思路。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-tree-search-for-language-model-agents]]:为 LLM web agent 提出 inference-time best-first tree search,在真实 web 环境中显式做探索与多步规划,把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%,并展示 test-time compute scaling 的收益。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。
- [[2024-rethinkmcts]]:一个面向代码生成的思路搜索框架,用 MCTS 探索写代码的推理过程,并通过 rethink 机制利用块级代码执行反馈直接精炼搜索树中的错误思路。
- [[2024-optima-optimizing-llm-multi-agent]]:OPTIMA 通过生成-排序-选择-训练的迭代范式同时优化 LLM 多智能体系统的通信效率与任务有效性,在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%。
- [[2025-ab-mcts-adaptive-branching-tree-search]]:提出 AB-MCTS:在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案",统一 repeated sampling 与多轮 refinement,实现更高效的 test-time scaling。
- [[2025-survey-self-evolving-agents]]:首个系统聚焦自进化智能体的综述,沿 what/when/how/where 四维建立统一框架并梳理评测体系与通往 ASI 的路线图。

## 相关

- [[test-time-compute]]:近义概念,强调推理期所投入的计算量本身。
- [[multi-agent-debate]]:本概念在该 wiki 中的具体实现形式之一。
- [[chain-of-thought]]:另一种典型的推理期增加计算的方式。
- [[self-consistency]]:通过多次采样并投票来扩展推理期计算。
- [[tree-of-thoughts]]:在推理期通过搜索扩展计算的方法。
- [[gsm8k]]:用于评估推理能力的基准。
- [[mmlu]]:用于评估事实性/知识的基准。
