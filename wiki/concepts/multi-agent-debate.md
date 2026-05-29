---
type: concept
subtype: method
tags: [multi-agent, debate, reasoning, factuality, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Multi-Agent Debate

Multi-Agent Debate 是一种让多个 LLM 实例(智能体)就同一问题各自给出答案、并通过多轮相互批评与辩论来收敛到更优结论的方法,用以提升推理质量与事实性。

## 在本 wiki 中的出现

- [[2023-multiagent-debate]]:让多个 LLM 实例进行多轮辩论、互相批评彼此的答案。该方法在推理任务(GSM8K 77%→85%)与事实性任务(MMLU 63.9%→71.1%)上均带来显著提升。
- [[2023-multi-agent-debate]]:提出 Multi-Agent Debate(MAD)框架,用多个 LLM 智能体"针锋相对"地辩论,并由裁判(judge)仲裁;借此缓解自我反思中的 Degeneration-of-Thought 问题,并激发模型的发散性思维。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。这对依赖模型自我批判的辩论/反思类方法提出了警示——若辩论各方仅靠自身判断而无外部反馈,纠错效果存疑。
- [[2024-multi-agent-tot-validator]]:将 Tree-of-Thoughts 与多智能体推理结合,新增 Thought Validator agent 过滤无效推理分支后再共识投票,在 GSM8K 上比标准 ToT 平均提升 5.6 个百分点。
- [[2024-optima-optimizing-llm-multi-agent]]:OPTIMA 通过生成-排序-选择-训练的迭代范式同时优化 LLM 多智能体系统的通信效率与任务有效性,在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:一篇系统综述,沿 actors、types、structures、strategies、coordination protocols 五个维度刻画基于 LLM 的多 agent 系统协作机制,并梳理其跨领域应用与挑战。
- [[2025-llm-multi-agent-autonomous-driving-survey]]:系统综述 LLM 驱动的多智能体自动驾驶系统,按智能体交互模式与结构分类已有方法,并梳理 agent-human 交互、应用、数据集与未来方向。
- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 MARL(Dec-POMDP)并提出 Multi-Agent GRPO(MAGRPO),在写作与编码协作上微调多个 LLM;TLDR/arXiv return 达 94.5%/93.1%,HumanEval/CoopHumanEval return 达 86.7%/88.5%。

## 相关

- [[self-reflection]]
- [[degeneration-of-thought]]
- [[chain-of-thought]]
- [[self-consistency]]
- [[llm-as-a-judge]]
