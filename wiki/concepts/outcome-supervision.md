---
type: concept
subtype: method
tags: [reward-model, supervision, reasoning, math, RLHF]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# 结果监督

结果监督(outcome supervision)是一种只对模型最终答案的正确与否提供监督信号的训练范式,据此训练出的奖励模型称为 ORM(Outcome-supervised Reward Model)。

## 在本 wiki 中的出现

- [[2023-lets-verify-step-by-step]]:在该论文中,结果监督(ORM)作为对照基线出现。OpenAI 证明过程监督(PRM)在 MATH 多步数学推理任务上显著优于结果监督(ORM),其 best-of-N 达到 78.2%,并开源了步骤级标注数据集 PRM800K。

## 相关

- [[process-supervision]]
- [[reward-model]]
- [[prm800k]]
- [[best-of-n]]
- [[math-benchmark]]
