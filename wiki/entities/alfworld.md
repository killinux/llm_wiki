---
type: entity
subtype: benchmark
tags: [benchmark, embodied, interactive, agents, evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# ALFWorld

ALFWorld 是一个**文本化的交互式具身任务**基准:智能体在模拟家居环境中通过文本指令完成多步任务,常用于评测 LLM 智能体的交互式决策与规划能力。

## 在本 wiki 中的出现
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour,让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[reflexion]]
- [[scienceworld]]
- [[self-reflection]]
- [[llm-agents|llm-agent]]

- [[2023-reflexion]]:用作评测环境之一,验证用语言化的自我反思反馈(而非梯度更新)能否让 LLM 智能体从失败轨迹中迭代改进、提升任务成功率。
- [[2023-agentbench]]:作为系统评估 LLM-as-Agent 能力的多维基准所覆盖的交互环境之一,用于横向测评多个商业与开源模型在此类具身/交互任务上的表现。
- [[2023-autogen]]:作为该开源多 agent 框架的应用与示例场景之一,展示通过可定制、可对话 agent 间的会话编程来求解交互式任务。
- [[2023-expel]]:用作评测环境,验证 LLM Agent 在不更新参数的前提下,通过抽取跨任务自然语言洞见并召回相似成功轨迹来提升决策表现。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架,其中 ALFWorld 作为评测智能体记忆与多步决策能力的基准之一被涉及。

## 相关

- [[2023-reflexion]]
- [[2023-agentbench]]
- [[2023-autogen]]
- [[2023-expel]]
- [[react]]
- [[webshop]]
- [[textcraft]]
- [[llm-agents]]
- [[embodied-agent]]
- [[interactive-decision-making]]
