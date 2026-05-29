---
type: concept
subtype: method
tags: [fairness, exposure, recommendation, two-sided-market, bankruptcy-problem]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Minimum exposure guarantee

最低曝光保障(Minimum exposure guarantee)指在推荐或排序系统中,为各提供方(provider)/物品分配曝光时,确保每一方都能获得一个不低于约定下限的曝光量,以实现长期的提供方公平性。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。

## 相关

- [[provider-fairness]]
- [[exposure-fairness]]
- [[bankruptcy-problem]]
- [[talmud-rule]]
- [[two-sided-recommendation]]
