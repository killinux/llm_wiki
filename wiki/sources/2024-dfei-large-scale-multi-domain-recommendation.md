---
type: source
subtype: paper
tags: [multi-domain-learning, recommender-system, multi-task-learning, ctr-prediction, feed-recommendation, mixture-of-experts]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2404.08361
raw: raw/2404.08361.pdf
authors: [Dongbo Xi, Zhen Chen, Yuexian Wang, He Cui, Chong Peng, Fuzhen Zhuang, Peng Yan]
year: 2024
---

# Large-Scale Multi-Domain Recommendation: an Automatic Domain Feature Extraction and Personalized Integration Framework (DFEI)

DFEI 是来自 Meituan 的大规模多域(multi-domain)[[recommender-system]] 框架,自动地把单个用户行为聚合为"域特征",并为每个用户个性化地整合来自其他域的域特征,从而在 [[multi-task-learning]] 之上显著提升多场景 CTR 预测性能。

## 问题

在 feed 推荐中,一个 App 往往包含很多场景(域),需要在 App 内甚至 App 外的多个域上同时建模并预测用户兴趣。多域学习(multi-domain learning, MDL)是常用方案,常见做法是为每个域分别设计共享模块与专有模块(如 [[mmoe]]、[[ple]]、STAR、HiNet 等)。但仍存在两个长期挑战:

1. 用域特征准确刻画各域之间的差异对提升每个域的性能至关重要,但为大量域手工设计域特征与模型既费力又易出错。
2. 用户通常只在少数几个域有曝光(impression),在新域推断时其域相关特征往往缺失;如何自动地从其他域抽取特征并用于提升本域预测,一直是难题。

## 方法

DFEI 框架包含两个核心模块,建立在共享 Embedding、Shared Tower 与各域专有 Tower 之上(域差异建模本身不是本文重点):

- 自动域特征抽取 DFE(Domain Feature Extraction):把每个用户的行为转化为域内所有用户行为的聚合,作为域特征。训练阶段用滑动平均更新域特征 v_d^t = α·v_d^{t-1} + (1-α)·pooling(u_d^t),其中 pooling 为 mini-batch 内样本的 mean-pooling,α 为衰减系数;推断阶段直接采用最终训练状态 v_d = v_d^T。相比传统离线特征工程,抽取出的域特征是与目标 label 直接相关的高阶表示。
- 个性化域特征整合 DFI(Domain Feature Integration):用所有域特征 v_1,...,v_D 增强每个域的预测,z_d = Σ_d w_d·h_1(v_d),其中个性化整合权重 w_d 由 h_2(e_d) 与 h_3(v_d) 的点积经 softmax(缩放 √k)得到。最终预测 ŷ_d = sigmoid(MLP(concat([s_d, u_d, v_d, z_d])))。

联合优化采用各域 cross-entropy 损失,循环喂入各域 mini-batch;在共享参数 θ^s 的学习率上施加 1/D 的缩放因子以平衡学习过程(每个训练步会更新各域专有参数 θ_d 一次,而共享参数被更新 D 次)。框架用 TensorFlow 实现,Adam 优化器,batch size 512,学习率 1e-3,在 NVIDIA Tesla V100 (16G) 上训练。

## 结果

在两个数据集上评测 CTR 预测,指标为 AUC,每个实验跑 5 次取平均并做配对 t 检验。

- 工业数据集:来自 Dianping(大众点评)的真实日志,共 21 个场景(#A1–#A21),数千万样本,按用户 id 以 8:1:1 划分训练/验证/测试,各域 CTR 从 1.09% 到 9.45%。DFEI 平均 AUC 达 0.6761,优于所有 baseline(MLP 0.6221、MMoE 0.6579、PLE 0.6597、AITM 0.6625、HiNet 0.6740 等),提升具统计显著性。
- 公开数据集:[[kuairand]](KuaiRand-1K,来自 Kuaishou),按 "tab" 字段划分域,选取 6 个最大域(#B1–#B6),各域 CTR 从 12.00% 到 56.05%。DFEI 平均 AUC 0.7281,优于 MLP 0.7107、MMoE 0.7225、PLE 0.7183、AITM 0.7236、HiNet 0.7256 等。
- 消融实验(公开数据集):去掉 DFEI(w/o DFEI)与去掉 DFI(w/o DFI)都使平均 AUC 下降,说明 DFE 与 DFI 均有效;在共享参数上使用 1/D 学习率缩放因子可获得更高的平均 AUC。
- 超参研究:衰减系数 α 在 0.9 时取得最佳平均 AUC。t-SNE 可视化显示学到的域特征能区分 CTR<5% 与 CTR>5% 的域,表明域特征编码了与 label 相关的高阶信息。

代码已开源:https://github.com/xidongbo/DFEI

## 在本 wiki 中的位置

本文属于推荐系统中的多域/多场景建模方向,可与 [[recommender-system]]、[[multi-task-learning]]、[[mmoe]]、[[ple]] 等基础方法相互对照(DFEI 把它们作为 baseline 与组件)。其实验使用了本 wiki 已收录的 [[kuairand]] 数据集。该工作不涉及 LLM,但展示了"自动特征抽取 + 个性化整合"在大规模工业推荐中的工程范式,与 wiki 中推荐系统去偏/多任务相关条目互补。
