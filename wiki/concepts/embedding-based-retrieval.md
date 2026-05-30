---
type: concept
subtype: method
tags: [retrieval, embedding, recommendation, recall, ANN]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Embedding-based retrieval

Embedding-based retrieval(EBR)是一种把 query 与候选物料映射到同一向量空间、用向量相似度进行近似最近邻检索来召回候选的方法,广泛用于搜索与推荐系统的召回阶段。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:作为推荐系统召回阶段的核心方法被改造。该工作把推荐召回的 embedding-based retrieval 拆成"物料聚类 + 簇内并行检索 + 可控合并"三步,并使用 prompt-like 的多任务适配来统一不同检索目标。在公开数据集上 Recall 最高提升约 40%,且已在快手线上部署。
- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图",并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。
- [[2025-meminsight-autonomous-memory-augmentation]]:MemInsight 让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2025-gnolr-progressive-implicit-preference]]:GNOLR 用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进,又把多路检索简化为单次最近邻搜索。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[2026-nestpipe-nested-pipelining]]:NestPipe 通过两层嵌套流水线(inter-batch 的 Dual-Buffer Pipelining 与 intra-batch 的 Frozen-Window Pipelining)在保持同步训练语义下隐藏大规模推荐 embedding 训练的 lookup 与 All2All 通信瓶颈,在 1,536 worker 上实现 3.06× 加速、94.07% 扩展效率。

## 相关

- [[approximate-nearest-neighbor-search]]
- [[recommendation-retrieval]]
- [[embedding]]
- [[two-tower|two-tower-model]]
- [[multi-task-learning]]
