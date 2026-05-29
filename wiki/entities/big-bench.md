---
type: entity
subtype: benchmark
tags: [benchmark, evaluation, reasoning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# BIG-Bench

BIG-Bench(Beyond the Imitation Game Benchmark)是一个由社区协作构建的大规模、多任务语言模型评测基准,涵盖数百个跨语言、推理、常识、数学等领域的任务,用于衡量与探测大型语言模型的能力边界。

## 在本 wiki 中的出现

- [[2023-multi-agent-debate|2023-multiagent-debate]]:作为评测来源被使用。该工作让多个 LLM 实例多轮辩论、相互批评彼此答案,在推理(GSM8K 77%→85%)与事实性(MMLU 63.9%→71.1%)任务上显著提升;其中事实性实验里的 "Chess Move Validity(走子合法性)" 一项即取自 BIG-Bench 的 Chess-State Tracking 任务(synthetic_short),多智能体辩论将该任务准确率从 29.3% 提升到 45.2%。

## 相关

- [[mmlu]]
- [[gsm8k]]
- [[multiagent-debate]]
- [[large-language-models|llm]]
- [[benchmark]]
- [[reasoning]]
