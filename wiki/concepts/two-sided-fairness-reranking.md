---
type: concept
subtype: method
tags: [fairness, re-ranking, recommendation, two-sided-marketplace, exposure-allocation]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Two-sided fairness re-ranking

在双边推荐市场中,对推荐列表进行重排序的方法,旨在同时兼顾用户侧的推荐质量(准确性)与提供方侧的曝光公平性,平衡两类参与者的利益。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。
- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。

## 相关

- [[provider-fairness]]
- [[exposure-allocation]]
- [[talmud-rule]]
- [[online-learning]]
