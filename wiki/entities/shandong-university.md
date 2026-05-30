---
type: entity
subtype: lab
tags: [university, china, recommendation, sequence-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Shandong University

山东大学(Shandong University），中国高校,在本 wiki 中作为推荐系统与序列建模相关研究的参与机构出现。

## 在本 wiki 中的出现

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >= 2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。
- [[2025-caserec-counterfactual-augmentation-system-exposure]]:CaseRec 用 Decision Transformer 式 offline RL 建模完整 system exposure 序列,并通过 user simulator 驱动的反事实数据增强发掘未见用户兴趣,改进 sequential recommendation 并缓解 exposure bias。

## 相关

- [[mamba]]
- [[state-space-model]]
- [[sasrec]]
- [[sequential-recommendation|lifelong-sequential-recommendation]]
- [[sequential-recommendation]]
- [[offline-rl]]
- [[exposure-bias]]
- [[decision-transformer]]
