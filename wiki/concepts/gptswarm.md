---
type: concept
subtype: method
tags: [multi-agent, llm-agents, graph, optimization, collaboration]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# GPTSwarm

GPTSwarm 是一种将 LLM agent 系统建模为可优化计算图的方法,把单个 agent 表示为节点、agent 间的协作关系表示为边,并通过对图结构与提示的自动优化来提升多 agent 群体的协作推理能力。

## 在本 wiki 中的出现

- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。

## 相关

- [[multi-agent-systems|multi-agent-system]]
- [[agent-communication-topology]]
- [[2025-agentsnet-multi-agent-reasoning]]
