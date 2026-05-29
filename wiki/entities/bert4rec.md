---
type: entity
subtype: model
tags: [recommendation, transformer, sequential-recommendation, bert]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# BERT4Rec

BERT4Rec 是一种用于序列推荐的模型,采用双向 Transformer 编码器,通过掩码物品预测(Cloze 任务)从用户历史行为中学习物品表示。

## 在本 wiki 中的出现

- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。

## 相关

- [[sequential-recommendation]]
- [[transformer]]
- [[decision-transformer]]
- [[generative-recommendation]]
