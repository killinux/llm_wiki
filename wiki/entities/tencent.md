---
type: entity
subtype: lab
tags: [tencent, recommendation, multi-task-learning, user-modeling, ctr]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Tencent

腾讯,一家中国科技公司,在本 wiki 中以其在推荐系统与多任务学习方向的研究工作出现。

## 在本 wiki 中的出现

- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模,用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。其中 TenRec 数据集与腾讯相关。

## 相关

- [[multi-task-learning]]
- [[recommendation-system]]
- [[htlnet]]
- [[bi-level-user-modeling]]
- [[deep-recommender-systems]]
- [[ctr-prediction]]
- [[tenrec]]
