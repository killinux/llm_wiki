---
type: entity
subtype: benchmark
tags: [benchmark, truthfulness, evaluation, factuality]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# TruthfulQA

TruthfulQA 是一个用于衡量语言模型回答问题时真实性的基准,重点考察模型是否会复述人类常见的错误信念或虚假说法。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:该论文用 RLHF(SFT → 奖励模型 → PPO)对齐 GPT-3,使 1.3B 的 InstructGPT 在人类偏好上胜过 175B 的 GPT-3,并表现得更真实、毒性更低。TruthfulQA 在此作为衡量模型"真实性"的评测基准之一。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。

## 相关

- [[2022-instructgpt]]
- [[rlhf]]
- [[gpt-3]]
- [[hallucination]]
- [[benchmark]]
- [[truthfulness]]
