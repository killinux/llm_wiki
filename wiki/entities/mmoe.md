---
type: entity
subtype: model
tags: [multi-task-learning, recommendation, mixture-of-experts, MTL]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# MMoE

MMoE(Multi-gate Mixture-of-Experts)是一种多任务学习模型,通过共享一组 expert 网络并为每个任务配置独立的 gate 网络来自适应组合 expert 输出,从而在任务间灵活共享与隔离信息,广泛用于推荐系统的多目标建模。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:在将推荐召回的 embedding-based retrieval 拆解为"物料聚类+簇内并行检索+可控合并"的框架中,作为 prompt-like 多任务适配的相关多任务建模背景出现;该工作在公开数据集上 Recall 最高提升约 40%,并已在快手线上部署。
- [[2023-multi-task-recommendations-with-rl]]:作为多任务推荐的典型基线/范式被对照,RMTL 用 actor-critic 强化学习按 session 级序列动态生成多任务损失权重以替代固定常数加权,在 RetailRocket 与 Kuairand 上提升 CTR/CTCVR 的 AUC。
- [[2023-multi-task-deep-recommender-systems-survey]]:作为多任务深度推荐系统(MTDRS)的代表性模型被纳入,该综述从任务关系与方法论两个维度建立系统分类体系,梳理代表模型、数据集与未来方向。
- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2025-deep-interest-life-cycle-network]]:提出 DILN,显式建模用户兴趣生命周期(emergent/stable/declining)并用 VQ 聚类离散化、注入 MMOE 排序模型,Lofter 线上 CTR +0.38%、CVR +1.04%、时长 +0.25%。

## 相关

- [[multi-task-learning]]
- [[mixture-of-experts]]
- [[recommendation-system]]
- [[ctr-prediction]]
- [[embedding-based-retrieval]]
- [[rmtl]]
- [[ple]]
- [[star]]
- [[hierrec]]
- [[multi-task-fusion]]
