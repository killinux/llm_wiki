---
type: concept
subtype: method
tags: [safety, fine-tuning, refusal, robustness, abliteration]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Extended-Refusal Fine-tuning

一种安全微调方法:将模型的拒绝(refusal)信号从单一潜在方向分散到多个 token 位置与多个表示维度上,从而抵御针对单一方向的移除型攻击(如 abliteration)。

## 在本 wiki 中的出现

- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。

## 相关

- [[abliteration]]
- [[refusal-direction]]
- [[safety-fine-tuning]]
- [[llm-safety]]
