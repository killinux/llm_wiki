---
type: entity
subtype: model
tags: [lora, peft, fine-tuning, low-rank-adaptation]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# LoRA

LoRA(Low-Rank Adaptation,低秩适配)是一种参数高效微调方法,通过向预训练模型的权重注入可训练的低秩矩阵,在冻结原始权重的情况下以极少的额外参数适配下游任务。

## 在本 wiki 中的出现
- [[2023-memorybank]]:在 MemoryBank 构建情感陪伴机器人 SiliconFriend 时,LoRA 被用作对底层 LLM 进行轻量化微调/适配的手段,使模型在保持基础能力的同时更贴合特定角色与对话风格,与基于记忆机制的个性化形成互补。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。
- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。
- [[2025-generative-mmo-simulation]]:用 LLM 驱动的生成式多智能体 MMO 游戏仿真系统,在真实玩家数据上 SFT+GRPO 微调 agent,高保真模拟玩家决策,低成本评估数值系统与机制设计的干预效果。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[fine-tuning]]
- [[instruction-tuning]]
- [[prompt-tuning]]
- [[foundation-models]]
- [[llm-long-term-memory]]
- [[siliconfriend]]

- [[2024-unbounded-generative-infinite-game]]:提出"生成式无限游戏"概念并实现一个角色生活模拟系统,游戏机制、叙事与角色/环境图像全部由 LLM 与 text-to-image 模型实时生成;核心创新是带 Block Drop 的 regional IP-Adapter(保证角色与环境一致性)与将多 LLM 协作能力蒸馏进 Gemma-2B 的实时游戏引擎。

## 相关

- [[ip-adapter]]
- [[text-to-image]]
- [[gemma-2b]]
- [[knowledge-distillation]]
- [[peft]]
