---
type: entity
subtype: dataset
tags: [recommendation, dataset, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Yelp

Yelp 是基于 Yelp 平台用户对商户的评论与评分构建的公开数据集,常用作推荐系统研究中的基准数据。

## 在本 wiki 中的出现

- 在 [[2023-data-heterogeneity-recommendation]] 中,Yelp 作为评估数据集之一。该工作提出双层聚类方法 BHE,显式挖掘推荐数据中的预测机制异质性与协变量分布异质性,用于多子模型预测与去偏;在 Yelp / MovieLens-1M 上以 NFM 为骨干,NDCG@20 从 14.01 提升到 22.57。
- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。

## 相关

- [[movielens-1m]]
- [[nfm]]
- [[recommendation-system]]
- [[bhe]]
- [[ndcg]]
