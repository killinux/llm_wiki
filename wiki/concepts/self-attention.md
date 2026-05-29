---
type: concept
subtype: method
tags: [self-attention, transformer, attention]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Self-Attention

自注意力是一种让序列中每个元素根据与其它元素的相关性(注意力分数)动态加权聚合信息的机制,是 Transformer 的核心计算单元。

## 在本 wiki 中的出现

- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。

## 相关

- [[transformer]]
- [[cross-domain-sequential-recommendation]]
- [[negative-transfer]]
- [[multi-objective-optimization]]
