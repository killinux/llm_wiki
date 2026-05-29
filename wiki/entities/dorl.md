---
type: entity
subtype: model
tags: [offline-rl, recommendation, model-based-rl, matthew-effect]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# DORL

DORL 是一种基于模型的离线强化学习(model-based offline RL)推荐方法,通过在悲观惩罚之外引入熵惩罚来缓解推荐系统中的马太效应(Matthew effect),从而提升交互式推荐的用户长期满意度。

## 在本 wiki 中的出现
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。
- [[popularity-bias]]
- [[offline-reinforcement-learning]]
- [[diffusion-models|diffusion-model]]
- [[hierarchical-reinforcement-learning]]
- [[recommendation-fairness]]
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[model-based-offline-rl]]
- [[reward-shaping]]
- [[world-model]]
- [[long-term-recommendation]]
- [[uncertainty-penalty]]

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:提出 DORL,在 model-based offline RL 的悲观惩罚上加入熵惩罚以缓解推荐中的马太效应,提升交互式推荐的用户长期满意度。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[offline-rl]]
- [[model-based-rl]]
- [[matthew-effect]]
- [[interactive-recommendation]]
- [[pessimism-penalty]]
- [[roler]]
