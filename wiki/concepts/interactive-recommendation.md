---
type: concept
subtype: method
tags: [recommendation, interactive-recommendation, llm-agent, planning, reinforcement-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 6
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

## 相关

- [[long-term-recommendation]]
- [[llm-agent]]
- [[reinforcement-learning]]
- [[planning]]
