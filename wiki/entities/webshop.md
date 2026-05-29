---
type: entity
subtype: benchmark
tags: [agent, web-agent, benchmark, e-commerce, interactive-environment]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# WebShop

WebShop 是一个模拟在线购物网站的交互式环境与基准,要求 agent 根据自然语言指令在网页中搜索、浏览并完成商品购买任务,用于评测语言 agent 的网页操作与决策能力。

## 在本 wiki 中的出现

- [[2023-agentbench]]:WebShop 作为该多维基准所横跨的 8 个交互环境之一(Web Shopping 网页类任务,指标 reward),用于在网页购物场景中评测 LLM-as-Agent 的能力,从而揭示商业与开源模型在 agent 任务上的差距。
- [[2023-expel]]:WebShop 被用作四个评测 benchmark 之一,验证 ExpeL 在不更新模型参数的前提下,通过从跨任务经验中抽取自然语言洞见并召回相似成功轨迹来提升 agent 的决策表现(WebShop 成功率 41%,优于 ReAct 35%、Act 34%)。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。
- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。

## 相关

- [[2023-agentbench]]
- [[2023-expel]]
- [[react|react-reasoning-and-acting]]
- [[alfworld]]
- [[hotpotqa]]
- [[web-agent]]
- [[llm-agents|llm-agent]]
- [[benchmark]]
