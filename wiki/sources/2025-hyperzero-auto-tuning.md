---
type: source
subtype: paper
tags: [recommender-system, hyperparameter-optimization, bayesian-optimization, gaussian-process, thompson-sampling, zeroth-order-optimization, constrained-optimization, value-model, kdd]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2501.18126
raw: raw/2501.18126.pdf
authors: [Xufeng Cai, Ziwei Guan, Lei Yuan, Ali Selman Aydin, Tengyu Xu, Boying Liu, Wenbo Ren, Renkai Xiang, Songyi He, Haichuan Yang, Serena Li, Mingze Gao, Yue Weng, Ji Liu]
year: 2025
---

# HyperZero: A Customized End-to-End Auto-Tuning System for Recommendation with Hourly Feedback

来自 Meta 的端到端超参数自动调优系统 HyperZero,利用工业级 [[recommender-system]] 的**小时级反馈**信号,把 value model 阶段权重向量的调优周期从数周压缩到 2-3 天,通过 GP + Thompson Sampling 的零阶约束优化求解多目标带约束问题。

## 问题

现代 [[recommender-system]] 分两阶段:ranking stage 预测各类用户互动概率(p(click)、p(share)、p(follow)、watch time 等),value model (VM) stage 把这些预测通过一个函数(常为线性组合,score = θ0·p(click) + θ1·p(share) + θ2·p(follow) + …)聚合成单一价值分数用于最终排序。第二阶段的权重向量 θ 如何系统化优化此前缺乏研究。

传统调优依赖**日级**系统反馈、靠工程团队经验,需要 **2-3 周**才能找到合理平衡。但配置参数常需随业务需求快速调整(如上新界面时需在多约束下同时提升长视频曝光)。改用**小时级**反馈做自动调优面临三大挑战:

1. **Estimator —— non-i.i.d. 小时级反馈**:小时数据方差高且随时间相关,违反多数算法所需的 i.i.d. 假设,缺乏性能保证。
2. **Optimizer —— 多目标优化**:每个指标都是分布未知的随机变量,无法直接估计;梯度/Hessian 不可得,使一阶/二阶方法失效;且存在通用约束。
3. **Delayed environment —— 系统反馈延迟**:超参数变更生效有延迟,反馈收集也有延迟,跨数小时,可能抵消小时级数据的效率收益。

核心问题:How do we reduce the tuning time from weeks to days?

## 方法

**HyperZero**(Hyperparameter 的 Zero-th order optimization)三大组件:

- **数据归一化(Challenge 1)**:提出 semi-i.i.d. 信号,用 test 组与 control 组小时指标读数的比值 delta:ΔX(θ) := X(θ)/X(θ0) − 1,其中 θ0 为固定 base 超参数。该归一化基于"不同处理组的用户群呈现相似小时波动模式"的观察,可有效去相关([[selection-bias]] 之外的时序相关问题)。再用高阶 Taylor 展开估计两个随机变量之比的均值 μ(ΔX;θ) 与方差 σ²(ΔX;θ),并以各轮 test 组规模 N_t 加权聚合(可流式更新)。

- **零阶约束优化 GP + TS(Challenge 2)**:把调优写成带约束的优化问题 max_θ E[f(ΔX(θ))] s.t. E[g_i(ΔX(θ))] ≥ c_i。
  - **Challenge 2(a)** ΔX(θ) 分布未知 → 用 [[gaussian-process]] (GP) 估计每个 metric delta 的连续分布(假设高斯先验)。
  - **Challenge 2(b)** 目标/约束的梯度不可得 → 用 [[thompson-sampling]] (TS):从 GP 采样 metric delta,挑选满足约束且最大化目标的候选 θ*。Algorithm 1 把 TS 重复 K 次生成多个候选;重复出现的候选会获得更多在线流量(这是 desirable 的)。

- **异步并行探索(Challenge 3)**:把框架实现为基础设施层的异步并行循环。每轮在 test bed 上并行测试多个候选(一组在线 A/B 测试),由于配置变更与反馈收集的延迟,某轮反馈可能尚不可用;系统在每轮基于当前所有可用数据更新 metric 估计记录 R 并决策。延迟即使超过 6 轮,3 天调优作业的收敛速度几乎不变。

整体框架(Algorithm 2):初始化约 100 个候选的 bucket,每轮记录最新小时估计、做 GP 回归、调 Algorithm 1 选候选、以概率 p 用 Algorithm 3 提新候选(每轮采样 N 点、用 GP 插值,优于 Monte Carlo 采样),提交在线测试并更新 bucket。系统设计(Figure 4)含 data aggregator(异步收集反馈)、model updater(异步选处理)、exp updater(定时在线提交)等模块。

## 结果

**合成数据(50 个随机种子,T=30)**:

- 消融研究(Q1)证明三组件均必要:HyperZero 的目标增益学习速度与约束违反控制都远优于去掉 delta metric 或同步并行的变体;同步变体学习速度慢约 **50%**;不用 delta metric 则算法无法从环境学到任何东西。
- 与 Bayesian optimization 对比(Table 1,30 步后 50 次平均):HyperZero **Gain 4.951% ± 0.205**、**Violation 0.001 ± 0.0004**;Unconstrained BO Gain 2.128% ± 0.856、Violation 0.592 ± 0.0051;Penalized BO Gain 2.080% ± 0.760、Violation 0.592 ± 0.0044。HyperZero 在增益和约束可行性上都更优(约束违反接近 0,而 penalized BO 仍严重违反)。

**工业环境(Meta 生产部署)**:

- 候选提议消融(Figure 6):用 candidate proposal (p≠0) 的 HyperZero 性能增益是不用的 **两倍**。
- 与开源 Bayesian optimizer Botorch 对比(Figure 7,3 天 view count 增益):HyperZero 在 mean value **1.2% vs Botorch 0.8%**,在 LCB **0.7% vs 0.5%**,且探索更高效(Botorch 偏 exploitation,难找到显著更优候选)。

发布于 KDD '25。约一半性能提升来自 value model 阶段的函数精炼,而现有调优系统无法在 2-3 天关键时间窗内交付可行解。

## 在本 wiki 中的位置

这是一篇 [[recommender-system]] 工业系统论文,核心是把 [[hyperparameter-optimization]] / [[bayesian-optimization]] 适配到 value model 权重调优这一长期缺乏系统研究的场景。方法上属 [[zeroth-order-optimization]] + [[constrained-optimization]],技术栈是 [[gaussian-process]] 估计 + [[thompson-sampling]] 选择,与通用 BO 框架([[bayesian-optimization]])形成对比——后者因 non-i.i.d. 小时反馈和任意形式约束不能直接套用。与本 wiki 中偏 RL/causal 的 recsys 调优路线不同,HyperZero 走的是在线 A/B test bed + 零阶优化路线,关键创新是 semi-i.i.d. delta 信号与异步并行。作者来自 [[bytedance-research]] 之外的 Meta(论文未涵盖的实体),实验含合成与生产两类。论文用开源数据集 [[kuairand]] 作小时 view count 波动的示意(Figure 2)。
