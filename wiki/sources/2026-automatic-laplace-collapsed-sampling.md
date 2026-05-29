---
type: source
subtype: paper
tags: [bayesian-inference, nested-sampling, laplace-approximation, automatic-differentiation, marginal-likelihood, cosmology]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.26644
raw: raw/2603.26644.pdf
authors: [Toby Lovick, David Yallup, Will Handley]
year: 2026
---

# Automatic Laplace Collapsed Sampling (ALCS)

ALCS 用自动微分把高维隐变量 `z` 在每次 likelihood 评估时坍缩成一个标量贡献(MAP + Laplace 近似),使外层 nested sampling 只在低维超参数 `θ` 空间运行,从而把 Bayesian evidence 计算扩展到 `d_z ~ 25,600` 的高维隐空间。

## 问题

Bayesian model comparison 依赖 marginal likelihood(evidence)`Z = ∫ L(D|θ) π(θ) dθ`。计算 evidence 的标准方法 nested sampling 随参数维度 `d` 呈约 `O(d^3)` 的代价增长(需同时扩大 live points 数 `m`、内层采样去相关步数 `f`,以及先验到后验的 KL 收缩 `D_KL`),当 `d ≳ 100` 时基本不可行。许多高价值的科学推断流水线(分层超新星宇宙学、星系族群建模、引力波族群推断等)天然分为两类参数:少量"感兴趣参数"`θ` 与大量"隐变量/冗余参数"`z`(逐对象测量噪声、离散场值等)。后者本身不重要,但其不确定性必须正确传播到 `θ` 的后验上。现有做法要么把 nuisance 在单一参考点边缘化(损失 `θ` 依赖的真实灵敏度),要么需要逐问题手工推导 gradient 与 Hessian。

## 方法

ALCS 假设先验可分解 `π(θ,z) = π(θ) π(z|θ)`,目标是 latent-marginalised likelihood `L_marg(θ) = ∫ L(D|θ,z) π(z|θ) dz`。对每个固定 `θ`,算法两步走(见 Algorithm 1):

- Step 1 优化:用 L-BFGS 求隐变量的条件 MAP `ẑ(θ) = argmax_z [log L + log π(z|θ)]`,gradient 由 [[automatic-differentiation]] 提供。
- Step 2 Laplace:在 MAP 处用 `jax.hessian`(forward-over-reverse)计算 negative Hessian `H(θ)`(精度矩阵),代入 [[laplace-approximation]] 公式得到 `log L_ALCS(θ) = log L(D|θ,ẑ) + log π(ẑ|θ) + (d_z/2)log(2π) − (1/2)log det H`。

外层用 [[nested-sampling]] 的 nested slice sampling 实现(基于 [[blackjax]]),只在 `θ` 空间探索;每个 dead point 调用一次 ALCS,batch 内通过 `jax.vmap` 在 GPU 上并行(本文用 NVIDIA H200)。整套实现"automatic":只需可微的 joint log-posterior,无需手写 gradient/Hessian 或模型专用代码,并支持 prior whitening、warm-start 预条件、block-diagonal/banded(稀疏)Hessian。计算代价中 log-det 为 `O(d_z^3)`(稠密 Cholesky)或 `O(d_z)`(块对角/三对角),总 nested sampling 代价 `~ O(d_θ^4 · d_z)`,相比联合采样的 `O((d_θ+d_z)^3)` 大幅降低。

Student-t 扩展:当隐变量后验重尾时,Gaussian Laplace 系统性低估 evidence。ALCS 在 Cholesky-whitened 基中,用每方向 log-posterior 的四阶导估计 excess kurtosis `κ̂_j` 与自由度 `ν̂_j = 4 + 6/κ̂_j`,把 Gaussian normalising constant 替换为 Student-t,仅需每方向两次额外标量 autodiff、无需采样。

## 结果

- 超新星宇宙学(Tripp 分层模型,ΛCDM/wCDM):Test 1 固定 `d_z=2`、`N` 从 64 到 2048,wall time 从 12s 增到 45s(ΛCDM),per-call 代价 `t_single ≈ 1.2ms` 在所有 `N` 上基本恒定;evidence 误差 `δ log Z` 始终 < 0.25 nats。Test 2 固定 `N=100`、隐维度扩到 `D = 25,602`,wall time 从 9s(D=200)增到 693s(约 12 分钟),而投影的全量 NS(`O(D^3)`)在同规模需约 37 年;`|δ log Z|` 在全部八个规模上不超过 0.06 nats,证实 Gaussian Laplace 找到了该模型的精确解。
- Student-t 扩展(`ν_true=5`):Gaussian ALCS 在 `N_obj=50` 误差 −1.00 nats、`N_obj=150` 为 −1.86 nats;Student-t 修正在 `N_obj=50` 降到 −0.17 nats(改善 83%),`N_obj=100` 与全量 NS 一致到 0.01 nats。IS ESS/K 诊断显示 Student-t proposal 一致优于 Gaussian(如 0.49 vs 0.38 @ N_obj=50)。
- Neal's funnel + tanh 观测(失败案例):全量 NS `log Z = −15.94 ± 0.05`,Gaussian ALCS `log Z = −16.68 ± 0.04`(误差 −0.74 nats,约 18σ)。误差在 `θ > 0`(tanh 饱和、非局部 flat shoulders)区域急剧增大;IS ESS/K 在 `θ < 0` 约为 1、`θ > 0` 远小于 0.01,精确定位了 Gaussian 假设失效的区域;Student-t 局部修正无法补救此类非局部失败。
- inference_gym 六模型基准:Eight Schools / Radon / Brownian Motion(隐条件 Gaussian)`δ` 分别为 0.00 / −0.003 / −0.027 nats(精确),ESS/K=1.00;LGCP(`δ=+0.15`,相对全量 102D NS 约 64× 加速,33s vs 35min);Stochastic Volatility `δ=−0.24`;IRT 边缘化 500 隐变量,`θ` 后验与 Stan MCMC 一致。NUTS vs ALCS wall time 上,Eight Schools 15×、Radon 17×、Brownian 13×、LGCP 3× 加速。

## 在本 wiki 中的位置

本文属于 Bayesian 推断/probabilistic ML 方法,核心机制是 [[laplace-approximation]] + [[nested-sampling]] + [[automatic-differentiation]],与本 wiki 主流的 LLM/agent 主题关联较弱,主要可作为"用 autodiff 实现可扩展概率推断"的方法参照。作者来自 [[university-of-cambridge]] Handley Lab,实现基于 [[jax]]/BlackJAX,并提到 Claude([[anthropic]])与 Gemini([[google]])辅助了代码、绘图与文稿校对。
