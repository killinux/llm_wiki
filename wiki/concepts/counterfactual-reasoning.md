---
type: concept
subtype: method
tags: [causal-inference, counterfactual, recommendation, explainability, fairness]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# Counterfactual Reasoning

Counterfactual Reasoning 是一种因果推断方式,关注"在反事实条件下会发生什么"——即对某个个体或情境,若其处理(treatment)取值不同于实际观测到的取值,结果将如何变化。

## 在本 wiki 中的出现

- [[2023-causal-inference-for-recommendation]]:在这篇关于将因果推断引入推荐系统的系统综述中,Counterfactual Reasoning 作为因果框架的核心组成出现。它支撑了对潜在结果(potential outcomes)与因果效应的刻画,并被用于解决推荐系统中的若干实际问题:通过反事实问题("如果未曾推荐该物品会怎样")构建可解释性(explainability);校正观测数据中的选择偏差以追求无偏性(unbiasedness);以及在公平性(fairness)、鲁棒性(robustness)与 uplift 估计等场景中作为推理基础。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-limits-of-agency-in-agent-based-models]]:提出 LLM archetypes——为少数代表性 agent 类型查询 LLM 行为再概率采样到个体,从而在百万级 ABM 仿真(NYC 840 万人 COVID-19)中保持规模的同时引入 LLM 自适应行为。
- [[2026-pdqubo-quantum-feature-selection]]:PDQUBO 用反事实分析量化单特征与特征对的推荐性能影响,构造性能驱动的 QUBO 系数矩阵,在量子退火器上做模型无关、指标无关的推荐系统特征选择。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[causal-inference]]
- [[potential-outcomes]]
- [[treatment-effect]]
- [[uplift-modeling]]
- [[selection-bias]]
- [[recommendation-system]]
