---
type: concept
subtype: method
tags: [fine-tuning, reasoning, self-improvement, data-generation, sampling]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Rejection Sampling Fine-Tuning

Rejection Sampling Fine-Tuning 是一种自举式微调方法:让模型对同一问题采样多条候选输出,依据某种验证信号(如答案是否正确)拒绝错误样本、只保留通过筛选的高质量样本,再用这些样本继续微调模型自身。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:STaR 是 Rejection Sampling Fine-Tuning 在推理任务上的代表性实践。它用少量 CoT(Chain-of-Thought)示例提示模型为各问题自行生成推理过程(rationale),然后以"最终答案是否正确"作为拒绝信号,**只保留答对的 rationale**用于微调;对答错的题目,再通过 rationalization(给定正确答案反向补全推理)生成可用样本,从而避免简单题之外的难题被全部丢弃。这一"生成 → 按正确性筛选 → 重新微调"的循环被反复执行,逐步 bootstrap 模型的推理能力。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM 用学习的 value function 进行 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。

## 相关

- [[chain-of-thought]]
- [[2022-star-self-taught-reasoner]]
- [[self-improvement]]
- [[supervised-fine-tuning]]
- [[reinforcement-learning-from-human-feedback]]
- [[best-of-n-sampling]]
- [[expert-iteration]]
- [[verifier]]
- [[direct-preference-optimization]]
- [[tree-search]]
