---
type: concept
subtype: method
tags: [recommendation, sequential-recommendation, user-behavior, dataset, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 11
---

# Sequential Recommendation

Sequential Recommendation 是一类推荐方法,它将用户的历史交互建模为按时间排列的行为序列,以此预测用户下一步可能感兴趣的物品。

## 在本 wiki 中的出现

- [[2022-kuairand]]:快手发布的无偏序列推荐数据集,通过在推荐流中随机插入视频收集百万级无偏交互(含 12 种反馈信号、完整用户/物品 ID 与特征)。在该工作中,Sequential Recommendation 是数据集所面向的核心任务场景——用户在信息流中产生的连续交互天然构成行为序列,数据集为这类序列建模提供了带有随机曝光(从而可去偏)的训练与离线评估基础。
- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2024-llm-tags-vs-classical-text-features]]:在统一协议下对照评估 LLM 生成语义标签与 TF-IDF/LDA/BERT 三类经典文本特征用于短视频推荐用户兴趣建模,发现 LLM 标签下游精度最优(CTR AUC 较 TF-IDF +0.9~1.6 点、SASRec HR@10 +2.1~3.4 点)且因稀疏化在在线成本上 Pareto 支配稠密嵌入,但离线生成贵约 40 倍。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2023-microlens-micro-video-recommendation-dataset]]:MicroLens:一个含 10 亿交互、3400 万用户、100 万微视频并提供原始视频/音频/图像/文本内容的内容驱动微视频推荐数据集与基准。
- [[2023-collaboration-transition-multi-query-self-attention]]:提出 MQSA-TED,用多查询自注意力建模协同信号、并把全局 item 转移模式蒸馏进 embedding,在序列推荐中平衡协同与转移信号。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。
- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度>=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。
- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。

## 相关

- [[recommendation-system]]
- [[user-behavior-modeling]]
- [[debiasing]]
- [[offline-evaluation]]
- [[implicit-feedback]]
- [[transformer]]
- [[state-space-model]]
- [[large-language-model]]
- [[multi-task-learning]]
- [[reranking]]
