---
type: source
subtype: paper
tags:
  - recommender-system
  - graph-contrastive-learning
  - graph-neural-network
  - adversarial-robustness
  - collaborative-filtering
created: 2026-05-29
updated: 2026-05-29
arxiv: 2407.10184
raw: raw/2407.10184.pdf
authors:
  - Jiakai Tang
  - Sunhao Dai
  - Zexu Sun
  - Xu Chen
  - Jun Xu
  - Wenhui Yu
  - Lantao Hu
  - Peng Jiang
  - Han Li
year: 2024
---

# Towards Robust Recommendation via Decision Boundary-aware Graph Contrastive Learning (RGCL)

提出 RGCL,用「决策边界感知」的对抗扰动来约束 graph contrastive learning 增强视图的探索空间,在保持语义不变性(rationality)与提升对比难度(hardness)之间取得平衡,从而构建更鲁棒的 [[recommender-systems|recommender-system]]。

## 问题

graph contrastive learning(GCL)近年被广泛用于缓解 [[recommender-systems|recommender-system]] 中由 data sparsity 引起的偏差,但现有 GCL 推荐模型存在两类局限:

- **Hardness-driven 方法**(如 SGL,用 node dropout / edge dropout 构造困难视图)盲目追求样本难度,可能删掉关键节点或边,破坏 task-specific 语义。
- **Rationality-driven 方法**(如 SimGCL,仅加入轻微特征扰动)保住了语义结构,但牺牲了引入 hard samples 带来的多样化知识。

作者指出,挑战性正样本对(challenging positive pairs)与 hard negative pairs 对 GCL 推荐都至关重要,而现有方法难以在动态训练过程中自适应地平衡 hardness 与 rationality。此外大多数方法假设实体独立(entity independence),忽略 user-user、item-item 间的全局协同关系;而无监督 GCL 一味追求表示均匀性还可能缩小数据点与决策边界的间隔(margin),降低模型鲁棒性。

## 方法

RGCL 以 LightGCN 为 backbone(BPR loss 为推荐主目标),包含三个核心组件:

- **Decision Boundary-aware Perturbation(决策边界感知扰动)**:把推荐建模为 ranking 问题,为每个 user/item 的每一高阶图表示层独立求解能保持成对排序(pair-wise ranking)不变的最大扰动 Δ,等价于该表示到决策超平面的正交投影(用 ℓ∞ 范数)。该最大扰动界定了「可容忍扰动球」,作为增强视图的可行探索空间。只扰动高阶表示、跳过原始特征,以保住最丰富的语义信息。
- **Relation-aware Adversarial-Contrastive Augmentation(关系感知对抗对比增强)**:在扰动约束内,借鉴 FGSM 通过最大化对比损失生成 instance-specific 的扰动 η,刻意「混淆」不同 user/item 的身份,从而利用全局 user-user、item-item 关系生成更难且与下游任务相关的第三个视图 Z^ac,再与两个随机增强视图一起做 multi-view contrastive learning。
- **Margin Maximization via Adversarial Optimization(对抗优化做间隔最大化)**:用前述最大扰动构造 adversarial examples 并在 BPR 目标上优化,显式拉大数据点与决策边界的距离,弥补 GCL 追求均匀性导致的鲁棒性下降。

最终联合优化目标为 L = L_BPR + μ·L_ADV + α·L_CL。RGCL 不引入额外可训练参数,训练时间复杂度 O((L|E|+B²)d),与 SimGCL、RocSE 等 SOTA GCL 方法同阶。论文还给出理论分析:证明 contrastive loss 本质是 hardness-aware 机制,并用边界-margin 定理与 PAC-Bayes / loss landscape sharpness 论证鲁棒性。

## 结果

在 5 个公开数据集(MovieLens-1M、Alibaba、Kuaishou、Gowalla、Yelp)上对比 12 个 baseline(传统:BPRMF、NeuMF;GNN:GCMC、NGCF、GCCF、LightGCN;GCL:GraphCL、SGL、LightGCL、RocSE、CGI、SimGCL),指标为 Recall@K 与 NDCG@K(K∈{10,20,50}),采用 full-ranking 评测。

- RGCL 在所有数据集上一致优于全部 baseline,多数提升的 p-value 远小于 0.01。
- 提升最显著的是 Kuaishou 数据集:Recall@10 从 SimGCL 的 0.0788 提升到 0.0899(+14.14%),NDCG@10 +8.00%。
- ML-1M 上 Recall@20 0.2901(SimGCL 0.2798,+3.69%);Yelp、Alibaba、Gowalla 也都有稳定增益。
- 收敛性:RGCL 比 SimGCL、LightGCN 收敛更快,且精度高于同样快速收敛的 LightGCL。
- 消融实验(ML-1M / Yelp):去掉扰动约束(w/o cons)、随机扰动(w/o rand)、关系感知视图生成器(w/o ac)、对抗正则项(w/o adv)后性能均下降,验证各组件均不可或缺。例如 ML-1M Recall@20 从完整 RGCL 的 0.2901 降到 w/o adv 的 0.2832。
- 鲁棒性评测显示 RGCL 对交互稀疏的 user/item 群体(inactive users、long-tailed items)提升更明显,且对扰动超参 ε 远比 SimGCL 不敏感。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] / [[collaborative-filtering]] 方向,核心是把 graph contrastive learning 与 adversarial robustness 结合。它与本 wiki 中的 GCL/对比学习推荐脉络相关,backbone 沿用 LightGCN,优化目标基于 BPR;数据集上用到 [[movielens-1m]](MovieLens-1M)与 Kuaishou 平台数据(参见 [[kuairand]]、[[kuairec]] 同源团队的无偏推荐数据集工作)。该工作由 [[renmin-university-of-china]] 与 [[kuaishou]] 合作完成,作者中包含 [[peng-jiang]]。它解决的 data sparsity 与长尾偏差问题,与本 wiki 中 debiasing / [[selection-bias]] / [[matthew-effect]] 等推荐去偏主题形成方法上的补充(此处走的是对抗+对比的自监督路线,而非因果/IPS 路线)。注意:与 LLM 主线关系较弱,属于推荐系统与图表示学习的支线工作。
