---
type: entity
subtype: model
tags: [decision-transformer, offline-rl, sequence-modeling, transformer, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Decision Transformer

Decision Transformer 是一种将强化学习问题转化为序列建模任务的模型,通过 Transformer 架构以期望回报(return-to-go)、状态和动作的序列为条件自回归地生成动作,从而无需传统的值函数或策略梯度即可完成离线强化学习。

## 在本 wiki 中的出现

- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[offline-reinforcement-learning]]
- [[transformer]]
- [[sequence-modeling]]
- [[conservative-q-learning]]
- [[maximum-entropy-rl]]
- [[generative-recommendation]]
