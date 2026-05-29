---
type: concept
subtype: method
tags: [self-attention, transformer, attention]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Self-Attention

自注意力是一种让序列中每个元素根据与其它元素的相关性(注意力分数)动态加权聚合信息的机制,是 Transformer 的核心计算单元。

## 在本 wiki 中的出现

- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。

## 相关

- [[transformer]]
- [[cross-domain-sequential-recommendation]]
- [[negative-transfer]]
- [[multi-objective-optimization]]
