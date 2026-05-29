---
type: source
subtype: paper
tags:
  - recommender-system
  - ctr-prediction
  - bias
  - fairness
  - factorization-machines
created: 2026-05-29
updated: 2026-05-29
arxiv: "2402.03600"
raw: raw/2402.03600.pdf
authors:
  - Jinqiu Jin
  - Sihao Ding
  - Wenjie Wang
  - Fuli Feng
year: 2024
---

# Understanding and Counteracting Feature-Level Bias in Click-Through Rate Prediction

通过自上而下的分析揭示 CTR 模型中 feature-level bias 主要来自**线性部分**(linear component),并提出移除/调整线性权重的极简非侵入式 debias 策略。

## 问题

[[recommender-systems|recommender-system]] 中的 CTR(click-through rate)预测模型常表现出 **feature-level bias**:针对某个特征字段(如电影 genre、video tag),模型会对不同 item group 过度推荐或推荐不足,导致 item-side 不公平,并扭曲用户真实偏好。

已有方法主要通过调整 CTR 模型的**学习过程**来缓解,如 regularization、adversarial training、causal [[inverse-propensity-score]] 等,但都未回答一个关键问题:**bias 是如何从原始训练数据中产生的,CTR 模型的哪个组件主要导致了 feature-level bias?**

本文聚焦广泛使用的 [[factorization-machines]](FM)及其扩展 NFM,做 top-down 分析。

## 方法

CTR 模型预测可抽象为 `ŷ = w0 + Σ wi·xi + fθ(x)`,即 **linear part**(线性权重 wi 建模特征的直接贡献)+ **high-order part**(fθ 建模特征交互,FM 用 embedding,NFM 用 DNN)。

**模型视角的 bias 分析**:逐一 block 训练好的 FM/NFM 的 linear 或 high-order 组件。计算各 item group 上正/负样本预测分数的方差(方差越大代表对 group 区分越强、bias 越强)。结果发现 linear part 的方差显著高于 high-order part,定位线性部分为 feature-level bias 的关键来源。

**数据视角的 bias 分析**:对 BCE loss 求 wj 的梯度,推导出线性权重 wj 应与训练集中第 j 个特征的正/负样本数量相关。用 Pearson 和 Spearman 检验线性权重与三种 group 级统计量(正样本数 Np、Np−Nn、正样本比例 Np/(Np+Nn))的相关性,发现线性权重与**正样本比例**强相关(SP > 0.87,PS > 0.80,p < 1e-4)。由此得到生成路径:**有偏的正样本比例 → 有偏的线性权重 → 有偏的预测分数 → 有偏的推荐**。

**提出两种 post-training 的极简非侵入式策略(Algorithm 1)**:
- **Linear Weight Reduction**:用系数 α 收缩 bias 字段的线性权重 `w'j = α·wj`,默认 α=0(完全移除)。无需额外数据,只在推理阶段调整 k 个线性权重(k≪n)。
- **Linear Weight Reconstruction**:利用少量 random exposure 数据(unbiased)重建线性权重。两步:(1) 对(正样本比例, 权重)做线性回归取残差 rj 以去除有偏正样本比例的影响;(2) 用无偏数据估计真实正样本比例 sj,线性组合 `w'j = β·sj + γ·rj` 重建权重。

[[evaluation]] 指标:item-side 用 REO@K(top-K 推荐概率的相对标准差,越小越公平,关联 Equal Opportunity 概念),准确率用 UAUC 与 NDCG@K。还引入 Exposure-to-Hit Ratio (EHR) 度量 group 的过度/不足推荐。

## 结果

数据集:**ML-1M**、**Book**(Amazon book)、**KuaiRand**(快手短视频,含 normal + random exposure)。Backbone 为 FM 与 NFM。

**Normal biased test(Table 4)**:Linear Weight Reduction 大幅降低 REO@5,即 item-side 不公平相对 basemodel 下降 **14.35% ~ 47.00%**;同时 UAUC/NDCG 平均仅下降约 -1.06%。对比基线:IPW、Unawareness 对数据集敏感(IPW 在 Book 上失败);DecRS、FairGo 因从 high-order embedding 入手,大多无法有效降低 REO@5。

**Debiased test on KuaiRand(Table 5)**:Linear Weight Reconstruction 取得所有基线中最佳性能,相对 basemodel 的 UAUC、NDCG@5 平均提升 **4.52% 和 7.71%**(FM:+4.37%/+7.56%;NFM:+4.67%/+7.85%),超过 Finetune 和 InterD,因其避免了无偏数据稀疏带来的过拟合。

**消融(Table 6)**:完整 Reconstruction 优于 w/o ratio 和 w/o residual 变体,验证残差去偏与无偏正样本比例两部分各自有效;即使 w/o ratio(不需 random exposure)也优于 basemodel。

**α 分析(Figure 7)**:α 增大时 UAUC 上升但准确率下降;在 ML-1M 上 REO@5 先降后升,说明小而非零的 α(如 0.1、0.2)可能实现公平-准确双赢;推荐选用小的非零 α。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 的 **bias & fairness** 方向,聚焦 CTR 预测。与基于 causal inference 的去偏方法(如 [[inverse-propensity-score]]、deconfounding 系列)不同,它从模型组件分解角度定位 [[factorization-machines]] 线性部分为 feature-level bias 主因,提出 post-training 的极简调权策略,无需重训。可与 wiki 中 [[selection-bias]]、[[exposure-bias]]、[[debiasing]]、[[matthew-effect]] 等推荐去偏概念互相参照;数据集 [[kuairand]] 与 backbone [[fm]] 已在本 wiki 出现。
