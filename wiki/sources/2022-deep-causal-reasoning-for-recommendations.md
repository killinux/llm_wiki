---
type: source
subtype: paper
tags: [causal-inference, recommender-systems, deconfounding, variational-autoencoder, multi-cause, collaborative-filtering]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2201.02088
raw: raw/2201.02088.pdf
authors: [Yaochen Zhu, Jing Yi, Jiayi Xie, Zhenzhong Chen]
year: 2022
---

本文提出 Deep-Deconf(deep deconfounded recommender),用深度神经网络把推荐建模为 multi-cause multi-outcome (MCMO) 因果推断问题,通过推断 substitute confounders 消除隐藏混杂偏差,并用 user features 作为 pre-treatment 变量降低估计方差。

## 问题

传统推荐系统(如 [[collaborative-filtering]])直接基于观测到的评分来估计用户偏好,但观测数据存在系统性偏差:同时影响 item exposure 和 user rating 的 hidden confounders(隐藏混杂因子,例如电影 genre)会在两者之间制造虚假依赖,导致少数类(如恐怖片)被系统性低估。

要消除这种 [[confounding-bias]],需要回答反事实问题(若某个先前未曝光的 item 被推荐给用户会得到什么评分)。经典 [[causal-inference]] 要求找到并控制**所有**混杂因子,但这在推荐场景中不可行也不可检验。前人工作 [[deconf-mf]](Deconfounded Recommender)用浅层 Poisson 矩阵分解推断 substitute confounders,建模能力不足,无法捕捉非线性的 item co-exposure 关系,并退化为忽略 item co-recommendation 效应的 single-cause 情形。

## 方法

Deep-Deconf 把推荐建模为 multi-cause multi-outcome (MCMO) 推断问题:把一个用户对所有 item 的 exposures 看作 multi-cause treatments,把 ratings 看作 potential outcomes。

- **去偏(debias)**:基于 Pearl 的 SCG / Rubin 因果框架,假设不存在 single-cause confounder,只需控制 [[multi-cause-confounders]]。用 factorized logistic likelihood 的 VAE([[variational-autoencoder]])推断 user-specific 的 substitute confounders \(z_u\),使 item exposures 在给定 \(z_u\) 时变为独立的 Bernoulli trials,从而消除多因混杂偏差。intractable posterior 用 variational inference 近似。
- **评分预测(outcome model)**:用 deep outcome network(拼接 exposures、substitute confounders、user features 后过 MLP)预测 potential ratings,利用多项式似然得到更准确的评分,并能建模 item co-recommendation 效应(网络权重可解释为 CATE/ATE)。
- **方差降低**:作者从理论上证明 MCMO 建模因 counterfactual 数量随 item 数指数增长(\(2^I\))而方差很大;引入 user features 作为 pre-treatment 变量(对 item exposure 不变但能预测 ratings)可显著降低 OLS 估计量的极限方差,缓解过拟合。
- **理论分析**:给出线性与非线性情形下网络 global/local Jacobian 与 ATE/CATE 的对应关系,并讨论模型可识别性(依赖 substitute confounder 的 pinpoint 条件)。

## 结果

在一个 simulated 数据集和两个半真实数据集 [[ml-causal]](基于 [[movielens]]-1M)、[[vg-causal]](基于 Amazon-Videogames)上评测,指标为 R@20 和 N@20(strong generalization 设定)。

- Deep-Deconf 在几乎所有 confounding level(\(\gamma_\theta \in \{0.1,0.3,0.5,0.7,0.9\}\))下都优于全部基线,包括 [[deconf-mf]]、WMF、IPW-MF、VSR-VAE、Concat-VAE。
- Simulated 数据上,Deep-Deconf 最佳 R@20 达 0.696、N@20 达 0.712(\(\lambda_\theta=0.7\)),优于 Deconf-MF(约 0.612/0.623)与 Concat-VAE(约 0.677/0.690)。
- VG-causal 上最佳 R@20=0.431、N@20=0.420(\(\lambda_\theta=0.5\));ML-causal 上最佳 R@20=0.124、N@20=0.121(\(\lambda_\theta=0.7\)),均显著超过基线(多数 p-value < 0.05)。
- 提出 "duality of multi-cause confounders" 理论,解释为何推荐性能随 confounding level 先升后降(非单调):混杂因子作为共享 item 属性既提供协同信息又带来偏差,二者此消彼长。
- 敏感性分析(Table 3)显示 user features 噪声越小(越能预测评分)估计方差越低、性能越好;在高 confounding 时引入 user features 的提升更明显。

## 在本 wiki 中的位置

本文属于 causal recommender systems 方向,把 [[deconf-mf]] 的 substitute confounder 思想推广到深度神经网络与 MCMO 建模,与 [[causal-inference]]、[[deconfounding]]、[[variational-autoencoder]]、[[collaborative-filtering]] 等主题相关。它的方法可作为插件嵌入面向用户的 auto-encoder 推荐系统中以降低混杂偏差。
