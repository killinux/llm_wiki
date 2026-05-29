---
type: concept
subtype: method
tags: [representation-learning, recommendation, multi-domain, embedding]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Dimensional Collapse

维度坍缩(Dimensional Collapse)指学到的表示向量虽然分布在高维空间中,却实际上只占据了远低于其名义维度的子空间,导致表示能力受限、各部分表示趋于冗余或同质化的现象。

## 在本 wiki 中的出现

- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。

## 相关

- [[multi-domain-recommendation]]
- [[mixture-of-experts]]
- [[representation-decorrelation]]
