---
type: concept
subtype: method
tags: [code-execution, agent, tool-use, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Code Execution

Code Execution 指让 LLM 或 agent 生成代码并在真实运行环境(如 Python 解释器、shell)中执行,以完成任务、获取结果反馈或与外部系统交互的能力。

## 在本 wiki 中的出现

- 在 [[2023-autogen]] 中,Code Execution 是 agent 能力的核心组成部分之一。AutoGen 作为微软提出的开源多 agent 框架,通过可定制、可对话的 agent 之间会话编程来构建复杂 LLM 应用;其中的 agent 可以生成并执行代码,作为完成任务和相互协作的手段之一。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。

## 相关

- [[2023-autogen]]
- [[tool-use]]
- [[multi-agent-systems|multi-agent]]
- [[llm-agents|llm-agent]]
