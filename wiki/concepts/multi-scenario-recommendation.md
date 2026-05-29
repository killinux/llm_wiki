---
type: concept
subtype: method
tags: [recommendation, multi-scenario, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Multi-Scenario Recommendation

多场景推荐(Multi-Scenario Recommendation, MSR)指在同一推荐系统中同时服务多个业务场景(如不同频道、页面或广告位),通过共享与场景特定建模来提升各场景的整体推荐效果。

## 在本 wiki 中的出现

- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。

## 相关

- [[multi-scenario-learning]]
- [[multi-task-learning]]
- [[recommender-systems|recommendation-system]]
