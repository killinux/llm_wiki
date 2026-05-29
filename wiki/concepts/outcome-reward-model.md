---
type: concept
subtype: method
tags: [reward-model, rlhf, reasoning, verification, math]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# 结果奖励模型 (ORM)

结果奖励模型 (Outcome Reward Model, ORM) 是一类只依据最终结果(整条推理/生成的最终答案是否正确)来给出奖励信号的奖励模型,与逐步评分的过程奖励模型 (Process Reward Model, PRM) 相对。

## 在本 wiki 中的出现

- [[2023-lets-verify-step-by-step]]:作为对照基线方法出现。OpenAI 在 MATH 多步数学推理任务上比较了过程监督 (PRM) 与结果监督 (ORM),证明 PRM 显著优于 ORM——PRM 的 best-of-N 选择准确率达到 78.2%,并配套开源了步骤级标注数据集 PRM800K。在该工作中,ORM 代表"仅对最终答案对错进行监督/打分"的训练范式。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平)。

## 相关

- [[process-supervision]]:过程监督 / 过程奖励模型 (PRM),逐步对推理过程打分,与 ORM 形成核心对照。
- [[outcome-supervision]]:结果监督,ORM 所采用的监督范式。
- [[reward-model]]:奖励模型这一上位概念。
- [[rlhf]]:基于人类反馈的强化学习,奖励模型的典型应用场景。
- [[test-time-scaling]]:测试时扩展,ORM 常用于 best-of-N 等候选择优场景。
- [[self-consistency]]:另一种聚合多个候选解的择优方法,可与基于奖励模型的重排序对比。
