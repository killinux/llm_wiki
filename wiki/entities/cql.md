---
type: entity
subtype: model
tags: [offline-rl, conservative, value-function, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# CQL

CQL(Conservative Q-Learning)是一种 offline RL 算法,通过在训练中对 Q 值施加保守性约束(对数据分布外的动作压低估计的 Q 值),缓解纯离线设置下的价值高估问题。

## 在本 wiki 中的出现
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。
- [[decision-transformer]]
- [[reward-shaping]]
- [[model-based-rl]]
- [[q-learning]]

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:该论文提出 DORL,在 model-based offline RL 的悲观惩罚(pessimistic penalty)上叠加熵惩罚(entropy penalty)以缓解推荐中的马太效应(Matthew effect),从而提升交互式推荐的用户长期满意度。CQL 作为这一研究脉络中代表保守性思想的 offline RL 方法之一出现于该工作的相关讨论中。

## 相关

- [[mopo]]:同属 offline RL,基于悲观性思想,与 DORL 中的悲观惩罚一脉相承
- [[td3]]:常作为 offline/online RL 中的 actor-critic 基础算法
- [[dorl]]:在悲观惩罚基础上加入熵惩罚的推荐 offline RL 方法
- [[offline-rl]]
- [[conservatism]]
- [[matthew-effect]]
