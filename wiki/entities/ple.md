---
type: entity
subtype: model
tags: [multi-task-learning, recommendation, expert-network]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# PLE

PLE(Progressive Layered Extraction)是一种多任务学习模型,通过区分任务共享专家与任务专属专家,并以渐进式分层结构提取与融合特征,缓解多任务之间的负迁移(negative transfer)与跷跷板(seesaw)现象。

## 在本 wiki 中的出现

- [[2023-multi-task-recommendations-with-rl]]:在该工作中,PLE 作为多任务推荐的代表性骨干网络之一被使用/对比,RMTL 提出用 actor-critic 强化学习按 session 级序列动态生成多任务损失权重,以替代固定常数加权,在 RetailRocket 与 Kuairand 上提升 CTR/CTCVR 的 AUC。
- [[2023-multi-task-deep-recommender-systems-survey]]:该综述从任务关系与方法论两个维度为多任务深度推荐系统(MTDRS)建立系统分类体系,PLE 作为基于专家网络的代表模型之一被纳入分类与梳理。
- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。

## 相关

- [[mmoe]]
- [[multi-task-learning]]
- [[expert-network]]
- [[negative-transfer]]
- [[seesaw-phenomenon]]
- [[ctr]]
- [[ctcvr]]
- [[star]]
- [[hierrec]]
