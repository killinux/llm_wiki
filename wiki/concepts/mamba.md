---
type: concept
subtype: method
tags: [ssm, mamba, sequence-modeling, linear-attention, architecture]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Mamba

Mamba 是一种基于选择性状态空间模型(Selective State Space Model, SSM)的序列建模架构,通过输入依赖的状态转移参数在线性复杂度下捕捉长程依赖,作为 Transformer 自注意力机制的高效替代方案。

## 在本 wiki 中的出现

- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。

## 相关

- [[state-space-model]]
- [[mamba2]]
- [[ssd]]
- [[sequential-recommendation]]
- [[linear-attention]]
