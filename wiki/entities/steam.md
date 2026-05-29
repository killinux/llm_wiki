---
type: entity
subtype: dataset
tags: [recommendation, dataset, llm-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Steam

Steam 是 Valve 的数字游戏分发平台,其用户与游戏交互数据常被用作推荐系统研究中的公开数据集。

## 在本 wiki 中的出现

- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。

## 相关

- [[interecagent]]
- [[billp]]
- [[recllama]]
- [[recommender-system]]
- [[llm-agent]]
