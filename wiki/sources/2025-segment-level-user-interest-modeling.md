---
type: source
subtype: paper
tags: [recommender-system, short-video, user-modeling, segment-level-interest, multi-modal, video-recommendation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2504.04237
raw: raw/2504.04237.pdf
authors: [Zhiyu He, Zhixin Ling, Jiayu Li, Zhiqiang Guo, Weizhi Ma, Xinchen Luo, Min Zhang, Guorui Zhou]
year: 2025
---

# Short Video Segment-level User Dynamic Interests Modeling in Personalized Recommendation

把短视频拆成时间片段(segment),用混合表示 + 多模态用户-视频编码器 + 片段兴趣解码器,建模用户在浏览过程中沿时间线动态演变的片段级兴趣,用于 video-skip 预测与视频推荐。

## 问题

现有短视频推荐普遍把整支视频当作一个整体来建模,为其分配单一的偏好分数,忽视了用户偏好在视频浏览过程中**沿时间线动态演变**的本质。短视频节奏快、场景切换频繁,不同片段会吸引不同用户;用户的注意力和兴趣在不同 segment 间漂移,常体现为"滑走/跳过下一个视频"等行为。

把视频整体化处理从根本上限制了 [[recommender-system]] 的精度。建模片段级(segment-level)兴趣面临三大挑战:
1. 用户兴趣沿视频时间线演变,受独立于视频内容的人类注意力模式影响;
2. 片段级用户反馈通常是隐式且稀疏的(如滑动行为),缺乏显式标签,存在 missing segment-level label 问题;
3. 多模态融合挑战:结合用户-物品交互信号与内容信息时如何互补。

## 方法

作者提出一个 modality-agnostic(模态无关)的片段兴趣模型,含三大组件:

- **Hybrid User & Video Representation(混合表示)**:用两类模态表示用户与目标视频——visual modality(用预训练 [[clip]] ViT-L/14-336 作为 Vision Encoder 抽特征)与 ID modality(ID embedding 实现个性化)。引入 segment position(1..N)嵌入以区分同一视频内不同片段,缓解 challenge 1 的位置偏置。
- **Multi-modal User-video Encoder(多模态编码器)**:核心是 Modal-aware Interest Detection,基于 **User-Video Cross-Attention**(区别于把 user/item 放进同一序列的标准 transformer,显式建模用户与视频间的句法/语义结构),逐模态输出 modal-specific 兴趣分数,L 层堆叠后接 MLP 降维。
- **Segment Interest Decoder(片段兴趣解码器)**:用 **multi-modal bilinear fusion** 融合各模态分数,既保留模态独立优势又允许互补;再加上可学习的 **inner-video position bias**(片段位置偏置 `p = o + (w_p · pos + b_p)`)建模"兴趣随片段位置递减"的人类注意力模式。
- **intra-video loss(片段内损失函数)**:针对 challenge 2(无显式片段标签),假设被跳过位置的片段兴趣应是已观看片段中最低的,用成对 BPR 式损失 `L_{u,v} = -Σ ln σ(p_j - p_i)` 利用隐式交互。

下游两个任务验证有效性:**Task 1 video-skip prediction**(预测哪些片段会被跳过,按兴趣分数排序,负相关于跳过概率);**Task 2 video recommendation**(把片段兴趣分数引入推荐,提出 **SegRec** 框架:冻结片段兴趣模型,将分数作为权重聚合到 video-level CTR 预测)。

## 结果

发布了 **SegMM** 数据集(商业短视频平台,2,369 用户、902,115 物品、3,920,483 segment,3 天,June 1-3 2024,含 visual 特征,首个同时含片段级特征与行为的短视频推荐数据集),并补充使用公开 [[kuairand]] 数据集(983 用户、1,615,315 view、8,140,477 segment,2 周,无 visual)。代码与数据见 GitHub(hezy18/SegMMInterest)。

- **Task 1 (video-skip prediction)**:在 SegMM 上 Ours(Both)取得 HR@1 **0.4072**、HR@5 **0.8214**、N@5 **0.6228**、HR@10 **0.9225**、N@10 **0.6572**,显著超过最强基线(如 AdaGIN HR@5 0.5868、CAN 等);在 KuaiRand 上 HR@1 **0.2904**、HR@5 **0.5709**。Both(ID+Visual)优于单模态,visual modality 优于 ID modality。
- **Cold-start(Table 3)**:在冷启动视频上 Ours(Both)SegMM HR@1 **0.4068**、HR@10 **0.9234**,仍显著超过 MostPopular(ItemPosition)与各推荐基线,显示泛化能力;ItemPosition 优于 AllPosition,说明同一视频内跳过位置具一致性。
- **Task 2 (video recommendation)**:SegRec 接入 WideDeep / [[adagin]] / [[din]] / [[can]] 等 backbone 均提升,如 SegMM 上 DIN backbone SegRec(Both)AUC **0.7581**、F1 **0.6915**;Both(多模态融合)整体最佳,ID 始终优于纯 visual。
- **消融**:移除 cross-attention、segment position、或用 BCE 替换 intra-video loss 均导致明显下降,验证各组件必要性。
- **Case study**:展示同一视频下不同用户(emoticon 视频用户 A 在 segment 2 跳过、用户 B 看完)的可解释片段兴趣热力图,并指出可用于 personalized thumbnail 生成与 video editing。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] / 短视频推荐方向,把粒度从 video-level 细化到 segment-level,与 [[kuairand]]、[[kuaishou]] 等数据集/平台线索相连;在多模态融合上使用 [[clip]],并以 [[din]]、[[can]]、[[adagin]]、[[sasrec]]、[[lightgcn]] 等为基线,可作为细粒度用户建模与多模态推荐的参考节点。作者来自 [[tsinghua-university]] 与 [[kuaishou]]。
