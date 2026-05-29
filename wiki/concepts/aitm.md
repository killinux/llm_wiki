---
type: concept
subtype: method
tags: [multi-task-learning, recommendation, task-dependency, gradient-adjustment]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# AITM

AITM(Adaptive Information Transfer Multi-task)是一类在多任务学习中沿任务依赖链显式建模并自适应传递任务间信息的方法,常用于推荐系统中处理具有先后依赖关系的多目标(如点击、转化)预估。

## 在本 wiki 中的出现

- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-residual-multi-task-learner-resflow]]:ResFlow 是一种轻量多任务学习框架,通过跨任务网络对应层之间的残差连接高效传递信息;部署于 Shopee Search pre-rank,线上 OPU 提升 1.29% 且无额外延迟。

## 相关

- [[multi-task-learning]]
- [[task-dependency]]
- [[gradient-adjustment]]
- [[recommendation-system]]
