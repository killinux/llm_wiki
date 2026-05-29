---
type: entity
subtype: lab
tags: [lab, ai, llm, alignment, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# OpenAI

OpenAI 是一家人工智能研究实验室,以 GPT 系列大语言模型及一系列对齐与推理方法的研究而著称。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:OpenAI 提出 InstructGPT,使用 RLHF(SFT → 奖励模型 → PPO)对齐 GPT-3,使 1.3B 模型在人类偏好评测上胜过 175B 的 GPT-3,且回答更真实、毒性更低。
- [[2023-lets-verify-step-by-step]]:OpenAI 证明过程监督(PRM)在 MATH 多步数学推理任务上显著优于结果监督(ORM),best-of-N 达到 78.2%,并开源了步骤级标注数据集 PRM800K。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。

## 相关

- [[gpt-3]]
- [[rlhf]]
- [[ppo]]
- [[reward-model]]
- [[process-supervision]]
- [[prm800k]]
- [[math-benchmark]]
- [[scalable-oversight]]
- [[gpt-4]]
- [[self-correction]]
- [[long-term-memory]]
