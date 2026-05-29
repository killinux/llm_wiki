---
type: entity
subtype: model
tags: [model, llm, google, large-language-model]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# PaLM

PaLM(Pathways Language Model)是 Google 提出的大规模 dense Transformer 语言模型,最大规模达 540B 参数,常被用作研究大模型推理与规模涌现能力的代表性模型。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作为验证 chain-of-thought prompting 的核心模型。该工作在 few-shot 示例中加入中间推理步骤,显著提升大模型的多步推理能力,且增益随模型规模涌现——PaLM 540B 在 GSM8K 上达到 57%。
- [[2022-inner-monologue]]:作为可被复用的 frozen LLM,通过持续注入自然语言环境反馈形成"内心独白",实现机器人的闭环、可重规划具身推理。
- [[2023-causal-inference-for-recommendation]]:在这篇将因果推断引入推荐系统的系统综述中被提及。
- [[2023-tree-of-thoughts]]:作为 LLM 推理研究的背景模型出现。该工作将 LLM 推理建模为在「思考」树上的搜索(可前瞻、自评估、回溯),并在 24 点任务上把 GPT-4 成功率从 CoT 的 4% 提升到 74%。

## 相关

- [[chain-of-thought-prompting]]
- [[tree-of-thoughts]]
- [[emergent-abilities]]
- [[gsm8k]]
- [[gpt-4]]
- [[large-language-model]]
- [[transformer]]
- [[google]]
