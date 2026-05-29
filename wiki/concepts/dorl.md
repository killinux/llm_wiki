---
type: concept
subtype: method
tags: [recommendation, reinforcement-learning, offline-rl, long-term-recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# DORL

DORL(Debiased model-based Offline RL)是一类面向推荐系统的离线强化学习方法,通过对 world model 的奖励估计进行去偏与不确定性惩罚,以优化推荐的长期累积收益。

## 在本 wiki 中的出现

- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。

## 相关

- [[model-based-offline-rl]]
- [[reward-shaping]]
- [[world-model]]
- [[long-term-recommendation]]
- [[uncertainty-penalty]]
