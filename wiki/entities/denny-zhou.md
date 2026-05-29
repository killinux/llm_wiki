---
type: entity
subtype: person
tags: [researcher, llm, reasoning, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Denny Zhou

Denny Zhou 是一位从事大语言模型推理与提示(prompting)方法研究的研究者,参与了 chain-of-thought prompting 等多项工作。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作者之一。该工作提出 chain-of-thought prompting,即在 few-shot 示例中加入中间推理步骤,从而显著提升大模型的多步推理能力;该增益随模型规模涌现(PaLM 540B 在 GSM8K 上达到 57%)。
- [[2023-self-debugging]]:作者之一。该工作提出 SELF-DEBUGGING,通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,实现无需人工反馈的自我调试。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。

## 相关

- [[chain-of-thought]]
- [[self-debugging]]
- [[few-shot-prompting]]
- [[llm-reasoning]]
- [[code-generation]]
- [[self-correction]]
- [[PaLM]]
- [[GSM8K]]
