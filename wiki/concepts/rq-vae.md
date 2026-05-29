---
type: concept
subtype: method
tags: [vae, quantization, semantic-id, generative-recommendation, representation-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# residual-quantized VAE (RQ-VAE)

residual-quantized VAE (RQ-VAE) 是一种用多层残差向量量化(逐层量化上一层的量化残差)将连续表征编码为一串离散码元(即 semantic ID)的自编码器,常用于为物品生成可作为生成式模型输入的层次化离散标识。

## 在本 wiki 中的出现

- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。

## 相关

- [[semantic-id]]
- [[generative-recommendation]]
- [[vector-quantization]]
- [[vae]]
