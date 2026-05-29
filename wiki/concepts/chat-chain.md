---
type: concept
subtype: method
tags: [multi-agent, llm-agent, role-playing, software-engineering, code-generation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# 对话链

Chat Chain(对话链)是一种将复杂任务沿预定流程拆分为一系列顺序子任务、每个子任务由两个角色化 LLM 智能体通过多轮对话求解、并将前一子任务的输出作为后一子任务输入的多智能体协作方法。

## 在本 wiki 中的出现

- [[2023-chatdev]]:ChatDev 用多个 LLM 驱动的角色化软件智能体,通过 chat chain 沿瀑布式流程(设计 / 编码 / 测试 / 文档)协作完成完整的软件开发生命周期。对话链把开发过程拆成顺序子任务,每个子任务由一个指令者(instructor)与一个助手(assistant)进行多轮对话求解,前一子任务的解作为后一子任务的输入,是该框架组织多智能体协作的核心机制。

## 相关

- [[2023-chatdev]]
- [[multi-agent-collaboration]]
- [[multi-agent-systems]]
- [[role-playing-agent]]
- [[role-playing]]
- [[inception-prompting]]
- [[communicative-dehallucination]]
- [[llm-agent]]
- [[code-generation]]
