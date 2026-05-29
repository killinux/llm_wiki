---
type: source
subtype: paper
tags: [recommender-system, scaling-law, large-recommendation-model, HSTU, generative-recommendation, sequential-recommendation, ranking]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2412.00714
raw: raw/2412.00714.pdf
authors: [Wei Guo, Hao Wang, Luankang Zhang, Jin Yao Chin, Zhongzhou Liu, Kai Cheng, Qiushi Pan, Yi Quan Lee, Wanqi Xue, Tingjia Shen, Kenan Song, Kefan Wang, Wenjia Xie, Yuyang Ye, Huifeng Guo, Yong Liu, Defu Lian, Ruiming Tang, Enhong Chen]
year: 2024
---

# Scaling New Frontiers: Insights into Large Recommendation Models

来自 [[huawei-noahs-ark-lab]] 与 [[university-of-science-and-technology-of-china]] 的工作,系统评估了 large recommendation models 的 scaling law,以 Meta 的生成式推荐模型 HSTU 为代表,在多种 backbone、复杂用户行为建模与 ranking 任务上验证其可扩展性。

## 问题

传统 [[recommender-system]] 主要靠扩大稀疏参数(如 embedding table,可达数十 TB)来提升规模,但 dense 网络参数往往在千万到亿级就出现瓶颈,难以从更多参数中持续获益。受 [[large-language-models]] 成功启发,出现了通过创新结构扩展 dense 参数的 large recommendation models,其中 Meta 的生成式推荐模型 HSTU 把参数扩展到数千亿、展示了推荐系统的 [[scaling-law]]。但 large recommendation models 的 scaling 仍研究不足:scaling law 是否跨不同 backbone 架构成立?它源自哪些组件?HSTU 在复杂行为建模与 ranking 任务上的表现如何?本文旨在系统回答这些问题。

## 方法

论文围绕四个研究问题(RQ1-RQ4)展开:

- **RQ1 跨 backbone 的 scaling**:在 recall 任务上比较 HSTU、[[llama]]、[[gpt-3]](GPT 架构)与 [[sasrec]] 四种 transformer-based backbone,通过增加 attention block 数量(2/4/8/16/32)考察参数扩展是否带来性能提升。
- **RQ2 scaling law 的来源**:对 HSTU 做 ablation,逐一移除关键组件——relative attention bias(r.a.b.,基于相对位置与时间差 bucket)、用 SiLU 替代 softmax 做 attention score weighting、feature interaction(point-wise transformation layer);并分析 embedding dimension、模型层数、attention head、序列长度等超参数。还尝试把 r.a.b. 与不同残差连接方式(HSTU 式 vs [[llama]] 式 pre-norm)引入 [[sasrec]],探索能否赋予传统模型 scaling 能力。
- **RQ3 复杂用户行为建模**:评估 HSTU 在三类场景——带 side information(用户/物品属性)的序列建模、multi-behavior 序列建模(CIKM、IJCAI 数据集,显式 behavior token)、multi-domain 序列建模([[amazon-reviews]] 跨域 AMZ-MD,对比 C2DSR、SASRec)。
- **RQ4 ranking 任务**:首次系统评估 HSTU 在 ranking 上的可扩展性,用 binary cross-entropy loss 预测点击,对比 DIN 与 [[llama]];研究负采样比例、scoring network 架构(Dot / MLP / FFN)、embedding size 的影响。

实验数据集包括 [[movielens]] ML-1M / ML-20M、[[amazon-reviews]] AMZ-Books、[[kuairand]] KuaiRand-27k 等;评测指标用 HR@K、[[ndcg]]@K、MRR(recall)与 AUC、Logloss(ranking);用 8x 华为 D910B NPU + Accelerate 训练。

## 结果

- **RQ1**:block 数较少时四种 backbone 表现接近;扩大参数后只有 HSTU 与 [[llama]] 表现出良好 scaling,[[gpt-3]]、[[sasrec]] 几乎无 scaling。在 ML-20M 上 HSTU HR@10 从 2 blocks 的 0.2915 升到 16 blocks 的 0.3520;GPT 在 8 blocks 后崩溃(HR@10 跌至 0.0302)。性能随数据集规模与模型规模变化,即使架构固定。
- **RQ2 ablation**(ML-20M):去掉单个组件 HSTU 仍基本保持可扩展性,说明其鲁棒。relative attention bias 中以时间信息最关键:Rel. Position + Time Diff. Bucket 取得 HR@10 0.3376 / NDCG@10 0.1967,优于仅相对位置(0.3122)或无 bias(0.3083),RoPE(0.3149)甚至不如仅位置信息。attention score function 用 SiLU(0.3376)优于 Softmax(0.3298),因 softmax 会限制 attention 表达力。移除 feature interaction 使 HR@10 从 0.3376 降至 0.3154。参数分析结论:更长序列不一定更好;模型规模需与数据集规模匹配,最优层数 L 与 embedding dim D 之积近似恒定(size ∝ O(LD));attention head 数对 recall 影响不大。t-SNE 可视化显示 HSTU embedding 最接近原点 (0,0),归一化对浅层与深层模型都重要。把 r.a.b. 加到 Llama 式残差连接可显著提升 SASRec 的可扩展性。
- **RQ3**:side information 多数情况下略微降低性能(简单 mean pooling 不足以提取 metadata 价值),但加深网络仍保持 scaling。multi-behavior:更丰富的行为数据(buy & pv → all)提升性能(CIKM HR@50 从 0.1089 升到 0.1761);显式 behavior token(HSTU w/b)优于不显式建模。multi-domain:HSTU 在 AMZ-MD 多数域超过 C2DSR/SASRec(如 Digital Music HR@10 0.1451 vs SASRec 0.1332),在物品少的域获益于跨域知识迁移,有望缓解 [[cold-start]]。
- **RQ4**:HSTU 在 ranking 上优于传统 DIN 与 [[llama]],且随 block 增加持续 scaling(ML-1M AUC 最高 0.7947);Llama 在小 block 时常更好但扩展性差。Logloss 下降不一定对应 AUC 提升,提示不能只盯 loss 的 scaling。增大负采样比(0.2→1.0)持续提升性能,大数据集(ML-20M)增益更明显。scoring network:小数据集(ML-1M、AMZ-Books)用更简单结构(Dot)更好,大数据集(ML-20M)用复杂结构(FFN)更优。把 embedding size 缩到 4,小数据集反而提升、大数据集 ML-20M 持续下降,说明模型规模(含 embedding 横向尺度)需与数据规模匹配。

## 在本 wiki 中的位置

本文是把 [[scaling-law]] 从 [[large-language-models]] 引入 [[recommender-system]] 的代表性综述加实证工作,核心研究对象是生成式推荐范式下的 large recommendation model(以 HSTU 为代表)。它与 wiki 中 [[llm-for-recommendation]]、[[sequential-recommendation]]、[[sasrec]]、[[movielens]]/[[amazon-reviews]]/[[kuairand]] 等条目相连,提供了推荐侧 scaling、ablation 与 ranking 可扩展性的系统证据,可作为理解“推荐模型如何 scale”的入口。
