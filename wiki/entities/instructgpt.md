---
type: entity
subtype: model
tags: [model, RLHF, alignment, GPT-3, OpenAI]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# InstructGPT

InstructGPT 是 OpenAI 通过 RLHF(基于人类反馈的强化学习)对齐 GPT-3 而得到的指令遵循模型,使模型输出更符合人类意图、更真实且毒性更低。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:本体论文。InstructGPT 采用 RLHF 流程(SFT → 奖励模型 → PPO)对齐 GPT-3,使得 1.3B 的 InstructGPT 在人类偏好评测上胜过 175B 的 GPT-3,同时更真实、毒性更低。
- [[2022-inner-monologue]]:作为对比/相关工作被提及。该工作通过持续注入自然语言环境反馈让 frozen LLM 形成"内心独白",实现机器人的闭环、可重规划具身推理。
- [[2022-constitutional-ai]]:作为对齐方法的对照被提及。Anthropic 的 Constitutional AI 用一套人类书写的原则替代人类有害性标注,通过模型自我批评修改与 AI 反馈(RLAIF)训练既无害又非回避的助手。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。

## 相关

- [[gpt-3]]:InstructGPT 对齐的基础模型。
- [[rlhf]]:InstructGPT 所采用的核心对齐方法。
- [[ppo]]:RLHF 中用于策略优化的强化学习算法。
- [[reward-model]]:RLHF 流程中用于建模人类偏好的组件。
- [[supervised-fine-tuning|sft]]:RLHF 第一阶段的监督微调。
- [[constitutional-ai]]:以 AI 反馈(RLAIF)替代人类标注的对齐路线。
- [[alignment]]:InstructGPT 所属的研究主题。
