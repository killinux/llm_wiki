---
type: concept
subtype: method
tags: [prompting, in-context-learning, llm, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Few-shot Prompting

Few-shot Prompting 是一种在 prompt 中提供少量输入-输出示例(demonstrations),让 LLM 在不更新参数的情况下,通过 in-context learning 推断并完成目标任务的方法。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作为承载推理的基础范式。Chain-of-thought prompting 在 few-shot 示例中加入中间推理步骤,显著提升大模型的多步推理能力,且该增益随模型规模涌现(PaLM 540B 在 GSM8K 达 57%)。
- [[2022-inner-monologue]]:作为引导 frozen LLM 行为的手段。通过持续注入自然语言环境反馈让 frozen LLM 形成"内心独白",实现机器人的闭环、可重规划具身推理。
- [[2023-self-refine]]:作为测试时迭代改进的基础。用同一个 LLM 在测试时迭代"自我反馈→自我修正",无需训练即在 7 个任务上平均提升约 20%。
- [[2023-self-debugging]]:作为驱动自我调试的核心机制。提出 SELF-DEBUGGING,通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,实现无人工反馈的自我调试。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。

## 相关

- [[in-context-learning]]
- [[zero-shot-prompting]]
- [[chain-of-thought]]
- [[self-refine]]
- [[self-debugging]]
- [[prompt-engineering]]
- [[language-agent-fine-tuning]]
