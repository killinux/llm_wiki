---
type: concept
subtype: method
tags: [decision-transformer, offline-rl, sequence-modeling, recommendation, transformer]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Decision Transformer

Decision Transformer 是一种把强化学习(尤其是离线 RL)重新表述为序列建模问题的方法:它用 Transformer 以自回归方式,基于历史的回报、状态与动作来生成后续动作,从而把策略学习转化为条件序列生成,并可通过指定目标回报来控制生成行为。

## 在本 wiki 中的出现

- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-caserec-counterfactual-augmentation-system-exposure]]:CaseRec 用 Decision Transformer 式 offline RL 建模完整 system exposure 序列,并通过 user simulator 驱动的反事实数据增强发掘未见用户兴趣,改进 sequential recommendation 并缓解 exposure bias。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[offline-reinforcement-learning]]
- [[sequence-modeling]]
- [[transformer]]
- [[sequential-recommendation]]
- [[generative-recommendation]]
