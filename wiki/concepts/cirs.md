---
type: concept
subtype: method
tags: [offline-rl, recsys, reward-shaping, world-model, uncertainty]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# CIRS

CIRS(Causal Inference for Recommendation Systems / 因果干预推荐方法)是一类用于推荐系统的强化学习方法,旨在通过对反馈回路中的混杂与偏差进行建模与修正,缓解 model-based offline RL 在推荐场景中因 world model 估计误差导致的策略退化问题。

## 在本 wiki 中的出现

- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2026-lerl-llm-enhanced-rl-long-term-recommendation]]:分层框架 LERL 用 LLM 做高层语义类别规划、用 RL(PPO)做低层细粒度物品选择,在 KuaiSim 模拟器上优化交互式推荐的长期用户满意度并缓解 filter bubble。
- [[2026-fairness-begins-with-state-dsrm-hrl]]:DSRM-HRL 用扩散模型把被 popularity bias 污染的用户状态提纯回真实偏好流形,再用分层 RL 解耦长期公平与短期参与,在 KuaiRec/KuaiRand 上实现 accuracy 与 fairness 更优的 Pareto 前沿。

## 相关

- [[reward-shaping]]
- [[model-based-offline-rl]]
- [[world-model]]
- [[uncertainty-penalty]]
- [[recommender-systems|recommendation-system]]
- [[agentic-feedback-loop]]
- [[user-simulation]]
