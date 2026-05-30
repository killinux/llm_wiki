---
type: concept
subtype: method
tags: [retrieval, embedding, rag, question-answering, search]
created: 2026-05-30
updated: 2026-05-30
sources: 6
---

# 稠密检索 (Dense Retrieval)

稠密检索用**学习到的稠密向量**(而非稀疏词袋如 BM25)表示查询与文档,通过向量相似度(内积/余弦)做语义匹配,
能召回"词面不同但语义相关"的结果。是开放域问答与 [[rag|RAG]] 的核心召回组件。

## 机制
- **双编码器 (bi-encoder)**:查询塔与文档塔各自独立编码为 [[embedding]],离线建库、在线 ANN 检索——高效但交互弱;代表 [[dpr|DPR]]。
  推荐侧的同构结构是双塔 [[two-tower]]/[[dssm]]。
- **交叉编码器 (cross-encoder)**:查询-文档拼接联合编码,精度高但贵,通常只用于**精排重排**少量候选。
- **召回-重排级联**:bi-encoder 召回 + cross-encoder 重排是标准两段式;[[2023-divide-and-conquer-ebr]] 优化召回 EBR。
- **稀疏-稠密混合**:与 BM25 融合(hybrid)兼顾词面精确匹配与语义泛化。

## 与 RAG / LLM 的关系
[[rag|RAG]] 用稠密检索把外部知识喂给 [[seq2seq]] 生成,缓解幻觉与知识过时;检索质量直接决定生成可靠性
(见 [[2025-mitigating-hallucination-rag-reasoning-agentic]])。工程上依赖 [[faiss]] 等向量索引。

## 相关页
[[embedding]]、[[dpr]]、[[rag]]、[[two-tower]]、[[faiss]]、[[embedding-based-retrieval]]
