---
type: concept
subtype: method
tags: [recommendation, diffusion-models, sequential-recommendation, generative-model]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# DreamRec

DreamRec 是一种基于扩散模型(diffusion model)的序列推荐方法,将"预测下一个交互物品"建模为以用户历史行为为条件、在物品表示空间中逐步去噪生成"理想物品 oracle"的生成式过程,从而摆脱传统判别式推荐对负采样的依赖。

## 在本 wiki 中的出现

- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。

## 相关

- [[diffusion-models|diffusion-model]]
- [[sequential-recommendation]]
- [[generative-recommendation]]
