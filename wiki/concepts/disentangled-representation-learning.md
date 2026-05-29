---
type: concept
subtype: method
tags: [representation-learning, disentanglement, recommendation, multi-domain]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Disentangled Representation Learning

解耦表示学习,旨在让模型学到的表示中不同维度/子表示分别对应数据背后相互独立的潜在因子,从而提升可解释性、可迁移性与下游任务的鲁棒性。

## 在本 wiki 中的出现

- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。

## 相关

- [[multi-domain-recommendation]]
- [[mixture-of-experts]]
- [[multi-task-learning]]
