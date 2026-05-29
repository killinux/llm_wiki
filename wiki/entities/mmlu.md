---
type: entity
subtype: benchmark
tags: [benchmark, evaluation, knowledge, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# MMLU

MMLU(Massive Multitask Language Understanding)是一个覆盖多学科知识与推理能力的多选题基准,用于衡量 LLM 的广泛事实性知识与综合理解水平。

## 在本 wiki 中的出现

- [[2023-multiagent-debate]]:作为事实性(factuality)任务的评测基准之一,用于验证多智能体辩论方法的效果。该方法通过让多个 LLM 实例多轮辩论、互相批评彼此答案,将 MMLU 上的表现从 63.9% 提升到 71.1%(同时在 GSM8K 推理任务上从 77% 提升到 85%)。
- [[2023-agentbench]]:作为已有 LLM 评测基准的参照与背景被提及。AgentBench 关注的是 LLM-as-Agent 在交互环境中的能力,与 MMLU 这类静态知识问答基准形成对比,凸显了智能体能力评测的独特维度。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。

## 相关

- [[gsm8k]]
- [[2023-multiagent-debate]]
- [[2023-agentbench]]
- [[benchmark]]
- [[llm-evaluation]]
