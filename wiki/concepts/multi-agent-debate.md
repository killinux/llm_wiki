---
type: concept
subtype: method
tags: [multi-agent, debate, reasoning, factuality, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Multi-Agent Debate

Multi-Agent Debate 是一种让多个 LLM 实例(智能体)就同一问题各自给出答案、并通过多轮相互批评与辩论来收敛到更优结论的方法,用以提升推理质量与事实性。

## 在本 wiki 中的出现

- [[2023-multiagent-debate]]:让多个 LLM 实例进行多轮辩论、互相批评彼此的答案。该方法在推理任务(GSM8K 77%→85%)与事实性任务(MMLU 63.9%→71.1%)上均带来显著提升。
- [[2023-multi-agent-debate]]:提出 Multi-Agent Debate(MAD)框架,用多个 LLM 智能体"针锋相对"地辩论,并由裁判(judge)仲裁;借此缓解自我反思中的 Degeneration-of-Thought 问题,并激发模型的发散性思维。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。这对依赖模型自我批判的辩论/反思类方法提出了警示——若辩论各方仅靠自身判断而无外部反馈,纠错效果存疑。

## 相关

- [[self-reflection]]
- [[degeneration-of-thought]]
- [[chain-of-thought]]
- [[self-consistency]]
- [[llm-as-a-judge]]
