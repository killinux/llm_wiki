---
type: concept
subtype: method
tags: [transfer-learning, multi-task, cross-domain, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Negative Transfer

Negative Transfer(负迁移)指在多任务、多领域或迁移学习中,来自源任务/领域的知识不仅没有帮助目标任务,反而损害其性能的现象。

## 在本 wiki 中的出现

- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。

## 相关

- [[cross-domain-sequential-recommendation]]
- [[self-attention]]
- [[multi-objective-optimization]]
- [[transfer-learning]]
