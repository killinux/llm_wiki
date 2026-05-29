---
type: concept
subtype: method
tags: [parameter-efficient-fine-tuning, fine-tuning, llm, adaptation]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# LoRA

LoRA(Low-Rank Adaptation)是一种参数高效微调(parameter-efficient fine-tuning)方法,通过在冻结的预训练权重旁注入可训练的低秩分解矩阵来适配下游任务,从而大幅减少需要训练和存储的参数量。

## 在本 wiki 中的出现

- [[2023-memorybank]]:在 MemoryBank 构建情感陪伴机器人 SiliconFriend 时,LoRA 被用作对底层 LLM 进行轻量化微调/适配的手段,使模型在保持基础能力的同时更贴合特定角色与对话风格,与基于记忆机制的个性化形成互补。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。

## 相关

- [[fine-tuning]]
- [[instruction-tuning]]
- [[prompt-tuning]]
- [[foundation-models]]
- [[llm-long-term-memory]]
- [[siliconfriend]]
