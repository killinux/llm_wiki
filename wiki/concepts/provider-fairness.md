---
type: concept
subtype: method
tags: [fairness, recommendation, exposure-allocation, two-sided-market]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Provider fairness

提供方公平性(Provider fairness)指在推荐或排序系统中,确保各内容/服务提供方能获得公平的曝光与流量分配,而非仅以用户侧短期准确性为唯一目标。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。
- [[2026-proactive-guiding-item-side-fairness]]:HRL4PFG 用分层强化学习"主动引导"用户偏好逐步转向长尾物品,在 KuaiRec/KuaiRand 上同时取得最高累积奖励、最长交互长度与最低 Gini Index,在不牺牲满意度的前提下提升 item-side 公平。
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。

## 相关

- [[exposure-allocation]]
- [[two-sided-fairness]]
- [[reranking]]
- [[bankruptcy-problem]]
- [[popularity-bias]]
- [[item-side-fairness]]
- [[hierarchical-reinforcement-learning]]
- [[llm-agent-recommendation]]
