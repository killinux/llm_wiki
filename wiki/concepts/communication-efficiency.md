---
type: concept
subtype: method
tags: [multi-agent, communication, efficiency, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Communication Efficiency

通信效率指在 LLM 多智能体系统中,以尽可能少的 token 交换实现有效协作与任务完成的能力,即在保证任务有效性的同时降低智能体间通信开销。

## 在本 wiki 中的出现

- [[2024-optima-optimizing-llm-multi-agent]]:OPTIMA 通过生成-排序-选择-训练的迭代范式同时优化 LLM 多智能体系统的通信效率与任务有效性,在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%。
- [[2026-nestpipe-nested-pipelining]]:NestPipe 通过两层嵌套流水线(inter-batch 的 Dual-Buffer Pipelining 与 intra-batch 的 Frozen-Window Pipelining)在保持同步训练语义下隐藏大规模推荐 embedding 训练的 lookup 与 All2All 通信瓶颈,在 1,536 worker 上实现 3.06× 加速、94.07% 扩展效率。

## 相关

- [[multi-agent-system]]
- [[task-effectiveness]]
- [[token-efficiency]]
- [[pipeline-parallelism]]
