---
type: entity
subtype: model
tags: [recommendation, sequential-recommendation, rnn, gru]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# GRU4Rec

GRU4Rec 是一种基于门控循环单元(GRU)的会话/序列推荐模型,通过 RNN 对用户的行为序列建模来预测下一个交互物品,是序列推荐领域的经典基线之一。

## 在本 wiki 中的出现

- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度 >=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。GRU4Rec 作为序列推荐的经典 RNN 基线在该工作所属领域被对照参考。

## 相关

- [[sasrec]]
- [[recmamba]]
- [[sequential-recommendation]]
- [[mamba]]
