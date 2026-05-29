---
type: entity
subtype: model
tags: [recommendation, state-space-model, mamba, sequential-recommendation, lifelong-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LinRec

LinRec 是一类用于推荐场景的线性复杂度序列建模方法,旨在以接近线性的开销替代 Transformer 自注意力,从而高效建模超长的终身用户行为序列。

## 在本 wiki 中的出现
- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。
- [[attention]]
- [[sequence-recommendation]]
- [[relative-position-encoding]]
- [[long-context]]

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >= 2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。

## 相关

- [[mamba]]
- [[sasrec]]
- [[sequential-recommendation]]
- [[state-space-model]]
- [[lifelong-sequential-recommendation]]
