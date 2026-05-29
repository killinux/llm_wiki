---
type: concept
subtype: method
tags: [transformer, attention, deep-learning, neural-network]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Transformer

Transformer 是一种基于自注意力(self-attention)机制的神经网络架构,通过并行建模序列中元素之间的全局依赖关系,已成为现代大语言模型及众多深度学习任务的主流骨干结构。

## 在本 wiki 中的出现

- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化(作为 Transformer 注意力在序列推荐中的线性复杂度替代路线)。
- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图",并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能(为基于 Transformer 的生成式推荐提供可解释的 ID 表征)。

## 相关

- [[attention-mechanism]]
- [[graph-neural-network]]
- [[recommender-system]]
- [[large-language-model]]
- [[mamba]]
- [[decision-transformer]]
- [[sequential-recommendation]]
- [[generative-recommendation]]
- [[diffusion-model]]
- [[semantic-id]]
