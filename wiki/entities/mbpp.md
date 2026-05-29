---
type: entity
subtype: benchmark
tags: [benchmark, code-generation, llm, python]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# MBPP

MBPP(Mostly Basic Python Problems)是一个用于评估代码生成能力的基准,由众多入门级 Python 编程问题组成,每道题配有自然语言描述、参考解法与测试用例。

## 在本 wiki 中的出现

- [[2023-reflexion]]:作为代码生成类任务的评测基准之一,用于检验语言化自我反思反馈对 LLM 智能体从失败中迭代改进的效果。
- [[2023-self-debugging]]:作为评测基准,用于验证 SELF-DEBUGGING 通过 few-shot prompting 让 LLM 执行并解释自身生成代码、实现无人工反馈自我调试的效果。
- [[2023-metagpt]]:MetaGPT 将人类 SOP 编码进 prompt,以专业化角色与结构化输出构建多智能体软件开发框架,在 HumanEval/MBPP 上达到 SoTA。
- [[2024-v-star-verifiers-for-self-taught-reasoners]]:V-STaR 在自我提升迭代中复用正确与错误的模型生成解,用 DPO 训练 verifier 在测试时对候选解排序,使 LLaMA2 在数学推理上绝对提升 6%~17%、代码生成 4%~12%。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。

## 相关

- [[humaneval]]
- [[code-generation]]
- [[large-language-models|llm]]
- [[few-shot-prompting]]
