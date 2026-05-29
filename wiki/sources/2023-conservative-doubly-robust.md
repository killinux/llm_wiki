---
type: source
subtype: paper
tags: [recommender-systems, debiasing, doubly-robust, selection-bias, causal-inference]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.08461
raw: raw/2308.08461.pdf
authors: [Zijie Song, Jiawei Chen, Sheng Zhou, Qihao Shi, Yan Feng, Chun Chen, Can Wang]
year: 2023
---

CDR(Conservative Doubly Robust)针对推荐系统去偏中 Doubly Robust 方法的"毒性插补"(poisonous imputation)问题,提出通过审查插补值的均值与方差来过滤不可靠插补,从而降低偏差与方差,提升去偏推荐性能。

## 问题

推荐系统中的用户行为数据是观察性而非实验性的,导致普遍存在 [[selection-bias]]。[[doubly-robust|Doubly Robust]](DR)方法因其性能与"双重稳健"特性(只要倾向分数或插补误差之一准确即可保证无偏)受到广泛关注。然而,DR 的插补模型通常只在小规模观察数据上训练,却要外推到全部 user-item 对,不可避免地在某些 pair 上产生不准确估计。

本文将这种现象定义为**毒性插补(Poisonous Imputation)**:当插补误差 ê_ui 与真实误差 e_ui 偏离过大(|ê_ui − e_ui| > e_ui)时,插补不仅无法减少反而增大偏差与方差,起到反作用。作者在 Coat、Yahoo、KuaiRand 三个数据集上用 DR-JL、MRDR、DR-BIAS、TDR 四种方法实测,发现毒性插补比例普遍**超过 35%**(如 DR-JL 在 Coat 上达 45.9%),问题严重。

## 方法

CDR 的核心思想:不在所有 user-item 对上盲目插补,而是采用保守、自适应的策略,只保留有益插补、过滤毒性插补。理想的过滤准则是比较 |ê_ui − e_ui| 与 e_ui,但真实标签不可得,故无法直接计算。

- **理论基础(Lemma 1)**:假设 ê_ui 与 e_ui 分别服从两个高斯分布,把"是否毒性"的判断重构为对插补值**均值与方差**的审查。给出了在置信水平 ρ 下,基于 σ̂_ui / μ̂_ui 比值的过滤不等式(eq.6)。直觉:方差越大越应丢弃;μ̂_ui 越大越应保留;ε_μ、ε_σ 越大越需保守过滤。
- **均值/方差估计**:采用 **Monte Carlo Dropout**(MC-dropout),对插补模型施加 10 次 dropout(随机丢弃 50% 的 embedding 维度),由此估计 ê_ui 的均值 μ̂_ui 与方差 σ̂_ui。dropout 只在估计时使用,不影响插补模型训练。
- **过滤条件**:把 eq.6 右端复杂表达式重参数化为单一超参数 η(过滤阈值),当 σ̂_ui / μ̂_ui < η 时保留插补(γ_ui=1),否则丢弃。
- **CDR estimator**(eq.7):L_CDR = |D|⁻¹ Σ (o_ui·e_ui/p̂_ui + γ_ui·ê_ui·(1 − o_ui/p̂_ui))。

CDR 可理解为 IPS 与 DR 的整合:毒性插补被过滤后回退到 IPS(其方差/偏差优于 DR),否则保留 DR 的优势。理论分析(Lemma 2、Corollary 3.1)证明在适当阈值 η 下,CDR 比 IPS 和 DR 有更优的方差与尾界。CDR 是 **model-agnostic** 的,可即插即用到现有 DR 方法。

## 结果

实验在三个真实数据集上进行:**Coat**(290 用户/300 物品,6960 biased + 4640 unbiased 评分)、**Yahoo!R3**(15400 用户/1000 物品,311704 biased + 54000 unbiased)、**KuaiRand-Pure**(7583 视频,1436609 biased + 1186059 unbiased)。评分以阈值 3 二值化,用 [[matrix-factorization|Matrix Factorization]] 作 base model,指标为 AUC、Recall@5、NDCG@5。

- **RQ1 性能(Table 2)**:CDR 持续提升 EIB、DR-JL、MRDR、DR-BIAS 四个基线。在 KuaiRand 上平均提升 AUC 0.95%、NDCG 3.86%、Recall 3.28%。最佳结果均由 CDR 系列取得,达到 SOTA。例如 DR-BIAS+CDR 在 Coat 上 AUC 0.7513(基线 +1.20%)、NDCG@5 0.6567;DR-JL+CDR 在 KuaiRand 上 Recall@5 提升 +4.14%。
- **RQ2 毒性插补比例(Figure 2)**:CDR 在三数据集上都显著降低了毒性插补占比,相对原始 DR 方法明显下降。
- **RQ3 阈值 η(Figure 3)**:η→0 等价于 IPS,η→∞ 等价于 DR;性能随 η 先升后降,存在最优折中,需调到合适值。
- **RQ4 运行时间(Table 3)**:CDR 虽多次 dropout 估计均值方差,但额外开销不大——均值方差计算只需前向传播无需反向传播,且过滤掉部分插补反而减少训练样本、加速推荐模型训练。

代码开源于 https://github.com/CrazyDumpling/CDR_CIKM2023。论文发表于 CIKM '23。

## 在本 wiki 中的位置

本文属于推荐系统去偏方向,核心是改进 [[doubly-robust]] 学习以缓解 [[selection-bias]]。它建立在 [[inverse-propensity-score]](IPS)基础上,并用 [[monte-carlo-dropout]] 做不确定性估计来识别毒性插补。可与 DR 系列方法 [[dr-jl]]、[[mrdr]]、[[dr-bias]]、[[tdr]] 以及插补基线 [[eib]] 对照阅读。虽然主题是推荐而非 LLM,但其"用不确定性/方差审查模型外推质量、过滤不可靠伪标签"的思路,与 LLM 训练中的伪标签筛选、数据去偏有相通之处。
