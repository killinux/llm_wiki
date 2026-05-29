---
type: concept
subtype: method
tags: [causal-inference, potential-outcome, counterfactual, treatment-effect, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Potential Outcome Framework

Potential Outcome Framework(又称 Rubin Causal Model / Neyman-Rubin 框架)是一套形式化定义因果效应的方法:为每个个体在不同 treatment 取值下设想各自的 potential outcome,通过比较这些(实际只能观测到其一的)结果来定义并估计因果效应。

## 在本 wiki 中的出现

- 在 [[2023-causal-inference-for-recommendation]] 中,Potential Outcome Framework 作为该综述介绍因果推断的两大基础语言之一(与 structural causal model 并列),用于建立因果记号、假设与效应的形式化定义。综述借助 potential outcome 记号刻画 treatment 与 outcome 的关系,定义诸如 ATE / ITE 等 treatment effect,并据此讨论将因果推断引入推荐系统时的估计方法,以及可解释性、公平性、鲁棒性、uplift、无偏性(unbiasedness)等实际问题。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[causal-inference]]
- [[structural-causal-model]]
- [[treatment-effect]]
- [[counterfactual]]
- [[uplift-modeling]]
- [[confounding-bias]]
- [[deconfounding]]
- [[debiasing]]
- [[recommender-systems]]
