---
type: source
subtype: paper
tags: [multi-domain-recommendation, recommender-system, disentangled-representation-learning, multi-embedding, covariance-loss, dimensional-collapse, mixture-of-experts]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2405.12706
raw: raw/2405.12706.pdf
authors: [Zhutian Lin, Junwei Pan, Haibin Yu, Xi Xiao, Ximei Wang, Zhixiang Feng, Shifeng Wen, Shudong Huang, Dapeng Liu, Lei Xiao]
year: 2024
---

Crocodile 是一个面向多域推荐(MDL)的多嵌入(Multi-Embedding)架构,通过对多张共享 embedding 表施加 cross-experts covariance loss(CovLoss)来解耦各 expert 的表示,同时用 Prior Informed Element-wise Gating(PEG)路由,从而在"保持各域差异性"与"充分学习参数"这两个相互冲突的目标之间取得平衡。

## 问题

多域学习([[recommender-systems|recommender-system]] 中的 Multi-Domain Learning, MDL)既要学习域间的共性,又要保留每个域的差异性(distinctiveness)。作者指出现有方法陷入一个两难:

- **保持域差异性 vs. 充分学习参数**。沿"Tower→Embedding"方向,各类方法逐层把 domain-aware 模块下沉:Shared-Bottom 与 STAR 在 tower 层做域专属;HiNet、M-scan、HierRec 把焦点放到 expert 层;PEPNet 进一步强调 domain-specific 的 transformed embedding。但由于 embedding 占据了模型绝大多数参数,这些 expert/transformation 网络容量有限,保持域差异性的能力存疑(Finding 1)。
- 受单任务多嵌入(Multi-Embedding)范式启发,可为每个特征学多张 embedding 以缓解 [[dimensional-collapse]](由 Interaction-Collapse 理论引起)。多任务领域的 STEM(Shared and Task-specific EMbedding)用任务专属 embedding 保留差异性。但作者把它们迁到 MDL(得到 ME-PLE、SDEM 等基线)后发现:**domain-specific embedding 在小域上训练样本太少,学不充分,出现 dimensional collapse**(Finding 2)。例如 Kuairand1k 数据集 S0 与 S6 之间数据量相差 12 倍。

作者用两个指标量化这两个困境:Diversity Index(DI,衡量 expert 输出的多样性/域差异性)与 Information Abundance(IA,奇异值之和除以最大奇异值,衡量是否发生 dimensional collapse)。

## 方法

Crocodile = **Cro**ss-experts **Co**variance loss for **Di**sentangled **Le**arning。整体由三部分组成(见原文 Fig. 3):

- **Multi-Embedding (ME) Layer**:为输入的 F 个 field 维护 M 套 embedding 表,每套喂给对应的 expert。关键设计:与 ME-PLE / SDEM 不同,Crocodile 的所有 embedding 与 expert **全部跨域共享**,因此小域也能被所有域的数据共同优化,缓解小域 embedding 学不充分的问题。
- **Cross-expert Covariance Loss(CovLoss)**:受 VICReg、Maximal Coding Rate Reduction 等工作启发,对任意两个 expert 输出 O^(p)、O^(q) 计算去中心化后的协方差矩阵的 L1 范数并求和:L_Cov = (1/d²) Σ_{p,q∈M×M, p≥q} || (O^(p)−Ō^(p))ᵀ (O^(q)−Ō^(q)) ||_1。它显式地在 expert 之间做表示解耦(de-correlation),从而让不同 expert 编码用户多样甚至冲突的兴趣。总损失为 L = Σ_s (1/N_s) Σ_k L_BCE(ŷ_k^(s), y_k^(s)) + α·L_Cov。
- **Prior Informed Element-wise Gating(PEG)**:针对域数量很大时门控参数随域数膨胀的问题,用独立于域的 prior embedding(选取 user ID / item ID / domain ID 作为 prior field)生成门控权重 g_k^s = Softmax(r_k W_g^s),再对 expert 输出做 element-wise 门控 t_k^s = g_k^s ⊙ O_k(逐维度而非整体加权,以配合 CovLoss 的逐维度解耦)。

作者还讨论了计算复杂度:CovLoss 复杂度为 M(M−1)/2 × (d²N),远小于 MMoE expert 本身的开销;且通过采样(低至 32 个样本即可,p>0.1 不显著)可再降约 99.2%。

## 结果

在两个公开数据集 **Kuairand1k**(11.6M 样本,5 个域)与 **AliCCP**(85.3M 样本,3 个域)上评测,指标为 AUC 与 gAUC,实验重复 6 次取均值。

- **整体最优(RQ1)**。Kuairand1k 上 Crocodile 整体 AUC 0.78683 / gAUC 0.66373,较第二名分别显著提升 0.09% 与 0.19%;AliCCP 上整体 AUC 0.62327 / gAUC 0.59170,较第二名分别提升 0.138% 与 0.12%。论文引用业界经验:0.1% 的 gAUC 提升即被视为巨大改进。
- **ME 版基线退化**。ME-PLE 相比 PLE 的整体 AUC/gAUC 反而低 0.07%/0.02%,最小域(S6)下降最严重(均超 0.3%),印证 Finding 2;Crocodile 在最小域 S6 上比 ME-PLE 高 0.68% AUC、1.8% gAUC,比 SDEM 高 0.37% AUC、0.98% gAUC。
- **CovLoss 有效解耦(RQ2)**。加 CovLoss 后 3-th 与 5-th expert 之间的协方差比不加时低约 3×10³ 倍;在 Base(仅 BCE)之上,CovLoss 带来 0.07% AUC / 0.17% gAUC 提升,优于 Dot、Cos、dCorr、OLE、Importance、Trans5 等其它解耦/正则损失(其中 dCorr 仅 +0.01%,Trans5 甚至 −0.06% AUC / −0.19% gAUC)。
- **消融(RQ3)**。逐一去掉 CovLoss、PEG、ME 三个组件性能均显著下降;在 Kuairand1k 上 CovLoss 最关键,在 AliCCP 上 CovLoss 与 EG 同等重要。
- **超参/容量敏感性(RQ4)**。α 只要不低于 2×10⁻⁵,AUC>0.78590、gAUC>0.66174,保持次优以上;即便仅用 2 套 embedding,Crocodile 的 gAUC(0.66198)/AUC(0.78595)也超过用 5 套 embedding 的其它 ME 方法。
- **线上部署(RQ5)**。在 Tencent 广告平台用 Heterogeneous Experts + ME 框架部署,2024 年 3 月做 5% A/B:转化点击预测多个主任务 +0.11% AUC,主场景 **+0.72% CTR、+0.73% GMV**。并设计了 False Tolerance 容错:辅助域数据异常时回滚到最近有效 checkpoint 仅用主域继续训练。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] / 多域推荐方向,核心贡献是把 [[disentangled-representation-learning]] 的 covariance 思想引入 [[multi-embedding]] 推荐架构以对抗 [[dimensional-collapse]]。

- 方法层面用 [[mixture-of-experts]] 风格的 expert/tower 结构,损失设计与 VICReg、Maximal Coding Rate Reduction 一脉相承(在 expert 之间而非单一表示内部做去相关)。
- 与之对照的多嵌入/多任务方法包括 STEM、PLE、MMoE([[mmoe]])、[[ple]],以及多域基线 STAR、HiNet、PEPNet、AdaSparse。
- 由 [[tencent-ai-lab]] / Tencent 与 Tsinghua University([[tsinghua-university]])合作,提供了从公开数据集到 Tencent 广告平台线上 A/B 的完整证据链,可作为"多域推荐 + 表示解耦 + 工业部署"的参考来源。
