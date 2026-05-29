---
type: source
subtype: paper
tags:
  - generative-recommendation
  - recommender-systems
  - dataset
  - benchmark
  - sequential-recommendation
  - multi-modal
  - advertising
  - ctr
created: 2026-05-29
updated: 2026-05-29
arxiv: "2604.04976"
raw: raw/2604.04976.pdf
authors: Junwei Pan, Wei Xue, Chao Zhou, Xing Zhou, Lunan Fan, Yanbo Wang, Haoran Xin, Zhiyu Hu, Yaozheng Wang, Fengye Xu, Yurong Yang, Xiaotian Li, Junbang Huo, Wentao Ning, Yuliang Sun, Chengguo Yin, Jun Zhang, Shudong Huang, Lei Xiao, Huan Gu, Irwin King, Haijie Gu, Jie Jiang
year: 2026
---

# The Tencent Advertising Algorithm Challenge 2025: All-Modality Generative Recommendation

腾讯广告算法大赛 2025 围绕"全模态生成式推荐"(All-Modality Generative Recommendation),发布了两个真实工业广告日志构建的大规模多模态数据集 TencentGR-1M / TencentGR-10M,并配套基线模型与加权评测协议,目标是填补工业广告场景下大规模、全模态、含点击与转化信号的 [[generative-recommendation]] 公共基准的空白。

## 问题

判别式推荐模型长期主导工业推荐,但近年来推荐系统正从判别式范式转向直接在用户行为序列上运行的 [[generative-recommendation]](GR)架构。GR 将检索/排序重构为在 item ID 或 semantic codes 上的序列生成问题。

