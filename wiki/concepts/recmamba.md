---
type: concept
subtype: method
tags: [recommendation, mamba, ssm, sequential-recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# RecMamba

RecMamba 指将 Mamba / 状态空间模型(SSM)及其线性复杂度的序列建模能力引入推荐系统(尤其是序列推荐与召回)的一类方法。

## 在本 wiki 中的出现

- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。
- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图"并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。

## 相关

- [[mamba]]
- [[state-space-model]]
- [[sequential-recommendation]]
- [[two-tower-retrieval]]
- [[diffusion-recommendation]]
