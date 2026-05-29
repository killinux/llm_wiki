---
type: entity
subtype: model
tags: [state-space-model, sequence-modeling, selective-mechanism, long-sequence]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Mamba

Mamba 是一种带选择机制(selective mechanism)的状态空间模型(State Space Model, SSM),在长序列建模中以接近线性的复杂度替代 Transformer 的注意力层,从而大幅降低训练与推理的时间和显存开销。

## 在本 wiki 中的出现

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。

## 相关

- [[state-space-model]]
- [[transformer]]
- [[sasrec]]
- [[lifelong-sequential-recommendation]]
