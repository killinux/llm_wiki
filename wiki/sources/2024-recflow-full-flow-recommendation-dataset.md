---
type: source
subtype: paper
tags: [recommender-system, dataset, selection-bias, multi-stage-recommendation, debiasing, kuaishou]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.20868
raw: raw/2410.20868.pdf
authors: [Qi Liu, Kai Zheng, Rui Huang, Wuchao Li, Kuo Cai, Yuan Chai, Yanan Niu, Yiqun Hui, Bing Han, Na Mou, Hongning Wang, Wentian Bao, Yunen Yu, Guorui Zhou, Han Li, Yang Song, Defu Lian, Kun Gai]
year: 2024
---

RecFlow 是首个包含工业推荐系统多级漏斗中各阶段“被过滤(未曝光)样本”的大规模全流程推荐数据集,旨在弥合离线 benchmark 与真实在线环境之间的差距。

## 问题

工业 [[recommender-system]] 依赖多级漏斗 pipeline(retrieval → pre-ranking → ranking → re-ranking)在效果与效率间取得平衡。现有公开 RS 数据集(如 [[movielens]]、[[amazon-reviews]]、[[kuairec]]、[[kuairand]] 等)几乎只采集**曝光空间(exposure space)**的样本,带来两个核心缺陷:

1. **分布偏移(distribution shift)**:模型在曝光空间训练,但在线服务时要对海量**未曝光**候选打分,训练与服务空间不一致,导致 [[selection-bias]] 与次优表现。
2. **多阶段交互被忽视**:各阶段模型独立训练评估,但实际需作为统一系统协作;缺乏对后续阶段信息的建模会损害如 retrieval 等前序阶段的在线表现。

现有数据集无法支持对未曝光空间、[[debiasing]]、多阶段一致性与最优性等问题的研究。

## 方法

作者从 [[kuaishou]] 真实工业 RS 采集 **RecFlow** 数据集,核心是在单次请求中,除记录全部曝光样本外,还采集六级漏斗(retrieval → pre-ranking → coarse ranking → ranking → re-ranking → edge ranking)**每一阶段被过滤掉的代表性未曝光样本**(见收集流程图)。

- 各阶段输出视频数量级:8000 → 3000 → 500 → 120 → 10 → 6。
- 采样 42K 种子用户,记录其自 2024-01-13 起的请求日志,跨 37 天、6 个阶段。
- 采用 stage-wise 采样策略:对 pre-rank_neg、coarse_neg 各采 10/40 个过滤视频;后三阶段尽量保留全部 rank_pos/rank_neg/rerank_pos/rerank_neg 及 realshow 字段。
- 每条样本含丰富特征:request_id、user_id、device_id、age、gender、province、video_id、author_id、category、duration、realshow、playing_time,以及七类正反馈(effective_view、long_view、like、follow、share、comment 等)与各阶段排名位置(rank_index、rerank_index)。
- 基于该数据集开展三类探索实验:在 retrieval 阶段把各阶段过滤视频用作 **hard negative**([[hard-negative-mining]]);利用阶段样本缓解 coarse ranking 的分布偏移;以及借鉴 FS-LTR(Full-Stage Learning to Rank)联合建模多阶段偏好(用额外 ranking loss 强制高优先级阶段样本 logit 大于低优先级阶段)。

## 结果

- 数据规模:跨 **42K 用户**、近 **9M(8.7M)曝光视频**、**82M** 全部视频,来自 **9.3M 在线请求**;含 **38M 曝光交互** + **1.9B 阶段样本**。约 **89%** 的视频从未曝光;阶段样本比曝光样本大 **14.8x**(第二周期达 **236 倍**)。
- **Retrieval / Hard Negative**:用 [[sasrec]] + [[bpr]] 训练,以 effective_view 为正样本、每正样本配 200 负样本。把各阶段过滤视频作 hard negative 全面提升 Recall/[[ndcg]];加入 1 个 pre-rank_neg 时 Recall@100/500/1000 相对提升 **24.7% / 18.2% / 9.2%**,NDCG@100/500/1000 提升 **28.3% / 20.7% / 12.6%**。来自 rerank_pos 的 hard negative 效果最佳(R@100 达 0.687,baseline 0.461)。
- **FS-LTR(retrieval)**:联合建模多阶段偏好优于单纯 hard negative;加 1 个 pre-rank_neg 时 Recall@100/500/100 相对提升 **46.8% / 42.4% / 28.3%**。完整 FS-LTR 在 R@100 达 **0.803**、N@100 达 **0.215**,显著优于 baseline。
- **Coarse Ranking**:用 [[dssm]] 建模,把阶段样本补充为额外负样本可缓解分布偏移,大幅提升 Recall/NDCG(论文采用与在线一致的 Recall@K 而非曝光空间的 AUC)。
- 部分算法已在线上部署并持续取得显著收益。数据集与代码以 CC-BY-NC-SA-4.0 许可公开。

## 在本 wiki 中的位置

RecFlow 是一个面向 [[recommender-system]] 的工业级 [[dataset]] 与 [[benchmark]],来自 [[kuaishou]]。它的独特价值在于显式记录多级漏斗的未曝光阶段样本,因而成为研究 [[selection-bias]]、[[debiasing]]、分布偏移与多阶段联合优化的基础设施,可与 [[kuairec]]、[[kuairand]] 等同源数据集对照。在方法层面它连接了 [[hard-negative-mining]]、[[sasrec]]、[[dssm]]、[[bpr]]、[[ndcg]] 等检索/粗排技术。作者包括 [[guorui-zhou]]、[[kun-gai]] 等,机构涵盖 [[university-of-science-and-technology-of-china]]、[[kuaishou]]、[[tsinghua-university]]。
