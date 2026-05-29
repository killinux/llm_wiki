---
type: concept
subtype: method
tags: [multi-agent, communication, hallucination, software-engineering, LLM]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# 沟通式去幻觉

沟通式去幻觉(communicative dehallucination)是一种在多 agent 协作中,通过 agent 之间显式的多轮对话(例如要求对方先澄清细节、再给出回应)来减少由信息缺失或含糊导致的幻觉(hallucination)的方法。

## 在本 wiki 中的出现

- [[2023-chatdev]]:ChatDev 让多个 LLM 驱动的角色化软件智能体沿瀑布式流程,通过对话链协作完成设计、编码、测试与文档。在这种以对话为核心的协作中,角色之间的多轮沟通(由提出方先澄清需求、再由响应方作答)被用作抑制幻觉的机制,以提升各阶段产出的准确性与一致性。

## 相关

- [[2023-chatdev]]
- [[multi-agent-collaboration]]
- [[hallucination]]
- [[role-playing]]
- [[waterfall-process]]
- [[llm-agents|llm-agent]]
