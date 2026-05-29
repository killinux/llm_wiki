---
type: concept
subtype: method
tags: [representation-learning, disentanglement, recommendation, multi-domain]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Disentangled Representation Learning

解耦表示学习,旨在让模型学到的表示中不同维度/子表示分别对应数据背后相互独立的潜在因子,从而提升可解释性、可迁移性与下游任务的鲁棒性。

## 在本 wiki 中的出现

- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。

## 相关

- [[multi-domain-recommendation]]
- [[mixture-of-experts]]
- [[multi-task-learning]]
- [[user-modeling]]
- [[semantic-id]]
- [[generative-recommendation]]
- [[orthogonal-loss]]
