---
type: source
subtype: paper
tags: [recommender-system, large-language-models, feature-engineering, short-video, ctr-prediction]
created: 2026-05-29
updated: 2026-05-29
arxiv: ""
raw: raw/10.69987_aimlr.2024.50111.pdf
authors: [Tianxing Tang, Mingzhuo Yu]
year: 2024
---

# A Comparative Evaluation of LLM-Generated Semantic Tags versus Classical Text Features (TF-IDF, LDA, BERT Embeddings) for User-Interest Enrichment in Short-Video Recommendation

一项受控对照实验，在同一套短视频公开基准上，把 LLM 生成的语义标签与三类经典文本特征（TF-IDF、LDA、BERT 句向量）放在统一协议下，沿"特征质量、下游精度、成本"四个轴做正面比较，回答"用 LLM 标签做用户兴趣特征是否值得它的代价"。

## 问题

短视频[[recommender-system]]靠从稀疏交互历史中推断用户兴趣来驱动 CTR/CVR 预估，而附在每个视频上的文本元数据（标题、字幕、类别）是注入语义的主要手段。但视频文本嘈杂（口号、缩写、emoji 混杂），把它蒸馏成数值特征的方式直接影响排序精度、冷启动覆盖与服务成本。

候选的四类文本特征——稀疏加权关键词、潜在主题、上下文嵌入、LLM 生成标签——通常只在单一系统或消融实验里被局部比较，缺乏在公开基准上、匹配协议下的正面对决。近期工作主张 instruction-tuned 解码器能产出比用户生成文本更干净、更可迁移的语义单元，但这类信号的成本以及相对强经典基线的边际价值在公开数据上基本没被量化。本文提出一个范围明确的实证问题：在固定下游架构、相同原始文本的前提下，哪一类文本特征在"兴趣表示质量 vs 计算成本"上权衡最优。

## 方法

- **四类特征家族**：TF-IDF（对数词权重 + 用户侧按 engagement 加权聚合，凸组合 0.4/0.4/0.2 对应 click/watch-completion/like）；[[large-language-models]] 主题分布 LDA（K∈{50,100,200}，按困惑度选最优 K）；BERT 句向量（sentence-transformers all-MiniLM-L6-v2，384 维）；LLM 标签（用 Llama-3-8B-Instruct，temperature 0.3、top-p 0.9，提示生成 5–10 个短语标签，并加约束避免幻觉出 caption 之外的实体，标签再喂回同一 TF-IDF 管线以隔离聚合层差异）。Word2Vec 也评估过但全轴被上下文嵌入压制，故主表只留上下文变体。
- **四个评估轴**：特征可分性（silhouette 系数、k-NN 标签纯度@10）；与点击标签的互信息（k-NN 估计）；五个 backbone 上的下游精度（[[sequential-recommendation]] 的 [[sasrec]]、BERT4Rec，以及 CTR/CVR 的 DIN、DIEN、SIM）；离线特征生产成本（GPU-hours、存储），并结合在线服务延迟做 Pareto 前沿分析。
- **数据集**：[[kuairand]]-Pure（27,285 用户 / 7,551 视频 / 1,436,609 次曝光交互）、MicroLens-100K、[[kuairec]] 为主，MIND-small 作为跨域探针。

## 结果

- **特征可分性**：LLM 标签在四个数据集 silhouette 均最高，跨集均值 0.21，对比 BERT 0.17、LDA 0.12、TF-IDF 0.09；KuaiRand-Pure 上 k-NN 纯度@10 达 0.68（BERT 0.63）。LLM 与 BERT 的差距明显小于 BERT 与 TF-IDF 的差距，体现"有了稠密语义后收益递减"。
- **互信息**：LLM 标签在四个数据集中有三个领先；KuaiRand-Pure 上 LLM 标签与 TF-IDF 的互信息差是 BERT 与 TF-IDF 差的两倍以上。
- **下游精度（KuaiRand-Pure CTR AUC）**：LLM 标签使 DIN 0.738→0.751（较 TF-IDF +0.013，较 BERT +0.005）、DIEN 0.744→0.760、SIM 0.751→0.765；三个 backbone 较 TF-IDF 的 AUC 增益区间 0.009–0.016。CVR 因标签稀疏增益被压缩（DIN +0.009）。
- **序列任务（MicroLens-100K）**：SASRec HR@10 从 0.164（TF-IDF）升到 0.198（LLM 标签），即 +3.4 个点；BERT4Rec 增益约 +2.1 个点。跨四数据集（DIN）LLM 对 BERT 的增益从 MicroLens-100K 的 +0.006 收窄到文本更干净的 MIND-small 的 +0.002。
- **成本与 Pareto 权衡**：在 KuaiRand-Pure（7,551 视频）上，TF-IDF 拟合 3.1 CPU-分钟、LDA 47.2 CPU-分钟、BERT 编码 0.24 GPU-小时，而 Llama-3-8B 标签生成耗 9.4 GPU-小时（约为 BERT 的 40 倍；MicroLens-100K 线性放大到 22.7 GPU-小时）。但因 LLM 标签塌缩成平均仅约 7 个非零项的稀疏整数集，其在线存储/检索成本反而低于 BERT 的 384 维稠密向量，故在"精度-在线成本"平面上 Pareto 支配 LDA 与 BERT。
- **结论**：四类特征质量稳定排序为 LLM 标签 > BERT > LDA > TF-IDF，但绝对差距温和；LLM 改写在文本短、噪、歧义时价值最大。三条工程建议：目录稳定且有离线 LLM 预算 → 选 LLM 标签；目录churn剧烈或离线算力受限 → 稠密 BERT 更划算；完全无 GPU → 加权 TF-IDF 仅损约 1 个 AUC 点却省三个数量级算力，仍可能 [[pareto]] 最优。

## 在本 wiki 中的位置

本文把 [[large-language-models]] 用作[[recommender-system]]的**特征增强语义层**（而非端到端预测器），与本 wiki 中 LLM-for-recommendation、[[sequential-recommendation]] 及 [[kuairand]]/[[kuairec]] 数据集相关条目互为补充。其核心贡献是统一评估协议与"LLM 标签何时值得其成本"的成本-收益判断，提供了一个把生成式语义信号与经典文本特征做正面对比的入口。
