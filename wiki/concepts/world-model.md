---
type: concept
subtype: method
tags: [reasoning, planning, world-model, LLM, MCTS]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# World Model

World Model(世界模型)是对环境状态及其在动作作用下如何演化的内部建模——给定当前状态与一个动作,预测下一个状态(以及相应的回报),从而支持智能体在不真正执行动作的情况下进行前瞻式的推理与规划。

## 在本 wiki 中的出现

- [[2023-reasoning-via-planning-rap]]:RAP(Reasoning via Planning)把 LLM 同时当作 World Model 和推理智能体两种角色。LLM 作为 World Model 负责预测推理状态在每一步推理动作之后的演化,使得推理过程可以被表述为一个带 World Model 的规划问题;在此基础上 RAP 用 MCTS 在推理空间中进行规划,从而把 LLM 的推理重新表述为"带 World Model 的规划"。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-policy-guided-causal-state-representation]]:PGCR 是面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示,为构建可靠的环境模型提供更鲁棒的状态输入。
- [[2025-socioverse-world-model-social-simulation]]:SocioVerse 是一个由 LLM agents 驱动、依托 1000 万真实用户池与四个对齐模块的社会模拟 world model,在政治、新闻、经济三大领域复现大规模人群行为。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[monte-carlo-tree-search]]:RAP 在 World Model 提供的推理状态空间上用 MCTS 做规划与搜索。
- [[llm-planning]]:World Model 是把推理转化为规划问题的核心组件。
- [[tree-of-thoughts]]:同样把推理建模为状态空间上的搜索,但不显式引入 World Model 预测状态转移。
- [[chain-of-thought]]:RAP 把 World Model + 规划作为 CoT 这类自回归推理的进阶替代。
- [[markov-decision-process]]:World Model 对"状态—动作—下一状态(及回报)"的建模本质上对应 MDP 的状态转移。
