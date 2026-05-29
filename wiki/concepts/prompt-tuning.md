---
type: concept
subtype: method
tags: [prompt-tuning, parameter-efficient, fine-tuning, adaptation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Prompt tuning

Prompt tuning 是一种参数高效的模型适配方法:冻结预训练模型的全部权重,仅训练一组附加在输入端的连续可学习向量(soft prompt),以低成本驱动模型适应下游任务。

## 在本 wiki 中的出现

- [[2023-divide-and-conquer-ebr]]:该工作把推荐召回的 embedding-based retrieval 拆成"物料聚类 + 簇内并行检索 + 可控合并"的分治结构,并采用 prompt-like 的多任务适配方式来统一不同检索子任务。这里 Prompt tuning 思路的角色是作为轻量的多任务适配机制,使单一模型/检索框架能够在不同簇与任务间共享主体参数而仅通过 prompt 区分。公开数据集上 Recall 最高提升约 40%,方案已在快手线上部署。

## 相关

- [[soft-prompt]]
- [[prefix-tuning]]
- [[lora]]
- [[parameter-efficient-fine-tuning]]
- [[in-context-learning]]
- [[multi-task-learning]]
- [[embedding-based-retrieval]]
