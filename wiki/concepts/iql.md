---
type: concept
subtype: method
tags: [offline-rl, reinforcement-learning, value-learning, q-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# IQL

IQL(Implicit Q-Learning,隐式 Q 学习)是一种离线强化学习算法,通过期望回归(expectile regression)在不显式查询分布外动作的前提下逼近最优值函数,从而缓解离线 RL 中的分布外动作高估问题。

## 在本 wiki 中的出现

- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[offline-rl]]
- [[decision-transformer]]
- [[q-learning]]
- [[expectile-regression]]
