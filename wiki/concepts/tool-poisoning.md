---
type: concept
subtype: method
tags: [tool-poisoning, agent-safety, tool-using-agent, security]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Tool poisoning

Tool poisoning 指攻击者通过工具侧(如工具描述、返回结果、外部数据)注入恶意指令或内容,诱导 tool-using agent 执行有害操作的威胁,与用户侧的直接攻击共同构成 agent 安全的两大威胁面。

## 在本 wiki 中的出现

- [[2025-agent-safety-alignment-via-reinforcement-learning]]:首个面向 tool-using agent 的统一安全对齐框架,通过 structured reasoning + sandbox 强化学习,用 benign/malicious/sensitive 三模态分类与 execute-refuse-verify 策略同时抵御用户侧与工具侧威胁。

## 相关

- [[agent-safety-alignment]]
- [[prompt-injection]]
- [[tool-using-agent]]
- [[reinforcement-learning]]
