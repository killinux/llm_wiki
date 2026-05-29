---
type: source
subtype: paper
tags:
  - recommender-systems
  - embedding-based-retrieval
  - multi-task-learning
  - candidate-generation
  - prompt-tuning
created: 2026-05-29
updated: 2026-05-29
arxiv: "2302.02657"
raw: raw/2302.02657.pdf
authors:
  - Yuan Zhang
  - Xue Dong
  - Weijie Ding
  - Biao Li
  - Peng Jiang
  - Kun Gai
year: 2023
---

# Divide and Conquer: Towards Better Embedding-based Retrieval for Recommender Systems from a Multi-task Perspective

把推荐系统候选生成阶段的 embedding-based retrieval(EBR)拆成"先把物料聚类、再在每个簇内并行检索、最后合并"的 divide-and-conquer 流程,并从多任务学习视角用 prompt-like 技术为每个簇做轻量任务适配,在公开数据集上 Recall 最高提升约 40%,并已在快手线上部署。

## 问题

EBR(用户塔/物品塔双编码器 + ANN 近邻检索)因简单高效被工业推荐系统广泛用于召回(candidate generation)阶段,但作者在生产实践中发现几个根本问题:

- **easy vs hard negative 的权衡冲突**:召回阶段既要把正样本(positives)从完全不相关的 easy negatives 中区分出来,又要从"相关但竞争力不足"的 hard negatives 中区分出来,这两个目标常相互冲突。业界惯用"按精心调过的比例混合 easy/hard 负样本"其实只是折中,限制了 EBR 上限。
- **多样性与公平性不可控**:ANN 搜索本质是"贪婪地"取最近邻,忽视用户兴趣的多模态结构(如既看喜剧又偶尔看惊悚片),导致长尾兴趣被低估,检索结果的多样性完全依赖 embedding 与长尾兴趣表达。

## 方法

提出 divide-and-conquer 方案([[embedding-based-retrieval]] 的分治改造):

1. **聚类划分**:把整个候选物料集 I 划分为 K 个语义相关的簇 {C_1,...,C_K}。离线实验用对 Word2Vec 物品 embedding 做 K-means 聚类;生产系统则用内部视频品类(如 Sports、Gourmet、Kids 等)兼顾冷启动与可解释性。
2. **簇内并行检索**:在每个簇上分别跑一个 EBR 模型做召回,训练时每个簇只用"同簇内"的负样本(都是 hard negatives),从而让模型专注于难负样本判别;K 个簇并行、每次搜索空间约缩小为 1/K,几乎不增加响应延迟。
3. **可控合并**:训练 user-intent 模型预测用户落入各簇的概率 p_uk,按 M_k = M·[(p_uk)^α / Σ(p_uk')^α] 从各簇取 top-M_k 合并;α 可调,α=0 为绝对公平、α→∞ 为只推最相关簇。
4. **prompt-like 多任务学习(MTL)**:把"各簇内检索"视作 K 个子任务。受 prompt/prefix-tuning 启发,为第 k 个任务引入可训练的 prompt embedding t_k,以参数高效方式做任务适配。由于推荐用的 Transformer(以 [[sasrec]] 为骨干)层数远少于 NLP 场景,简单把 prompt 拼到输入序列收效有限;改用 **Hadamard 积**把 prompt 与每个 token embedding 显式交互(类似 HyperPrompt),即 e_u = Transformer([s_1⊙t_k, ..., s_n⊙t_k])。相比 MMoE/PLE 等重型 MTL,该方法计算开销可忽略。

## 结果

- **离线效果(Table 2)**:在 [[movielens]] ML-1M 与 [[kuairand]] 两个公开数据集上一致优于全部基线(MF、SASRec、SASRec+、MIND、ComiRec)。相对其 base model SASRec,Recall 最高提升 **+27.9%**(ML-1M)与 **+42.7%**(KuaiRand);具体如 KuaiRand R@1000 从 SASRec 的 0.254 提升到 **0.359**(+41.3%)。
- **消融**:去掉 prompt 模块(退化为 naive MTL 共享 SASRec)时,整体性能在 ML-1M/KuaiRand 上分别下降约 5.6% 和 4.2%,但仍显著优于 SASRec+,说明分治本身有效;加上 prompt 后簇内检索效果进一步提升。
- **训练吞吐(Table 4)**:本方法吞吐 25K samples/sec,与 SASRec 持平;而 MMoE 仅 7.2K(约下降 70%),即本方法几乎不增加训练成本。
- **线上 A/B(快手,2022-07-03 至 07-05,实验组 >4000 万用户)**:作为召回通路之一,App Usage Time +0.096%、Likes +0.75%、Follows +1.01%、Shares +1.04%、Downloads +2.40%,均在 p<0.05 显著。与 ComiRec 对比,Click/Like/Follow/Share Rate 分别 +7.8%/+2.5%/+52.3%/+14.4%。该方案已在快手线上稳定运行超过四个月。

## 在本 wiki 中的位置

这是工业级推荐召回的代表性工作,把 [[embedding-based-retrieval]] 与 [[multi-task-learning]] 结合,核心创新是分治召回 + prompt-like 任务适配。它以 [[sasrec]] 为骨干,基线涉及 [[mmoe]]、ComiRec、MIND 等;评测用 [[movielens]] 与快手开源的 [[kuairand]] 数据集。可与本 wiki 中其它多任务推荐工作([[2023-multi-task-deep-recommender-systems-survey]])及 NLP 侧的 prompt-tuning 思想互参。作者来自 [[kuaishou]],含 Peng Jiang、Kun Gai 等。
