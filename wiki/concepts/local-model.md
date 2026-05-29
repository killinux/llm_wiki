---
type: concept
subtype: method
tags: [local-model, multi-agent, distributed-computing, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LOCAL Model

LOCAL 模型是分布式计算中的经典理论模型,指网络中每个节点(agent)只能与其拓扑邻居进行同步消息交换、基于局部信息进行决策,被借用来刻画多 agent LLM 网络在给定通信拓扑下的去中心化协作推理能力。

## 在本 wiki 中的出现

- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。

## 相关

- [[distributed-computing]]
- [[multi-agent-system]]
- [[leader-election]]
- [[consensus]]
- [[communication-topology]]
