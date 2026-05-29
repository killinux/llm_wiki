---
type: concept
subtype: method
tags: [AI safety, alignment, harmlessness, RLHF, RLAIF]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# AI safety

AI safety 是指通过技术与方法手段,让 AI 系统的行为保持无害(harmless)、诚实且与人类意图对齐(aligned),从而降低其造成伤害或被滥用风险的研究领域。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:在 Constitutional AI 中,AI safety 是核心目标。Anthropic 用一套人类书写的原则(constitution)替代逐条的人类有害性标注,先通过模型对自身回答的自我批评与修改(self-critique & revision)生成更无害的样本,再以 AI 反馈(RLAIF)进行强化学习训练。其目标是得到一个既无害又非回避(non-evasive)的助手,即在拒绝有害请求的同时仍能解释拒绝理由、保持有用性。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估,可用于在受控环境中研究 agent 行为与社会影响。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督(scalable oversight)方式帮助人类更准确评估模型生成的代码。

## 相关

- [[constitutional-ai]]
- [[rlaif]]
- [[rlhf]]
- [[alignment]]
- [[harmlessness]]
- [[self-critique]]
- [[scalable-oversight]]
- [[generative-agent-based-modeling]]
- [[2022-constitutional-ai]]
