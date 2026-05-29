---
type: concept
subtype: method
tags: [fair-division, resource-allocation, game-theory, fairness, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Bankruptcy problem

破产问题是公平分配理论中的经典模型:当一份有限资源(如曝光、资金)不足以满足所有索取方的全部诉求时,如何在各方之间公平地分配该资源,代表性求解规则包括 Talmud rule。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。

## 相关

- [[talmud-rule]]
- [[provider-fairness]]
- [[two-sided-recommendation]]
- [[online-learning]]
