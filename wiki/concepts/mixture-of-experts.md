---
type: concept
subtype: method
tags: [mixture-of-experts, MoE, sparse-models, conditional-computation, multi-task-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Mixture of Experts

Mixture of Experts(MoE)是一种条件计算方法:模型由多个并行的子网络(experts)与一个门控网络(gating network)组成,门控网络根据输入动态决定激活哪些 experts 并对其输出进行加权组合,从而在增大模型容量的同时控制实际计算量。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:在这篇多任务深度推荐系统(MTDRS)综述的方法论分类中,MoE 是"专家共享(expert sharing)"这一参数共享范式的思想来源。综述指出专家共享受 MoE 启发,其中 [[mmoe]] 用 softmax 门控装配多个 experts 被视为里程碑,后续的 [[ple]](提出 Customized Gate Control 显式分离共享专家与任务专属专家)、SNR、DSelect-k、MoSE 等都沿此路线发展。因此在本综述里,MoE 扮演的是连接多个 experts 与任务专属门控网络、以在任务间灵活共享与隔离表示的基础架构角色,被广泛用于并行任务关系下的多任务推荐。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 在多域推荐中采用多嵌入架构 + cross-experts covariance loss(CovLoss)来解耦各 expert 的表示,并以 Prior Informed Element-wise Gating(PEG)进行路由,以平衡"保持域差异性"与"充分学习参数"这一两难。MoE 在此作为多 expert 表示学习的基础框架,通过对各 expert 之间的协方差施加约束并配合先验感知的逐元素门控,提升了 expert 表示的解耦程度;方法在公开数据集与 Tencent 线上 A/B 测试中均取得提升。

## 相关

- [[multi-task-learning]]
- [[mmoe]]
- [[ple]]
- [[gating-network]]
- [[sparse-activation]]
- [[conditional-computation]]
- [[recommender-systems]]
