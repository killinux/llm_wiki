---
type: concept
subtype: method
tags: [deep-learning, sequence-modeling, recurrent-neural-network]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# LSTM

LSTM(Long Short-Term Memory)是一种带有门控机制(gating)的循环神经网络(RNN),通过引入记忆单元(cell state)以及输入门、遗忘门和输出门来缓解长序列训练中的梯度消失问题,从而建模长程依赖。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:该综述从任务关系与方法论两个维度为多任务深度推荐系统(MTDRS)建立分类体系。在方法论维度的"专家共享(expert sharing)"分类下,综述提到代表模型 MoSE 使用 LSTM 来建模用户的序列行为,使专家网络能够捕捉随时间变化的兴趣表示,从而服务于多任务的共享/特定表示学习。在此 LSTM 充当推荐场景中处理序列依赖的具体序列建模组件。

## 相关

- [[multi-task-learning]]
- [[sequential-recommendation]]
- [[recommender-system]]
- [[reinforcement-learning]]
