---
type: concept
subtype: method
title: 组相对策略优化 (Group Relative Policy Optimization, GRPO)
tags: [reinforcement-learning, rlhf, policy-optimization, reward-design, llm-training]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# 组相对策略优化 (Group Relative Policy Optimization, GRPO)

GRPO 是一种用于 LLM 策略优化的强化学习算法:对同一输入采样一组(group)多条输出,用组内相对奖励(组内回报减去组均值、常再除以标准差)来估计优势(advantage),从而**省去独立的 value/critic 网络**。

## 概述

GRPO 属于 [[ppo|PPO]] 家族,但不再训练单独的价值网络来提供 baseline,而是对每个 prompt 采样若干条轨迹构成一个 group,以组内回报的相对高低作为优势信号(典型形式 A=(R−mean)/std)。这显著降低了显存与训练开销,因此被广泛用于具备可验证奖励(verifiable reward)的推理任务,以及缺乏稳定 value 估计的多智能体、用户模拟器等场景。在本 wiki 中,GRPO 既被直接用作 online RL 优化器,也被多篇论文扩展(MAGRPO、GA-GRPO)或把其"组内相对优势"思想借用到推荐去偏等非典型场景。

## 在本 wiki 中的出现

- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 Dec-POMDP,提出 **MAGRPO(Multi-Agent GRPO)**。基于单智能体 GRPO 思路,每个 turn 每个 agent 采样一组 G 个回复并获得 joint reward,用 group-based Monte Carlo 估计期望回报、advantage 取组内回报减组均值,从而无需大 value model;为简化还去掉了 importance sampling、epsilon clipping 并把 KL 系数设为 0。这是本 wiki 中对 GRPO 最直接的多智能体扩展。
- [[2025-g-ubs-group-aware-user-behavior-simulation]]:提出 **GA-GRPO(Group-Aware GRPO)**,先 SFT 热启动再用 GA-GRPO 做 RL 训练 User Feedback Modeler——对来自不同画像的奖励 {R_T, R_S, R_G} 加权,用组内相对优势 A=(R−mean)/std 优化策略,并加 KL 散度项约束策略不偏离参考策略。
- [[2025-reinforcement-pre-training]]:把 next-token prediction 重构为带可验证奖励的 next-token reasoning,对每个 token 位置采样 G 个 (thinking + prediction) 响应,用 GRPO 做 on-policy 优化,奖励来自字节级 prefix matching,无需人工标注。
- [[2025-sotopia-rl-reward-design-social-intelligence]]:在 [[sotopia-eval|SOTOPIA]] 社交环境中,Stage 2 先 behavior cloning 热身,再用 GRPO 做单轮 online RL,reward 来自训练好的 utterance 级 reward model,用于提升 social intelligence。
- [[2025-multi-agent-evolve]]:Proposer/Solver/Judge 三角色自我博弈,采用 **Task-Relative REINFORCE++** ——对每个角色分别计算 baseline 与归一化 advantage A=(r−μ)/σ,被描述为 per-question 算法(如 GRPO)与单 baseline REINFORCE++ 的插值,在共享 backbone 上同步更新。
- [[2025-user-mirrorer-preference-aligned-user-simulator]]:微调轻量用户模拟器时,主路线为 SFT + [[direct-preference-optimization|DPO]],同时实验了 GRPO;论文报告 DPO 的改进比 GRPO 更显著。
- [[2025-relative-advantage-debiasing-watch-time]]:把 GRPO 的 group-relative 思想迁移到推荐去偏——RAD 的条件分位标签被指出可作为 RL 中奖励变换(如 GRPO)与 listwise 推荐的校准信号(此处是借用思想,而非训练 LLM)。
- [[2025-generative-mmo-simulation]]:GRPO 出现在该 source 中,作为相关 RL 训练方法被引用。
- [[2025-ai-agent-behavioral-science]]:综述类 source 中提及 GRPO 等 RL 方法用于塑造 agent 行为。

## 相关

- [[ppo]] —— GRPO 的基础,GRPO 通过去掉 value 网络对其做了简化。
- [[actor-critic]] —— GRPO 用组内 baseline 取代了 actor-critic 中的 critic。
- [[reinforcement-learning]] —— GRPO 所属的方法大类。
- [[rlhf]] —— GRPO 常用于 RLHF / online RL 的策略优化阶段。
- [[direct-preference-optimization]] —— 另一种省去显式 reward/value 建模的偏好优化路线,常与 GRPO 并列对比(见 user-mirrorer)。
- [[reward-design]] —— GRPO 的组内相对优势对 reward 尺度更鲁棒,与 reward 设计紧密相关。
- [[multi-agent-reinforcement-learning]] —— MAGRPO 将 GRPO 推广到多智能体联合训练。
- [[process-reward-model]] —— 在过程级/可验证奖励场景中常与 GRPO 配合使用。
- [[value-function]] —— GRPO 的核心动机正是避免显式拟合 value function。
