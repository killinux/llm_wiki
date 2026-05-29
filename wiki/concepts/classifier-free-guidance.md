---
type: concept
subtype: method
tags: [diffusion, guidance, generative-models, conditional-generation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Classifier-Free Guidance

Classifier-Free Guidance(无分类器引导,CFG)是一种用于条件扩散模型的采样技术:通过在训练时联合学习条件模型与无条件模型,在采样时将两者的预测做外推组合,从而在不依赖外部分类器的情况下增强生成结果对条件的契合度。

## 在本 wiki 中的出现

- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。

## 相关

- [[diffusion-models]]
- [[conditional-generation]]
- [[guidance]]
