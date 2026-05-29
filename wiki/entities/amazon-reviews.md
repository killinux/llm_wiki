---
type: entity
subtype: dataset
tags: [recommendation, dataset, product-reviews]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Amazon Reviews

源自 Amazon 电商平台的商品评论与评分数据集,包含用户对商品的评价、评分及相关元数据,是推荐系统研究中常用的公开基准之一。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:作为多任务深度推荐系统(MTDRS)综述中梳理的常用评测数据集之一。
- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。

## 相关

- [[recommendation-system]]
- [[multi-task-learning]]
- [[movielens]]
- [[collaborative-filtering]]
- [[sequential-recommendation]]
- [[conversational-recommendation]]
- [[llm-agent]]
- [[graph-based-recommendation]]
- [[merrec-dataset]]
