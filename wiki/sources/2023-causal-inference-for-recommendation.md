---
type: source
subtype: paper
tags: [causal-inference, recommender-systems, survey, fairness, debiasing, counterfactual, uplift, robustness]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2301.04016
raw: raw/2301.04016.pdf
authors: [Shuyuan Xu, Jianchao Ji, Yunqi Li, Yingqiang Ge, Juntao Tan, Yongfeng Zhang]
year: 2023
---

# Causal Inference for Recommendation: Foundations, Methods and Applications

一句话概述:这是一篇系统综述,梳理了如何将 [[causal-inference|因果推断]] 引入 [[recommender-systems|推荐系统]],从因果记号、假设、因果效应、估计方法,到可解释性、公平性、鲁棒性、uplift、无偏性等实际问题,统一整理了相关方法与开放问题。

## 问题

传统推荐系统(协同过滤、基于内容、混合方法)本质上是从数据中挖掘**相关性(correlation)**模式。但现实世界由底层**因果机制(causation)**驱动,只学相关而忽视因果会导致一系列实际问题:不公平、缺乏可解释性、鲁棒性差、各类 bias、回声室(echo chamber)/过滤气泡、以及可控性问题。作者用经典的"啤酒与尿布"例子说明:纯相关学习会因为两者强相关而互相推荐,但真实机制是"年轻父亲常一起买啤酒和尿布",忽视机制会损害用户满意度。因此本文要回答:如何把 [[causal-inference|因果推断]] 系统性地引入推荐,以应对上述问题。

## 方法

本综述沿两个维度组织内容:

- **因果推断的基础(pipeline 维度)**:
  - 两大框架——[[potential-outcome-framework|潜在结果框架]](Neyman–Rubin / Rubin Causal Model)与 Pearl 的 [[structural-causal-model|结构因果模型(SCM)]],以及二者的联系。
  - 关键概念:potential outcome、treatment / control、[[counterfactual-reasoning|counterfactual]]、pre-/post-treatment 变量、SUTVA / ignorability / positivity 等因果假设、混淆因子(confounders)、Simpson's paradox。
  - 因果效应:ATE / ATT / CATE / ITE,以及中介分析中的 CDE / NDE / NIE。
  - 因果效应估计:随机实验(randomized experiment)、观测数据下的重加权(IPS 倾向得分、confounder balancing)、分层(stratification)、后门 / 前门调整(back-door / front-door adjustment)、[[do-calculus|do-calculus]] 三条规则、工具变量(instrumental variables),以及 [[causal-discovery|因果发现]](约束/打分/函数因果模型三类)。
- **推荐中的实际问题(problem 维度)**,逐一介绍问题、因果方法与开放问题:
  - 因果**可解释性**(counterfactual explanation、causal discovery 生成解释);
  - 因果**公平性**(group/individual fairness、user-side/item-side fairness、counterfactual fairness);
  - 因果**鲁棒性**(应对 distributional shift、攻击、稀疏性);
  - **uplift-based** 推荐(估计推荐带来的增量 Y(1)−Y(0));
  - 因果**无偏性 / debiasing**(应对 selection / exposure / conformity / position / popularity / feedback-loop bias)。

## 结果

作为一篇**综述论文**,本文不提供新模型的 benchmark 分数,其贡献在于知识体系的系统整理:

- 给出了推荐场景下因果效应的统一数学定义,例如 ATE = E[Y(1)] − E[Y(0)],ATT = E[Y(1)|X=1] − E[Y(0)|X=1],并推导出观测式 E[Y|X=1] − E[Y|X=0] 中 ATT 项与 bias 项的分解(式 10),解释了相关与因果的差距。
- 整理了后门调整公式 P(y|do(x)) = Σ_z P(y|x,z)P(z) 与前门调整公式,以及 do-calculus 的三条规则。
- 用一个新药研究的例子(Table 1:男性服药 81/87=93%、女性 192/263=73%、总体 273/350=78% vs 不服药 234/267=87%、55/80=69%、289/350=83%)演示了 Simpson's paradox 在离线评估中的体现。
- 指出多项 open problems:预定义因果机制的正确性难以量化评估、缺乏统一的因果机制、IPS 倾向得分正确性难评估、因果公平的理论基础尚不完善、需要因果驱动的仿真(causality-driven simulation)来评估因果发现方法等。

## 在本 wiki 中的位置

本文是连接 [[causal-inference|因果推断]] 与 [[recommender-systems|推荐系统]] 的总览性入口,可作为理解推荐中 debiasing、公平性、uplift、鲁棒性等专题的地图。它系统使用了 [[potential-outcome-framework]]、[[structural-causal-model]]、[[counterfactual-reasoning]]、[[do-calculus]]、[[inverse-propensity-scoring]]、[[causal-discovery]] 等方法概念。文中也提到推荐社区开始借助 [[foundation-models|foundation models]] / [[gpt-3]] / [[t5]] / [[palm]] 等大模型构建个性化基础模型(如 P5),这与本 wiki 的 LLM 主线相呼应——即如何把因果思想引入到以大模型为基础的推荐与决策系统中。作者为 Rutgers 大学的 [[yongfeng-zhang|Yongfeng Zhang]] 团队。
