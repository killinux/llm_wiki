---
type: concept
subtype: method
tags: [diffusion-models, generative-models, recommendation, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Diffusion Models

扩散模型是一类生成模型,通过逐步向数据添加噪声的前向过程与学习逐步去噪的反向过程来建模数据分布,从而能够从噪声中生成或重建目标样本。

## 在本 wiki 中的出现
- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[recommender-systems|recommendation-system]]
- [[offline-reinforcement-learning]]
- [[world-model]]
- [[generative-model]]

- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图",并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。

- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[two-tower-retrieval]]
- [[late-interaction]]
- [[generative-recommendation]]
