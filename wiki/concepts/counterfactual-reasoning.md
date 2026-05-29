---
type: concept
subtype: method
tags: [causal-inference, counterfactual, recommendation, explainability, fairness]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Counterfactual Reasoning

Counterfactual Reasoning 是一种因果推断方式,关注"在反事实条件下会发生什么"——即对某个个体或情境,若其处理(treatment)取值不同于实际观测到的取值,结果将如何变化。

## 在本 wiki 中的出现

- [[2023-causal-inference-for-recommendation]]:在这篇关于将因果推断引入推荐系统的系统综述中,Counterfactual Reasoning 作为因果框架的核心组成出现。它支撑了对潜在结果(potential outcomes)与因果效应的刻画,并被用于解决推荐系统中的若干实际问题:通过反事实问题("如果未曾推荐该物品会怎样")构建可解释性(explainability);校正观测数据中的选择偏差以追求无偏性(unbiasedness);以及在公平性(fairness)、鲁棒性(robustness)与 uplift 估计等场景中作为推理基础。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。

## 相关

- [[causal-inference]]
- [[potential-outcomes]]
- [[treatment-effect]]
- [[uplift-modeling]]
- [[selection-bias]]
- [[recommendation-system]]
