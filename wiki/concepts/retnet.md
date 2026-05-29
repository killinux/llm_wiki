---
type: concept
subtype: method
tags: [retnet, retention, linear-attention, sequence-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# RetNet

RetNet(Retentive Network)是一种用"保留机制"(retention)替代标准注意力的序列建模架构,兼具并行训练、低成本循环推理与线性复杂度,常作为 Transformer 在长序列场景下的高效替代方案。

## 在本 wiki 中的出现

- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。

## 相关

- [[linear-attention]]
- [[transformer]]
- [[relative-position-encoding]]
- [[sequential-recommendation]]
