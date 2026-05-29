---
type: concept
subtype: method
tags: [distributed-computing, multi-agent, coordination, llm-benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Leader Election

Leader Election 是分布式计算中的经典问题:在一组对等节点(或 agent)中,通过去中心化的通信协议选出唯一的协调者(leader),用以衡量网络在给定通信拓扑下的自组织与协作推理能力。

## 在本 wiki 中的出现

- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。

## 相关

- [[consensus]]
- [[graph-coloring]]
- [[vertex-cover]]
- [[matching]]
- [[multi-agent-systems]]
