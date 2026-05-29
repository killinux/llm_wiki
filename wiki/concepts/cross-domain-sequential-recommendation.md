---
type: concept
subtype: method
tags: [recommendation, sequential-recommendation, cross-domain, transfer-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Cross-domain Sequential Recommendation

跨域序列推荐(Cross-domain Sequential Recommendation)旨在利用多个领域的用户行为序列,迁移有益的跨域知识以提升目标域的下一项预测效果,同时抑制 negative transfer。

## 在本 wiki 中的出现

- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。

## 相关

- [[sequential-recommendation]]
- [[transfer-learning]]
- [[self-attention]]
- [[negative-transfer]]
