---
type: concept
subtype: method
tags: [distributed-computing, multi-agent, coordination, infrastructure, theory]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# 分布式计算 (Distributed Computing)

**分布式计算 (distributed computing)** 是指由多个独立节点(进程/机器/agent)通过通信协作完成同一计算任务的范式,其核心挑战在于各节点仅持有局部信息、只能通过消息交换在并发、去中心化、给定通信拓扑的条件下达成全局目标。

## 概述

分布式计算既是一套关于协调、通信与局部决策的经典理论(如 [[local-model]] 模型,以及 consensus、leader election、graph coloring 等经典问题),也是一类支撑大规模 agent 系统运行的工程基础。在本 wiki 中,它沿两条线索出现:一条把分布式计算的经典问题改造为评测 LLM 多 agent 协调与协作推理能力的基准;另一条把分布式仿真引擎作为大规模社会 agent 模拟的并行计算底座。

## 在本 wiki 中的出现

- [[2025-agentsnet-multi-agent-reasoning]]:AGENTSNET 直接借鉴分布式计算的五个经典问题(coloring、vertex cover、matching、leader election、consensus)构造可任意扩展的多 agent LLM 基准——agent 放在图上、只能与拓扑邻居通过 [[message-passing]] 通信,在类似 [[local-model]] 的局部信息约束下求解全局问题,以此衡量协调能力随网络规模(实验最多探测 100 个 agent)的扩展性。
- [[2025-agentsociety-large-scale-social-simulation]]:把分布式计算用作大规模社会模拟的工程底座,基于 [[ray]] 等分布式仿真引擎将上万个 LLM 生成式社会 agent 并行调度到真实城市-社会-经济环境中,复现极化、谣言、UBI、飓风、城市可持续性等社会实验。

## 相关

- [[message-passing]]
- [[local-model]]
- [[consensus]]
- [[leader-election]]
- [[graph-coloring]]
- [[ray]]
- [[multi-agent-systems]]
- [[agentsnet]]
