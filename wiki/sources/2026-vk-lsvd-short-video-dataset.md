---
type: source
subtype: paper
tags: [dataset, recommender-system, short-video, sequential-recommendation, cold-start, industrial-dataset]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2602.04567
raw: raw/2602.04567.pdf
authors: [Aleksandr Poslavsky, Alexander D'yakonov, Yuriy Dorn, Andrey Zimovnov]
year: 2026
---

# VK-LSVD: A Large-Scale Industrial Dataset for Short-Video Recommendation

VK-LSVD 是迄今规模最大的公开短视频推荐工业数据集,来自俄罗斯社交平台 VK,包含超过 400 亿次交互、1000 万用户、近 2000 万视频,跨越 6 个月。

## 问题

短视频推荐有独特挑战:用户兴趣快速漂移、主要依赖 implicit feedback(如 watch time),且需结合多模态内容建模复杂、快速演化的用户行为。但研究进展受限于缺乏能真实反映工业平台动态的大规模公开数据集。现有公开数据集普遍在规模、时间覆盖或反馈多样性上受限(见论文 Table 1),且高度集中于 Kuaishou 平台(如 [[kuairand]]、[[kuairec]]、KuaiSAR、MicroLens 等),阻碍学术成果向工业场景迁移,也缺乏平台多样性。

## 方法

VK-LSVD 从 VK 短视频服务的匿名交互日志构建,作为一个 [[dataset]],由四个核心组件组成:

- **Interaction Records**(`interactions/`):每周一个 Parquet 文件,超过 400 亿次曝光事件,按时间排序。采用 **Global Temporal Split (GTS)** 全局时间切分:train 为前 25 周,validation 1 周,test 1 周,为连续时间段。watch time 为累计值(可超过视频时长,因重看),均被截断(timespent 上限 255s)。
- **User Metadata**:1000 万用户的静态人口学/行为特征(age 18-70、gender、geo 共 80 个唯一值),支持按活跃度采样。
- **Item Metadata**:2000 万视频的 author ID 与时长(duration),支持按热度采样。
- **Embeddings**(`item_embeddings.npz`):每个 item 的 64 维 content-based embedding,由本地模型生成后经 truncated SVD 压缩,分量按重要性排序以支持灵活降维。

反馈信号丰富,涵盖 implicit(watch time)、explicit(like、dislike)、viral(share)、deeper engagement(comment opens、bookmark、click on author),并附带 consumption context(feed/search)、platform(Android/Web)、agent 等 contextual metadata。出于隐私考虑,**不包含任何原始视频、音频或文本内容**,所有 ID 均不可逆匿名化,采用 [[apache license 2.0]],发布于 Hugging Face Hub。还提供 pre-configured subsets(如 1% 随机用户 ur0.01、1% 热门 item ip0.01)以降低算力门槛。

论文在 ur0.01_ir0.01 子集上对若干简单推荐方法做基准测试:Random、Global Popularity、Conversion-based(优化 CTR)、[[iALS]](将 watch time > 10s 作为正信号)。并做了基于 iALS 表征的 pairwise similarity 分析(余弦相似度,按人口学/内容特征分组)。

## 结果

核心统计(论文 Table 3):用户数 10,000,000;item 数 19,627,601;交互数 40,774,024,903;总观看时长约 8.58×10^11 秒;数据集密度 0.0208%。反馈量:likes 约 11.7 亿、dislikes 约 1186 万、shares 约 2.63 亿、bookmarks 约 4012 万、clicks on author 约 8463 万、comment opens 约 4.81 亿。

简单算法基准(论文 Table 4,Global Temporal Split):
- Coverage:Random 0.96449、Popular 0.00010、Conversion 0.00010、iALS 0.00501。
- ROC AUC:Random 0.50003、Popular 0.57383、Conversion 0.60341、iALS 0.58126。
- NDCG@20:Random 0.00006、Popular 0.00244、Conversion 0.00000、iALS 0.02623。
(Random Split 下各指标普遍更高,如 Conversion ROC AUC 达 0.68107,iALS NDCG@20 达 0.06554,表明时间切分更具挑战性。)

相似度分析(论文 Figure 2):人口学因素(gender、age)强烈影响用户相似度;author 是 item 相似度的主导因素(0.58);共享全部 metadata 的 item 对相似度达 0.66,印证数据集捕获了丰富的内容关系。用户活跃度与 item 热度均呈典型的重尾 power-law 分布。

数据集已作为 **VK RecSys Challenge 2025** 的核心数据集,有近 800 名参赛者,任务为非常规的"为新冷启动视频排序用户"(而非为用户排序 item),每用户最多 100 条推荐,以 NDCG@100 评估,结果预计 2026 年 1 月公布。

## 在本 wiki 中的位置

本文是一个 [[recommender-system]] 领域的工业级 [[dataset]] 资源,可用于 [[sequential-recommendation]]、[[cold-start]]、context-aware 与 hybrid 推荐研究。它与同类短视频推荐数据集 [[kuairand]]、[[kuairec]]、[[microlens]]、[[recflow]]、[[tenrec]]、[[movielens]] 形成对比,主要补足了平台多样性(来自 Kuaishou 之外的 VK 生态)与规模(400 亿交互)。其基准方法 [[iALS]] 与 [[ndcg]] 评估指标是推荐系统研究的标准工具。
