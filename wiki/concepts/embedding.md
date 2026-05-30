---
type: concept
subtype: method
tags: [representation-learning, embedding, retrieval, deep-learning]
created: 2026-05-30
updated: 2026-05-30
sources: 10
---

# 嵌入 (Embedding)

嵌入是把离散对象(词、用户、物品、图像、节点)映射到**低维稠密向量空间**的表示,使语义/行为相近的对象在空间中靠近,
便于用内积/距离做相似度计算。它是深度学习与现代检索、推荐、多模态系统的通用底座。

## 关键性质与用途
- **相似度检索**:向量内积/余弦近似语义相关,支撑 [[dense-retrieval|稠密检索]] 与推荐召回(双塔 [[two-tower]]/[[dssm]] 各出一个塔的 embedding)。
- **可迁移表示**:预训练 embedding(词向量、[[clip]] 图文、[[bert]])可下游复用;[[representation-learning|表示学习]]的产物。
- **ANN 加速**:大规模检索用 [[faiss]] 等近似最近邻索引。
- **多模态对齐**:[[clip]] 把图文映射到同一空间;视频帧 embedding 聚合见 [[2026-compressed-video-aggregator]]。

## 在推荐中的角色
用户/物品 ID 与特征经 embedding 层进入模型,是 CTR 模型([[deepfm]]、[[autoint]])与序列推荐([[bert4rec]]、[[gru4rec]])的输入基础;
embedding 的冷启动([[2024-prompt-tuning-item-cold-start]])、多 embedding([[multi-embedding]])、量化(生成式推荐的离散码 [[rq-vae]])都是活跃方向。

## 相关页
[[representation-learning]]、[[dense-retrieval]]、[[embedding-based-retrieval]]、[[two-tower]]、[[clip]]、[[faiss]]
