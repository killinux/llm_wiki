---
type: concept
subtype: method
tags: [multi-task-learning, recommendation, cvr, ctr]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# ESMM

ESMM(Entire Space Multi-task Model)是一种推荐系统中的多任务学习方法,通过在全样本空间上联合建模 CTR 与 CVR(以 CTCVR = CTR × CVR 作为辅助监督),缓解传统 CVR 估计中的样本选择偏差与数据稀疏问题。

## 在本 wiki 中的出现

- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。

## 相关

- [[multi-task-learning]]
- [[ctr-prediction]]
- [[cvr-prediction]]
- [[htlnet]]
