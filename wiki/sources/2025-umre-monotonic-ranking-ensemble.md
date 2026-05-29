---
type: source
subtype: paper
tags:
  - recommender-system
  - ranking-ensemble
  - multi-task-learning
  - monotonic-neural-network
  - pareto-optimality
  - kuaishou
  - watch-time
created: 2026-05-29
updated: 2026-05-29
arxiv: "2508.07613"
raw: raw/2508.07613.pdf
authors:
  - Zhengrui Xu
  - Zhe Yang
  - Zhengxiao Guo
  - Shukai Liu
  - Luocheng Lin
  - Xiaoyan Liu
  - Yongqi Liu
  - Han Li
year: 2025
---

# UMRE: A Unified Monotonic Transformation for Ranking Ensemble in Recommender Systems

UMRE 把工业 [[recommender-systems|recommender-system]] 中的 ranking ensemble(集成排序 / ensemble sorting)做成端到端可学习框架:用 **Unconstrained Monotonic Neural Network(UMNN)**替代手工设计的 pxtr 变换,用注意力做个性化融合,并用 Pareto 最优策略动态调整多目标权重。

## 问题

工业推荐系统通常是 retrieval → pre-rank → rank 的漏斗式多阶段流程。在每个排序阶段,先由 [[multi-task-learning]](MTL)模型(如 [[mmoe]]、[[ple]])预测多种用户行为概率(论文统一记作 pxtr,如 pctr、pltr),再由 **ensemble sorting** 把多个 pxtr 融合成一个最终排序分。这一融合通常分两步:

- **pxtr transformation**:对每个 pxtr 做非线性变换(传统用多项式 / 指数函数,带 α、b、β 等缩放参数),以拉开分数区分度、对齐不同任务的分布尺度。
- **pxtr fusion**:把变换后的分数加权聚合成 ensemble score(加法或乘法公式)。

传统做法的痛点:(1) 变换函数和融合权重都靠人工调参,任务一多,超参空间组合式爆炸,难以达到 [[pareto-optimality|Pareto efficiency]];(2) 静态权重无法捕捉个体用户偏好,缺乏个性化;(3) ensemble 任务缺乏显式监督信号(不像 MTL 有明确的二值标签),常见做法是只用单一主目标(如 [[watch-time]] / long view)做监督,或用 RL 把权重当 action,但都难以兼顾多个相互冲突的指标。

## 方法

UMRE 用一个全可学习的端到端框架同时替换变换函数 gk 和融合函数 F:

- **UMNN 单调变换模块**:每个目标 k 的变换 gk 用 Unconstrained Monotonic Neural Network 建模——把变换写成对一个被约束为严格正(MLP 输出加 ELU+1)的积分函数 fk(t, h; θk) 的积分,从而保证 gk 严格单调(保序),同时积分函数以用户/物品 embedding h 为条件,实现个性化、非线性缩放。推理时用 Clenshaw-Curtis 积分(Q=32 节点)近似;反向传播用 Leibniz 积分法则避免存储中间积分结果,显存仅 ∝ 模型大小。
- **Ranking Ensemble 模块**:用户历史行为序列(item / category / action-type embedding 拼接)经 [[gru4rec]] 编码成用户向量,再以用户向量为 query 对变换后的预测 embedding 与类别 embedding 做 **cross-attention**,得到动态、个性化的融合权重 w,最终 ensemble score 为 s = Σ wk·tk。
- **Pareto-Optimal 奖励设计**:训练目标是 ensemble score 与一个加权复合 reward r(多种二值行为反馈加权和)之间的 MSE。行为权重 ωm 不固定,而是按 epoch 根据各任务 **UAUC(User-level AUC)**的变化动态调整(Algorithm 1):某指标下降则提高其权重(优先欠拟合目标),上升则降低,形成负反馈,逼近 Pareto 最优。
- 预训练:公开数据集无现成 pxtr,作者用 [[ple]] 作为 MTL 模型生成各任务 pxtr 作为输入。

## 结果

在两个公开数据集 [[kuairand]](短视频,KuaiRand-1K 子集,1,000 用户)与 **Tenrec**([[tencent]] 文章/视频推荐,取曝光最多的 50,000 用户)上,以每个任务标签的 **HR@3** 与 **NDCG@3** 评测(Table 4):

- UMRE 在所有任务、两个指标上均优于基线(SingleSort、LR、MLP、aWELv、IntEL)。KuaiRand 上 Click 的 HR@3 从最优基线 0.8821(IntEL)提升到 **0.9523**;Like HR@3 0.4629、Follow 0.3502、Comment 0.2653、Forward 0.2113、Long view 0.9192,在稀疏交互目标(follow/comment/forward)上提升尤为显著。
- **UMNN 模块的通用性**(Table 5,KuaiRand NDCG@3):把 UMNN 加到 LR/MLP/aWELv/IntEL 等各基线上,HR 与 NDCG 均一致提升(例如 MLP 的 Follow 0.0612→0.1071,IntEL 的 Click 0.6064→0.6628),证明该单调变换模块可即插即用。
- **消融**(Table 6):去掉 Pareto 最优策略后需手工设权重,效果下降;Pareto 自适应加权在欠拟合任务上提升明显;同时引入 user-side 与 item-side 特征带来最大增益。
- **在线 A/B**(Table 7):在一个超 4 亿用户的短视频平台精排阶段测试,相对 formula-based MTF 基线,Like +5.477%、Follow +2.730%、Forward +5.023%、Comment +6.408%。

## 在本 wiki 中的位置

本文属于工业 [[recommender-systems|recommender-system]] 的 **multi-task fusion / ranking ensemble** 方向,与 [[mmoe]]、[[ple]]、[[esmm]] 等 [[multi-task-learning]] 工作衔接:MTL 负责产出多任务 pxtr,UMRE 负责把它们个性化、保序地融合成最终排序分。它把 [[pareto-optimality]] 思想用于多目标权重的动态调度,并用 [[gru4rec]] 编码用户序列做 context-aware 融合;数据与场景上与 [[kuairand]]、[[kuaishou]]、[[watch-time]] 等短视频推荐研究密切相关。作者来自 Beijing Jiaotong University 与 [[kuaishou]]。
