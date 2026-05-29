---
type: entity
subtype: model
tags: [model, llm, openai, gpt, few-shot]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# GPT-3

GPT-3 是 OpenAI 推出的 175B 参数自回归大语言模型,以强大的 few-shot / in-context learning 能力著称,被本 wiki 多篇论文作为基础模型或对比基线使用。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作为被研究的大模型之一。该工作提出 chain-of-thought prompting,在 few-shot 示例中加入中间推理步骤以提升多步推理能力,并指出该增益随模型规模涌现(如 PaLM 540B 在 GSM8K 达 57%),GPT-3 这类大模型属于此类规模上展现 CoT 收益的对象。
- [[2022-instructgpt]]:作为被对齐与对比的基础模型。InstructGPT 用 RLHF(SFT → 奖励模型 → PPO)对齐 GPT-3,使 1.3B 的 InstructGPT 在人类偏好上胜过 175B GPT-3,且更真实、毒性更低。
- [[2022-star-self-taught-reasoner]]:作为可被自举(bootstrap)推理能力的大模型。STaR 用少量 CoT 示例让模型自己生成推理过程,只保留答对的 rationale(并用 rationalization 从答错题反向补全),反复微调自身。
- [[2023-causal-inference-for-recommendation]]:在这篇关于将因果推断引入推荐系统的系统综述中被提及。
- [[2023-plan-and-solve-prompting]]:作为零样本提示方法所作用的 LLM。该工作提出 Plan-and-Solve (PS/PS+) 提示,让 LLM 先制定计划再执行子任务,改进 Zero-shot-CoT 的多步推理。
- [[2023-timesfm-time-series-foundation-model]]:Google Research 的 TimesFM 是一个在 O(100B) 时间点真实+合成时序上预训练的 decoder-only 时序预测基础模型,zero-shot 表现接近全监督 SOTA;其 decoder-only 架构与基础模型范式与 GPT-3 一脉相承。
- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件;GPT-3 作为 NLP 领域 scaling law 的代表性参照。

## 相关

- [[instructgpt]]
- [[chain-of-thought|chain-of-thought-prompting]]
- [[few-shot-learning]]
- [[in-context-learning]]
- [[rlhf]]
- [[palm]]
- [[large-language-models|large-language-model]]
- [[openai]]
- [[zero-shot-cot]]
- [[plan-and-solve-prompting]]
- [[timesfm]]
- [[foundation-model]]
- [[scaling-law]]
- [[hstu]]
- [[recommender-systems|recommendation-system]]
