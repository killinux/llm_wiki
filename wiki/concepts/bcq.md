---
type: concept
subtype: method
tags: [offline-rl, batch-rl, recommendation, rl]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# BCQ

BCQ(Batch-Constrained deep Q-learning)是一种 offline / batch 强化学习方法,通过约束策略只在与离线数据分布相近的动作上取值,缓解 off-policy 学习中的外推误差(extrapolation error),常被用作离线 RL 推荐系统的经典对照基线。

## 在本 wiki 中的出现

- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法(含 BCQ 类离线方法)的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。

## 相关

- [[offline-rl]]
- [[model-based-rl]]
- [[reward-shaping]]
- [[rl-based-recommendation]]
- [[extrapolation-error]]
