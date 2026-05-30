---
type: concept
subtype: method
tags: [function-calling, tool-use, agent, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Function calling

Function calling 是让大语言模型在生成过程中以结构化方式调用外部工具/函数(并把返回结果纳入后续推理)的方法,是构建 tool-using agent 的核心机制。

## 在本 wiki 中的出现

- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。
- [[2026-orchestration-multi-agent-systems]]:Skan AI 提出的编排式多 agent 系统统一架构(专门化 agent + 四单元编排层 + MCP/A2A 双通信协议 + 治理与可观测性),其中 agent 通过工具/函数调用与外部系统及彼此协作,是该工程蓝图落地的基础能力之一。

## 相关

- [[tool-use]]
- [[llm-agents|agent]]
- [[reinforcement-learning]]
- [[agent-safety]]
- [[mcp]]
- [[a2a-protocol]]
- [[orchestration]]
