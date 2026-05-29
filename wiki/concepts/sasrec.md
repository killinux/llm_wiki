---
type: concept
subtype: method
tags: [recommendation, sequential-recommendation, self-attention, baseline]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# SASRec

SASRec(Self-Attentive Sequential Recommendation)是一种基于自注意力机制的序列推荐方法,通过对用户历史交互序列建模来预测下一个交互物品,常被用作序列/RL 推荐研究中的经典基线。

## 在本 wiki 中的出现

- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。

## 相关

- [[sequential-recommendation]]
- [[self-attention]]
- [[rl-recommendation]]
