---
type: concept
subtype: method
tags: [mixture-of-experts, MoE, sparse-models, conditional-computation, multi-task-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Mixture of Experts

Mixture of Experts(MoE)是一种条件计算方法:模型由多个并行的子网络(experts)与一个门控网络(gating network)组成,门控网络根据输入动态决定激活哪些 experts 并对其输出进行加权组合,从而在增大模型容量的同时控制实际计算量。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:在这篇多任务深度推荐系统(MTDRS)综述的方法论分类中,MoE 是"专家共享(expert sharing)"这一参数共享范式的思想来源。综述指出专家共享受 MoE 启发,其中 [[mmoe]] 用 softmax 门控装配多个 experts 被视为里程碑,后续的 [[ple]](提出 Customized Gate Control 显式分离共享专家与任务专属专家)、SNR、DSelect-k、MoSE 等都沿此路线发展。因此在本综述里,MoE 扮演的是连接多个 experts 与任务专属门控网络、以在任务间灵活共享与隔离表示的基础架构角色,被广泛用于并行任务关系下的多任务推荐。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 在多域推荐中采用多嵌入架构 + cross-experts covariance loss(CovLoss)来解耦各 expert 的表示,并以 Prior Informed Element-wise Gating(PEG)进行路由,以平衡"保持域差异性"与"充分学习参数"这一两难。MoE 在此作为多 expert 表示学习的基础框架,通过对各 expert 之间的协方差施加约束并配合先验感知的逐元素门控,提升了 expert 表示的解耦程度;方法在公开数据集与 Tencent 线上 A/B 测试中均取得提升。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模,用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。

## 相关

- [[multi-task-learning]]
- [[mmoe]]
- [[ple]]
- [[gating-network]]
- [[sparse-activation]]
- [[conditional-computation]]
- [[recommender-systems]]
