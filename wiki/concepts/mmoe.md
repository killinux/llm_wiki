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

- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-dfei-large-scale-multi-domain-recommendation]]:DFEI 是 Meituan 提出的大规模多域推荐框架,自动把用户行为聚合为域特征并为每个用户个性化整合跨域特征,在 Dianping 与 KuaiRand 上的多场景 CTR 预测显著优于 MMoE/PLE/STAR/HiNet 等基线。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。

## 相关

- [[ple]]
- [[star]]
- [[hinet]]
- [[multi-task-learning]]
- [[multi-domain-recommendation]]
- [[mixture-of-experts]]
