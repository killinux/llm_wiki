---
type: concept
subtype: method
tags: [alignment, oversight, RLHF, AI-feedback]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Scalable oversight

Scalable oversight 指在任务难度或规模超出人类直接、逐例监督能力的情况下,仍能有效地引导和监督模型行为的一类方法,通常借助模型自身或 AI 反馈来放大有限的人类监督信号。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:Anthropic 提出 Constitutional AI,用一套人类书写的原则(constitution)替代逐条的人类有害性标注,通过模型自我批评修改与 AI 反馈(RLAIF)训练既无害又非回避的助手。这是 scalable oversight 的一种具体实现路径——把人类监督压缩为少量原则,再由模型自身放大为大量训练信号。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。

## 相关

- [[constitutional-ai]]
- [[rlaif]]
- [[rlhf]]
- [[ai-feedback]]
- [[ai-alignment]]
- [[harmlessness]]
- [[multi-agent-systems]]
- [[evolutionary-game-theory]]
