---
type: concept
subtype: method
tags: [length-generalization, reasoning, generalization, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Length Generalization

Length Generalization 指模型在训练或示例中只见过较短(较少步骤)的输入,却能在推理时正确处理更长、步骤更多的实例的能力。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:该工作提出 chain-of-thought prompting,在 few-shot 示例中显式写出中间推理步骤,从而把单步映射拆解为多步推理过程。通过让模型逐步生成中间步骤,它在 GSM8K 等多步算术与符号推理任务上显著提升表现(PaLM 540B 达 57%),并且这种增益随模型规模涌现。这与 Length Generalization 密切相关:CoT 使模型能够把少量短示例所示范的推理模式延展到包含更多步骤的更长问题上,是缓解长度/步数泛化困难的一种代表性方法。

## 相关

- [[chain-of-thought]]
- [[2022-chain-of-thought]]
- [[emergent-abilities]]
- [[multi-step-reasoning]]
- [[in-context-learning]]
- [[generalization]]
