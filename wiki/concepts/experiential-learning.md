---
type: concept
subtype: method
tags: [experiential-learning, agent, in-context-learning, memory, self-improvement]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# 经验式学习

经验式学习(experiential learning)指 Agent 不依赖参数更新,而是从自身与环境交互积累的经验中提炼可复用的知识,并在后续决策中加以运用以持续提升表现的方法。

## 在本 wiki 中的出现

- [[2023-expel]]:在该工作中,经验式学习是核心机制。LLM Agent 不更新模型参数,而是从跨任务的经验中自主抽取自然语言形式的洞见(insights),并在面对新任务时召回相似的成功轨迹,从而提升决策表现。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。

## 相关

- [[in-context-learning]]
- [[llm-agent]]
- [[memory]]
- [[self-reflection]]
