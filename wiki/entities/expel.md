---
type: entity
subtype: model
tags: [llm-agent, in-context-learning, experiential-learning, memory, no-finetuning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# ExpeL

ExpeL(Experiential Learning agent)是一种不更新模型参数的 LLM Agent,它通过从一批训练任务的跨任务经验中自主抽取自然语言洞见,并在推理时召回相似的成功轨迹,从而提升决策表现。

## 在本 wiki 中的出现

- [[2023-expel]]:提出 ExpeL 的论文。让 LLM Agent 不更新参数,从跨任务经验中自主抽取自然语言洞见(insights)并召回相似成功轨迹来辅助决策,实现无需微调的经验式学习。

## 相关

- [[in-context-learning]]:ExpeL 依赖在上下文中注入经验与洞见,而非梯度更新。
- [[llm-agent]]:ExpeL 属于 LLM Agent 范式。
- [[memory-augmented-agent]]:通过召回历史成功轨迹作为记忆来增强决策。
- [[reflexion]]:同样通过自然语言反思/经验改进 Agent 表现的相关方法。
