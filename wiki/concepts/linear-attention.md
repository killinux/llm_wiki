---
type: concept
subtype: method
tags: [architecture, attention, efficiency, long-context, sequence-modeling]
created: 2026-05-30
updated: 2026-05-30
sources: 6
---

# 线性注意力 (Linear Attention)

线性注意力是一类把标准 [[attention|自注意力]] 的 **O(N²)** 计算/显存复杂度降到 **O(N)** 的方法,以支持更长序列与更低推理成本。
核心思路:去掉 softmax 的非线性核,改用**可分解的核函数 φ(q)·φ(k)ᵀ**,从而把"先算 N×N 注意力矩阵"改写为"维护一个固定大小的状态/累加和",
使序列计算可写成**线性递归**形式。

## 与相关架构的关系
- **核技巧线性化**:Linear Transformer、Performer 等用特征映射近似 softmax 注意力。
- **状态空间 / 递归**:[[mamba]] 等 SSM、RWKV 把序列建模为线性递归,与线性注意力在"常数状态、线性扫描"上同构;
  本 wiki 中 [[2024-recmamba-lifelong-sequential-recommendation]]、[[2024-tim4rec-time-aware-mamba]] 把其用于**终身/长序列推荐**。
- **效率工程**:[[2026-fuxi-linear]] 等在推荐场景用线性复杂度建模超长行为序列;[[hstu]] 等生成式推荐架构也关注注意力的可扩展性。

## 权衡
线性注意力以**表达力**换**效率**:固定大小状态会压缩历史信息,在需要精确长程检索(retrieval-heavy)的任务上可能弱于全注意力;
实务中常用**混合**(局部全注意力 + 全局线性)折中。

## 相关页
[[attention]]、[[transformer]]、[[mamba]]、[[long-context]]、[[2026-fuxi-linear]]
