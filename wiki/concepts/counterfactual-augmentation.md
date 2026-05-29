---
type: concept
subtype: method
tags: [counterfactual-augmentation, data-augmentation, offline-rl, sequential-recommendation, exposure-bias, user-simulator]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Counterfactual augmentation

反事实数据增强(counterfactual augmentation)是一种通过构造"如果当时呈现的是另一组内容会怎样"的反事实样本来扩充训练数据的方法,用以发掘观测数据中未出现的交互可能、缓解偏差并提升模型泛化能力。

## 在本 wiki 中的出现

- [[2025-caserec-counterfactual-augmentation-system-exposure]]:CaseRec 用 Decision Transformer 式 offline RL 建模完整 system exposure 序列,并通过 user simulator 驱动的反事实数据增强发掘未见用户兴趣,改进 sequential recommendation 并缓解 exposure bias。

## 相关

- [[offline-reinforcement-learning]]
- [[decision-transformer]]
- [[sequential-recommendation]]
- [[exposure-bias]]
- [[user-simulator]]
- [[data-augmentation]]
