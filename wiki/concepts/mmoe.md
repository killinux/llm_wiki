---
type: concept
subtype: method
tags: [multi-task-learning, recommendation, mixture-of-experts, multi-domain]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# MMoE

MMoE(Multi-gate Mixture-of-Experts)是一种多任务学习方法,通过共享一组底层 expert 网络并为每个任务配置独立的 gating 网络,让不同任务自适应地组合 expert 输出,从而在缓解任务间负迁移的同时实现知识共享,广泛用作推荐系统多任务/多域建模的基线与骨干。

## 在本 wiki 中的出现

- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。

## 相关

- [[ple]]
- [[star]]
- [[hinet]]
- [[multi-task-learning]]
- [[multi-domain-recommendation]]
- [[mixture-of-experts]]
