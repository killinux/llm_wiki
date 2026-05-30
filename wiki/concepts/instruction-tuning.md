---
type: concept
subtype: method
tags: [instruction-tuning, alignment, fine-tuning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Instruction Tuning

Instruction Tuning 指在带有自然语言指令(及其期望输出)的数据上对预训练语言模型进行微调,使模型学会遵循人类指令、按要求完成任务的方法。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:InstructGPT 是 Instruction Tuning 的代表性实践。它采用 RLHF 流程(SFT → 训练奖励模型 → PPO 强化学习)对齐 GPT-3,使得 1.3B 参数的模型在人类偏好评估中胜过 175B 的 GPT-3,同时输出更真实、毒性更低。其中第一步的 SFT(supervised fine-tuning)正是基于人工编写的指令-回答数据进行的 Instruction Tuning。

- [[2023-camel-communicative-agents]]:CAMEL 关注 Instruction Tuning 的数据来源问题。它通过角色扮演与 inception prompting,让两个 LLM 智能体(AI User 与 AI Assistant)在最少人工干预下自主协作完成任务,从而自动、规模化地生成指令/对话数据,可用于后续的 Instruction Tuning。

- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。

- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。

- [[2025-opencharacter-role-playing-synthetic-personas]]:用 Persona Hub 大规模合成 persona 造角色对齐 SFT 数据,微调 LLaMA-3 8B 获得 out-of-domain 角色泛化能力,在 PersonaGym 上比肩 GPT-4o。

- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。

## 相关

- [[rlhf]]
- [[supervised-fine-tuning]]
- [[2022-instructgpt]]
- [[2023-camel-communicative-agents]]
- [[alignment]]
- [[ppo]]
- [[reward-model]]
- [[inception-prompting]]
- [[role-playing]]
- [[2023-chain-of-verification]]
- [[2023-agenttuning]]
- [[hallucination]]
- [[llm-agents|agent]]
- [[synthetic-data]]
- [[abliteration]]
