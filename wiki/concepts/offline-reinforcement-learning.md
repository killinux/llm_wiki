---
type: concept
subtype: method
tags: [offline-rl, reinforcement-learning, rl-based-recsys, decision-transformer, model-based-rl, recommender-system]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# 离线强化学习 (Offline Reinforcement Learning / Offline RL)

离线强化学习指仅从预先收集的固定历史交互日志中学习决策策略、训练全程不与真实环境在线交互的强化学习范式,也称 batch RL。

## 概述

[[reinforcement-learning]] 在推荐、出价等序列决策场景表现强大,但在线探索成本高、风险大,因此实践中转向只用 logged data 训练的 offline RL。其核心难点是 distribution shift 与 value overestimation:函数逼近器会对日志未覆盖的 out-of-distribution(state, action)外推出过高 Q 值,导致策略发散。围绕这一难点形成两条主流技术路线——model-free 的保守性方法(如 [[bcq]]、[[cql]]、[[iql]])和 model-based 方法(如 [[mopo]],先学 [[world-model]] 再在其中训练策略),以及把 offline RL 重述为 return-conditioned 序列建模的 [[decision-transformer]] 路线。在本 wiki 中,offline RL 几乎都被用在 [[rl-based-recsys]] / [[recommender-systems|recommender-system]] 方向,用来优化以累积奖励衡量的长期用户满意度。

## 在本 wiki 中的出现

- [[2023-dorl-matthew-effect-offline-rl-recommendation]](DORL):把 model-based offline RL([[mopo]])用于交互式推荐,发现直接套用保守性会加剧 [[matthew-effect]] 与 filter bubble,提出在悲观惩罚之外加 entropy penalty 做反事实探索,是本 wiki 离线 RL 推荐方向的代表性起点。
- [[2024-roler-reward-shaping-offline-rl-recsys]](ROLeR):沿用 DORL 的两阶段 model-based 离线 RL 流程,指出 [[world-model]] 的 reward 估计不准是关键瓶颈,用基于聚类/kNN 的非参数 reward shaping 修正奖励、并以聚类质量替代 ensemble 做不确定性惩罚。
- [[2025-darlr-dual-agent-offline-rl-recsys]](DARLR):面向 model-based offline RL 推荐,批评 DORL/ROLeR 的 frozen reward 与静态不确定性惩罚,引入 selector 与 recommender 双 agent,在策略学习过程中动态精炼 world model 奖励函数。
- [[2025-maximum-in-support-return-modeling]](MDT4Rec):把推荐建模为 [[markov-decision-process]],用 off-policy-evaluation 式 offline RL 训练;在 [[decision-transformer]] 基础上把 trajectory stitching 移到 action inference 阶段,并用 LLM 先验初始化,体现 DT 一支离线 RL 推荐工作。
- [[2025-multi-objective-controllable-decision-transformer]](MocDT):借鉴 offline RL 中的 upside-down RL / return-to-go 条件建模,把"未来多目标"作为控制信号在推理阶段自回归生成物品序列,将 DT 类离线 RL 推荐从单目标推广到多目标可控。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]](TADT-CSA):面向工业级生成式推荐改进 [[decision-transformer]] 这一离线 RL 路线,用 Temporal Advantage 信号与对比式状态抽象缓解 DT 的轨迹拼接弱、状态空间过大问题。
- [[2025-energy-guided-diffusion-rl-recommendation]](DAC4Rec):指出 offline RL 推荐依赖对 behavior policy 的模仿、表达力不足,用 diffusion 策略替代 DT 的行为建模,并加 Q 值引导与能量引导采样建模长期偏好。
- [[2026-lerl-llm-enhanced-rl-long-term-recommendation]](LERL):把推荐作为序列决策用 [[reinforcement-learning]] 优化长期累积奖励,以分层 RL(LLM 高层规划 + 低层 [[ppo]])缓解 [[filter-bubble]],与离线 RL 推荐评测生态(KuaiRand/KuaiRec 模拟器)一脉相承。

## 相关

- [[reinforcement-learning]] —— offline RL 的上位范式(在线/离线之分)。
- [[rl-based-recsys]] —— 本 wiki 中 offline RL 的主要应用场景。
- [[markov-decision-process]] —— offline RL 的形式化建模基础。
- [[decision-transformer]] —— 把 offline RL 重述为 return-conditioned 序列建模的代表路线。
- [[world-model]]、[[mopo]] —— model-based offline RL 的核心组件与代表方法。
- [[bcq]]、[[cql]]、[[iql]] —— model-free offline RL 的保守性代表方法。
- [[behavior-cloning]] —— offline RL 在弱策略改进时容易退化到的纯模仿形式。
- [[matthew-effect]]、[[filter-bubble]]、[[long-term-recommendation]]、[[user-retention]] —— offline RL 推荐关注与缓解的下游问题/目标。
- [[dorl]]、[[mocdt]]、[[rlur]] —— 本 wiki 中相关的方法/实体页。
