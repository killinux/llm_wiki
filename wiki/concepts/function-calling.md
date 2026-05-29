---
type: concept
subtype: method
tags: [function-calling, tool-use, agent, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Function calling

Function calling 是让大语言模型在生成过程中以结构化方式调用外部工具/函数(并把返回结果纳入后续推理)的方法,是构建 tool-using agent 的核心机制。

## 在本 wiki 中的出现

- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。

## 相关

- [[tool-use]]
- [[agent]]
- [[reinforcement-learning]]
- [[agent-safety]]
