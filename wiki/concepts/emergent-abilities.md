---
type: concept
subtype: method
tags: [emergent-abilities, scaling, reasoning, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Emergent Abilities

Emergent Abilities 指某些能力在小模型上几乎不存在,但当模型规模(参数量、训练计算量等)跨过某个阈值后突然显现并快速提升的现象。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:该论文提出 chain-of-thought prompting,即在 few-shot 示例中加入中间推理步骤。其多步推理能力的增益被观察为随模型规模涌现——只有足够大的模型才能从中获益,而小模型几乎无提升。例如 PaLM 540B 在 GSM8K 上达到 57%。在此论文中,Emergent Abilities 作为解释 chain-of-thought 为何依赖大规模模型的核心视角出现。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。

## 相关

- [[2022-chain-of-thought]]
- [[chain-of-thought-prompting]]
- [[scaling-laws]]
- [[few-shot-prompting]]
- [[palm]]
- [[gsm8k]]
- [[multi-agent-systems]]
- [[swarm-intelligence]]
