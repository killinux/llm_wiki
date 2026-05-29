---
type: entity
subtype: benchmark
tags: [benchmark, mathematics, reasoning, dataset]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# MATH dataset

MATH dataset 是一个面向数学问题求解的基准数据集,包含带有完整分步解答的竞赛级数学题,常用于评测 LLM 的数学推理能力。

## 在本 wiki 中的出现

- [[2023-autogen]]:微软提出的开源多 agent 框架 AutoGen。MATH dataset 在其中作为评测基准之一,用于衡量基于可对话 agent 构建的应用在数学推理任务上的求解表现。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。
- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段+奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%)、HumanEval 上达 12.2%。

## 相关

- [[2023-autogen]]
- [[llm-reasoning]]
- [[benchmark]]
- [[gsm8k]]
