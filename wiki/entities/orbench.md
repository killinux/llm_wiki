---
type: entity
subtype: benchmark
tags: [benchmark, over-refusal, llm-safety, false-refusal]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# OR-Bench

OR-Bench 是用于评测大语言模型过度拒绝(over-refusal / false refusal)现象的基准,衡量模型在面对看似敏感但实际无害的提示时被错误拒绝的程度。

## 在本 wiki 中的出现

- [[2024-mitigating-false-refusal-single-vector-ablation]]:提出 training-free、零推理开销的方法,通过正交化并消融单个 false refusal vector 来缓解 LLM 的过度拒绝,同时保持安全性与通用能力。

## 相关

- [[false-refusal]]
- [[llm-safety]]
- [[single-vector-ablation]]
