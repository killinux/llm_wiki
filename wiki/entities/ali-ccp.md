---
type: entity
subtype: dataset
tags: [dataset, ctr, recommendation, multi-scenario]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Ali-CCP

Ali-CCP(Alibaba Click and Conversion Prediction)是阿里巴巴公开的大规模点击与转化预测数据集,常用于多场景 CTR/CVR 预测研究。

## 在本 wiki 中的出现

- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。
- [[2024-residual-multi-task-learner-resflow]]:ResFlow,轻量多任务学习框架,通过跨任务网络对应层的残差连接高效传递信息;部署于 Shopee Search pre-rank,线上 OPU 提升 1.29% 且无额外延迟。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2025-gnolr-progressive-implicit-preference]]:提出 GNOLR,用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进又把多路检索简化为单次最近邻搜索。

## 相关

- [[kuairand]]
- [[ctr-prediction]]
- [[multi-scenario-recommendation]]
