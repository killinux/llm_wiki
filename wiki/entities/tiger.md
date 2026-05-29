---
type: entity
subtype: model
tags: [generative-recommendation, semantic-id, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# TIGER

TIGER 是一种基于 Semantic ID 的生成式推荐模型,通过将物品表示为语义化的离散 ID 序列并以生成方式预测下一个物品,成为生成式推荐领域的代表性工作之一。

## 在本 wiki 中的出现

- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。
- [[2025-fuxi-gamma-efficient-sequential-recommendation]]:decoder-only 生成式序列推荐框架,用受 Ebbinghaus 遗忘曲线启发的指数幂时间编码器与对角稀疏位置剪枝,在 SOTA 推荐质量下把训练加速最多 4.74×、推理 6.18×。

## 相关

- [[semantic-id]]
- [[generative-recommendation]]
- [[hid-vae]]
