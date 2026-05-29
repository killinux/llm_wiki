---
type: concept
subtype: method
tags: [reward-model, rlhf, alignment, preference-learning, ppo]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Reward Model

Reward Model 是一个从人类偏好数据中训练出来的模型,用于给语言模型的输出打分(标量奖励),从而在 RLHF 中作为强化学习的奖励信号,引导策略模型生成更符合人类偏好的回复。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:在 InstructGPT 的 RLHF 三阶段流程(SFT → 奖励模型 → PPO)中,Reward Model 是承上启下的核心环节。它在 SFT 模型基础上训练,学习对同一 prompt 的多个候选回复进行人类偏好排序,输出标量奖励;随后该奖励被用作 PPO 优化的目标信号。借助这一流程,1.3B 的 InstructGPT 在人类偏好评测上胜过了 175B 的 GPT-3,并表现得更真实、毒性更低。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降——侧面说明需要外部奖励/反馈信号(如奖励模型)才能可靠改进。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier(一种奖励模型)在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益——其打分/估值模型在推荐排序中扮演奖励信号的角色。
- [[2024-compute-optimal-inference]]:提出 inference scaling laws / compute-optimal inference 研究问题与新型树搜索算法 REBASE,实证表明固定推理算力下小模型配合高级推理策略比大模型更具性价比(Llemma-7B 约省 2× FLOPs 达到 34B 水平),其中树搜索依赖奖励/价值模型对中间步骤打分。

## 相关

- [[rlhf]]:Reward Model 是 RLHF 流程中的关键组件。
- [[ppo]]:利用 Reward Model 提供的奖励信号进行策略优化。
- [[sft]]:Reward Model 通常在 SFT 模型的基础上构建并初始化。
- [[2022-instructgpt]]:本 wiki 中提及 Reward Model 的资料。
- [[human-preferences]]:Reward Model 的训练数据来源。
- [[gpt-3]]:InstructGPT 所对齐的基础模型。
- [[verifier]]:用于对候选解打分排序的奖励模型变体。
- [[dpo]]:可直接从偏好数据优化,或用于训练 verifier。
- [[scalable-oversight]]:用模型辅助人类评估的范式。
- [[inference-scaling]]:测试时搜索常依赖奖励/价值模型。
