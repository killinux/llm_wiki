---
type: concept
subtype: method
tags: [graph-coloring, distributed-computing, multi-agent, benchmark, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Graph Coloring

图着色(Graph Coloring)是一个经典的分布式计算与组合优化问题:为图中的每个节点分配一种颜色,使得任意相邻节点的颜色都不相同,通常目标是使用尽可能少的颜色。

## 在本 wiki 中的出现

- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 是一个可任意扩展的多 agent LLM 基准,借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)来衡量 agent 网络在给定通信拓扑下的自组织、去中心化通信与协作推理能力,实验最多探测 100 个 agent。其中 coloring 即图着色问题。

## 相关

- [[vertex-cover]]
- [[matching]]
- [[leader-election]]
- [[consensus]]
- [[distributed-computing]]
- [[multi-agent-systems]]
