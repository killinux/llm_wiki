---
type: concept
subtype: method
tags: [multi-task-learning, recommendation, deep-learning, optimization]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Multi-task learning

Multi-task learning(多任务学习,MTL)是一种让单个模型同时学习多个相关任务、通过共享表示与知识迁移来提升各任务泛化能力的机器学习范式。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:在推荐召回的 embedding-based retrieval 中,采用 prompt-like 的多任务适配,把"物料聚类 + 簇内并行检索 + 可控合并"统一到一个框架下;multi-task learning 在此作为适配多种检索目标的机制,公开数据集 Recall 最高提升约 40%,并已在快手线上部署。
- [[2023-multi-task-recommendations-with-rl]]:RMTL 直接以多任务推荐为目标场景,用 actor-critic 强化学习按 session 级序列动态生成各任务的损失权重,替代固定常数加权,从而缓解 multi-task learning 中的任务平衡问题,在 RetailRocket 与 Kuairand 上提升 CTR/CTCVR 的 AUC。
- [[2023-multi-task-deep-recommender-systems-survey]]:该综述以 multi-task learning 在深度推荐系统中的应用(MTDRS)为主题,从任务关系与方法论两个维度建立系统分类体系,梳理代表模型、数据集与未来方向。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。
- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-dfei-large-scale-multi-domain-recommendation]]:DFEI 是 Meituan 提出的大规模多域推荐框架,自动把用户行为聚合为域特征并为每个用户个性化整合跨域特征,在 Dianping 与 KuaiRand 上的多场景 CTR 预测显著优于 MMoE/PLE/STAR/HiNet 等基线。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。

## 相关

- [[recommendation-system]]
- [[embedding-based-retrieval]]
- [[reinforcement-learning]]
- [[actor-critic]]
- [[loss-weighting]]
- [[transfer-learning]]
