---
type: concept
subtype: method
tags: [recommendation, offline-rl, bias, exposure-bias, fairness]
created: 2026-05-29
updated: 2026-05-29
sources: 10
---

# Matthew Effect

Matthew Effect(马太效应)指"强者愈强、弱者愈弱"的累积优势现象;在推荐系统语境下,表现为热门物品因被反复曝光而获得越来越多的交互,长尾物品则愈发难以被推荐,导致推荐结果同质化、内容多样性下降。

## 在本 wiki 中的出现

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:该论文将 Matthew Effect 视为 model-based offline RL 推荐中需要缓解的核心问题。其方法 DORL 在悲观惩罚(pessimistic penalty)的基础上引入熵惩罚(entropy penalty),以抑制策略对少数热门物品的过度集中,从而缓解推荐中的马太效应,提升交互式推荐(interactive recommendation)的用户长期满意度。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2024-online-item-cold-start-popularity-aware-meta-learning]]:提出 PAM,一种按物品热度固定切分 meta-learning 任务的 model-agnostic 框架,在流式在线推荐中解决新物品冷启动并缓解马太效应。
- [[2025-policy-guided-causal-state-representation]]:PGCR,面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。

## 相关

- [[recommender-system]]
- [[sequential-recommendation]]
- [[debiasing]]
- [[exposure-bias]]
- [[reinforcement-learning]]
- [[markov-decision-process]]
- [[entropy-regularization]]
- [[recommendation-diversity]]
