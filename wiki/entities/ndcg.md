---
type: entity
subtype: benchmark
tags: [ranking-metric, recommendation, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# NDCG

NDCG(Normalized Discounted Cumulative Gain,归一化折损累积增益)是一种排序质量评估指标,通过对排序结果中相关项的位置进行折损加权并归一化,衡量推荐或检索系统给出的排序列表与理想排序的接近程度。

## 在本 wiki 中的出现

- [[2025-fine-grained-skip-micro-video-recommendation]]:将 micro-video 中的 skip 行为细分为 highly positive、less positive、negative 三类,用双层图与分层 BPR ranking loss 建模,在 MVA 与 KuaiRand-Pure 的八项指标上超越 FRAME/LightGT/BM3。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。

## 相关

- [[recommendation-system]]
- [[bpr-loss]]
- [[generative-recommendation]]
- [[recall]]
