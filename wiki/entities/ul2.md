---
type: entity
subtype: model
tags: [model, language-model, pretraining, encoder-decoder]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# UL2

UL2 是一个统一的预训练语言模型,通过混合多种去噪目标(Mixture-of-Denoisers)在不同任务设置下进行预训练。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作为参与对比/评测的大语言模型之一出现。该论文提出 chain-of-thought prompting——在 few-shot 示例中加入中间推理步骤,显著提升大模型的多步推理能力,并指出该增益随模型规模而涌现(PaLM 540B 在 GSM8K 上达到 57%)。UL2 在其中作为对照模型一并参与了相关推理能力的评估。

## 相关

- [[2022-chain-of-thought]]
- [[chain-of-thought]]
- [[palm]]
- [[emergent-abilities]]
- [[few-shot-prompting]]
