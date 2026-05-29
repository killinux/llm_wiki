---
type: entity
subtype: dataset
tags: [recommendation, dataset, sequential-recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# ZhihuRec

ZhihuRec 是源自知乎平台的推荐系统数据集,常用于序列推荐(sequential recommendation)及曝光偏差(exposure bias)相关研究的评测。

## 在本 wiki 中的出现

- [[2025-caserec-counterfactual-augmentation-system-exposure]]:CaseRec 用 Decision Transformer 式 offline RL 建模完整 system exposure 序列,并通过 user simulator 驱动的反事实数据增强发掘未见用户兴趣,改进 sequential recommendation 并缓解 exposure bias。

## 相关

- [[sequential-recommendation]]
- [[exposure-bias]]
- [[offline-rl]]
- [[decision-transformer]]
