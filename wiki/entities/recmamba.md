---
type: entity
subtype: model
tags: [recommendation, sequential-recommendation, mamba, state-space-model, lifelong-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# RecMamba

RecMamba 是一种用于终身序列推荐的模型,它用带选择机制的状态空间模型 Mamba 替换 Transformer 层,以高效建模超长的用户行为序列。

## 在本 wiki 中的出现

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。

## 相关

- [[mamba]]
- [[state-space-model]]
- [[sasrec]]
- [[sequential-recommendation]]
- [[transformer]]
