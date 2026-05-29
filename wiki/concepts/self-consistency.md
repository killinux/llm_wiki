---
type: concept
subtype: method
tags: [reasoning, prompting, chain-of-thought, decoding, ensembling]
created: 2026-05-29
updated: 2026-05-29
sources: 17
---

# Self-Consistency

Self-Consistency 是一种解码与推理策略：对同一道题用 chain-of-thought 采样多条不同的推理路径，再对最终答案做多数投票（marginalize），以替代单一的 greedy decoding，从而提升复杂推理任务的准确率。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]：本 wiki 中与 Self-Consistency 关系最密切的工作。该论文提出 chain-of-thought prompting——在 few-shot 示例中加入中间推理步骤——是 Self-Consistency 所依赖的基础：Self-Consistency 正是在 CoT 生成的多条推理路径之上做多数投票。论文展示了 CoT 推理增益随模型规模涌现（PaLM 540B 在 GSM8K 达 57%）。

- [[2023-tree-of-thoughts]]：将 LLM 推理建模为在「思考」树上的搜索（可前瞻、自评估、回溯），在 24 点上把 GPT-4 成功率从 CoT 的 4% 提升到 74%。相对于 Self-Consistency 对完整答案做事后投票，ToT 提供了更结构化的搜索式探索方案，可视为对「多路径推理」思路的进一步扩展。

- [[2023-multi-agent-debate|2023-multiagent-debate]]：让多个 LLM 实例多轮辩论、互相批评彼此答案，在推理（GSM8K 77%→85%）与事实性（MMLU 63.9%→71.1%）任务上显著提升。与 Self-Consistency 同属「利用多条/多份输出来提升可靠性」的范式，但用交互式辩论与批评取代了独立采样后的静态投票。

- [[2023-plan-and-solve-prompting]]：提出零样本 Plan-and-Solve (PS/PS+) 提示，让 LLM 先制定计划再执行子任务，显著改进 Zero-shot-CoT 的多步推理。它改进的是单条推理链的质量，与 Self-Consistency 改进的是「如何聚合多条推理链」相互正交、可叠加使用。

- [[2023-ts-llm-tree-search-decoding-training]]：TS-LLM：用学习的 value function 的 AlphaZero 风格树搜索，同时指导 LLM 的推理解码与迭代训练，适配任意规模 LLM 并将搜索深度扩展到 64。

- [[2023-llms-cannot-self-correct-reasoning-yet]]：本文证明在无外部反馈的"内在自我纠正"设定下，LLM 无法纠正自身推理错误，性能反而往往下降。

- [[2024-v-star-verifiers-for-self-taught-reasoners]]：V-STaR 在自我提升迭代中复用正确与错误的模型生成解，用 DPO 训练 verifier 在测试时对候选解排序，使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。

- [[2024-reflection-on-search-trees]]：RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt，显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率，且任务越难收益越大。

- [[2024-when-can-llms-correct-mistakes]]：批判性综述：细分自我纠错的三类研究问题并提出实验检查清单，论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错，瓶颈在于反馈生成，而外部工具/大规模 fine-tuning 可使其奏效。

- [[2024-tree-search-for-language-model-agents]]：为 LLM web agent 提出 inference-time best-first tree search，在真实 web 环境中显式做探索与多步规划，把 GPT-4o 在 VisualWebArena 上成功率相对提升 39.7% 至 SOTA 26.4%，并展示 test-time compute scaling 的收益。

- [[2024-recursive-introspection-rise]]：RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调，让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

- [[2024-compute-optimal-inference]]：提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE，实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比（Llemma-7B 约省 2× FLOPs 达到 34B 水平）。

- [[2024-multi-agent-tot-validator]]：将 Tree-of-Thoughts 与多智能体推理结合，新增 Thought Validator agent 过滤无效推理分支后再共识投票，在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。

- [[2024-score-self-correct-via-rl]]：SCoRe 用完全自生成数据的多轮在线强化学习（两阶段+奖励塑形）训练单个 LLM，在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%（整体提升 15.6%）、HumanEval 上达 12.2%。

- [[2024-optima-optimizing-llm-multi-agent]]：OPTIMA 通过生成-排序-选择-训练的迭代范式同时优化 LLM 多智能体系统的通信效率与任务有效性，在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%。

- [[2024-lmagent-multimodal-agents-society]]：基于多模态 LLM 的万级规模 agents 社会，在电商场景模拟多用户的购物、社交、直播行为，复现真实 co-purchase 模式与从众等 emergent behavior。

- [[2025-ab-mcts-adaptive-branching-tree-search]]：提出 AB-MCTS：在推理时树搜索中用 Thompson sampling 自适应决定"向宽采样新候选"还是"向深用外部反馈细化已有答案"，统一 repeated sampling 与多轮 refinement，实现更高效的 test-time scaling。

## 相关

- [[chain-of-thought]]
- [[tree-of-thoughts]]
- [[multiagent-debate]]
- [[zero-shot-cot]]
- [[sampling-decoding]]
- [[majority-voting]]
- [[ensembling]]
- [[tree-search]]
- [[self-correction]]
- [[verifier]]
- [[inference-scaling]]
