---
type: concept
subtype: method
tags: [learning-to-rank, ranking, information-retrieval, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# learning to rank

Learning to Rank(LTR)是一类用机器学习方法训练排序模型的技术,目标是对候选项(文档、商品、广告等)按相关性或效用进行最优排序,广泛用于搜索、推荐和广告系统。

## 在本 wiki 中的出现

- [[2024-residual-multi-task-learner-resflow]]:ResFlow 是轻量多任务学习框架,通过跨任务网络对应层的残差连接高效传递信息;部署于 Shopee Search 的 pre-rank 阶段,线上 OPU 提升 1.29% 且无额外延迟。
- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。
- [[2026-graphrag-irl]]:GraphRAG-IRL 把 graph-grounded 特征、Maximum Entropy 逆强化学习预排序与 persona-guided LLM 重排融合,LLM 只对 IRL 短候选列表做语义重排,在 MovieLens/KuaiRand 上 NDCG@10 比监督基线提升 15.7%/16.6%。
- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[multi-task-learning]]
- [[pre-ranking]]
- [[search-ranking]]
- [[recommender-systems|recommendation-systems]]
- [[two-tower|two-tower-model]]
- [[inverse-reinforcement-learning]]
