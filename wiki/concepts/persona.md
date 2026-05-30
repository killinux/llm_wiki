---
type: concept
subtype: method
tags: [persona, user-simulation, agent, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Persona

Persona 指为 LLM agent 赋予的一组角色画像(如偏好、属性、行为倾向),用于约束和引导其在模拟或交互中的表现,使其行为更贴近特定用户或人物。

## 在本 wiki 中的出现

- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。
- [[2026-graphrag-irl]]:GraphRAG-IRL 把 graph-grounded 特征、Maximum Entropy 逆强化学习预排序与 persona-guided LLM 重排融合,LLM 只对 IRL 短候选列表做语义重排,在 MovieLens/KuaiRand 上 NDCG@10 比监督基线提升 15.7%/16.6%。

## 相关

- [[user-simulation]]
- [[llm-agents|llm-agent]]
- [[agent-memory|memory]]
- [[recommender-system-evaluation]]
