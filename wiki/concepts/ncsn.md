---
type: concept
subtype: method
tags: [generative-model, score-based, diffusion, score-matching]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# NCSN

NCSN(Noise Conditional Score Network,噪声条件得分网络)是一类基于得分匹配的生成模型,通过在多个噪声尺度上估计数据分布的得分(对数概率密度的梯度),再借助朗之万动力学采样生成数据,是扩散类生成模型的重要早期代表。

## 在本 wiki 中的出现

- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。

## 相关

- [[diffusion-model]]
- [[score-matching]]
- [[langevin-dynamics]]
- [[ddpm]]
