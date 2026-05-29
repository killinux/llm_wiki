---
type: concept
subtype: method
tags: [GFlowNet, generative-model, reinforcement-learning, diversity, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# GFlowNet

GFlowNet(Generative Flow Network)是一类通过流匹配(flow matching)训练的生成模型,它把对象的生成过程建模为有向无环图上的流动,使得最终采样到某个对象的概率正比于该对象的奖励(reward),从而能够采样出多样化的高奖励解,而非只收敛到单一最优。

## 在本 wiki 中的出现

- [[2023-gflownet-listwise-recommendation]]:GFN4Rec 用 GFlowNet 流匹配让推荐列表的生成概率正比于其 list-wise 奖励,在保持高质量的同时显著提升列表多样性与在线探索能力。这里 GFlowNet 作为列表生成的核心方法,把推荐列表的构造视为序列化的生成过程,并以奖励为目标进行流匹配训练。

## 相关

- [[flow-matching]]
- [[reinforcement-learning]]
- [[list-wise-recommendation]]
- [[diversity]]
- [[online-exploration]]
