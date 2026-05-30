---
type: concept
subtype: method
tags: [planning, llm-agent, recommendation, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Self-Inspiring planning

Self-Inspiring 是一种用于 LLM agent 的规划算法,它在规划过程中保留所有已探索过的状态(而非丢弃次优路径),从而让模型从历史探索中"自我启发",增强多步规划与决策能力。

## 在本 wiki 中的出现

- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。

## 相关

- [[recmind]]
- [[llm-agents|llm-agent]]
- [[llm-planning|planning]]
- [[zero-shot-recommendation]]
