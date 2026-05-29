---
type: concept
subtype: method
tags: [fairness, bankruptcy-problem, resource-allocation, exposure-allocation, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Talmud rule

Talmud rule 是源自破产问题(bankruptcy problem)的经典资源分配方法,用于在可分配资源不足以满足所有索取方需求时,给出一种公平且满足若干公理性质的分配方案。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。

## 相关

- [[bankruptcy-problem]]
- [[provider-fairness]]
- [[exposure-allocation]]
- [[online-learning]]
- [[two-sided-recommendation]]
