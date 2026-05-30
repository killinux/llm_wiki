---
type: entity
subtype: person
tags: [recommendation, retrieval, embedding-based-retrieval, kuaishou, reinforcement-learning, short-video, graph-contrastive-learning, user-simulator, offline-rl, diffusion-model, advertising, two-tower]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Peng Jiang

Peng Jiang 是一位从事推荐系统与 embedding-based retrieval(EBR)研究的作者,相关工作已在快手(Kuaishou)落地。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:作为作者之一,参与提出"分而治之"的推荐召回方案——将 embedding-based retrieval 拆解为"物料聚类 + 簇内并行检索 + 可控合并",并采用 prompt-like 的多任务适配方式。该方法在公开数据集上 Recall 最高提升约 40%,并已在快手线上部署。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[embedding-based-retrieval]]
- [[recommender-systems|recommendation-system]]
- [[kuaishou]]
- [[multi-task-learning]]
- [[2023-divide-and-conquer-ebr]]
- [[reinforcement-learning-for-recommendation]]
- [[user-simulator]]
- [[short-video-recommendation]]
- [[graph-contrastive-learning]]
- [[offline-rl]]
- [[diffusion-world-model]]
- [[two-tower|two-tower-retrieval]]
- [[cascade-ranking]]
