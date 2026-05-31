---
type: concept
subtype: method
tags: [graph, deep-learning, representation-learning, gnn, recommender-system]
created: 2026-05-31
updated: 2026-05-31
sources: 0
---

# 图神经网络 (Graph Neural Network, GNN)

图神经网络是一类直接在图结构数据上进行消息传递与表示学习的深度学习方法。节点通过聚合邻居信息来更新自身表示，从而捕获拓扑结构与节点/边属性。

## 核心范式

- **消息传递（Message Passing）**：每层中，节点从邻居收集消息并聚合（求和/均值/注意力加权），再与自身表示结合更新。
- **代表模型**：GCN（谱卷积简化）、GAT（注意力加权聚合）、GraphSAGE（采样+聚合）、GIN（可证明区分力最强的消息传递）。

## 在推荐系统中的应用

GNN 是推荐系统中建模用户-物品交互图的主要工具：
- [[lightgcn]] 简化 GCN 去掉特征变换和非线性，仅做邻居聚合与层间均值，成为协同过滤 GNN 基线。
- [[sigformer]] 等将带符号图（正/负反馈）与 Transformer 结合。
- 知识图谱增强推荐中也广泛使用 GNN 做实体/关系表示学习。

## 相关页

[[collaborative-filtering]]、[[lightgcn]]、[[recommender-systems]]、[[transformer]]、[[attention]]、[[knowledge-graph]]
