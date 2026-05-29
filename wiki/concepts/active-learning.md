---
type: concept
subtype: method
tags: [active-learning, data-selection, annotation, machine-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# 主动学习

主动学习(active learning)是一种机器学习范式,模型主动挑选信息量最大、最有价值的样本交由人工(或更强的 oracle)进行标注,从而以更少的标注成本获得更好的模型表现。

## 在本 wiki 中的出现

- [[2023-lets-verify-step-by-step]]:在构建步骤级标注数据集 PRM800K 的过程中,OpenAI 使用 active learning 来选择最值得人工标注的模型生成样本——优先呈现当前 reward model 评分较高(看似令人信服)的解答供人工审查,以提升标注效率和数据价值。该论文证明过程监督(PRM)在 MATH 多步数学推理上显著优于结果监督(ORM),best-of-N 达 78.2%。
- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。

## 相关

- [[process-supervision]]
- [[reward-model]]
- [[prm800k]]
- [[rejection-sampling-fine-tuning]]
- [[scalable-oversight]]
- [[2023-lets-verify-step-by-step]]
