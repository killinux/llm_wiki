---
type: concept
subtype: method
tags: [self-correction, tool-use, verification, self-improvement]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# CRITIC

CRITIC 是一种让 LLM 借助外部工具进行交互式验证与迭代修正的自我纠错方法。

## 在本 wiki 中的出现

- [[2023-critic]]:CRITIC 是该论文提出的核心方法,让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,证明外部反馈对自我改进至关重要。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述,细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。

## 相关

- [[self-refine]]:同样基于迭代式自我修正,但反馈来自模型自身而非外部工具。
- [[reflexion]]:通过反思机制改进 LLM 输出的自我改进方法。
- [[react]]:同样以 LLM 与外部工具/环境交互为基础。
- [[toolformer]]:LLM 调用外部工具的相关方法。
- [[self-correction]]:CRITIC 所属的自我纠错方法范畴。
- [[tool-use]]:CRITIC 依赖的外部工具调用能力。
