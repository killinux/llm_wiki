---
type: entity
subtype: product
tags: [vector-search, ann, retrieval, embedding, library]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# FAISS

FAISS(Facebook AI Similarity Search)是用于稠密向量高效相似度搜索与聚类的开源库,广泛用于大规模近似最近邻(ANN)检索与嵌入召回场景。

## 在本 wiki 中的出现
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐;其记忆与检索环节常借助向量相似度检索(如 FAISS)来召回历史经验。
- [[embedding]]
- [[retrieval-augmented-generation]]
- [[2024-llm-learnable-planners-long-term-recommendation]]

- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。
- [[2026-tencent-advertising-algorithm-challenge-2025]]:腾讯广告算法大赛 2025 发布两个真实工业广告日志构建的大规模全模态生成式推荐数据集(TencentGR-1M/10M)、基线模型与含转化加权的评测协议。
- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。

## 相关

- [[vector-database]]
- [[approximate-nearest-neighbor]]
- [[embedding-retrieval]]
- [[two-tower-retrieval]]
