---
type: concept
subtype: method
tags: [reward-model, reasoning, process-supervision, math, RLHF]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# 过程奖励模型 (PRM)

过程奖励模型 (Process Reward Model, PRM) 是一种对推理过程中每一步骤分别给予奖励/打分的模型,与只对最终结果打分的结果奖励模型 (Outcome Reward Model, ORM) 相对。

## 在本 wiki 中的出现

- 在 [[2023-lets-verify-step-by-step]] 中,PRM 是论文的核心方法。OpenAI 通过过程监督 (process supervision) 训练 PRM,证明其在 MATH 多步数学推理任务上显著优于结果监督 (ORM):用 PRM 做 best-of-N 重排序,准确率达到 78.2%。论文同时开源了步骤级人工标注数据集 PRM800K,用于训练这类逐步打分的奖励模型。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。

## 相关

- [[outcome-reward-model]] —— PRM 的对照方法,只对最终答案打分。
- [[prm800k]] —— 用于训练 PRM 的步骤级标注数据集。
- [[best-of-n]] —— PRM 常用的推理时应用方式,对 N 个候选解打分后选优。
- [[chain-of-thought]] —— 多步推理的载体,PRM 针对其中的每一步进行评估。
- [[rlhf]] —— 奖励模型所属的更广义的训练范式。
- [[math-benchmark]] —— PRM 取得显著提升的评测基准。
