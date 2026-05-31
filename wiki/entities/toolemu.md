---
type: entity
subtype: benchmark
tags: [benchmark, agent-safety, tool-use, risk-evaluation, sandbox]
created: 2026-05-31
updated: 2026-05-31
sources: 1
---

# ToolEmu

ToolEmu 是一个用于评估 LLM agent 工具使用安全风险的仿真沙箱框架。它利用一个 LLM 模拟工具执行环境，系统性地测试 agent 在调用工具时可能引发的安全隐患（如数据泄露、未授权操作、不可逆危险动作等），无需接入真实工具即可进行大规模安全评估。

## 在本 wiki 中的出现

- [[2023-toolemu]] — ToolEmu 原始论文，提出基于 LLM 仿真的工具安全评估方法

## 相关

- [[benchmark]] — 基准概念总览
- [[agent-safety-alignment]] — agent 安全与对齐
- [[tool-use]] — 工具使用概念总览
