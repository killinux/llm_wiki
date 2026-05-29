---
type: entity
subtype: benchmark
tags: [code-generation, benchmark, evaluation, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# HumanEval

HumanEval 是一个用于评测代码生成能力的基准,由一组带函数签名、文档字符串与单元测试的 Python 编程问题构成,通过 pass@k 等指标衡量模型生成功能正确代码的能力。

## 在本 wiki 中的出现

- [[2023-reflexion]]:作为代码生成类任务的评测基准之一,用于检验语言化自我反思反馈对 LLM 智能体从失败中迭代改进的效果。
- [[2023-camel-communicative-agents]]:在围绕角色扮演与 inception prompting 的智能体协作研究中,作为衡量所生成代码质量的评测基准出现。
- [[2023-metagpt]]:作为核心评测基准之一,MetaGPT 的多智能体软件开发框架在 HumanEval/MBPP 上达到 SoTA。
- [[2023-agenttuning]]:通过构建跨任务 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 Llama 2 获得可泛化的 agent 能力且不损害通用能力。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。
- [[2024-rethinkmcts]]:一个面向代码生成的思路搜索框架,用 MCTS 探索写代码的推理过程,并通过 rethink 机制利用块级代码执行反馈直接精炼搜索树中的错误思路。
- [[2024-score-self-correct-via-rl]]:SCoRe 用完全自生成数据的多轮在线强化学习(两阶段+奖励塑形)训练单个 LLM,在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%(整体提升 15.6%)、HumanEval 上达 12.2%。
- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。

## 相关

- [[MBPP]]
- [[code-generation]]
- [[pass-at-k]]
- [[2023-metagpt]]
- [[2023-agenttuning]]
- [[2024-v-star-verifiers-for-self-taught-reasoners]]
- [[2024-megaagent-large-scale-mas-without-sop]]
- [[verifier]]
- [[multi-agent-systems|multi-agent-system]]
- [[2024-rethinkmcts]]
- [[2024-score-self-correct-via-rl]]
- [[monte-carlo-tree-search|mcts]]
- [[self-correction]]
- [[2023-reflexion]]
- [[2025-multi-agent-reflexion-mar]]
