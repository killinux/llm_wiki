---
type: source
subtype: paper
tags: [recommender-system, dataset, micro-video, multimodal-recommendation, benchmark, sequential-recommendation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2309.15379
raw: raw/2309.15379.pdf
authors: [Yongxin Ni, Yu Cheng, Xiangyan Liu, Junchen Fu, Youhua Li, Xiangnan He, Yongfeng Zhang, Fajie Yuan]
year: 2023
---

# A Content-Driven Micro-Video Recommendation Dataset at Scale (MicroLens)

来自 Westlake University 等机构的工作,提出 **MicroLens**:一个规模达 10 亿(one billion)用户-物品交互、3400 万用户、100 万微视频的内容驱动微视频推荐数据集,且首次公开提供原始视频内容(标题、封面图、音频、完整视频),用于研究直接从原始内容学习的推荐。

## 问题

微视频(short-form video)推荐对娱乐、广告、电商意义重大,但缺乏**大规模公开微视频数据集**严重制约了 [[recommender-system]] 的研究。现有视频推荐数据集存在两类局限:

- [[movielens]] 等主要面向较长的电影类视频,内容类别窄,且数据来自模拟评分网站,不能真实反映观看行为。
- [[kuairec]]、Tenrec、KuaiRand 等只提供 video ID 或从缩略图预提取的视觉特征,无法支持模型**直接从原始视频内容**学习物品表征。

因此急需一个提供多样化原始内容、大规模的微视频推荐数据集。

## 方法

- **数据构建管线(5 步)**:Seed Video Collection → Dataset Expansion → Data Filtering → Interaction Collection → Data Integration。数据采自一个以社交娱乐为主的微视频平台,采集跨越约一年(2022.06–2023.06)。由于平台出于隐私保护不提供 like/click 交互,作者用**公开的评论行为(comment)**作为强偏好的隐式信号(平均每 100 个 like 约 1 条评论)。
- **多模态原始内容**:每个微视频附带 title、cover image、audio、full-length video 四种原始模态(VAIT),并含 view/like 数、用户性别、评论内容等附加特征。
- **隐私与版权**:用户与物品 ID 均匿名化;为规避版权,提供视频 URL 与下载工具而非直接分发视频(类似 YouTube8M / ImageNet 做法)。
- **基线与协议**:对比三类推荐范式——
  - **IDRec**:纯 ID,含 CF 模型(DSSM、LightGCN、DeepFM、NFM)与 [[sequential-recommendation]] 模型(GRU4Rec、NextItNet、[[sasrec]])。
  - **VIDRec**:在 ID embedding 中融合冻结视频编码器(frozen encoder)预提取的视频特征作为 side information。
  - **VideoRec**:作者提出的新基线,用**可学习视频编码器**端到端(E2E)替代 item ID,联合优化推荐模型与视频编码器(计算昂贵但精度最高)。
- 视频编码器涵盖 R3D、X3D、C2D、I3D、Slow/SlowFast、CSN、VideoMAE 等;训练用 in-batch softmax loss,评测用 leave-one-out 切分,指标为 HR@N 与 NDCG@N(N=10/20)。

## 结果

- **数据规模**:完整 MicroLens 含 34,492,051 用户、1,142,528 物品、1,006,528,709 次交互(sparsity 99.997%)。提供两个子集:MicroLens-100K(100K 用户 / 19,738 物品 / 719,405 交互 / sparsity 99.96%)与 MicroLens-1M(1M 用户 / 91,402 物品 / 9,095,620 交互 / sparsity 99.99%)。三者分别含 15,580、28,383、258,367 个 tags;平均视频时长约 138–162 秒。
- **基准结论(MicroLens-100K,Table 2)**:
  - 序列模型(SASRec、NextItNet、GRU4Rec)全面优于非序列 CF 模型(DSSM、LightGCN、DeepFM、NFM、YouTube);其中 [[sasrec]] 最佳,较 NextItNet / GRU4Rec 提升超 10%(如 SASRec HR@10=0.0909 vs NextItNet 0.0805)。
  - **E2E 的 VideoRec 精度最高**:SASRec_V(VideoRec)HR@10=0.0948、NDCG@10=0.0515,优于对应的 ID-only 与 frozen-encoder 版本,显示直接学习原始视频内容的潜力。
  - 但 VideoRec 训练成本极高(比 IDRec 多 10–50 倍计算)。
- **核心洞见**:当前视频理解技术与视频推荐之间存在显著 gap,需要面向推荐任务的专门视频理解研究。

## 在本 wiki 中的位置

这是 [[recommender-system]] 主题下的**大规模多模态数据集 / benchmark**资源,定位与 [[movielens]]、[[kuairec]]、[[amazon-reviews]] 等推荐数据集同类,但首创提供原始视频内容、支持端到端内容驱动推荐。它与 [[sequential-recommendation]] 方法(尤其 [[sasrec]])直接相关,可作为评测序列与多模态推荐模型的测试床,衔接 recommender system 与视频理解两个社区。
