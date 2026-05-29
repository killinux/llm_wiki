---
type: concept
subtype: method
tags: [activation-steering, steering-vector, representation-engineering, refusal, safety]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# activation steering

Activation steering 是一种通过在推理时向模型的内部激活(隐藏状态)上加减特定方向向量(steering vector),从而引导或调控模型行为的方法,无需重新训练模型参数。

## 在本 wiki 中的出现

- [[2024-mitigating-false-refusal-single-vector-ablation]]:提出 training-free、零推理开销的方法,通过正交化并消融单个 false refusal vector 来缓解 LLM 的过度拒绝,同时保持安全性与通用能力。

## 相关

- [[steering-vector]]
- [[representation-engineering]]
- [[false-refusal]]
- [[refusal-direction]]
