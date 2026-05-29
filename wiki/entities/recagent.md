---
type: entity
subtype: product
tags: [LLM-agent, recommender-system, user-simulation, social-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# RecAgent

RecAgent 是一个基于 LLM-based agent 的用户行为模拟器,在沙盒环境中近乎零样本地模拟用户的推荐与社交行为。

## 在本 wiki 中的出现
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent,一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户的多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强。
- [[llm-agent]]
- [[user-simulation]]
- [[recommender-system]]
- [[ab-testing]]
- [[multimodal-llm]]
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[llm-agents|llm-agent]]
- [[collaborative-filtering]]
- [[recommender-systems|recommendation-system]]

- [[2023-recagent-user-behavior-simulation]]:提出 RecAgent,用 LLM-based agent 在沙盒中近乎零样本地模拟用户的推荐与社交行为,并以此研究信息茧房与从众现象。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2024-lmagent-multimodal-agents-society]]:基于多模态 LLM 的万级规模 agents 社会,在电商场景模拟多用户的购物、社交、直播行为,复现真实 co-purchase 模式与从众等 emergent behavior。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。

## 相关

- [[llm-based-agent]]
- [[user-behavior-simulation]]
- [[recommender-systems|recommender-system]]
- [[information-cocoon]]
- [[conformity]]
