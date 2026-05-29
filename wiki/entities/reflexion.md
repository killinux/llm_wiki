---
type: entity
subtype: model
tags: [llm-agent, self-reflection, reinforcement-learning, decision-making]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Reflexion

Reflexion 是一种让 LLM Agent 通过对自身行为产生的反馈进行语言化反思(self-reflection)、并将反思结果存入记忆以改进后续决策的框架,无需更新模型参数。

## 在本 wiki 中的出现

- [[2023-expel]]:作为对比与思想来源出现。ExpeL 沿用了"不更新参数、依靠自然语言经验改进 Agent"的思路,让 LLM Agent 从跨任务经验中自主抽取自然语言洞见(insights),并召回相似的成功轨迹来提升决策表现。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour,让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。

## 相关

- [[react]]
- [[llm-agent]]
- [[2023-expel]]
- [[in-context-learning]]
- [[self-reflection]]
- [[sweet-and-sour]]
- [[scienceworld]]
