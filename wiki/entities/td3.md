---
type: entity
subtype: model
tags: [reinforcement-learning, actor-critic, off-policy, baseline]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# TD3

TD3(Twin Delayed Deep Deterministic policy gradient)是一种面向连续动作空间的 off-policy actor-critic 强化学习算法,通过双 Q 网络、延迟策略更新和目标策略平滑来缓解 DDPG 的价值高估问题。

## 在本 wiki 中的出现

- [[2023-rlur-user-retention-short-video]]:作为对比基线(baseline)出现。该工作将短视频用户留存建模为无限时域请求级 MDP,提出 RLUR 用强化学习直接最小化累计回访时间;在 KuaiRand 数据集上,RLUR 的表现优于 TD3 与 CEM,并在 Kuaishou 全量上线后提升了留存与 DAU。
- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。

## 相关

- [[ddpg]]
- [[reinforcement-learning]]
- [[actor-critic]]
- [[cem]]
- [[multi-agent-rl]]
- [[2023-rlur-user-retention-short-video]]
