---
type: concept
subtype: method
tags: [agent-based-modeling, simulation, multi-agent, social-simulation, emergence]
created: 2026-05-29
updated: 2026-05-29
sources: 12
---

# Agent-Based Modeling

Agent-Based Modeling(ABM,基于智能体的建模)是一种通过模拟大量自主智能体(agent)的局部行为与相互作用,来研究系统层面涌现现象的计算建模方法。

## 在本 wiki 中的出现

- [[2026-generative-social-simulation-validation]]:一篇系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。
- [[2024-limits-of-agency-in-agent-based-models]]:提出 LLM archetypes——为少数代表性 agent 类型查询 LLM 行为再概率采样到个体,从而在百万级 ABM 仿真(NYC 840 万人 COVID-19)中保持规模的同时引入 LLM 自适应行为。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2024-oasis-million-agent-social-simulation]]:通用、可扩展的 LLM-agent 社交媒体模拟器,在 X 与 Reddit 上模拟最多 100 万个 agent,复现信息传播、群体极化与从众效应,并发现规模越大群体动态越丰富、意见越多样有用。
- [[2025-agentsociety-large-scale-social-simulation]]:一个整合 LLM 生成式社会 agent、真实城市-社会-经济环境与大规模分布式仿真引擎的社会模拟器,支持上万 agent 并复现极化、谣言、UBI、飓风、城市可持续性五类真实社会实验。
- [[2025-socioverse-world-model-social-simulation]]:SocioVerse 是一个由 LLM agents 驱动、依托 1000 万真实用户池与四个对齐模块的社会模拟 world model,在政治、新闻、经济三大领域复现大规模人群行为。
- [[2025-emergent-llm-behaviors-data-leakage]]:批判性短文,指出 LLM 多智能体模拟中"自发涌现的社会约定"在观测上等价于 data leakage——模型只是复述预训练中已知的协调博弈知识,而非真正自组织。
- [[2025-mmoagent-economic-simulation-mmo]]:提出 MMOAgent,一个基于 LLM 的 Generative Agent-Based Modeling 框架,用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济,涌现出角色分化与符合供需规律的价格波动。
- [[2025-multi-actor-genai-as-game-engine]]:Google DeepMind 的立场/架构论文,主张用游戏引擎式的 Entity-Component 架构统一支撑 Evaluationist/Dramatist/Simulationist 三类多智能体生成式 AI 用户动机,以 Concordia v2 为实例。
- [[2025-generative-mmo-simulation]]:用 LLM 驱动的生成式多智能体 MMO 游戏仿真系统:在真实玩家数据上 SFT+GRPO 微调 agent,高保真模拟玩家决策,低成本评估数值系统与机制设计的干预效果。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。

## 相关

- [[emergence]]
- [[swarm-intelligence]]
- [[social-simulation]]
- [[generative-agents]]
- [[multi-agent-systems]]
