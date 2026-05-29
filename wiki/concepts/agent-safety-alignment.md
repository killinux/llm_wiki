---
type: concept
subtype: method
tags: [agent, safety, alignment, reinforcement-learning, tool-use]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Agent safety alignment

Agent safety alignment 指针对会调用工具、与外部环境交互的 LLM agent，使其行为在面对用户侧与工具侧威胁时保持安全、可控且符合预期意图的对齐方法。

## 在本 wiki 中的出现

- [[2025-agent-safety-alignment-via-reinforcement-learning]]：首个面向 tool-using agent 的统一安全对齐框架，通过 structured reasoning + sandbox 强化学习，用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。

## 相关

- [[reinforcement-learning]]
- [[tool-use]]
- [[llm-alignment]]
- [[prompt-injection]]
