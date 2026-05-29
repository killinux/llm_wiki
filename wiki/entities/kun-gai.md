---
type: entity
subtype: person
tags: [recommendation-system, reinforcement-learning, kuaishou, short-video, author, moe]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Kun Gai

Kun Gai 是一位活跃于推荐系统与强化学习交叉领域的研究者,在本 wiki 收录的多篇面向短视频推荐(尤以 Kuaishou/快手 生产环境为背景)的论文中作为(共同)作者出现。

## 在本 wiki 中的出现

- [[2023-two-stage-constrained-actor-critic]]:作为作者参与提出 TSCAC 两阶段约束式 actor-critic,在最大化短视频 WatchTime 主目标的同时软约束平衡 Like/Share 等稀疏交互行为,该方法已在快手生产系统全量上线。
- [[2023-rlur-user-retention-short-video]]:作为作者参与将短视频用户留存建模为无限时域请求级 MDP,提出 RLUR 用强化学习直接最小化累计回访时间,在 KuaiRand 上优于 TD3/CEM 并在 Kuaishou 全量上线,提升留存与 DAU。
- [[2023-divide-and-conquer-ebr]]:作为作者参与将推荐召回的 embedding-based retrieval 拆为"物料聚类 + 簇内并行检索 + 可控合并",并用 prompt-like 多任务适配,公开数据集 Recall 最高提升约 40%,已在快手线上部署。
- [[2023-gflownet-listwise-recommendation]]:作为作者参与提出 GFN4Rec,用 GFlowNet 流匹配让推荐列表的生成概率正比于其 list-wise 奖励,在保持高质量的同时显著提升列表多样性与在线探索能力。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。

## 相关

- [[kuaishou]]:上述多篇工作的生产部署与业务背景。
- [[reinforcement-learning-for-recommendation]]:其研究主线之一,将 RL 应用于推荐排序与召回。
- [[short-video-recommendation]]:其工作聚焦的应用场景。
- [[watchtime-optimization]]:多目标推荐中的核心优化目标。
- [[user-retention]]:RLUR 等工作直接优化的长期目标。
- [[embedding-based-retrieval]]:divide-and-conquer 召回工作所属的技术方向。
- [[gflownet]]:GFN4Rec 所基于的生成式建模框架。
- [[user-simulator]]:KuaiSim 所属的推荐系统模拟器方向。
- [[mixture-of-experts]]:SMES 所基于的稀疏 MoE 多任务建模方向。
