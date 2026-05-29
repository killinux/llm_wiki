---
type: entity
subtype: dataset
tags: [recommendation, dataset, ctr, multi-task]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# RetailRocket

RetailRocket 是一个来自电商平台的公开推荐系统数据集,包含用户的浏览、加购、购买等行为日志,常用于点击率(CTR)与转化率等多任务推荐建模的评测。

## 在本 wiki 中的出现

- [[2023-multi-task-recommendations-with-rl]]:作为评测数据集之一。RMTL 用 actor-critic 强化学习按 session 级序列动态生成多任务损失权重,替代固定常数加权,在 RetailRocket 与 Kuairand 上提升 CTR/CTCVR 的 AUC。
- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。

## 相关

- [[kuairand]]
- [[ctr]]
- [[ctcvr]]
- [[multi-task-learning]]
- [[rmtl]]
- [[merrec]]
- [[mercari]]
- [[gtrs]]
- [[transformer]]
- [[graph-recommendation]]
