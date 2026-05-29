---
type: source
subtype: paper
tags: [recommender-system, cold-start, prompt-tuning, recsys-2024, kuaishou]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2412.18082
raw: raw/2412.18082.pdf
authors: [Yuezihan Jiang, Gaode Chen, Wenhan Zhang, Jingchi Wang, Yinjie Jiang, Qi Zhang, Jingjian Lin, Peng Jiang, Kaigui Bian]
year: 2024
---

# Prompt Tuning for Item Cold-start Recommendation (PROMO)

PROMO 是一种面向 item cold-start 推荐的 [[prompt-tuning]] 方法,它用高价值正反馈("pinnacle feedback")替代内容描述作为 prompt 信息,并为每个 item 构造 item-wise 个性化 prompt network,从而同时缓解数据侧的标注成本/语义鸿沟与模型侧的热门偏置(warm-start 主导)问题,已在快手十亿用户级短视频平台上线。

## 问题

item cold-start 问题(新 item 无/少交互记录,如 click、rating)决定了一个 item 能否成功转化为热门 item,是在线 [[recommender-systems|recommender-system]] 的关键环节。已有把 [[prompt-tuning]] 引入 [[cold-start]] 推荐的工作存在两类缺陷:

- **数据侧成本与鸿沟**:现有方法多依赖额外的人工标注(如候选 item 的文本描述)作为 prompt,在面对数百万/数十亿新 item 的工业场景中成本极高;且内容特征与推荐任务之间存在语义 gap,缺乏与推荐过程的端到端衔接。论文用实验(Figure 1)验证:用 positive feedback 作为 prompt 比用 content feature 在 cold-start item 上准确率显著更高(如 25 个输入时 0.62 vs 0.42)。
- **模型侧偏置**:cold-start item 仅占在线流量的一小部分,共享模型参数主要被热门 item 优化,导致模型给 warm-start item 高分、cold-start item 低分。Figure 2 显示在 KuaiRand 上,cold-start 正样本与 warm-start 负样本的预测分布严重重叠,模型对 cold-start item 个性化不足、倾向给热门 item 打高分。

## 方法

PROMO 在固定的两塔 base model(backbone 沿用 [[sasrec]],可替换为其他表示学习方法)之上工作,核心由三部分组成:

- **Prompt Generator / Prompt Data(pinnacle feedback)**:把对某 item 提供"卓越正反馈"的用户(如正向评论、转发)视为 pinnacle feedback,作为 prompt 信息。对 item i,用打分公式 v_{u,i} = α·CR_{u,i} + β·IR_{u,i}(CR 为页面停留时间,IR 为综合交互分如点赞、关注作者)选 top-k 用户构成正反馈列表 Pos_i;并随机选 k 个负反馈用户构成 Neg_i。对缺乏反馈的 item,借助 [[collaborative-filtering]] 思想,用 base model 编码的 item embedding 计算与热门 item 的相似度,生成 pseudo-pinnacle feedback。
- **个性化 Prompt Network**:用 prompt generator 为每个 cold-start item i 生成 l 套独立 embedding,reshape/split 成该 item 专属 prompt network 的权重 W 和 bias b。这样每个 item 只更新自己的 item-wise prompt network 参数,避免热门 item 主导模型更新,缓解 model bias,且 prompt network 独立于 base model、只编码 prompt 信息。该模块参数高效:在 MovieLens100K/1M/KuaiRand/TMall 上待更新参数仅为 fine-tuning 的 20.1%/27.6%/17.7%/25.6%。
- **两类 prompt-enhanced loss**:(1) **Per-sample Pinnacle Feedback Prompt-enhanced Loss** L_pfpe,借鉴 contrastive learning,用 L1 距离拉大每个 pinnacle 正反馈与负反馈表示的 gap(配合 log(1+exp(-Δ)) 实现),为 point-wise 训练的 base model 补充 pair-wise 排序信息;(2) **Intra-batch Popularity-aware Prompt-enhanced Loss** L_pape,在 batch 内计算 cold-start 正样本与热门 item 负样本之间的距离并推大,实现公平打分、纠正热门偏置。

优化时把 pretrained 表示与 PROMO 表示拼接得到最终 embedding,以内积估计 ŷ_{u,i},总损失 L = λ1·L_pfpe + λ2·L_pape + L_rec。base model 全程 frozen,沿用 prompt learning 范式,参数高效且避免 catastrophic forgetting。

## 结果

- **数据集**:MovieLens 100K / MovieLens 1M / KuaiRand-Pure / TMall,按正反馈频次把 item 分为 popular 与 cold-start(cold-start:popular ≈ 8:2,近似长尾定义),采用 leave-one-out 切分。
- **指标**:Hitrate@K 与 NDCG@K(K=5,10),每个测试正样本配 100 个随机负样本。
- **整体性能(Table 2)**:PROMO 在四个数据集所有指标上一致超越所有 baseline(Pre-train、Fine-tune、CDN、DCN、DeepFM、SASRec、DSSM、DropoutNet、CB2CF、MetaEmb,以及 prompt 类 PPR、PLATE)。例如 MovieLens 100K 上,相对 SASRec 在 H@5/H@10/N@5/N@10 分别提升约 16.3% / 13.1% / 14.7% / 13.7%;相对 CB2CF 与 MetaEmb 在 MovieLens 1M HitRate@5 上分别提升约 37.8% 与 27.2%。KuaiRand 上 PROMO 取得 H@5 88.7 / H@10 92.6 / N@5 80.3 / N@10 81.6。
- **消融**:用 item-ID(PROMO-I)、item feature(PROMO-F)或两者(PROMO-IF)替换 pinnacle feedback 均弱于完整 PROMO(Table 3),说明 pinnacle feedback 更契合用户兴趣;把个性化 prompt network 换成共享 MLP(PROMO-M)或直接拿正反馈做输入特征(PROMO-T)也都更差(Table 4),其中 PROMO-IF 在 MovieLens 100K 上仍落后完整版 H@10/N@10 各约 10.6%/11.9%。
- **可解释性**:t-SNE 可视化(Figure 4)显示 PROMO 产出的 item 表示比 DSSM 更能把同类 item 聚到一起,prompt embedding 富含与下游任务对齐的信息。
- **工业部署**:PROMO 已成功部署于快手十亿用户级商业短视频应用,在 cold-start 场景多项商业指标上取得显著收益。

## 在本 wiki 中的位置

本文属于 [[llm-for-recommendation]] 与 [[recommender-systems|recommender-system]] 中 [[cold-start]] 推荐方向,把 NLP 中的 [[prompt-tuning]] / [[prompt-engineering]] 思想迁移到推荐:用 pinnacle feedback 替代 content feature 作 prompt,用 item-wise 个性化 prompt network + 两类 prompt-enhanced loss 同时治理冷启动的数据成本与热门偏置。backbone 复用序列推荐模型 [[sasrec]],并与 [[collaborative-filtering]]、[[deepfm]] 等经典方法及 prompt 类推荐方法对比。作者来自 [[kuaishou]] 与北京大学。
