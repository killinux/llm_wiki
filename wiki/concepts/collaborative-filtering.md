---
type: concept
subtype: method
tags: [recommendation, machine-learning, collaborative-filtering]
created: 2026-05-29
updated: 2026-05-29
sources: 6
---

# Collaborative Filtering

Collaborative Filtering 是一类推荐方法,通过挖掘用户与物品之间的历史交互(如评分、点击),利用相似用户或相似物品的偏好模式来预测某个用户对未交互物品的偏好。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:该论文将 Collaborative Filtering 作为推荐任务的基础范式,并指出传统做法易受混杂偏差影响。其提出的 Deep-Deconf 用深度 VAE 推断 substitute confounders,把推荐建模为 MCMO 因果推断,从而在 Collaborative Filtering 的基础上消除混杂偏差并降低方差。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。
- [[2024-lusifer-llm-user-simulation]]:提出 Lusifer:基于 LLM 的用户模拟环境,在每次交互后增量更新可解释的用户画像,为 RL-based 推荐系统生成动态真实的用户反馈,并在 cold-start 场景超越传统协同过滤基线。
- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。

## 相关

- [[deep-deconf]]
- [[substitute-confounders]]
- [[causal-inference]]
- [[variational-autoencoder]]
- [[recommender-systems]]
- [[confounding-bias]]
