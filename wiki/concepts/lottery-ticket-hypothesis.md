---
type: concept
subtype: method
tags: [neural-network-pruning, sparsity, lottery-ticket-hypothesis, model-compression]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# 彩票假说

Lottery Ticket Hypothesis 指出:一个随机初始化的稠密神经网络中,存在一个稀疏子网络(即"中奖彩票"),当其以原始初始化权重单独训练时,能在相当或更少的迭代次数内达到与原网络相当的精度。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:该综述从任务关系与方法论两个维度为多任务深度推荐系统(MTDRS)建立分类体系。Lottery Ticket Hypothesis 作为稀疏化与参数共享思路的来源之一,为通过提取任务专属子网络来实现参数高效的多任务模型设计提供了理论依据。

## 相关

- [[sparse-sharing]]
- [[sparse-activation]]
- [[multi-task-learning]]
