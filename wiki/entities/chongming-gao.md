---
type: entity
subtype: person
tags: [recommendation, llm-agent, reinforcement-learning, planning]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Chongming Gao

Chongming Gao 是一位从事推荐系统与大语言模型相关研究的研究者,工作涉及将 LLM 的规划能力用于长期推荐任务。

## 在本 wiki 中的出现

- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。

## 相关

- [[billp]]
- [[long-term-recommendation]]
- [[llm-agents|llm-agent]]
- [[trirec]]
