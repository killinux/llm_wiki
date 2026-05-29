---
type: concept
subtype: method
tags: [reflection, prompting, llm, reasoning, self-improvement]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Reflection

Reflection 是指让 LLM 回顾自身或他人过往的推理 / 行动经验,从中总结教训或指导原则,并反馈到后续决策中以提升表现的一类方法。

## 在本 wiki 中的出现

- [[2024-reflection-on-search-trees]]:RoT 让 strong LLM 反思 weak LLM 的历史树搜索经验、对关键状态总结出任务级 guideline 注入后续 prompt,显著提升 BFS/MCTS 等树搜索 prompting 在 Blocksworld、GSM8k、议价任务上的准确率与搜索效率,且任务越难收益越大。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-rethinkmcts]]:一个面向代码生成的思路搜索框架,用 MCTS 探索写代码的推理过程,并通过 rethink 机制利用块级代码执行反馈直接精炼搜索树中的错误思路。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour:让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[2025-llm-multi-agent-autonomous-driving-survey]]:系统综述 LLM 驱动的多智能体自动驾驶系统,按智能体交互模式与结构分类已有方法,并梳理 agent-human 交互、应用、数据集与未来方向。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent,一个基于 LLM 的 Generative Agent-Based Modeling 框架,用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济,涌现出角色分化与符合供需规律的价格波动。
- [[2025-multi-actor-genai-as-game-engine]]:Google DeepMind 的立场/架构论文,主张用游戏引擎式的 Entity-Component 架构统一支撑 Evaluationist/Dramatist/Simulationist 三类多智能体生成式 AI 用户动机,以 Concordia v2 为实例。

## 相关

- [[tree-search]]
- [[prompting]]
- [[self-improvement]]
