---
type: concept
subtype: method
tags: [recommendation, exposure-bias, sequential-recommendation, offline-rl, counterfactual]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# System exposure

System exposure 指推荐系统实际向用户展示(曝光)过的物品集合及其序列,是连接系统决策与用户反馈的中间环节;由于用户只能对被曝光的物品作出反应,曝光过程会引入 exposure bias,影响模型训练与评估。

## 在本 wiki 中的出现

- [[2025-caserec-counterfactual-augmentation-system-exposure]]:CaseRec 用 Decision Transformer 式 offline RL 建模完整 system exposure 序列,并通过 user simulator 驱动的反事实数据增强发掘未见用户兴趣,改进 sequential recommendation 并缓解 exposure bias。

## 相关

- [[exposure-bias]]
- [[sequential-recommendation]]
- [[offline-rl]]
- [[decision-transformer]]
- [[counterfactual-data-augmentation]]
- [[user-simulator]]
