---
type: concept
subtype: method
tags: [semantic-id, generative-recommendation, quantization, tokenization]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# semantic ID

semantic ID 是一种通过对内容/物品的语义表示进行量化(如残差量化、层次化码本)而生成的离散标识符序列,用语义相近的物品共享相近的 ID,使生成式模型可以直接自回归地生成物品标识。

## 在本 wiki 中的出现

- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。

## 相关

- [[generative-recommendation]]
- [[residual-quantization]]
- [[variational-autoencoder|vae]]
- [[codebook]]
