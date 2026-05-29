---
type: concept
subtype: method
tags: [exploration, intrinsic-reward, reinforcement-learning, curiosity]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Random Network Distillation

Random Network Distillation (RND) 是一种为强化学习提供内在奖励(intrinsic reward)的探索方法:用一个随机初始化且固定的 target network 对状态进行编码,再训练一个 predictor network 去拟合该编码,以两者输出的预测误差作为衡量状态新颖度的探索奖励——状态越陌生,误差越大,奖励越高。

## 在本 wiki 中的出现

- [[2023-rlur-user-retention-short-video]]:该工作把短视频用户留存建模为无限时域的请求级 MDP,并提出 RLUR 用强化学习直接最小化累计回访时间。在这种长时域、回访信号稀疏的留存优化场景中,RND 可作为内在奖励/探索机制,缓解奖励稀疏带来的探索困难,帮助策略在 KuaiRand 上优于 TD3/CEM 并在 Kuaishou 全量上线提升留存与 DAU。(注:RND 在该论文中的具体使用方式以原文为准,此处仅就其作为探索方法的一般角色作链接。)
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF 用协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。在这类多智能体 RL 推荐场景中,RND 作为探索方法可缓解动作空间稀疏与样本选择偏差带来的探索不足。(注:RND 在该论文中的具体使用方式以原文为准,此处仅就其作为探索方法的一般角色作链接。)

## 相关

- [[intrinsic-reward]]
- [[exploration]]
- [[curiosity-driven-exploration]]
- [[reward-sparsity]]
- [[td3]]
- [[mdp]]
- [[2023-rlur-user-retention-short-video]]
