---
type: concept
subtype: method
tags: [multi-task-learning, recommendation, expert-network, gating]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# PLE

PLE(Progressive Layered Extraction)是一种多任务学习模型,通过将专家网络划分为任务共享专家与任务专属专家,并以渐进式分层提取缓解多任务之间的负迁移(seesaw)问题,常用于推荐系统中的多任务/多场景建模。

## 在本 wiki 中的出现

- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-dfei-large-scale-multi-domain-recommendation]]:DFEI 是 Meituan 提出的大规模多域推荐框架,自动把用户行为聚合为域特征并为每个用户个性化整合跨域特征,在 Dianping 与 KuaiRand 上的多场景 CTR 预测显著优于 MMoE/PLE/STAR/HiNet 等基线。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2024-residual-multi-task-learner-resflow]]:ResFlow:轻量多任务学习框架,通过跨任务网络对应层的残差连接高效传递信息;部署于 Shopee Search pre-rank,线上 OPU 提升 1.29% 且无额外延迟。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。

## 相关

- [[mmoe]]
- [[star]]
- [[hinet]]
- [[multi-task-learning]]
- [[multi-domain-recommendation]]
