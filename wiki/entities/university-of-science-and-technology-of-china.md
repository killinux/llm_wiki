---
type: entity
subtype: lab
tags: [recommendation, llm-agent, planning, debiasing, scaling-law, simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 11
---

# University of Science and Technology of China

中国科学技术大学（USTC），在本 wiki 中主要以 LLM 推荐 agent、推荐系统去偏、全流程数据集、大规模推荐模型 scaling、基于 LLM 智能体的推荐与经济模拟等方向的研究机构身份出现。

## 在本 wiki 中的出现

- [[2023-recommender-ai-agent-interec]]：提出 InteRecAgent，以 LLM 为大脑、传统推荐模型为工具，通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent，并蒸馏出 7B 的 RecLlama。
- [[2024-llm-learnable-planners-long-term-recommendation]]：提出 BiLLP 双层可学习 LLM 规划框架（Planner/Reflector 宏观 + Actor/Critic 微观），在稀疏推荐数据上以 LLM 规划能力做长期推荐，Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2025-debias-can-be-unreliable]]：揭示用随机曝光数据集传统评估去偏推荐不可靠，提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2024-agentic-feedback-loop-recommendation]]：提出 AFL，让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作，同时提升推荐（平均 +11.52%）与用户模拟（平均 +21.12%），且不放大流行度/位置偏差。
- [[2024-recflow-full-flow-recommendation-dataset]]：首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集，用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2024-large-recommendation-models-scaling]]：华为诺亚与 USTC 的工作，系统评估 large recommendation models 的 scaling law，以生成式推荐模型 HSTU 为代表，在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。
- [[2025-multi-objective-controllable-decision-transformer]]：提出 MocDT，一种基于 Decision Transformer 的离线 RL 推荐方法，把未来多目标作为控制信号，在推理阶段自回归生成对齐指定目标（累积评分与多样性）的物品序列，无需重训。
- [[2025-mmoagent-economic-simulation-mmo]]：提出 MMOAgent，一个基于 LLM 的 Generative Agent-Based Modeling 框架，用具备 profile/感知/推理/记忆/行动的 LLM 智能体模拟 MMO 游戏经济，涌现出角色分化与符合供需规律的价格波动。
- [[2026-fuxi-linear]]：线性复杂度的时间感知序列推荐模型，解耦时间与语义信号、用可学习核近似相对位置编码，在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。
- [[2026-proactive-guiding-item-side-fairness]]：HRL4PFG 用分层强化学习"主动引导"用户偏好逐步转向长尾物品，在 KuaiRec/KuaiRand 上同时取得最高累积奖励、最长交互长度与最低 Gini Index，在不牺牲满意度的前提下提升 item-side 公平。
- [[2026-trirec-tri-party-agent-recommendation]]：TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架，让物品 agent 主动个性化自我推销，再由平台做曝光感知的多目标重排，在精度、公平与物品效用上同时提升。

## 相关

- [[interec-agent]]
- [[billp]]
- [[huawei-noah-ark-lab]]
- [[recommender-systems|recommendation-system]]
- [[debiased-recommendation]]
- [[large-recommendation-models]]
- [[llm-agents|llm-agent]]
- [[generative-agent-based-modeling]]
- [[decision-transformer]]
- [[sequential-recommendation]]
- [[item-side-fairness]]
- [[hierarchical-reinforcement-learning]]
