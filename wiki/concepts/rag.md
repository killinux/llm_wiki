---
type: concept
subtype: method
tags: [retrieval, memory, context-augmentation, LLM]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# RAG

RAG(Retrieval-Augmented Generation,检索增强生成)是一种在生成前先从外部知识源检索相关信息、再将其作为上下文喂给 LLM 的方法,用以补充模型参数中缺失或过时的知识。

## 在本 wiki 中的出现

- [[2023-memorybank]]:RAG 作为长期记忆的核心机制。MemoryBank 将历史对话与分层摘要存入记忆库,在交互时检索相关记忆并构建用户画像,从而让模型"读取"超出当前上下文窗口的历史信息,实现情感陪伴机器人 SiliconFriend。
- [[2023-expel]]:RAG 思想体现在经验召回上。ExpeL 让 Agent 在不更新参数的前提下,从跨任务经验中抽取自然语言洞见,并在面对新任务时召回相似的成功轨迹作为上下文,以增强决策。
- [[2023-autogen]]:RAG 作为可装配的能力之一。AutoGen 作为多 agent 框架,通过可对话 agent 的会话编程支持将检索/外部知识接入复杂 LLM 应用。
- [[2023-llms-cannot-self-correct-reasoning-yet]]:本文证明在无外部反馈的"内在自我纠正"设定下,LLM 无法纠正自身推理错误,性能反而往往下降。
- [[2024-sage-self-evolving-agents]]:由 User/Assistant/Checker 三 agent 组成、结合迭代反馈、反思与基于 Ebbinghaus 遗忘曲线的记忆优化的自进化 LLM agent 框架,对小模型提升尤为显著。
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient,一个由六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历构建的知识图谱驱动的模拟病人系统,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89,用户研究中匹配或优于真人模拟病人。

## 相关

- [[memory]]
- [[in-context-learning]]
- [[vector-database]]
- [[embedding]]
- [[llm-agents|llm-agent]]
- [[prompt-engineering]]
