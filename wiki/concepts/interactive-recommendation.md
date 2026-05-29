---
type: concept
subtype: method
tags: [recommendation, interactive-recommendation, llm-agent, planning, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 10
---

# interactive recommendation

交互式推荐(interactive recommendation)指系统与用户在多轮交互中持续推荐、并根据用户反馈动态调整策略,以优化长期累积收益而非单次点击的推荐范式。

## 在本 wiki 中的出现

- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2025-contrastive-representation-interactive-recommendation]]:提出 CRIR,用并行对比学习辅助任务 PRCL 增强交互式推荐中 DRL agent 的状态表示,显著提升样本效率。
- [[2025-multi-objective-controllable-decision-transformer]]:提出 MocDT,一种基于 Decision Transformer 的离线 RL 推荐方法,把未来多目标作为控制信号,在推理阶段自回归生成对齐指定目标(累积评分与多样性)的物品序列,无需重训。
- [[2025-meminsight-autonomous-memory-augmentation]]:提出 MemInsight,让 LLM agent 自主从历史交互挖掘语义属性以增强记忆表示与检索,在对话推荐、问答、事件摘要上显著提升(推荐说服力最高 +14%,LoCoMo 召回比 RAG 基线高 34%)。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[2026-lerl-llm-enhanced-rl-long-term-recommendation]]:分层框架 LERL 用 LLM 做高层语义类别规划、用 RL(PPO)做低层细粒度物品选择,在 KuaiSim 模拟器上优化交互式推荐的长期用户满意度并缓解 filter bubble。
- [[2026-proactive-guiding-item-side-fairness]]:HRL4PFG 用分层强化学习"主动引导"用户偏好逐步转向长尾物品,在 KuaiRec/KuaiRand 上同时取得最高累积奖励、最长交互长度与最低 Gini Index,在不牺牲满意度的前提下提升 item-side 公平。
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。
- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段,在用户意图模糊时兼顾追问效率与残余不确定性驱动的多样化推荐。

## 相关

- [[long-term-recommendation]]
- [[llm-agents|llm-agent]]
- [[reinforcement-learning]]
- [[planning]]
