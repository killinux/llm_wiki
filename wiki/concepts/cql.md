---
type: concept
subtype: method
tags: [offline-rl, conservative-q-learning, recommendation, q-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# CQL

CQL(Conservative Q-Learning,保守 Q 学习)是一种离线强化学习(offline RL)算法,通过对未见动作的 Q 值施加保守正则化来抑制分布外动作的价值高估,从而在仅依赖固定数据集训练时获得更稳健的策略。

## 在本 wiki 中的出现

- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[offline-rl]]
- [[decision-transformer]]
- [[reward-shaping]]
- [[model-based-rl]]
- [[q-learning]]
