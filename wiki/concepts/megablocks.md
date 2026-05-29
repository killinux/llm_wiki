---
type: concept
subtype: method
tags: [moe, sparsity, gpu-kernels, block-sparse, expert-parallelism]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# MegaBlocks

MegaBlocks 是一种用块稀疏(block-sparse)矩阵运算重构 Mixture-of-Experts(MoE)计算的高效训练系统,通过避免 token dropping 与 padding,把动态、不均衡的专家路由表达为单个块稀疏 GEMM,从而在 GPU 上获得更高的硬件利用率与吞吐。

## 在本 wiki 中的出现

- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。

## 相关

- [[mixture-of-experts]]
- [[expert-parallelism]]
- [[load-balancing]]
- [[block-sparse-gemm]]
- [[token-dropping]]
