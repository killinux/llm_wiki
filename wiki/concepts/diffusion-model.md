---
type: concept
subtype: method
tags: [diffusion-model, generative-model, denoising]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# diffusion model

扩散模型是一类生成模型,通过逐步向数据添加噪声的前向过程与学习逐步去噪的反向过程来建模数据分布,从而能从噪声中采样生成符合真实分布的样本。

## 在本 wiki 中的出现

- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。

## 相关

- [[denoising]]
- [[generative-model]]
- [[hierarchical-reinforcement-learning]]
- [[recommendation-system]]
