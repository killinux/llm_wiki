---
type: entity
subtype: model
tags: [llm-agent, in-context-learning, experiential-learning, memory, no-finetuning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# ExpeL

ExpeL(Experiential Learning agent)是一种不更新模型参数的 LLM Agent,它通过从一批训练任务的跨任务经验中自主抽取自然语言洞见,并在推理时召回相似的成功轨迹,从而提升决策表现。

## 在本 wiki 中的出现
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[reflexion]]
- [[in-context-learning]]
- [[llm-agents|llm-agent]]
- [[autoguide]]

- [[2023-expel]]:提出 ExpeL 的论文。让 LLM Agent 不更新参数,从跨任务经验中自主抽取自然语言洞见(insights)并召回相似成功轨迹来辅助决策,实现无需微调的经验式学习。
- [[2026-experiential-reflective-learning]]:介绍经验式反思学习(ERL),agent 反思单次任务轨迹与成败信号、提炼可迁移启发式存入持久经验池,新任务时按相关性检索 top-k 注入上下文,从而无需更新参数即可自我改进;在 Gaia2 上比 ReAct 基线提升 7.8% 成功率。

## 相关

- [[in-context-learning]]:ExpeL 依赖在上下文中注入经验与洞见,而非梯度更新。
- [[llm-agents|llm-agent]]:ExpeL 属于 LLM Agent 范式。
- [[memory-augmented-agent]]:通过召回历史成功轨迹作为记忆来增强决策。
- [[reflexion]]:同样通过自然语言反思/经验改进 Agent 表现的相关方法。
- [[experiential-reflective-learning]]:与 ExpeL 同源的经验式反思学习方法。
