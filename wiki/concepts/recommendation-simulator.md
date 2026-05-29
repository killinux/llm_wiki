---
type: concept
subtype: method
tags: [recommendation, simulation, llm-agent, user-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# recommendation simulator

推荐模拟器是用模拟用户(常由 LLM 驱动的生成式 agent 充当)在推荐系统中产生交互行为的方法,用于在无需真实用户的情况下评估推荐策略、复现用户行为模式并研究系统级现象(如 filter bubble、popularity bias)。

## 在本 wiki 中的出现

- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。

## 相关

- [[generative-agent]]
- [[llm-agent]]
- [[filter-bubble]]
- [[popularity-bias]]
- [[user-simulation]]
