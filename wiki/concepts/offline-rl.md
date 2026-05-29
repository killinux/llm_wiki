---
type: concept
subtype: method
tags: [reinforcement-learning, offline-rl, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Offline RL

Offline RL(离线强化学习)是一类不与环境实时交互、仅依赖预先收集的固定数据集来学习策略的强化学习方法,其核心挑战在于应对分布偏移(distribution shift)并避免对数据集之外动作的过度乐观估计。

## 在本 wiki 中的出现

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:该工作在 model-based offline RL 框架下展开,在其悲观惩罚(pessimistic penalty)的基础上引入熵惩罚,提出 DORL,用以缓解交互式推荐中的马太效应(Matthew effect),从而提升用户的长期满意度。在此场景中,Offline RL 作为从离线交互日志中学习推荐策略的基础范式,其悲观惩罚机制是 DORL 进行扩展和改进的出发点。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。

## 相关

- [[model-based-rl]]
- [[pessimism]]
- [[distribution-shift]]
- [[matthew-effect]]
- [[interactive-recommendation]]
- [[reinforcement-learning]]
- [[decision-transformer]]
- [[reward-shaping]]
- [[conservative-q-learning]]
- [[world-model]]
- [[user-simulation]]
