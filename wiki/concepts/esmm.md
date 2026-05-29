---
type: concept
subtype: method
tags: [multi-task-learning, recommendation, cvr, ctr]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# ESMM

ESMM(Entire Space Multi-task Model)是一种推荐系统中的多任务学习方法,通过在全样本空间上联合建模 CTR 与 CVR(以 CTCVR = CTR × CVR 作为辅助监督),缓解传统 CVR 估计中的样本选择偏差与数据稀疏问题。

## 在本 wiki 中的出现

- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-residual-multi-task-learner-resflow]]:ResFlow 轻量多任务学习框架,通过跨任务网络对应层的残差连接高效传递信息;部署于 Shopee Search pre-rank,线上 OPU 提升 1.29% 且无额外延迟。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。

## 相关

- [[multi-task-learning]]
- [[ctr-prediction]]
- [[cvr-prediction]]
- [[htlnet]]
