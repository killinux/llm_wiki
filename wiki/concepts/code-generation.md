---
type: concept
subtype: method
tags: [code-generation, llm, agent, self-debugging]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Code Generation

Code Generation 指由 LLM 根据自然语言描述、上下文或环境反馈自动生成可执行代码的方法。

## 在本 wiki 中的出现

- 在 [[2023-self-debugging]] 中,Code Generation 是被调试的对象:SELF-DEBUGGING 通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,从而在没有人工反馈的情况下完成对生成代码的自我调试与修正。
- 在 [[2023-voyager]] 中,Code Generation 是技能的载体:由 GPT-4 驱动的具身智能体在 Minecraft 中将技能表达为可执行代码,并结合自动课程与自我验证,把生成的代码技能存入技能库以支持终身学习。
- [[2024-eureka-reward-design-via-coding-llms]]:Eureka 用编码 LLM(GPT-4)零样本生成可执行奖励函数代码,结合进化搜索与奖励反思迭代改进,在 29 个 RL 环境上达到人类专家级奖励设计并首次让模拟 Shadow Hand 学会转笔。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。

## 相关

- [[self-debugging]]
- [[few-shot-prompting]]
- [[llm-agent]]
- [[self-verification]]
- [[skill-library]]
- [[verifier]]
- [[reward-design]]
- [[scalable-oversight]]
