---
type: concept
subtype: method
tags: [representation-learning, embedding, self-supervised, pretraining, deep-learning]
created: 2026-05-30
updated: 2026-05-30
sources: 9
---

# 表示学习 (Representation Learning)

表示学习指**自动从数据中学习有用特征表示**(而非人工特征工程)的范式,目标是把原始输入映射到能捕捉语义/结构、便于下游复用的
向量空间([[embedding]])。它是深度学习的核心思想,也是预训练大模型"通用能力"的来源。

## 主要范式
- **监督表示**:用标签端到端学表示(分类/排序的隐层)。
- **自监督 / 预训练**:从无标签数据构造代理任务学表示——掩码预测([[bert]]、[[bart]])、自回归([[gpt-3]])、
  对比学习(contrastive,[[clip]] 图文对齐、SimCLR);[[dinov3]] 等视觉基础模型产出可迁移帧表示。
- **对比 / 度量学习**:拉近正样本、推远负样本,广泛用于检索([[dense-retrieval]])与推荐召回。
- **解耦表示**:[[disentangled-representation-learning]] 让不同维度对应独立语义因子。

## 在本 wiki 的体现
- **推荐**:用户/物品表示是一切的基础(ID [[embedding]] → 序列建模 [[bert4rec]]/[[gru4rec]] → 图表示 [[sigformer]]);
  跨场景统一用户表示见 [[2025-cross-scenario-unified-user-interest-modeling-red-rec]]、[[dupn]]。
- **生成式推荐**:把表示量化为离散码([[rq-vae]])再做序列生成([[hstu]])。
- **LLM agent**:把经历压成自然语言"表示"存入 [[memory-stream|记忆流]],是另一种(符号化)表示学习。

## 相关页
[[embedding]]、[[self-supervised-learning]]、[[contrastive-learning]]、[[clip]]、[[disentangled-representation-learning]]、[[dense-retrieval]]
