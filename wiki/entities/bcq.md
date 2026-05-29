---
type: entity
subtype: model
tags: [offline-rl, batch-rl, q-learning, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# BCQ

BCQ(Batch-Constrained deep Q-learning)是一种 offline / batch reinforcement learning 算法,通过约束策略只在数据集中出现过的动作附近选择,以缓解 off-policy 学习中的分布外(out-of-distribution)动作带来的外推误差。

## 在本 wiki 中的出现
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。
- [[hierarchical-rl]]
- [[diffusion-models|diffusion-model]]
- [[recommendation-fairness]]
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法(含 BCQ 类离线方法)的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[model-based-rl]]
- [[reward-shaping]]
- [[rl-based-recommendation]]
- [[extrapolation-error]]

- 在 [[2023-dorl-matthew-effect-offline-rl-recommendation]] 中,BCQ 作为 offline RL 的对比 / 基线方法出现。该论文提出 DORL,在 model-based offline RL 的悲观惩罚上加入熵惩罚以缓解推荐中的马太效应,提升交互式推荐的用户长期满意度;BCQ 属于其讨论的 offline RL 方法范畴。

## 相关

- [[offline-rl]]
- [[batch-rl]]
- [[dorl]]
- [[matthew-effect]]
- [[interactive-recommendation]]
