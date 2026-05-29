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
- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。
- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-dfei-large-scale-multi-domain-recommendation]]:DFEI 是 Meituan 提出的大规模多域推荐框架,自动把用户行为聚合为域特征并为每个用户个性化整合跨域特征,在 Dianping 与 KuaiRand 上的多场景 CTR 预测显著优于 MMoE/PLE/STAR/HiNet 等基线。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2024-residual-multi-task-learner-resflow]]:ResFlow:轻量多任务学习框架,通过跨任务网络对应层的残差连接高效传递信息;部署于 Shopee Search pre-rank,线上 OPU 提升 1.29% 且无额外延迟。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[hinet]]
- [[multi-domain-recommendation]]

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
- [[recommender-systems|recommendation-system]]
- [[ctr-prediction]]
- [[embedding-based-retrieval]]
- [[rmtl]]
- [[ple]]
- [[star]]
- [[hierrec]]
- [[multi-task-fusion]]
