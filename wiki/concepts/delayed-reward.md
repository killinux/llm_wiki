---
type: concept
subtype: method
tags: [reinforcement-learning, reward-design, mdp, user-retention, credit-assignment]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Delayed Reward

Delayed Reward(延迟奖励)指智能体某一动作的真实回报并非即时显现,而是在若干步乃至更长时间之后才反馈,因而需要跨时间步进行信用分配(credit assignment)的强化学习场景。

## 在本 wiki 中的出现

- [[2023-rlur-user-retention-short-video]]:该工作将短视频用户留存建模为无限时域的请求级 MDP,核心难点正是 Delayed Reward——用户的回访/留存信号通常滞后于当前推荐动作,并跨越多个请求会话才体现。RLUR 用强化学习直接最小化累计回访时间,以应对这种长期、延迟的回报信号;在 KuaiRand 上优于 TD3/CEM,并在 Kuaishou 全量上线提升留存与 DAU。

## 相关

- [[reinforcement-learning]]
- [[markov-decision-process]]
- [[credit-assignment]]
- [[user-retention]]
- [[reward-shaping]]
- [[infinite-horizon-mdp]]
