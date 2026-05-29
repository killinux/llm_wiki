---
type: concept
subtype: method
tags: [emergent-abilities, scaling, reasoning, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Emergent Abilities

Emergent Abilities 指某些能力在小模型上几乎不存在,但当模型规模(参数量、训练计算量等)跨过某个阈值后突然显现并快速提升的现象。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:该论文提出 chain-of-thought prompting,即在 few-shot 示例中加入中间推理步骤。其多步推理能力的增益被观察为随模型规模涌现——只有足够大的模型才能从中获益,而小模型几乎无提升。例如 PaLM 540B 在 GSM8K 上达到 57%。在此论文中,Emergent Abilities 作为解释 chain-of-thought 为何依赖大规模模型的核心视角出现。
- [[2025-llm-multi-agent-swarm-intelligence]]:把 agent-based modeling 中 agent 的硬编码程序替换为 GPT-4o 驱动的 prompt,在蚁群觅食与鸟群 flocking 两个经典 swarm intelligence 场景中复现并诱导涌现集体行为。
- [[2024-oasis-million-agent-social-simulation]]:通用、可扩展的 LLM-agent 社交媒体模拟器,在 X 与 Reddit 上模拟最多 100 万个 agent,复现信息传播、群体极化与从众效应,并发现规模越大群体动态越丰富、意见越多样有用。
- [[2025-emergent-llm-behaviors-data-leakage]]:批判性短文,指出 LLM 多智能体模拟中"自发涌现的社会约定"在观测上等价于 data leakage——模型只是复述预训练中已知的协调博弈知识,而非真正自组织。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论"——固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强时才成立(存在能力门槛),体现了协调收益对模型能力的涌现式依赖。

## 相关

- [[2022-chain-of-thought]]
- [[chain-of-thought|chain-of-thought-prompting]]
- [[scaling-laws]]
- [[few-shot-prompting]]
- [[palm]]
- [[gsm8k]]
- [[multi-agent-systems]]
- [[swarm-intelligence]]
- [[social-simulation]]
- [[data-leakage]]
