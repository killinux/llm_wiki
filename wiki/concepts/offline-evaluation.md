---
type: concept
subtype: method
tags: [recommender-system, evaluation, offline-rl, counterfactual, simulator]
created: 2026-05-30
updated: 2026-05-30
sources: 7
---

# 离线评估 (Offline Evaluation)

离线评估指**不上线**、仅用历史日志或仿真器评估推荐/策略效果的方法。它规避了在线 A/B 的成本与风险,但核心难点是
**日志由旧策略产生**(off-policy)且存在曝光/选择偏差,导致离线指标与线上效果**未必一致**。

## 两大路线
- **反事实/off-policy 估计**:用 IPS(逆倾向加权)、doubly robust 等校正旧策略的曝光偏差,估计新策略的期望收益;
  采样与估计的可靠性见 [[2025-sampling-strategies-offline-recommender-evaluation]]。偏差严重时离线估计**不可靠**([[2025-debias-can-be-unreliable]])。
- **仿真器 (simulator)**:构造用户行为模拟器在沙盒里试策略——[[2023-kuaisim-recommender-simulator]]、[[easyrl4rec]];
  LLM 用户模拟器([[2024-lusifer-llm-user-simulation]]、[[2025-simuser-llm-user-simulation-recsys]])是新方向,但需验证是否真对齐人类(见 [[2025-can-llm-agents-simulate-human-behavior]])。

## 与 offline RL 的关系
离线评估是 [[reinforcement-learning-for-recommendation|推荐 RL]] 落地的前提:offline RL 既要离线**学**策略,也要离线**评**策略,
两者都受 OOD 与分布偏移困扰。基准化努力见 [[2025-sim4ia-bench-user-simulation-benchmark]]、[[2026-ab-agent-recsys-evaluation]]。

## 相关页
[[recommender-systems]]、[[reinforcement-learning-for-recommendation]]、[[offline-rl]]、[[causal-inference]]、[[user-simulation]]
