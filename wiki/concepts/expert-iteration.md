---
type: concept
subtype: method
tags: [self-improvement, bootstrapping, fine-tuning, reasoning, search]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Expert Iteration

Expert Iteration 是一种自我提升(self-improvement)训练范式:用一个"专家"过程(如搜索、采样筛选或更强的策略)生成高质量的目标行为数据,再用这些数据微调基础模型,如此反复迭代,使模型逐步将专家的能力"内化"为自身的策略。

## 在本 wiki 中的出现

- [[2022-star-self-taught-reasoner]]:STaR(Self-Taught Reasoner)是 Expert Iteration 思路在推理(reasoning)上的具体实例。它用少量 CoT 示例提示模型自己生成推理过程(rationale),只保留最终答对的 rationale,并通过 rationalization(给出正确答案后让模型反向补全推理)来覆盖原本答错的题目;随后用这批筛选/补全得到的 rationale 反复微调模型自身,从而 bootstrap 出更强的推理能力。这里"答案正确性筛选 + rationalization 补全"充当了生成高质量数据的专家过程,迭代微调对应 Expert Iteration 的循环。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。
- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。

## 相关

- [[2022-star-self-taught-reasoner]]
- [[chain-of-thought]]
- [[rationalization]]
- [[bootstrapping]]
- [[self-improvement]]
- [[rejection-sampling]]
- [[supervised-fine-tuning]]
- [[rlhf]]
