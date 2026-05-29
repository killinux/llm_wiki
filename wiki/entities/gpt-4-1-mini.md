---
type: entity
subtype: model
tags: [model, openai, gpt-4-1, multi-agent]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# GPT-4.1 mini

GPT-4.1 mini 是 OpenAI 推出的 GPT-4.1 系列中的轻量级模型,常被用作多 agent 推理与协作基准中的参与模型。

## 在本 wiki 中的出现

- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。
- [[2026-self-organizing-llm-agents]]:一项 25,000 任务的大规模实验发现"内生性悖论":固定智能体顺序但角色自主的混合协议(Sequential)在质量上同时超越中心化(+14%)与完全自主(+44%)协调,但仅当底层模型足够强(存在能力门槛)。

## 相关

- [[agentsnet]]
- [[multi-agent-reasoning]]
- [[openai]]
- [[gpt-4-1]]
- [[memori]]
- [[locomo]]
- [[self-organizing-llm-agents]]
