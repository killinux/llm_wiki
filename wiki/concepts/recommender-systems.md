---
type: concept
subtype: method
tags: [recommender-systems, recommendation, debiasing, causal-inference, ranking]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Recommender Systems

Recommender Systems(推荐系统)是一类根据用户历史行为、特征与上下文,从海量候选物品中预测用户偏好并排序推荐的方法体系,广泛用于内容流、电商与视频平台。

## 在本 wiki 中的出现

- [[2022-kuairand]]:作为**数据集贡献**。快手发布的无偏序列推荐数据集,通过在推荐流中随机插入视频收集百万级无偏交互(含 12 种反馈信号、完整用户/物品 ID 与特征),为推荐系统的去偏与离线评估研究提供数据基础。
- [[2023-causal-inference-for-recommendation]]:作为**综述主题**。系统梳理如何将因果推断引入推荐系统,涵盖因果记号/假设/效应/估计方法,以及推荐系统中可解释性、公平性、鲁棒性、uplift、无偏性等实际问题。
- [[2023-idcf-debiasing-recommendation]]:作为**去偏方法的应用场景**。提出 iDCF,借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证,在 Coat/Yahoo!R3/KuaiRand 上优于现有去混杂方法。
- [[2023-data-heterogeneity-recommendation]]:作为**预测与去偏对象**。提出双层聚类方法 BHE 显式挖掘推荐数据中的预测机制异质性与协变量分布异质性,用于多子模型预测与去偏,在 Yelp/MovieLens-1M 上 NFM 骨干 NDCG@20 从 14.01 提升到 22.57。

## 相关

- [[debiasing]]
- [[causal-inference]]
- [[proximal-causal-inference]]
- [[unobserved-confounding]]
- [[counterfactual-inference]]
- [[sequential-recommendation]]
- [[offline-evaluation]]
- [[ndcg]]
- [[data-heterogeneity]]
- [[uplift-modeling]]
