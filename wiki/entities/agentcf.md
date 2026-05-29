---
type: entity
subtype: product
tags: [llm-agent, recommendation, collaborative-filtering, multi-agent, user-simulation, agentic-feedback]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# AgentCF

AgentCF 是一种基于 LLM agent 的协同过滤推荐方法,将用户和物品都建模为可交互、可优化的 agent,通过模拟用户-物品之间的交互来学习偏好表示并完成推荐。

## 在本 wiki 中的出现
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。
- [[llm-agents|llm-agent]]
- [[recommender-systems|recommendation-system]]
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[llm-based-recommendation]]
- [[agent-memory]]
- [[cross-domain-recommendation]]

- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL(Agentic Feedback Loop),让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。

## 相关

- [[macrec]]
- [[llm-recommendation]]
- [[collaborative-filtering]]
- [[llm-agents|llm-agent]]
- [[agentic-feedback-loop]]
- [[user-simulation]]
- [[recommender-systems]]
