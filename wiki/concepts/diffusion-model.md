---
type: concept
subtype: method
tags: [diffusion-model, generative-model, recommendation, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Diffusion Model

扩散模型是一类生成模型,通过逐步向数据添加噪声的前向过程与学习逆向去噪过程来建模数据分布,从而生成新样本或对不确定性进行建模。

## 在本 wiki 中的出现

- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[recommendation-system]]
- [[offline-reinforcement-learning]]
- [[world-model]]
- [[generative-model]]
