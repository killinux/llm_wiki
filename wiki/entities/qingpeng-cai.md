---
type: entity
subtype: person
tags: [reinforcement-learning, recommender-systems, short-video, user-retention]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Qingpeng Cai

Qingpeng Cai 是一位从事强化学习与推荐系统研究的研究者,工作涉及将强化学习应用于短视频平台的用户留存优化。

## 在本 wiki 中的出现

- 在 [[2023-rlur-user-retention-short-video]] 中,作为作者参与该工作:将短视频用户留存建模为无限时域请求级 MDP,提出 RLUR 用强化学习直接最小化累计回访时间,在 KuaiRand 上优于 TD3/CEM,并在 Kuaishou 全量上线提升留存与 DAU。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。

## 相关

- [[rlur]]
- [[reinforcement-learning]]
- [[recommender-systems|recommender-system]]
- [[user-retention]]
- [[markov-decision-process]]
- [[kuaishou]]
- [[kuairand]]
- [[user-simulator]]
- [[request-level-recommendation]]
- [[value-function-decomposition]]
- [[temporal-difference-learning]]
