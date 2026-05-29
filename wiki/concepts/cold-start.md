---
type: concept
subtype: method
tags: [cold-start, recommendation, user-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# cold start

冷启动(cold start)指推荐系统在缺乏新用户或新物品历史交互数据时,难以做出准确推荐的场景与挑战。

## 在本 wiki 中的出现

- [[2024-lusifer-llm-user-simulation]]:提出 Lusifer:基于 LLM 的用户模拟环境,在每次交互后增量更新可解释的用户画像,为 RL-based 推荐系统生成动态真实的用户反馈,并在 cold-start 场景超越传统协同过滤基线。
- [[2024-online-item-cold-start-popularity-aware-meta-learning]]:提出 PAM,一种按物品热度固定切分 meta-learning 任务的 model-agnostic 框架,在流式在线推荐中解决新物品冷启动并缓解马太效应。
- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。
- [[2024-prompt-tuning-item-cold-start]]:PROMO 用高价值正反馈(pinnacle feedback)替代内容描述作 prompt,并为每个 item 构造个性化 prompt network,同时缓解 item cold-start 推荐的数据成本与热门偏置,已在快手十亿用户级平台部署。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。

## 相关

- [[cold-start-recommendation]]
- [[user-simulation]]
- [[collaborative-filtering]]
- [[recommender-systems|recommendation-system]]
