---
type: concept
subtype: method
tags: [abliteration, safety, refusal, alignment, activation-steering]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Abliteration

Abliteration 是一种推理时干预技术,通过在模型激活空间中识别并移除(消融)与"拒绝"行为相关的单一潜在方向,从而绕过对齐模型的安全拒绝机制。

## 在本 wiki 中的出现

- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。

## 相关

- [[refusal-direction]]
- [[activation-steering]]
- [[alignment|safety-alignment]]
- [[jailbreak]]
