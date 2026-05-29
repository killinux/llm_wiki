---
type: concept
subtype: method
tags: [self-critique, self-refine, RLAIF, alignment, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Self-critique

Self-critique 指让模型对自身的输出进行评判、指出问题并据此修正,从而在不依赖额外人类标注的情况下提升输出质量或安全性。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:Self-critique 是 Constitutional AI 的核心机制。模型依据一套人类书写的原则(constitution)对自己生成的有害回复进行自我批评(critique)并修改(revision),用以替代人类的有害性标注;修改后的数据进一步用于监督微调,并结合 AI 反馈(RLAIF)训练出既无害又非回避的助手。
- [[2023-self-refine]]:Self-critique 表现为测试时的"自我反馈(self-feedback)→自我修正(self-refine)"迭代循环。用同一个 LLM 既生成、又反馈、又修正,无需任何训练即可在 7 个任务上平均提升约 20%。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

## 相关

- [[constitutional-ai]]
- [[self-refine]]
- [[RLAIF]]
- [[RLHF]]
- [[self-consistency]]
- [[chain-of-thought]]
- [[AI-feedback]]
- [[iterative-refinement]]
