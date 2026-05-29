---
type: source
subtype: paper
title: "Regret-aware Re-ranking for Guaranteeing Two-sided Fairness and Accuracy in Recommender Systems"
tags: [recommender-system, two-sided-fairness-reranking, provider-fairness, re-ranking, regret-theory, fuzzy-programming, minimum-exposure-guarantee, individual-fairness]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2504.14550
raw: raw/2504.14550.pdf
authors: [Xiaopeng Ye, Chen Xu, Jun Xu, Xuyang Xie, Gang Wang, Zhenhua Dong]
year: 2025
---

# Regret-aware Re-ranking for Guaranteeing Two-sided Fairness and Accuracy in Recommender Systems

BankFair+ 是 BankFair(CIKM 2024)的扩展期刊版,在 [[provider-fairness]] 与用户平均精度之外,引入经济学 **regret theory(后悔理论)** 的非线性满意度函数与 **[[fuzzy-programming]](模糊规划)**,在多方([[two-sided-fairness-reranking]])推荐重排阶段同时保证用户平均精度、**用户个体公平(individual fairness)** 与供给侧公平。

## 问题

在多方([[recommender-systems|recommender-system]])平台中,用户与供给方(provider)的利益需要被平衡。作者之前的工作 [[2024-bankfair-fluctuating-traffic-reranking]](BankFair,CIKM 2024)用 [[bankruptcy-problem]] 的 [[talmud-rule]] 在波动用户流量(user traffic)下动态分配供给方曝光,从而在保证 [[minimum-exposure-guarantee]] 供给公平的同时维持用户平均精度。

但本文指出:即便平均精度达标,仍存在严重的 **用户个体不公平**——不同用户拿到的推荐精度差异很大。作者在 [[kuairand]](KuaiRand-1K)上用 BankFair 做实验:选取一个月内平均精度最高的一天(2022-04-22),按精度从高到低排序所有用户后发现,尽管平均精度超过最低精度阈值,仍有约 **41%** 的用户精度低于该阈值。并且,随着供给公平程度(provider fairness degree)从 90% 升到 100%,个体公平持续恶化(图 1c)。这种个体层面的不公平会引发用户流失与社会极化([[polarization]])。已有工作(如 TFROM、CPFair、P-MMF)大多只讨论"用户平均精度 vs 供给公平"的权衡,忽视了"供给公平 vs 用户个体公平"这条边。

## 方法

BankFair+ 把重排建模为一个 **regret-aware 模糊规划** 问题,并用在线学习算法求解(Algorithm 1),由两个模块组成:

- **Module 1(供给曝光分配,与 BankFair 相同)**:把全局所需最低曝光 m 通过 [[bankruptcy-problem]] 的 [[talmud-rule]] 顺序分配到每个时间区间 n,得到该区间的预测最低曝光,用以在流量波动下平衡用户精度与供给公平。
- **Module 2(regret-aware 在线推荐)**,分两步:
  - **Step 1 — 用 regret theory 保证个体公平与用户精度**:把重排看作平台的决策过程,参考点设为精度最大化的列表 π*。用户感知满意度 Z(π_u)=V(π_u)+R(ΔV),其中效用函数取幂函数 V(π_u)=q^α(论文取 α=1,即用户风险中性),regret-rejoice 函数 R(ΔV)=1−exp(−δ(q_{π_u}−q*_{π_u}))。δ 为后悔规避系数。该非线性函数把低质量推荐带来的满意度下降放大,从而促使优化器拉平个体精度。
  - **Step 2 — 用 fuzzy programming 平衡个体精度与供给公平**:由于"对每个用户加一条精度约束"会导致约束爆炸、可能无可行解,作者改用 [[fuzzy-programming]],把"用户满意度尽量高"和"供给不公平尽量低"表示为模糊目标(membership function),用 compromised approach 转成可解的单目标优化。精度用 DCG/[[ndcg]] 度量,供给公平用曝光方差 Var(e/γ) 度量。Theorem 1/2 给出其等价形式与对偶问题;在线版用 Lagrangian relaxation + 在线对偶镜像下降(online dual mirror descent)更新对偶变量 μ。

