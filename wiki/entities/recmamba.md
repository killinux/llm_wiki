---
type: entity
subtype: model
tags: [recommendation, sequential-recommendation, mamba, state-space-model, lifelong-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# RecMamba

RecMamba 是一种用于终身序列推荐的模型,它用带选择机制的状态空间模型 Mamba 替换 Transformer 层,以高效建模超长的用户行为序列。

## 在本 wiki 中的出现
- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。
- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图"并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。
- [[two-tower|two-tower-retrieval]]
- [[diffusion-recommendation]]

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。
- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。

## 相关

- [[mamba]]
- [[state-space-model]]
- [[sasrec]]
- [[sequential-recommendation]]
- [[transformer]]
