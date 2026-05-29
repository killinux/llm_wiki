---
type: source
subtype: paper
tags: [multi-task-learning, recommender-system, mixture-of-experts, scaling-law, ctr, kuaishou, sparse-routing]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2602.09386
raw: raw/2602.09386.pdf
authors: [Yukun Zhang, Si Dong, Xu Wang, Bo Chen, Qinglin Jia, Shengzhe Wang, Jinlong Jiao, Runhan Li, Jiaqing Liu, Chaoyi Ma, Ruiming Tang, Guorui Zhou, Han Li, Kun Gai]
year: 2026
---

# SMES: Towards Scalable Multi-Task Recommendation via Expert Sparsity

提出 **SMES(Scalable Multi-task recommendation via Expert Sparsity)**,一个可扩展的稀疏 [[mixture-of-experts]] 框架,通过 progressive expert routing 将参数 scaling 转化为多任务推荐中的稳定收益,并已在 [[kuaishou]] 服务超过 4 亿日活用户。

## 问题

工业级 [[recommender-systems]] 依赖 [[multi-task-learning]] 同时预测多种用户反馈信号(如 Click、Like、Share、Effective-view、Long-view)并聚合用于排序。近年来受 [[large-language-models]] 启发,推荐界尝试通过 model scaling 提升效果,但工业推荐受限于高并发、低延迟和 ROI:

- **uniform scaling 的失配**:盲目放大参数会带来过高的在线推理成本,且对 label 稀疏、分布倾斜的任务(如 like、follow)收益递减甚至性能下降(论文 Figure 1 在 [[kuairand]] 上展示了这一现象)。
- 直接把稀疏 [[mixture-of-experts]] 用于多任务推荐有两个核心障碍:
  - **exploded expert activation**:多任务各自独立 top-K 路由时,被激活专家的并集 |U| 随任务数 T 增长,实际可达 dense 状态(K ≤ |U| ≤ min{E, TK}),破坏 instance-level 稀疏性;
  - **severe expert load skew**:跨任务聚合的路由负载使少数热门专家被反复激活,大量专家欠训练,训练不稳定、大专家池利用率低。

## 方法

SMES 保留标准多任务架构(共享 encoder F、专家池 {f_e}、各任务 head φ_t),重新设计专家路由与执行,含两个核心组件:

1. **Progressive Expert Routing (PER)**:每个 instance、每个任务只激活 K ≪ E 个专家,分解为 K = K_s + K_a。
   - Stage-I task-shared experts:用任务加权 pooling 的 normalized 路由概率计算 global routing score s_e,选出所有任务共享的 K_s 个专家集合 S,保证每个 instance 至少有 K_s 的重叠。
   - Stage-II task-adaptive experts:每个任务从 S 的补集中再选 K_a 个专家,保留 task-specific 容量。
   - **Deduplicated Expert Execution**:跨任务并集 U = ∪ K_t,每个被选专家在一个 instance 上至多计算一次(|U| ≤ K_s + T·K_a),稀疏聚合时只在激活专家上 renormalize。

2. **Multi-Task Load-Balancing (MTLB) Regularizer**:对 mini-batch 内聚合的 selection frequency f̄_e 与 probability mass p̄_e,最小化 L_lb = (E/K) Σ f̄_e · p̄_e,抑制跨任务共同造成的专家热点,稳定大专家池下的训练。总目标 L = L_task + β·L_lb。

**部署与系统优化**:针对 deduplicated 路由导致的 ragged tensor / 动态形状问题,提出 **Reindexed Grouped GEMM**(受 [[megablocks]] 启发,把稀疏激活映射为紧凑 dense 计算,经 Traffic Calculation、Gather&Map reindexing、Grouped GEMM、按 π 重建任务表示四阶段),并用 profiling-guided workspace allocation 预分配固定大小内存页池以降低延迟。

## 结果

- 数据集:公开 **[[kuairand]]-1K**(1000 用户、12 任务)与工业 **Kuaishou**(4×10⁹ 用户、3×10⁸ items、5×10¹⁰ instances、21 任务);离线聚焦 Effective-view、Long-view、Click、Like 四个任务。指标为 AUC 与 **GAUC**(GAUC 为短视频推荐的主指标)。
- Baselines:[[mmoe]]、[[ple]]、MoME、[[home]]、[[rankmixer]]。两种配置:SMES-S(匹配 baseline 参数预算,sparsity ratio 8%)与 SMES-L(扩大专家容量,633M 参数)。
- **离线效果**(Table 2):SMES-S 在 KuaiRand-1K 与 Kuaishou 两数据集所有任务上取得最高 AUC/GAUC;相对 RankMixer,SMES 在 watch-time 类任务(Effective-view)平均 GAUC gain 约 **0.1%**,在 interaction 类任务(Click、Like)增益更大。SMES-L 进一步提升,说明可有效利用额外容量。
- **可扩展性**(Figure 3):SMES 随参数 scaling 持续受益、避免 dense MoE 的递减收益;扩展到 0.6B 参数带来 0.84% GAUC 提升而仅增加约 4ms 延迟,而 dense 模型延迟近线性增长。
- **消融**(Table 3):去掉 Task-SHA(task-shared)显著掉点,去掉 Task-ADA(task-adaptive)与去掉 Reg(load-balancing)均有明显/中等掉点,验证三组件互补。
- **在线 A/B**(Kuaishou Single Page,3.5% 流量,2025-10-25 至 10-31):相对 [[home]] baseline,user watch time 提升 **+0.31%**,Like **+0.64%**、Follow **+1.56%**、Comment **+2.45%**(均统计显著);相对同容量 dense MoE 推理延迟降低 **50%**。已全量部署,服务超 4 亿日活。

## 在本 wiki 中的位置

本文属于 **[[recommender-systems|recommender-system]] 的 [[multi-task-learning]] / model scaling** 方向,是 [[mmoe]]、[[ple]]、[[home]] 一脉 MoE 多任务推荐的延续,核心创新在于用 expert sparsity 解决多任务稀疏路由特有的 exploded activation 与 load skew 问题,使参数 [[scaling-law]] 在工业延迟约束下可落地。可与 [[rankmixer]](稀疏 scaling 排序模型)、[[megablocks]](sparse MoE 高效 kernel)、以及 [[deepfm]]/[[din]] 等 [[ctr]] backbone 对照阅读。来自 [[kuaishou]] / [[huawei-noahs-ark-lab]] 相关研究者。
