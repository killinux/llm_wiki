---
type: concept
subtype: method
tags: [state-space-model, mamba, ssd, sequence-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# State Space Duality

State Space Duality(SSD)是 Mamba2 提出的理论框架,揭示了结构化状态空间模型(SSM)与一类带结构化掩码的注意力机制之间的数学等价关系,使序列建模能在线性复杂度下高效计算。

## 在本 wiki 中的出现

- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。

## 相关

- [[mamba]]
- [[structured-state-space-model]]
- [[sequential-recommendation]]
- [[linear-attention]]
