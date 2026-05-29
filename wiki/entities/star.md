---
type: entity
subtype: model
tags: [multi-scenario, ctr-prediction, recommendation, baseline]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# STAR

STAR(Star Topology Adaptive Recommender)是一种面向多场景 CTR 预测的星型拓扑网络结构,通过共享中心参数与各场景专属参数相结合来同时服务多个业务场景,常被用作多场景推荐建模的基线方法。

## 在本 wiki 中的出现
- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。
- [[multi-task-learning]]
- [[cvr-prediction]]

- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。

## 相关

- [[hierrec]]
- [[mmoe]]
- [[ple]]
