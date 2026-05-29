---
type: concept
subtype: method
tags: [optimization, constrained-optimization, online-learning, fairness]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Lagrangian relaxation

拉格朗日松弛是一种约束优化方法,通过把难处理的约束以拉格朗日乘子的形式并入目标函数,将带约束问题转化为更易求解的松弛问题,从而在目标与约束之间进行权衡求解。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。

## 相关

- [[two-sided-fairness]]
- [[online-learning]]
- [[exposure-allocation]]
- [[bankruptcy-problem]]
