---
type: entity
subtype: model
tags: [offline-rl, conservative, value-function, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# CQL

CQL(Conservative Q-Learning)是一种 offline RL 算法,通过在训练中对 Q 值施加保守性约束(对数据分布外的动作压低估计的 Q 值),缓解纯离线设置下的价值高估问题。

## 在本 wiki 中的出现

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:该论文提出 DORL,在 model-based offline RL 的悲观惩罚(pessimistic penalty)上叠加熵惩罚(entropy penalty)以缓解推荐中的马太效应(Matthew effect),从而提升交互式推荐的用户长期满意度。CQL 作为这一研究脉络中代表保守性思想的 offline RL 方法之一出现于该工作的相关讨论中。

## 相关

- [[mopo]]:同属 offline RL,基于悲观性思想,与 DORL 中的悲观惩罚一脉相承
- [[td3]]:常作为 offline/online RL 中的 actor-critic 基础算法
- [[dorl]]:在悲观惩罚基础上加入熵惩罚的推荐 offline RL 方法
- [[offline-rl]]
- [[conservatism]]
- [[matthew-effect]]
