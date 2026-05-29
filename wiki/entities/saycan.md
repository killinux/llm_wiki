---
type: entity
subtype: benchmark
tags: [robotics, embodied-reasoning, grounding, llm-planning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# SayCan

SayCan 是一种将 LLM 的语义知识("say",大模型判断哪些动作对完成指令有用)与机器人可执行性的价值函数("can",判断哪些动作在当前环境下可行)相结合,从而把自然语言指令落地为机器人可执行技能序列的具身规划方法。

## 在本 wiki 中的出现

- [[2022-inner-monologue]]:在该工作中作为机器人具身推理的相关背景/对照。Inner Monologue 通过持续注入自然语言环境反馈,让 frozen LLM 形成"内心独白",实现闭环、可重规划的具身推理;SayCan 代表了用 LLM 进行机器人技能落地与规划的思路。
- [[2022-chain-of-thought]]:作为以 LLM 进行规划/推理的相关研究背景出现。该论文提出 chain-of-thought prompting,在 few-shot 示例中加入中间推理步骤,显著提升大模型的多步推理能力,且该增益随模型规模涌现(PaLM 540B 在 GSM8K 达 57%)。

## 相关

- [[inner-monologue]]
- [[chain-of-thought]]
- [[llm-planning]]
- [[embodied-reasoning]]
- [[affordance]]
- [[palm]]
