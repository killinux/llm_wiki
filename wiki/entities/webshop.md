---
type: entity
subtype: benchmark
tags: [agent, web-agent, benchmark, e-commerce, interactive-environment]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# WebShop

WebShop 是一个模拟在线购物网站的交互式环境与基准,要求 agent 根据自然语言指令在网页中搜索、浏览并完成商品购买任务,用于评测语言 agent 的网页操作与决策能力。

## 在本 wiki 中的出现

- [[2023-agentbench]]:WebShop 作为该多维基准所横跨的 8 个交互环境之一(Web Shopping 网页类任务,指标 reward),用于在网页购物场景中评测 LLM-as-Agent 的能力,从而揭示商业与开源模型在 agent 任务上的差距。
- [[2023-expel]]:WebShop 被用作四个评测 benchmark 之一,验证 ExpeL 在不更新模型参数的前提下,通过从跨任务经验中抽取自然语言洞见并召回相似成功轨迹来提升 agent 的决策表现(WebShop 成功率 41%,优于 ReAct 35%、Act 34%)。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。

## 相关

- [[2023-agentbench]]
- [[2023-expel]]
- [[react-reasoning-and-acting]]
- [[alfworld]]
- [[hotpotqa]]
- [[web-agent]]
- [[llm-agent]]
- [[benchmark]]
