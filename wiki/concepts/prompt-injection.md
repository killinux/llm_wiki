---
type: concept
subtype: method
tags: [prompt-injection, agent-safety, llm-security, tool-use]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Prompt injection

Prompt injection 是一类针对大语言模型及其智能体的攻击手法:攻击者通过用户输入或外部工具/数据返回的内容注入恶意指令,诱导模型偏离原始意图、执行非授权操作或泄露敏感信息。

## 在本 wiki 中的出现

- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。

## 相关

- [[agent-safety]]
- [[reinforcement-learning]]
- [[tool-use]]
- [[llm-security]]
