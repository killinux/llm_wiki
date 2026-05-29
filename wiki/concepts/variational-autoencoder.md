---
type: concept
subtype: method
tags: [generative-model, latent-variable, variational-inference, deep-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# Variational Autoencoder

Variational Autoencoder(VAE)是一种基于变分推断的深度生成模型,用 encoder 将输入数据映射到隐变量(latent variable)的近似后验分布,再由 decoder 从该隐空间采样并重建数据,从而学习数据的概率生成过程。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:该工作的 Deep-Deconf 方法使用深度 VAE 来推断 substitute confounders(替代混杂变量),将推荐建模为 MCMO(multi-cause multi-outcome)因果推断问题,从而消除混杂偏差并降低估计方差。VAE 在此作为隐变量推断工具,用于从观测的多因暴露中恢复潜在的混杂结构。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-deep-interest-life-cycle-network]]:提出 DILN,显式建模用户兴趣生命周期(emergent/stable/declining)并用 VQ 聚类离散化、注入 MMOE 排序模型,Lofter 线上 CTR +0.38%、CVR +1.04%、时长 +0.25%。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[2025-perscen-multi-scenario-matching]]:首个将用户个性化建模引入多场景匹配(召回)的两塔方法,用 user-specific 特征图+轻量 GNN、向量量化的场景偏好与渐进式 GLU,在 KuaiRand-Pure 与 Alimama 上以高效率刷新召回性能。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。

## 相关

- [[deconfounding]]
- [[multi-cause-confounders]]
- [[confounding-bias]]
- [[causal-inference]]
- [[deep-deconf]]
- [[deconfounder]]
- [[ivae]]
- [[collaborative-filtering]]
