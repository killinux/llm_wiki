---
type: entity
subtype: benchmark
tags: [web-agent, benchmark, llm-agent, generalist-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Mind2Web

Mind2Web 是一个面向通用网页智能体(generalist web agent)的基准,用于评估模型在真实网站上根据自然语言指令完成跨领域、跨网站任务的能力。

## 在本 wiki 中的出现

- [[2023-agentbench]]:AgentBench 是首个系统评估 LLM-as-Agent 能力的多维基准,横跨 8 个交互环境测评 29 个模型,揭示了商业模型与开源模型之间的巨大差距。Mind2Web 作为面向网页交互场景的代表性基准在该工作中被提及。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。

## 相关

- [[web-agent]]
- [[llm-agent]]
- [[agentbench]]
- [[tool-use]]
