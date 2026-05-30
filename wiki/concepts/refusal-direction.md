---
type: concept
subtype: method
tags: [safety, interpretability, refusal, abliteration, robustness]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Refusal Direction

拒绝方向(Refusal Direction)指在大语言模型的激活空间中,与"是否拒绝有害请求"这一行为高度相关的潜在方向;沿该方向的单一线性特征常被用来解释、引导甚至(通过 abliteration 等手段)移除模型的安全拒绝行为。

## 在本 wiki 中的出现

- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。

## 相关

- [[abliteration]]
- [[extended-refusal]]
- [[alignment|safety-alignment]]
- [[activation-steering]]
