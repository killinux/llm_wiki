---
type: concept
subtype: method
tags: [self-improvement, iterative-refinement, feedback, prompting, llm-reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 13
---

# SELF-REFINE

SELF-REFINE 是一种无需额外训练的测试时方法:用同一个 LLM 对自己的输出进行迭代式的"自我反馈(self-feedback)→自我修正(self-refinement)",从而逐步提升生成质量。

## 在本 wiki 中的出现

- [[2023-self-refine]]:提出 SELF-REFINE 本身。用同一个 LLM 在测试时迭代"自我反馈→自我修正",无需训练即可在 7 个任务上取得平均约 20% 的提升,是该方法的来源论文。
- [[2023-self-debugging]]:提出 SELF-DEBUGGING,可视为 SELF-REFINE 思想在代码领域的实例。通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,实现无人工反馈的自我调试。
- [[2023-critic]]:CRITIC 是对 SELF-REFINE 一类纯自我反馈方法的补充与质疑。它让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,论证外部反馈对自我改进至关重要。
- [[2023-multiagent-debate]]:让多个 LLM 实例多轮辩论、互相批评彼此答案,是单模型自我修正之外的另一条改进路径。在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上显著提升。
- [[2023-multi-agent-debate]]:提出 Multi-Agent Debate(MAD)框架,用多个 LLM 智能体"针锋相对"辩论加裁判仲裁,明确旨在缓解自我反思(self-reflection)中的 Degeneration-of-Thought 问题并激发发散性思维,可视作对 SELF-REFINE 局限的回应。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001)。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述:细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。
- [[2024-positive-experience-reflection]]:提出 Sweet&Sour,让 LLM agent 在交互式文本环境中不仅从失败、也从成功经验做反思,并配合双缓冲 managed memory,缓解 self-reflection 在初始成功与小模型上失效的问题;ScienceWorld 上 GPT-4o 平均 54.6、Llama 8B 32.5 均超 Reflexion。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。

## 相关

- [[2023-self-refine]]
- [[2023-self-debugging]]
- [[2023-critic]]
- [[2023-multiagent-debate]]
- [[2023-multi-agent-debate]]
- [[2023-shepherd-critic-for-lm-generation]]
- [[2023-chain-of-verification]]
- [[2023-llms-cannot-self-correct-reasoning-yet]]
- [[2024-self-reflection-llm-agents]]
- [[2024-when-can-llms-correct-mistakes]]
- [[2024-recursive-introspection-rise]]
- [[2024-positive-experience-reflection]]
- [[2025-llm-agents-cooperate-social-dilemma]]
- [[self-debugging]]
- [[critic]]
- [[multi-agent-debate]]
- [[self-feedback]]
- [[iterative-refinement]]
- [[test-time-compute]]
- [[chain-of-thought]]
