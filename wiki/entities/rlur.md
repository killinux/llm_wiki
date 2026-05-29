---
type: entity
subtype: model
tags: [reinforcement-learning, recommendation, user-retention, short-video, MDP]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# RLUR

RLUR(Reinforcement Learning for User Retention)是一种用强化学习直接优化短视频用户留存的推荐方法,目标是最小化用户的累计回访时间。

## 在本 wiki 中的出现

- 在 [[2023-rlur-user-retention-short-video]] 中作为核心方法提出:该工作把短视频用户留存建模为无限时域的请求级 MDP(infinite-horizon request-level MDP),并提出 RLUR 用强化学习直接最小化累计回访时间。实验中,RLUR 在 KuaiRand 数据集上优于 TD3 与 CEM 等基线,并在 Kuaishou 全量上线,带来用户留存与 DAU 的提升。

## 相关

- [[reinforcement-learning]]
- [[markov-decision-process]]
- [[user-retention]]
- [[short-video-recommendation]]
- [[td3]]
- [[cem]]
- [[kuairand]]
- [[kuaishou]]
