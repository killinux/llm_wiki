---
type: entity
subtype: product
tags: [llm-agent, recommender-system, conversational-recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# InteRecAgent

InteRecAgent 是一个交互式对话推荐 agent 框架,以 LLM 作为"大脑"、传统推荐模型作为"工具",构建能够理解用户意图并给出推荐的对话系统。

## 在本 wiki 中的出现

- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段,在用户意图模糊时兼顾追问效率与残余不确定性驱动的多样化推荐。

## 相关

- [[recllama]]
- [[llm-agents|llm-agent]]
- [[conversational-recommendation]]
- [[traditional-recommender-model]]
- [[llm-agents-for-recommender-systems]]
- [[simuser]]
