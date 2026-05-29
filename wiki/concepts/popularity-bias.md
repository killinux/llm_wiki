---
type: concept
subtype: method
tags: [recommendation, bias, user-simulation]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# popularity bias

流行度偏差(popularity bias)指推荐系统倾向于过度推荐热门物品、而忽视长尾物品的系统性偏差。

## 在本 wiki 中的出现

- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[2026-proactive-guiding-item-side-fairness]]:HRL4PFG 用分层强化学习"主动引导"用户偏好逐步转向长尾物品,在 KuaiRec/KuaiRand 上同时取得最高累积奖励、最长交互长度与最低 Gini Index,在不牺牲满意度的前提下提升 item-side 公平。
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。
- [[2026-graphrag-irl]]:GraphRAG-IRL 把 graph-grounded 特征、Maximum Entropy 逆强化学习预排序与 persona-guided LLM 重排融合,LLM 只对 IRL 短候选列表做语义重排,在 MovieLens/KuaiRand 上 NDCG@10 比监督基线提升 15.7%/16.6%。

## 相关

- [[user-simulation]]
- [[cross-domain-recommendation]]
- [[collaborative-filtering]]
