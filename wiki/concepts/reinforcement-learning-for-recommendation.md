---
type: concept
subtype: method
tags: [reinforcement-learning, recommender-system, offline-rl, long-term-value, user-retention]
created: 2026-05-30
updated: 2026-05-30
sources: 12
---

# 推荐中的强化学习 (RL for Recommendation)

把推荐建模为**序贯决策 (MDP)**:状态为用户当前情境与历史,动作为推荐的 item / 列表,奖励为反馈(点击、时长、留存),
目标是最大化**长期累计收益**而非单步即时指标。相比监督式 CTR/CVR 排序,它显式优化**跨期价值**与生态健康。

## 为什么需要 RL
- **长期 vs 短期**:贪心优化点击会损害留存 / 多样性;RL 直接优化长期目标,如 [[2023-rlur-user-retention-short-video]](最小化累计回访时间,快手上线)。
- **多目标 / 约束**:时长与稀疏交互的平衡,如 [[2023-two-stage-constrained-actor-critic]]、[[2023-multi-task-recommendations-with-rl]]。
- **生态/反馈回路**:缓解马太效应,如 [[2023-dorl-matthew-effect-offline-rl-recommendation]]。

## 核心难点:离线与外推
线上真实试错代价高,故主流是 **offline RL**——只用日志数据学习,核心风险是 **OOD 动作外推误差**:
- 约束类:[[bcq]](只取数据内动作)、[[cql]](压低 OOD 动作 Q 值);
- 推荐专用:[[2024-roler-reward-shaping-offline-rl-recsys]]、[[2025-darlr-dual-agent-offline-rl-recsys]]、[[2024-edt4rec-max-entropy-decision-transformer]]。
- **仿真器**评估:用 [[2023-kuaisim-recommender-simulator]]、[[easyrl4rec]] 等离线沙盒做策略评估,规避线上风险。

## 方法谱系
价值/策略类(DQN、DDPG、actor-critic)、序列建模类([[decision-transformer]] 及其推荐变体)、生成式(GFlowNet 列表推荐 [[2023-gflownet-listwise-recommendation]])、
以及与 [[contextual-bandits]] 的分界(无显著状态转移时退化为 bandit)。

## 相关页
[[reinforcement-learning]]、[[offline-rl]]、[[recommender-systems]]、[[user-retention]]、[[contextual-bandits]]、[[decision-transformer]]
