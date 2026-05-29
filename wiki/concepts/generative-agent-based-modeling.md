---
type: concept
subtype: method
tags: [generative-agent-based-modeling, social-simulation, llm-agents, agent-based-models, emergent-behavior, human-behavior-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# 生成式基于智能体的建模 (Generative Agent-Based Modeling / Generative ABM)

用 LLM 充当每个 agent 的"认知引擎"来扩展传统 agent-based modeling (ABM) 的建模范式：agent 不再由手工规则驱动，而是凭借记忆、反思、规划等机制生成可信的、开放域的类人行为，从而在群体层面涌现出社会现象。

## 概述

传统 ABM 用简单规则刻画 agent，难以覆盖真实人类行为的丰富度。Generative ABM 把 LLM 引入 agent 的决策回路，使个体具备自然语言驱动的记忆、反思与规划能力，进而在大规模交互中复现信息传播、群体极化、谣言扩散等社会规律。该范式被广泛用于"硅基社会"实验、推荐/社交媒体用户模拟、城市活动模拟与交互式叙事，但同时面临计算成本、可控性、可解释性以及与真实人口对齐等核心挑战。

## 在本 wiki 中的出现

- [[2023-generative-agents]]：提出 generative agent 架构(memory stream / retrieval / reflection / planning)，在 Smallville 沙盒中涌现社会行为，是该范式的奠基与起点。
- [[2025-agentsociety-large-scale-social-simulation]]：把带情绪、需求、认知的 generative agents 嵌入真实城市与社会制度，扩展到 10,000+ agent、500 万次交互，代表大规模社会模拟方向。
- [[2024-oasis-million-agent-social-simulation]]：将该范式推向百万级 agent 的社交媒体模拟，复现信息扩散曲线与回音室效应，代表超大规模方向。
- [[2025-socioverse-world-model-social-simulation]]：以"世界模型"框架用千万级真实用户数据从环境、用户、行为、交互四个维度对齐 agent 群体，强调模拟与真实人口的对齐。
- [[2025-can-llm-agents-simulate-human-behavior]]：从评测与方法论角度批判性审视该范式，指出群体层面可复现部分规律但个体层面仍与真实人类有显著差距。
- [[2024-limits-of-agency-in-agent-based-models]]：直接提出 generative ABM 概念并讨论其能力边界，建议在关键节点用 LLM、其余用规则的混合方法。
- [[2023-recagent-user-behavior-simulation]]：用 LLM-based generative agents 模拟推荐场景下的用户行为，将该范式落地为推荐系统的"虚拟用户"实验环境。
- [[2024-opencity-urban-llm-agents]]：用 LLM agents 模拟居民出行与活动安排，把该范式应用于可扩展的城市活动模拟与政策研究。
- [[2025-multi-actor-genai-as-game-engine]]：把多个 generative agents 当作"游戏引擎"，由 LLM 实时生成多角色叙事与世界状态，将该范式延伸到交互式故事与游戏。

## 相关

- [[agent-based-modeling]]
- [[generative-agents]]
- [[social-simulation]]
- [[human-behavior-simulation]]
- [[user-simulation]]
- [[computational-social-science]]
- [[emergent-abilities]]
- [[llm-multi-agent]]
- [[multi-agent-collaboration]]
- [[memory-stream]]
- [[large-language-models]]
- [[ai-safety]]
- [[national-university-of-singapore]]
- [[university-of-science-and-technology-of-china]]
