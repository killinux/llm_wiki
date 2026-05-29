---
type: concept
subtype: method
tags: [llm, evaluation, feedback, self-improvement, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# LLM-as-judge

LLM-as-judge 指用一个 LLM 来评估、批评或打分另一个(或同一个)模型的输出,以此替代或补充人工评估与显式奖励信号。

## 在本 wiki 中的出现

- [[2023-self-refine]]:LLM 既是生成者也是 judge——同一个 LLM 在测试时对自己的输出生成反馈(self-feedback),再据此自我修正(self-refine),迭代进行。无需额外训练即在 7 个任务上平均提升约 20%,体现了"模型自身充当评判者"这一思路。
- [[2023-multiagent-debate]]:多个 LLM 实例在多轮辩论中互相批评、评估彼此的答案,相当于让模型群体充当彼此的 judge。该机制在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上带来显著提升。
- [[2026-generative-social-simulation-validation]]:系统性文献综述指出,LLM 驱动的生成式 ABM 因黑箱性、文化偏见与随机性而加剧了模型"验证"难题,这直接质疑了将 LLM 作为评判与验证工具的可靠性。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 反馈数据微调 7B LLaMA critic 模型 Shepherd,精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,是 LLM-as-judge/critic 的典型实例。
- [[2023-sotopia-social-intelligence-evaluation]]:SOTOPIA-EVAL 提出多维评测框架,交互式评估 LLM 智能体的社会智能,体现了用 LLM 评判开放式社交互动表现的范式。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知模块,让 agent 观察并反思自身思考与行动,本质上是 agent 对自身输出的自我评判与动态调整。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练 7B LLM,使用 GPT-4 作为评判者来筛选训练数据。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类评估模型生成的代码。
- [[2024-megaagent-large-scale-mas-without-sop]]:大规模 LLM 多智能体系统中,agent 间相互监督与协调隐含了用 LLM 评判其它 agent 输出的机制。

## 相关

- [[self-critique]]
- [[self-refine]]
- [[reflexion]]
- [[reward-model]]
- [[rlaif]]
- [[scalable-oversight]]
- [[self-consistency]]
- [[2023-critic]]
- [[constitutional-ai]]
