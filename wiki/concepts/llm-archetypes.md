---
type: concept
subtype: method
tags: [llm, agent-based-model, simulation, sampling, scalability]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LLM archetypes

一种在大规模 agent-based model(ABM)中引入 LLM 自适应行为的方法:只为少数有代表性的 agent 类型(archetypes)查询 LLM 行为,再将查询结果概率采样到个体身上,从而在保持百万级仿真规模的同时让 agent 表现出 LLM 驱动的行为。

## 在本 wiki 中的出现

- [[2024-limits-of-agency-in-agent-based-models]]:提出 LLM archetypes——为少数代表性 agent 类型查询 LLM 行为再概率采样到个体,从而在百万级 ABM 仿真(NYC 840 万人 COVID-19)中保持规模的同时引入 LLM 自适应行为。

## 相关

- [[agent-based-model]]
- [[llm-agents|llm-agent]]
- [[probabilistic-sampling]]
