---
type: concept
subtype: method
tags: [reinforcement-learning, recommendation, action-space, policy-learning, latent-representation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Latent Action Space

Latent Action Space 指在强化学习策略中,用一个低维、连续的隐空间(latent space)来表示原本规模巨大或组合爆炸的离散动作集合,从而让策略在该隐空间中进行决策、再映射回真实动作,以缓解大动作空间下的学习困难。

## 在本 wiki 中的出现

- [[2023-hyper-actor-critic-recommendation]]:该工作提出 Hyper-Actor Critic(HAC)框架,把推荐列表生成解耦为两步——先在 latent action space 中推断 hyper-action,再据此选择 effect-action(具体推荐项)。Latent action space 在这里承担了"压缩并连续化大动作空间"的角色,使得 actor 不必直接在庞大的物品集合上做决策;同时框架引入对齐(alignment)与监督模块,保证 hyper-action 与 effect-action 之间的一致性,从而稳定大动作空间下的 RL 推荐策略学习。

## 相关

- [[reinforcement-learning]]
- [[actor-critic]]
- [[candidate-generation]]
- [[closed-loop-feedback]]
- [[recommender-systems|recommendation-system]]
- [[latent-representation]]
- [[action-space]]
- [[policy-learning]]
