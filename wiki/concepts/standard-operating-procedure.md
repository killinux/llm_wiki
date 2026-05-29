---
type: concept
subtype: method
tags: [multi-agent, sop, role-playing, code-generation, workflow]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# 标准作业程序(SOP)

标准作业程序(Standard Operating Procedure, SOP)是将人类在某一领域积累的最佳实践,拆解为明确分工、可执行步骤与结构化交付物的规范化流程,可被编码进 LLM 多智能体系统以约束其协作与输出。

## 在本 wiki 中的出现

- [[2023-metagpt]]:MetaGPT 把人类 SOP 编码进 prompt,通过为不同 agent 分配专业化角色并要求其产出结构化中间产物(structured output),来组织 LLM 多智能体的软件开发协作流程;借助 SOP 驱动的工作流,该框架在 HumanEval/MBPP 等代码生成基准上达到 SoTA。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,800 秒内开发五子棋、2991 秒协调 590 个 agent 生成国家政策。

## 相关

- [[2023-metagpt]]
- [[multi-agent-systems]]
- [[role-playing]]
- [[code-generation]]
- [[llm-agents|llm-agent]]
- [[2023-chatdev]]
- [[2023-autogen]]
- [[prompt-engineering]]
