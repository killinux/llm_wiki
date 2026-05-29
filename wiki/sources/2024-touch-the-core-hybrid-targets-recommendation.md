---
type: source
subtype: paper
tags: [multi-task-learning, recommender-system, task-dependence, hybrid-targets, watch-time, label-embedding, gradient-optimization]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2403.17442
raw: raw/2403.17442.pdf
authors: [Xing Tang, Yang Qiao, Fuyuan Lyu, Dugang Liu, Xiuqiang He]
year: 2024
---

# Touch the Core: Exploring Task Dependence Among Hybrid Targets for Recommendation

本文首次研究"hybrid targets"(多个离散转化任务 + 一个连续核心任务,如 watch time、revenue)下的 [[multi-task-learning]] 问题,提出 HTLNet(Hybrid Targets Learning Network),用 label embedding 显式传递任务标签信息,并设计梯度调整策略来稳定连续回归任务与离散分类任务之间的联合优化。

## 问题

在线推荐越来越关注与平台利益强相关的 **core conversion**,这些核心目标往往是连续值(continuous targets),如 watch time、revenue、投资金额等;它们的预测可由前序离散转化动作(click、purchase 等)增强。这类"离散动作 + 连续核心目标"的组合称为 **hybrid targets**。

已有的 sequential dependence MTL(SDMTL,如 [[esmm]]、[[aitm]])主要研究离散转化之间的顺序依赖,有两点不足:

- **忽略离散转化与连续核心目标之间依赖的复杂性**。SDMTL 假设 $\hat y^k - \hat y^{k-1} = P(t_k=0, t_{k-1}=1)$,即相邻任务预测之差等于"前序发生而后续不发生"的概率;但当预测为连续值时该等式不成立(不同连续值不能推出相同概率)。此外高 click rate 并不意味着高 conversion rate,这与 SDMTL 的假设相悖。
- **混合任务优化不稳定(volatile)**。核心回归任务的梯度在数量级与方向上与分类任务差异很大;若简单同时优化,强依赖的回归任务梯度可能主导(dominate)其他任务,导致训练不稳定、性能退化。

本文首次把这一 hybrid targets learning 问题与传统 MTL 区分开来正式研究。

## 方法

提出 **HTLNet(Hybrid Targets Learning Network)**,核心是探索 hybrid targets 间的任务依赖,并稳定优化。所有任务共享一个 embedding layer,各任务有自己的 task tower(回归 task 用 MLP + MSE loss,分类 task 用 sigmoid + BCE loss)。两大组件:

- **Label Embedding Unit(LEU)**:为每个分类任务引入一个两行 embedding table $E^t \in \mathbb{R}^{2\times L_d}$(对应标签 0/1),把离散标签显式映射为稠密向量传给后续任务。为避免直接用真实标签带来的 train-test discrepancy 与 cascading errors,LEU **从预测概率分布中采样**标签,并用 **Gumbel-Softmax** 重参数化使采样可微,输出为两行 embedding 的加权和 $le^t = [p^t, 1-p^t]E^t$。
- **Information Fusion Unit(IFU)**:用类似 attention 的机制自适应融合所有前序任务传来的两类信息——LEU 给出的显式 label embedding $le$ 与 task tower 给出的隐式 representation $rep$,得到融合后的 $le_f^t$ 与 $rep_f^t$,再作为后续任务 tower 的输入($h_{input,i}^t = concat(rep_f^{t-1}, le_f^{t-1}, e_i)$)。

**优化策略(针对共享 embedding 的梯度冲突)**:

- 对 LEU 与 IFU 的输出做 **stop_gradient**,使转移信息只通过共享 embedding 影响彼此,避免扰乱前序任务的 label 预测与 representation。
- **梯度方向去冲突**:以核心任务梯度 $G_{core}$ 为目标,若某分类任务梯度 $G_t$ 与 $G_{core}$ 余弦相似度为负,则把 $G_t$ 投影到 $G_{core}$ 的法平面(类似 Gradient Surgery)。
- **梯度幅度调整**:因核心任务用 MSE、量级通常远大于分类任务的 LogLoss,按 $G_t = \gamma\cdot\frac{\|G_{core}\|}{\|G_t\|}\cdot G_t + (1-\gamma)\cdot G_t$ 自适应调整幅度,并用阈值 $C$ 裁剪权重防止梯度爆炸。

## 结果

在两个公开数据集(KuaiRand-pure、Kaggle Acquire Valued Shoppers/Revenue)与一个真实工业基金推荐数据集(Product)上评测;数据按时间 8:1:1 划分。分类任务用 **AUC / LogLoss**,回归任务用 **NRMSE / NMAE**,并用 **Gini / Spearman** 衡量按金额排序的能力。Baselines 涵盖 DNN、Shared-Bottom、[[mmoe]]、[[ple]]、AdaTT、[[esmm]]、[[aitm]] 与优化方法 MetaBalance。

- **整体性能(Table 2)**:HTLNet 在所有数据集的全部目标任务上取得最佳指标,且在多数任务上相对 baseline 统计显著($p \le 0.05$)。例如 KuaiRand 上 watch time 的 NRMSE 0.8937、NMAE 0.9093(均最佳);click AUC 0.7574、long view AUC 0.7787。Kaggle-Revenue repurchase 1M amount 的 Spearman 0.2475、Gini 0.5233。Product 上 purchase amount 的 Spearman 0.2244、Gini 0.8362。
- **消融(Table 3)**:HTLNet w/o Architecture(换成 shared-bottom)与 w/o Optimization(去掉梯度处理算法)均明显变差,其中 w/o Optimization 是最差变体,说明针对架构定制的优化策略是必要的。
- **网络架构分析(Table 4)**:去掉 IFU 的 representation 或去掉 LEU 的 label embedding 都会掉点;IFU 用 attention 优于简单 concatenation(Figure 4)。
- **优化策略分析(Table 5)**:去掉 stop_gradient 影响最大;HTLNet 优于 Gradient Surgery 与 MetaBalance 等通用 MTL 优化方法。梯度幅度图(Figure 5)显示无梯度处理时 watch time 梯度发散并逐渐主导,加入梯度处理后三任务梯度收敛同步。
- **在线 A/B(Figure 6)**:在大规模基金推荐场景连续 14 天测试,CTR、CVR、purchase amount 的累计增益分别为 **+0.54%、+1.4%、+2.69%**。

代码开源于 github.com/fuyuanlyu/HTLNet。Limitations:训练时间多于其他 baseline;假设最终核心目标连续、前序任务离散。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 中的 [[multi-task-learning]] / [[sequential-recommendation]] 方向,聚焦"离散转化 + 连续核心目标(watch time、revenue)"的 hybrid targets 建模,是对 SDMTL 路线([[esmm]]、[[aitm]])的扩展。其多专家/塔结构与 [[mmoe]]、[[ple]] 同源;[[watch-time]] 作为核心连续目标与短视频推荐场景密切相关;梯度去冲突/幅度调整属于 MTL 优化策略。作者来自 Tencent FiT 与 McGill,数据集涉及 [[kuairand]]。
