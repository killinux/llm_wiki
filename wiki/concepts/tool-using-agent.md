---
type: concept
subtype: method
tags: [agent, tool-use, safety, alignment, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Tool-using agent

Tool-using agent(工具调用智能体)是指能够在推理过程中调用外部工具(如 API、代码执行、检索、沙箱环境等)以完成任务的大语言模型智能体,其核心挑战在于既要正确利用工具完成用户意图,又要抵御来自用户侧与工具侧的安全威胁。

## 在本 wiki 中的出现

- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。

## 相关

- [[reinforcement-learning]]
- [[agent-safety-alignment]]
- [[structured-reasoning]]
- [[sandbox-environment]]
