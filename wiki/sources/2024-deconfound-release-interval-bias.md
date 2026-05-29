---
type: source
subtype: paper
tags: [recommender-system, short-video, causal-inference, debiasing, backdoor-adjustment, recency, confounding-bias]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2408.17332
raw: raw/2408.17332.pdf
authors: [Lulu Dong, Guoxiu He, Aixin Sun]
year: 2024
---

# Not All Videos Become Outdated: Short-Video Recommendation by Learning to Deconfound Release Interval Bias

短视频推荐系统倾向于偏好"新近发布"的视频,本文将 release interval 识别为一个 confounder,提出模型无关的因果框架 LDRI(Learning to Deconfound Release Interval Bias),通过 backdoor adjustment 阻断后门路径,在保持任务性能的同时按每个视频自身的 recency sensitivity 做个性化推荐。

## 问题

短视频 [[recommender-system]] 通常对"recently released"视频表现出偏置:从 [[kuaishou]] 的 KuaiRand-1K 日志看,视频曝光率与用户正反馈(watch-time、favorite rate)都随 release interval(发布至今天数)增大而下降。由于 matching model 从已有的有偏交互中学习,模型会捕捉到"短 release interval → 正反馈"的 shortcut,从而进一步放大 feedback-loop bias。

但关键观察是:并非所有视频都会随时间过时。不同 topic 的视频对 recency 的敏感度不同(例如健身类视频长期保持相关性,而某些热点话题快速过时)。本文把这种"短 release interval 受偏好"的现象命名为 **release interval bias**,并指出现有方法(针对 popularity bias、duration bias 的去偏,以及基于 Cox 模型的 survival analysis)都未识别这一来源,且 survival analysis 依赖人工规则、需过滤未失活视频,在真实推荐中不实用。

## 方法

作者用 [[structural-causal-model]](因果图)刻画短视频推荐,节点包括:video features $V$、user features $U$、matching $M$、user interests $UI$、video recency sensitivity $T$、release interval confounder $A$。

- 因果路径:$\{U,V\} \to M \to UI$(用户-视频匹配)与 $V \to T \to UI$(视频内在 recency 敏感度)。
- 非因果(后门)路径:$V \leftarrow A \to UI$,由 confounder $A$(release interval)打开,在视频与用户兴趣间制造虚假关联。

**LDRI** 采用 [[do-calculus]] 的 [[backdoor-adjustment]]:对 $V$ 做 intervention $do(V=v)$,删除 $A \to V$ 的边以阻断后门路径,得到 $P(UI|do(v)) = \sum_A P(UI|A,m,t)P(A)$。

训练阶段是 [[multi-task-learning]]:
- **Backbone matching model** $\mathcal{M}(u,v)$:任意推荐模型作为骨干,预测匹配分 $m$,用 binary cross-entropy 训练。
- **Recency sensitivity perceptron** $\mathcal{T}(v)$:把视频投影成 $|A|$ 维向量 $\hat{t}$(用 Res-MLP 作为 projector),每一维表示该视频在对应 release interval 上的 recency 敏感度;用相邻 interval 的正反馈做监督(窗口 $2N+1$ 平滑),即使反馈稀疏或视频很新也能训练。
- 联合损失 $\mathcal{L} = \alpha \cdot BCE_m + (1-\alpha) \cdot BCE_t$。

推理阶段用 fusion function $\hat{y}_{m,t} = \beta \times \hat{m} + (1-\beta)\times \hat{t}$ 融合匹配分与 recency,并提供两种 backdoor adjustment 推理策略:**LDRI**(取真实 $A=a$)与 **LDRI-iter**(对所有 $A$ 加权,权重为 $P(A=a)$ 的全局频率)。

## 结果

数据集:KuaiRand-Pure(7,582 个视频、27,284 用户、130 万交互,随机曝光的无偏数据)与 KuaiRand-1K(1,000 活跃用户、1,100 万+交互、430 万视频,release interval 范围 0–1,400 天),均来自 [[kuaishou]] 的 [[kuairand]]。指标:RECALL@K、MAP@K、NDCG@K、HR@K。骨干:[[deepfm]]、NFM、AFM;对比方法含 TaFR、DCR-MoE、TCCM。

- **整体性能**:LDRI 与 LDRI-iter 在三个骨干、几乎所有指标上一致超过骨干及 SOTA 方法,且 $p<0.05$ 显著。例如在 Pure 上 DeepFM+LDRI 的 NDCG@5 = 0.2267(DeepFM baseline 0.2219),RECALL@5 = 0.5142;DeepFM+LDRI-iter RECALL@5 = 0.5148。在 1K 上 DeepFM+LDRI NDCG@500 提升至 0.1981 等。两策略中 LDRI 通常略优于 LDRI-iter,但差距不大。
- **运行时间**:LDRI 在保持较低额外时间成本下取得增益(相对 NFM 参考)。
- **各 release interval 表现**:Figure 4 显示 LDRI 在几乎所有 release interval 上提升 NDCG@5,DeepFM 与 AFM 尤为明显,并平抑了原有的剧烈波动。
- **冷启动**:在仅有 ≤2 天交互的新发布视频上,LDRI 显著提升骨干并超过 TCCM、DCR-MoE;由于 recency sensitivity 表示来自视频内在特征,LDRI 在反馈稀疏时仍有效,而 TaFR 表现较差。
- **预测分案例**:对 recency-sensitive 视频(Figure 6),LDRI 拉大新旧视频预测分差距,给新视频更多曝光;对 recency-insensitive 视频(Figure 7),LDRI 给新旧视频更接近的分数,使老视频获得公平曝光。证明去混淆"并非一刀切地抬高所有视频",而是按每个视频的 recency sensitivity 个性化调整。

## 在本 wiki 中的位置

本文属于 causal recommendation / 去偏方向,与 [[recommender-system]]、[[confounding-bias]]、[[selection-bias]]、[[debiasing]] 紧密相关。方法上使用 [[backdoor-adjustment]]、[[do-calculus]]、[[structural-causal-model]],与 duration-bias 去偏(DCR-MoE)、popularity bias 去偏属同一谱系,但聚焦此前被忽略的 release interval confounder。数据与场景来自 [[kuaishou]] / [[kuairand]],骨干模型涉及 [[deepfm]]。
