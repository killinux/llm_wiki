---
type: entity
subtype: benchmark
tags: [toxicity, safety, evaluation, language-generation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# RealToxicityPrompts

RealToxicityPrompts 是一个用于评测语言模型在文本续写中产生毒性内容(toxic degeneration)倾向的基准数据集,通过给定自然语言前缀提示并衡量模型续写的毒性来量化模型的安全性。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:在评估 InstructGPT 对齐效果时,作为衡量模型毒性的参考。InstructGPT 用 RLHF(SFT→奖励模型→PPO)对齐 GPT-3,使 1.3B 模型在人类偏好上胜过 175B GPT-3,并表现得更真实、毒性更低。
- [[2023-critic]]:在毒性相关任务中作为评测场景出现。CRITIC 让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,证明外部反馈对自我改进至关重要,其中毒性检测依赖 PERSPECTIVE API 提供外部信号。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。

## 相关

- [[perspective-api]]
- [[toxicity]]
- [[rlhf]]
- [[instructgpt]]
- [[gpt-3]]
