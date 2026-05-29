---
type: concept
subtype: method
tags: [agents, memory, retrieval, long-term-memory]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Memory Stream

Memory Stream 是一种为 LLM 智能体设计的长期记忆机制:把智能体的全部经历(如对话、观察)以自然语言逐条存档为一条随时间增长的记忆流,并在决策或回应时动态检索最相关的条目,而非全量读入。

## 在本 wiki 中的出现

- [[2023-memorybank]]:MemoryBank 为 LLM 设计了一套类人长期记忆机制,其核心即以记忆流形式存储并分层摘要历史对话。它按 Ebbinghaus 遗忘曲线更新记忆强度、检索与当前情境相关的记忆并据此构建用户画像,最终用于实现情感陪伴机器人 SiliconFriend。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-metacognition-generative-agents]]:为 generative agents 引入元认知(metacognition)模块,让 agent 观察并反思自身思考与行动以动态调整策略,在僵尸末日等目标导向场景中显著提升表现。

## 相关

- [[2023-memorybank]]
- [[ebbinghaus-forgetting-curve]]
- [[llm-long-term-memory]]
- [[embedding-based-retrieval]]
- [[user-profile]]
- [[llm-agent]]
- [[generative-agents]]
- [[reflexion]]
