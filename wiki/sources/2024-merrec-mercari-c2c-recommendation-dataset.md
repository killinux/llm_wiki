---
type: source
subtype: paper
tags: [recommender-system, dataset, c2c, e-commerce, ctr-prediction, sequential-recommendation, multi-task-learning, benchmark]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2402.14230
raw: raw/2402.14230.pdf
authors: [Lichi Li, Zainul Abi Din, Zhen Tan, Sam London, Tianlong Chen, Ajay Daptardar]
year: 2024
---

# MerRec: A Large-scale Multipurpose Mercari Dataset for Consumer-to-Consumer Recommendation Systems

提出 **MerRec**:首个面向 **C2C(Consumer-to-Consumer,个人对个人)电商**的大规模推荐数据集,来自 Mercari 平台,覆盖 2023 年半年内数百万用户与商品,并配套四类推荐任务基准与一个原型模型 Mercatran。

## 问题

学术界的推荐系统研究长期聚焦 **B2C(Business-to-Consumer)**模型,依赖 [[amazon-reviews]]、Netflix Prize、[[movielens]] 等成熟数据集。但 **C2C 电商**(如 eBay、Etsy、Mercari)正快速兴起,其特性与 B2C 截然不同:用户同时身兼买家与卖家(dual roles);商品描述由非专业卖家自填,质量参差、缺乏标准化;每个商品是**单件库存**,售出即不可复购;缺少 SKU 等标准商品标识符;商品上架/更新/下架高度动态。现有 C2C 数据集稀少且在商品属性、用户多样性、规模上严重不足,造成产业与学术之间的鸿沟。

## 方法

- **数据来源与规模**:从 Mercari 采集 2023 年连续 6 个月的买家侧交互。统计:**5,569,367 个用户**、**83,078,407 个商品(item)**、**1,274,814,848 条交互事件**、**227,167,616 个 session**、**69,144,727 个 sequence**;商品标题文本约 **82 亿 token**;类目为 3 级树状结构(c0=17 / c1=309 / c2=3073)。
- **特征丰富度**:除 user_id / item_id / session_id 外,含带时间戳的动作类型(6 种交互类型)、3 级类目、品牌(20,001 个 brand_id)、价格、成色(Good/New/Like new/Fair/Poor)、尺寸、颜色、运费承担方等。
- **SKU 替代方案**:针对 C2C 无 SKU 的难题,合成 **product_id = brand_id + 最细类目 c2_id**(约 140 万个),作为研究商品聚合的代理(论文也指出其粒度局限,见 iPhone 各代价格差异示例)。
- **数据清洗**:封号用户/违规商品过滤、长序列分段、连续重复动作去重、隐私保护(剔除特定地区、ID 假名化、时间戳统一为 UTC)。
- **四类任务基准**:① CTR 点击率预测;② **SBR / 序列推荐**([[sequential-recommendation]]);③ **多任务学习推荐(MLR)**([[multi-task-learning]]);④ 推理加速(IAR)。
- **原型模型 Mercatran**:受 YouTube 双塔(Two-Tower)启发,提出 **三塔(Three-Tower)Transformer** 架构(两个用户塔 + 一个物品塔),用内容特征而非物品 ID 编码,输出可直接做向量检索的 embedding,以适配动态、无 SKU、单件库存的 C2C 场景;支持由最多 22 步历史预测未来 4 步交互。

## 结果

- **规模对比(Table 2)**:相较其他公开电商数据集,MerRec 商品数 **+72%**(vs [[amazon-reviews]])、交互数 **+122%**(vs Amazon)、交互类型数 **+50%**(vs DIGINETICA)、类目数 **+103.6%**(vs [[retailrocket]])、session 数 **+2358%**(vs YOOCHOOSE),且时效性最新、生产流程最透明。它与 Retailrocket 是该列表中仅有的"时间快照式(back-in-time snapshot)"数据集。
- **CTR 任务(Table 3)**:在第 1 个月数据(30,221,983 商品 / 2,767,956 用户 / 9,809,155 序列)上测试。经典 **AFM 取得最高 AUC=0.703**,领先更新的 [[deepfm]](0.642)、DCNv2(0.6209)、xDeepFM(0.6066)、W&D(0.6626)等;带 cross network 的模型在 MerRec 上反而更难调优。
- **SBR 任务(Table 4)**:[[sasrec]]、GRU4Rec、NextItNet、Bert4Rec 四基线中,**NextItNet 最佳**(NDCG@5=0.257、Recall@20=0.490);双向 Bert4Rec 表现最差;GRU4Rec 全面优于 SASRec(与 TenRec 上的观察相反,凸显多 benchmark 评测的必要性)。
- **Mercatran**:相对双塔基线,Mercatran V2(三塔 4 步)在多步推荐多样性等指标上较 V1 有显著提升(论文报告 +124.4% / +92.1% 等相对增益)。
- **MLR 任务**:[[esmm]] 与 [[mmoe]] 等多任务模型表现接近;仅用商品标题训练的模型可超过使用更多特征的模型。
- 代码: github.com/mercari/mercari-ml-merrec-pub-us;数据: huggingface.co/datasets/mercari-us/merrec。

## 在本 wiki 中的位置

本文是 [[recommender-systems|recommender-system]] 方向的**数据集 / benchmark 类**工作,填补 C2C 推荐数据空白,可与 [[movielens]]、[[amazon-reviews]]、[[retailrocket]]、[[kuairand]]、[[rl4rs]] 等本 wiki 已收录的推荐数据集/基准并列比较。其任务覆盖 CTR、[[sequential-recommendation]]、[[multi-task-learning]],基线涉及 [[deepfm]]、[[sasrec]]、[[esmm]]、[[mmoe]] 等经典推荐模型,适合作为研究 cold-start、动态物品空间、无 SKU 标识下推荐的实验平台。
