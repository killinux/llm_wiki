---
type: source
subtype: paper
tags: [recommender-system, cross-domain-recommendation, llm-for-recommendation, sequential-recommendation, multi-scenario-recommendation, two-tower, multimodal, industrial-deployment]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.14788
raw: raw/2510.14788.pdf
authors: Manjie Xu, Xin Jia, Cheng Chen, Jingyi Zhou, Chi Zhang, Yongji Wu, Zejian Wang, Kai Zuo, Yibo Chen, Xu Tang, Yao Hu, Yixin Zhu
year: 2025
---

# Cross-Scenario Unified Modeling of User Interests at Billion Scale (RED-Rec)

一句话:提出 RED-Rec,一个 LLM 增强的分层两塔序列推荐框架,通过把用户在首页 feed、搜索、广告等异构场景下的行为统一建模,在十亿级工业 UGC 平台(小红书)上实现跨场景用户兴趣表征与服务。

## 问题

UGC 平台(如小红书)的用户兴趣本质上是多维的,跨越 search、feed browsing、内容发现、广告等多个异构场景。传统推荐系统在**孤立场景**内独立优化各自业务指标([[ctr]]、广告价值 ADVV 等),这种割裂设计带来三个核心问题:

- **割裂的用户理解**:每个模型只看到狭窄的行为上下文,无法做整体兴趣建模;
- **不一致的用户体验**:独立系统从同一用户身上推断出相互矛盾的偏好;
- **跨场景信号利用不足**:无法跨任务迁移知识,对某些场景活跃度稀疏的用户(如有上千次 feed 交互但只有几十次搜索)表现尤其差。

同时,在十亿级部署中引入 [[large-language-models]] 这类先进技术也受限于:动作 schema 异构、时序动力学复杂、场景间严重的活动量不均衡、亚毫秒级延迟与吞吐约束、以及在单一架构内调和不同优化目标的难度。真正端到端的工业级统一建模仍是空白。

## 方法

RED-Rec(Recommender Engine for Diversified scenarios)采用**分层两塔架构**,聚焦三个主要场景 S = {homefeed, advertisements, search},统一学习用户与 item 表征。核心组件:

- **多模态 Item 表征**:每个 item 经多模态编码器处理文本(title/tags/description/OCR,用预训练 LLM 编码)与视觉内容(用 [[vit]] / CLIP ViT-B/16 编码),投影到共享 d 维空间。Item LLM 编码器以特殊 token 抽取稠密语义嵌入(LLaMA2-1.3B 隐层维 1536,Qwen-7B 为 3584)。
- **跨场景序列建模**:把同一用户在三个场景的交互序列合并 S_u = S^h ∪ S^a ∪ S^s,每个事件融合 Content(item 嵌入)、Actions(like/share/comment/follow/messaging/block 等正负反馈的稠密嵌入)、Temporal(小时级时间戳 OneHot)三维信息。
- **2D Dense Mixing Policy(二维稠密混合策略)**:为解决场景间行为不均衡,沿**时序轴与场景轴**两个维度做平衡采样与混合,对每个场景做配额平衡([n_h]/[n_a]/[n_s]),并用 2D 位置编码(序列位置 PE_seq + 时间间隔 PE_gap)编码每个事件。
- **场景感知多兴趣查询(Scenario-Aware Interest Querying)**:用 K 个可学习 query 嵌入 Q 关注不同兴趣侧面,生成多个 scenario-aware 用户表征,表达细粒度、上下文特定的偏好。
- **训练目标**:用带温度缩放的 Noise Contrastive Estimation(NCE / [[contrastive-learning]])优化,并结合 window-based 对比损失捕捉演化偏好;用余弦相似度聚类 + 匈牙利算法匹配把目标 item 分配给对应兴趣向量,实现多兴趣解耦([[disentangled-representation-learning]],思路与 HyMiRec 一致)。
- 还探索了 CoT([[chain-of-thought]])辅助损失,让用户模型为每个动作生成自然语言 rationale 以做可解释跨场景推荐(用 GPT-4.1 生成 CoT 数据),但因大规模成本高仅做小规模验证,且未超过预训练模型。

骨干用 1.3B Chinese-LLaMA 或 1.5B [[qwen]]2.5,视觉用 CLIP ViT-B/16,在 8 张 [[nvidia]] H100 上训练。

## 结果

为严谨评测,提出新数据集 **RED-MMU(RedNote's Multi-Scenario Multimodal User Behaviors)**,源自小红书匿名化行为日志,覆盖 feed/search/广告三场景。其规模(训练侧):约 **1.0m 用户、300.6m items、683.2m actions**,content 含 text/image/video,远超 Amazon、JD Search、KuaiSAR([[kuairand]] 系)、Qilin 等公开数据集。评测用 1m 用户训练 + 10000 测试样本,候选池约 1m notes,默认窗口 W=10、序列长度 last_n=128、每场景 3 个 query。指标为 HR@K、[[ndcg]]@K、MRR(K∈{10,50,100,1000})。

- **单场景**(Table 1):RED-Rec 在 homefeed 与 advertisements 上一致超过 [[sasrec]]、MoRec、HSTU、HLLM、DLRM-v3 等强基线;预训练版 RED-Rec-mm-pt 在广告 HR/NDCG@1k 达 42.56/4.98、MRR 2.21,在冷启场景(语义理解关键)优势尤其明显。
- **跨场景**(Table 2):利用跨场景信号显著提升。如 Search+Homefeed 场景下 RED-Rec-pt 在 homefeed 上 HR/NDCG@10 达 2.92/1.33;Homefeed+Search+Advertisements 场景下广告 HR/NDCG@1k 达 49.17/5.93、MRR 2.41。两个最显著增益:搜索数据增强首页推荐、首页+搜索信号增强广告。
- **消融**(Table 3):更长序列(SeqLen=128 vs 32)、多兴趣 vs 单兴趣、大规模预训练均带来提升;2D-Mixing 优于 Sorted by Timestamp / Naive Combination / 1D 等混合方式。
- **Scaling**:在 LLaMA(0.5B-7B)与 Qwen(0.5B-7B)上,HR 随参数量增大持续提升至 7B,但大模型显著降低 serving 吞吐;**1.5B Qwen-2.5** 是性能与效率的最优平衡。
- **在线 A/B**(小红书广告召回阶段,10% vs 10% 流量,约 1.1b item 全量目录):总 **ADVV +0.8864%**、整体 Feed Ad Spend(Cost)+0.3401%,且 **90%+** 被选 item 是该召回路独有的增量。已全平台部署,服务约 **160m** 日活用户。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 中的 [[cross-domain-recommendation]] / [[multi-scenario-recommendation]] 方向,并把 [[llm-for-recommendation]] 推进到十亿级工业部署。

- 架构上是 [[two-tower]] + [[sequential-recommendation]],与 [[sasrec]]、[[bert4rec]]、HSTU、HLLM 等同源但用 LLM 骨干增强语义,可与 [[tallrec]]、[[llara]]、[[p5]] 等 LLM4Rec 工作对照;
- 多模态 item 编码用 [[vit]] / [[clip]],延续 MLLM4Rec 一类思路;
- 用 [[contrastive-learning]](NCE)+ [[disentangled-representation-learning]] 做多兴趣建模,与多兴趣推荐线相承;
- 数据集 RED-MMU 可与 [[kuairand]]、[[microlens]]、[[amazon-reviews]] 等推荐数据集并列参考;
- 出自 [[peking-university]]、[[fudan-university]] 与小红书(Xiaohongshu / RedNote)合作,属工业级 [[recommender-systems|recommender-system]] 部署案例。
