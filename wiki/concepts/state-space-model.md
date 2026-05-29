---
type: concept
subtype: method
tags: [state-space-model, mamba, sequence-modeling, long-sequence]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# State Space Model

状态空间模型(State Space Model, SSM)是一类用状态转移方程对序列建模的方法,以接近线性的时间复杂度处理长序列,其带选择机制的变体 Mamba 可作为 Transformer 的替代来高效建模超长序列。

## 在本 wiki 中的出现

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。

## 相关

- [[mamba]]
- [[transformer]]
- [[lifelong-sequential-recommendation]]
- [[sasrec]]
