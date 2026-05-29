---
type: concept
subtype: method
tags: [reinforcement-learning, actor-critic, policy-gradient, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 12
---

# Actor-Critic

Actor-Critic 是一类强化学习方法,由负责输出动作的 actor(策略)与负责评估动作价值的 critic(价值函数)协同组成:critic 用价值估计为 actor 提供低方差的梯度信号,actor 据此更新策略。

## 在本 wiki 中的出现

- [[2023-two-stage-constrained-actor-critic]]:提出两阶段约束式 actor-critic(TSCAC),以最大化短视频 WatchTime 为主目标,同时用软约束平衡 Like/Share 等稀疏交互信号;已在快手生产系统全量上线。这里 Actor-Critic 是承载多目标约束优化的核心 RL 框架。
- [[2023-multi-task-recommendations-with-rl]]:RMTL 用 actor-critic 强化学习按 session 级序列动态生成多任务损失权重,替代固定常数加权,在 RetailRocket 与 Kuairand 上提升 CTR/CTCVR 的 AUC。这里 Actor-Critic 被用作动态权重生成器,critic 评估状态以指导各任务损失的加权策略。
- [[2023-hyper-actor-critic-recommendation]]:提出 Hyper-Actor Critic(HAC)框架,把推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,并用对齐与监督模块稳定大动作空间下的 RL 推荐策略学习。这里 Actor-Critic 是处理超大离散动作空间(推荐列表)的策略学习基座。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-value-function-decomposition-mrp]]:提出把在线 RL 推荐中的标准 TD loss 分解为 state TD 与 action TD 两个独立目标,以分离随机策略与随机用户环境两类噪声,获得更准确、更快收敛、对动作探索更鲁棒的价值函数,可通用插入 A2C/DQN/DDPG/HAC/SQN。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[reinforcement-learning]]
- [[ppo]]
- [[rcpo]]
- [[constrained-mdp]]
- [[policy-gradient]]
- [[value-function]]
- [[recommender-systems]]
- [[sequential-recommendation]]
- [[llm-agent]]
- [[reward-shaping]]
- [[model-based-rl]]
