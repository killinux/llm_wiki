---
type: concept
subtype: method
tags: [deep-learning, neural-network, representation-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# 深度神经网络

深度神经网络(Deep Neural Network, DNN)是由多层非线性变换堆叠而成的神经网络模型,通过端到端学习从原始输入中自动提取多层次的特征表示。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:该综述聚焦于多任务深度推荐系统(MTDRS),DNN 是其底层的核心建模手段——推荐系统借助深度神经网络对用户、物品及上下文特征进行表示学习,并在此基础上构建多任务学习架构,从任务关系与方法论两个维度对代表模型进行分类。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[multi-task-learning]]
- [[recommender-system]]
- [[representation-learning]]
- [[feature-embedding]]
