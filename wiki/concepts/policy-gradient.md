---
type: concept
subtype: method
tags: [reinforcement-learning, policy-gradient, actor-critic, rlhf]
created: 2026-05-30
updated: 2026-05-30
sources: 8
---

# 策略梯度 (Policy Gradient)

策略梯度是一类**直接对参数化策略 π_θ 求梯度、沿提升期望回报方向更新**的强化学习方法,区别于先学价值函数再导出策略的 value-based 方法。
适合**连续/高维动作空间**与随机策略,是现代 RLHF 与 RL 推荐的基础。

## 核心
- **REINFORCE**:`∇J = E[∇log π_θ(a|s) · R]`,用回报加权 log 概率梯度;高方差。
- **基线 / 优势**:减去基线 V(s) 得**优势** A(s,a)=Q−V 降方差 → [[actor-critic|Actor-Critic]](critic 估值、actor 更新策略);A2C/A3C。
- **信赖域 / 截断**:TRPO、**PPO**(clip 限制更新步长)稳定训练,是 [[rlhf|RLHF]] 的主力优化器。
- **确定性策略**:DDPG/TD3 用于连续控制(推荐里 [[2023-rlur-user-retention-short-video]] 即 DDPG 思路)。

## 在本 wiki 的体现
- **RLHF / 对齐**:[[instructgpt]] 用 PPO 对齐;偏好优化的 [[direct-preference-optimization|DPO]] 则绕开显式 RL。
- **RL 推荐**:策略梯度 + 重要性采样做离线校正,见 [[2023-two-stage-constrained-actor-critic]]、[[2024-unex-rl-multi-stage-recommender]](多阶段 policy gradient + 方差缩减);
  与 [[reinforcement-learning-for-recommendation]] 的 offline 设定结合时需抑制 OOD 外推。
- **多智能体**:[[multi-agent-reinforcement-learning]] 的 MAGRPO 等([[2025-llm-collaboration-marl-magrpo]])。

## 相关页
[[reinforcement-learning]]、[[actor-critic]]、[[ppo]]、[[rlhf]]、[[reinforcement-learning-for-recommendation]]
