---
type: concept
subtype: method
tags: [multi-embedding, multi-domain, recommendation, representation-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Multi-Embedding

Multi-Embedding(多嵌入)是一种为同一特征/同一对象学习多套嵌入表示的方法,常用于多域、多任务或多专家场景,以在共享参数与保持差异性之间取得平衡。

## 在本 wiki 中的出现

- [[2024-crocodile-cross-experts-covariance]]:Crocodile 采用多嵌入架构,配合 cross-experts covariance loss(CovLoss)解耦各 expert 的表示,并以 Prior Informed Element-wise Gating(PEG)进行路由,缓解多域推荐中"保持域差异性"与"充分学习参数"的两难;在公开数据集与 Tencent 线上 A/B 测试中均取得提升。

## 相关

- [[cross-experts-covariance-loss]]
- [[prior-informed-element-wise-gating]]
- [[multi-domain-recommendation]]
- [[mixture-of-experts]]
