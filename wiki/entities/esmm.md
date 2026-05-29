---
type: entity
subtype: model
tags: [multi-task-learning, recommendation, ctr, cvr, deep-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# ESMM

ESMM(Entire Space Multi-Task Model)是一种用于推荐系统的多任务深度模型,通过在完整曝光样本空间上联合建模 CTR 与 CVR,并借助 CTCVR 这一辅助任务,缓解传统 CVR 估计中的样本选择偏差(sample selection bias)与数据稀疏问题。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:作为级联(cascaded)任务关系的代表模型。ESMM 共享 embedding,在全空间(entire space)上按 impression→click→conversion 的行为序列建模,利用 CTCVR = CTR × CVR 的依赖关系解决样本选择偏差(SSB)与数据稀疏(DS),并被列入综述 Table 1 的级联模型清单(与 ESM²、AITM、ESCM² 等并列)。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。

## 相关

- [[multi-task-learning]]
- [[multi-task-recommendation]]
- [[mmoe]]
- [[ple]]
- [[ctr]]
- [[cvr]]
- [[sample-selection-bias]]
- [[recommendation]]
- [[merrec]]
- [[mercatran]]