尽管多模态推荐数据集有所进展,仍缺乏专为工业广告 GR 设计、同时提供大规模、真实、全模态(包含 collaborative ID、视觉与文本模态特征)的公共基准。现有大规模数据集(如新闻领域 MIND、短视频领域 [[kuairand]]/KuaiRec/Tenrec、WWW'25 短视频数据集)通常面向经典 [[ctr]] 或 [[sequential-recommendation]],不暴露 semantic ID、工业广告创意或以转化为中心(conversion-centric)的标签。

核心任务为多模态广告交互序列上的 next-item recommendation:给定用户的全模态历史交互序列,预测其下一个最可能交互(点击或转化)的广告。

## 方法

**数据构建**。两个数据集均来自去标识化(de-identified)的 [[tencent]] 广告日志,移除所有个人身份信息与原始创意,仅暴露 hashed ID 与由生产模型提取的 embedding 向量。

- **TencentGR-1M(初赛)**:约 100 万用户序列,每用户最多 100 个交互 item,每个交互带有曝光与点击信号。统计:1,001,845 用户、4,783,154 广告、平均序列长 91.06、660,000 候选广告;曝光 90.19%、点击 9.81%。
- **TencentGR-10M(复赛)**:规模扩大到 1000 万用户(10,139,575 用户、17,487,676 广告),并显式区分序列与目标层面的点击与转化事件,任务变为 next click-or-conversion prediction。转化既作为序列内事件、也作为预测目标类型出现;曝光 94.63%、点击 2.85%、转化 2.52%。

**特征**。每个 item token 包含 collaborative ID、categorical 属性(单值 S / 多值 M)、action/feedback 信号,以及由 6 个生产模型提取的多模态 embedding(Table 3):文本侧 Bert-finetune、Conan-embedding-v1、gte-Qwen2-7B-instruct;图像侧 hunyuan_mm_7B_finetune、QQMM-embed-v1、UniME-LLaVA-OneVision-7B。Bert/Hunyuan 用真实协同数据以对比学习损失微调。

**基线模型**。采用 next-token prediction 公式,causal [[transformer]] backbone + 基于 Faiss 的 ANN 检索([[approximate-nearest-neighbor-search]])。多字段特征融合:categorical/ID 各有 embedding table,多模态特征直接用连续 embedding,经 MLP 投影到 token embedding 空间;user-profile token 前置并加位置编码。训练目标为 [[contrastive-learning]] 的 InfoNCE loss,从全局 item 池均匀采样负样本;复赛对 InfoNCE 加 action-type 权重以强调转化事件。基线实现:1 个 transformer block、hidden dim d=32、1 个 attention head、序列截断/padding 到 101、Adam(lr=0.001)、单 GPU 训练。推理时 user embedding 与 item embedding 解耦,item embedding 可预计算缓存。

**赛制**。初赛(TencentGR-1M)按 HitRate@10 与 NDCG@10 加权排名,top 50 进复赛;复赛(TencentGR-10M)用加权指标(转化权重更高),代码审查与可复现性检查后 top 20 进现场决赛。比赛在 Tencent Angel 机器学习平台上执行,严禁 model ensembling。

## 结果

**评测协议**。

- 初赛:next-click prediction,仅点击视为相关。Score_prelim = 0.31 · HitRate@10 + 0.69 · NDCG@10。系数在内部基线池上标定,使两项贡献大致相当;经验对比 K=10 与 K=100 后选用 K=10(团队间区分度更高)。
- 复赛:引入 weighted HitRate@10 与 weighted NDCG@10,relevance weight w(i):曝光-only = 0,点击 = 1,转化 = α = 2.5。Score_final = 0.31 · w-HitRate@10 + 0.69 · w-NDCG@10。模型需隐式推断行为类型(点击 vs 转化),user→ground-truth 行为类型映射仅用于评测端。最终排名 = 决赛榜分(75%)+ 委员会评审分(25%,技术新颖性/清晰度/影响)。

**规模与奖励**。吸引超过 8,440 名注册参赛者,来自近 30 国;约 4,600 名活跃选手组成约 2,800 队。冠军奖金 2,000,000 RMB,二、三名分别 600,000 / 300,000 RMB,4-10 名各 100,000 RMB;Technical Innovation Award 200,000 RMB。

**Top 方案关键思路**。

- **冠军**:基于 dense [[qwen]] backbone 的多模态自回归 GR 模型;per-position action-conditioning(gated fusion + FiLM 层 + attention biasing)以解耦不同行为语义;工程化时间特征层次(绝对时间戳、相对间隔、session 结构),多频 Fourier 编码周期性;对长尾 item 用 RQ-KMeans 生成 semantic ID。
- **亚军**:encoder-decoder 架构,encoder 用多 gated MLP,辅以用户-item 交互图上的 graph neural networks,decoder 为改进 SASRec 式 Transformer(2048 hidden、8 层、8 head);SVD-based RQ-KMeans 构建 semantic ID;两阶段训练(曝光预训练 + 点击/转化微调)。
- **季军**:decoder-only Transformer,引入丰富时间信号与显式 action-type conditioning;系统研究生成式推荐的 [[scaling-law]],将每批负样本数扩展到 380K 并观察到显著提升,强调"规模驱动性能"。
- **Technical Innovation Award**:decoder-only 生成模型,统一建模"下一个感兴趣 item"与"用户对该 item 的 action",联合 semantic-ID 生成损失 + action 预测损失;引入专用 decoder-only transformer(InfoNCE)抽取协同 embedding 与 collision-resolution 机制。

## 在本 wiki 中的位置

本文是 [[generative-recommendation]] 与工业 [[recommender-systems]] 的交叉工作,提供了大规模 [[dataset]] / [[benchmark]] 资源。与同类推荐数据集 [[kuairand]]、[[recflow]]、[[merrec]]、[[microlens]] 互补,但聚焦广告场景、全模态特征与以转化为中心的标签。技术上结合 [[transformer]] backbone、[[sequential-recommendation]]、[[contrastive-learning]](InfoNCE)、[[approximate-nearest-neighbor-search]](Faiss)与 semantic ID 思路。可与 [[2024-large-recommendation-models-scaling]] 关于推荐模型 [[scaling-law]] 的讨论、以及 [[ctr]] / [[ndcg]] 评测体系参照阅读。出品方为 [[tencent]],合作机构 [[hkust]]。
