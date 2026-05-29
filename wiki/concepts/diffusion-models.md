---
type: concept
subtype: method
tags: [diffusion-models, generative-models, recommendation, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Diffusion Models

扩散模型是一类生成模型,通过逐步向数据添加噪声的前向过程与学习逐步去噪的反向过程来建模数据分布,从而能够从噪声中生成或重建目标样本。

## 在本 wiki 中的出现

- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图",并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。

## 相关

- [[two-tower-retrieval]]
- [[late-interaction]]
- [[generative-recommendation]]
