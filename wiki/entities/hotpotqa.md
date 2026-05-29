---
type: entity
subtype: benchmark
tags: [QA, multi-hop, reasoning, retrieval, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# HotpotQA

HotpotQA 是一个基于 Wikipedia 的多跳(multi-hop)问答数据集,要求模型在多篇文档之间进行检索与组合推理才能得到答案,常被用作评测 LLM 智能体推理与工具使用能力的基准。

## 在本 wiki 中的出现

- [[2023-reflexion]]:作为评测基准之一,用于检验以语言化自我反思反馈(而非梯度更新)强化的 LLM 智能体能否从失败中迭代改进、在多跳问答上提升表现。
- [[2023-critic]]:作为评测任务,用于验证 CRITIC 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出的效果,体现外部反馈对自我改进的重要性。
- [[2023-expel]]:作为评测任务,用于检验 LLM Agent 在不更新参数的前提下,从跨任务经验中抽取自然语言洞见并召回相似成功轨迹以提升决策表现。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述:细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-sage-self-evolving-agents]]:SAGE 自进化 agent 框架(由 User/Assistant/Checker 三 agent 组成,结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化)在 HotpotQA 等任务上评估,对小模型提升尤为显著。

## 相关

- [[react]]
- [[multi-hop-reasoning]]
- [[wikipedia]]
- [[self-reflection]]
- [[tool-use]]
- [[retrieval-augmented-generation]]
