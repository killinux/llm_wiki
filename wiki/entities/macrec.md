---
type: entity
subtype: product
tags: [multi-agent, recommendation, llm-agent, recsys, user-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# MACRec

MACRec 是清华大学提出的一个基于大语言模型的多 agent 协作推荐框架,通过角色各异的 LLM agent 直接协作完成多种推荐任务。

## 在本 wiki 中的出现

- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL(Agentic Feedback Loop),让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。

## 相关

- [[multi-agent-system]]
- [[llm-recommendation]]
- [[recommender-system]]
- [[llm-agent]]
- [[user-simulation]]
