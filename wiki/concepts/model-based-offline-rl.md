---
type: concept
subtype: method
tags: [reinforcement-learning, offline-rl, model-based, world-model, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources:
  - "[[2023-dorl-matthew-effect-offline-rl-recommendation]]"
---

# 基于模型的离线强化学习 (Model-Based Offline RL)

基于模型的离线强化学习是一类离线强化学习方法：先用固定的、已收集好的离线数据集学习一个环境(动态/奖励)模型,再在该学习到的模型中做策略规划或 rollout,从而无需与真实环境进行在线交互即可优化策略。

## 概述

离线 RL 的核心难题是分布外(out-of-distribution)动作带来的价值高估与误差累积。基于模型的方法通过显式学习一个 world model 来生成额外的(想象的)轨迹以扩充数据,从而提升样本效率;但学习到的模型在数据稀疏区域不可靠,因此这类方法通常配合**保守化机制**——例如对模型预测的不确定性施加惩罚,把奖励向下修正,避免策略钻进模型误差大的区域。这一范式被广泛迁移到推荐系统场景:把用户视作环境、把推荐序列视作交互,从而在不做线上实验的情况下优化长期收益。

## 在本 wiki 中的出现

- [[mopo]]:作为基于模型的离线 RL 的代表性方法之一,以"在学习到的动态模型上做 rollout、并对模型不确定性施加惩罚"的思路定义了该范式的基本形态,是后续工作引用的方法学基础。
- [[dorl]] / [[2023-dorl-matthew-effect-offline-rl-recommendation]]:将基于模型的离线 RL 用于推荐系统,针对离线 RL 推荐中出现的 Matthew effect(强者愈强、推荐过度同质化)问题进行改造,在该范式下重新设计奖励/惩罚以缓解长期反馈循环带来的偏差。
- [[cirs]]:在基于模型的离线 RL 框架下处理推荐中的因果/过滤气泡问题,体现了"先学环境模型、再在模型内优化推荐策略"的典型用法。
- [[uncertainty-penalty]]:对应该范式中的关键保守化组件——对学习到的模型预测施加不确定性惩罚,把这一机制作为基于模型的离线 RL 控制模型误差的核心手段加以讨论。
- [[dynamic-reward-shaping]]:与基于模型的离线 RL 结合,通过在模型 rollout 过程中动态调整(塑形)奖励来引导策略,属于该范式下的奖励设计技术。
- [[reference-user-selection]]:在基于模型的离线 RL 的推荐建模中作为相关技术出现,涉及如何选取参考用户以更好地构建/利用学习到的环境模型。

## 相关

- [[uncertainty-penalty]] — 该范式中用于抑制模型误差的核心保守化机制
- [[dynamic-reward-shaping]] — 在模型 rollout 中塑形奖励的配套技术
- [[mopo]] — 代表性的基于模型的离线 RL 方法
- [[dorl]] — 面向推荐、缓解 Matthew effect 的应用
- [[cirs]] — 在该范式下处理推荐因果/过滤气泡的方法
- [[reference-user-selection]] — 推荐场景中与环境模型构建相关的技术
