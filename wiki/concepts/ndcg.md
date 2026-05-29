---
type: concept
subtype: method
tags: [ranking, evaluation, recommendation, information-retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# NDCG

NDCG(Normalized Discounted Cumulative Gain,归一化折损累计增益)是一种衡量排序列表质量的指标,通过对靠前位置赋予更高权重来累计相关性收益,并以理想排序进行归一化,常用于推荐系统与信息检索的排序效果评估。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。

## 相关

- [[recommendation-system]]
- [[information-retrieval]]
- [[ranking-metric]]
- [[two-sided-fairness]]