超参数 λ 控制"用户满意度 vs 供给公平"的权衡,δ 控制后悔规避强度。

## 结果

数据集:[[kuairand]](KuaiRand-1K,933 用户、6825 视频、174 providers、302870 交互)与 Huawei-Video(19355 用户、5364 items、200 providers、118765 交互)。基线:BankFair、Welf、P-MMF、CPFair、FairRec、TFROM、PCT。指标:用户精度用 [[ndcg]];供给公平用 ESP@K(enough satisfaction group)与 Gini@K;个体公平用 **MMR@K(Min-Max Ratio,最低/最高用户 NDCG 之比)** 与 Var@K。默认 β=0.9(每个 provider 至少拿到应得曝光的 90%)。

- **RQ1(平均精度 vs 供给公平)**:在 NDCG–Gini 与 NDCG–ESP 的 Pareto 前沿上 BankFair+ 占优。在 NDCG@10–Gini@10 上,同一公平水平(Gini<0.1)BankFair+ 的 NDCG 比最佳基线(P-MMF)至少高 **0.2**;在 NDCG@10–ESP@10 上,同一供给满意度(ESP=80%)下 NDCG 比最佳基线高 **0.18**。
- **RQ2(个体公平 vs 供给公平)**:在 MMR–Gini / MMR–ESP 前沿上,当 Gini@K 从 0.4 降到 0、ESP 从 0.4 升到 0.8 时,BankFair+ 的 **MMR 仍保持在 0.7 以上**(最低精度用户拿到最高精度用户 70% 以上的精度);同一公平水平(如 Gini=0.1、ESP=0.7)下,基线的 MMR 不超过 50%。
- **RQ3(个体精度分布,case study,75% ESP@10)**:BankFair+ 的 **MMR=0.741**,而 BankFair=0.493、CPFair=0.065、Welf=0.5247;BankFair+ 在更公平的同时平均精度也更高。
- **RQ4(不同 β / 最低曝光阈值)**:在不同 m_p 水平下 BankFair+ 始终保持更高 NDCG@10、更高 MMR@10、更低 Var@10。
- **RQ5(后悔规避系数 δ)**:δ 增大时平均精度上升并趋于上限、个体公平(MMR)上升,但供给公平略有下降(ESP 降、Gini 升);体现精度/个体公平与供给公平之间可调的权衡。
- 在不同底层排序模型 [[lightgcn]] 与 NeuMF 上,BankFair+ 仍对所有基线 Pareto 占优。

结论:本文是 BankFair(CIKM 2024)的扩展版,首次在重排阶段同时平衡用户平均精度、用户个体公平与供给公平;未来计划把该思路扩展到排序(ranking)阶段。

## 在本 wiki 中的位置

本文属于推荐系统中的多方公平/[[two-sided-fairness-reranking]] 这一支,是 [[2024-bankfair-fluctuating-traffic-reranking]] 的直接续作,核心贡献是把 [[minimum-exposure-guarantee]]、[[bankruptcy-problem]]([[talmud-rule]])与经济学的 regret theory、[[fuzzy-programming]] 结合,解决 [[provider-fairness]] 与用户个体公平之间被忽视的权衡,缓解推荐中的个体不公平与 [[polarization]]。相关供给公平/重排方法包括 [[two-sided-fairness-reranking]] 框架下的 P-MMF、FairRec、TFROM 等。作者来自 [[renmin-university-of-china]](高瓴人工智能学院,[[jun-xu]] 为通讯作者)与 [[huawei-noahs-ark-lab]]([[zhenhua-dong]] 等)。它与 LLM 主题相对正交,主要作为推荐系统公平性 / RecSys 方向的参考节点。
