---
type: entity
subtype: model
tags: [recommendation, sequential-recommendation, self-attention, baseline]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# SASRec

SASRec(Self-Attentive Sequential Recommendation)是一种基于自注意力机制的序列推荐模型,通过对用户历史行为序列建模来预测下一个交互物品。

## 在本 wiki 中的出现

- 在 [[2023-divide-and-conquer-ebr]] 中,SASRec 作为序列推荐 / embedding-based retrieval 场景下的相关基线或建模组件出现,用于在公开数据集上对比召回效果(该工作将推荐召回拆为"物料聚类 + 簇内并行检索 + 可控合并",Recall 最高提升约 40%,并已在快手线上部署)。
- 在 [[2023-hyper-actor-critic-recommendation]] 中,SASRec 作为序列推荐建模 / 基线方法出现,与所提出的 Hyper-Actor Critic(HAC)框架相关联;HAC 将推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,并用对齐与监督模块稳定大动作空间下的 RL 推荐策略学习。
- [[2024-llm-tags-vs-classical-text-features]]:在统一协议下对照评估 LLM 生成语义标签与 TF-IDF/LDA/BERT 三类经典文本特征用于短视频推荐用户兴趣建模,发现 LLM 标签下游精度最优(CTR AUC 较 TF-IDF +0.9~1.6 点、SASRec HR@10 +2.1~3.4 点)且因稀疏化在在线成本上 Pareto 支配稠密嵌入,但离线生成贵约 40 倍。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-microlens-micro-video-recommendation-dataset]]:MicroLens:一个含 10 亿交互、3400 万用户、100 万微视频并提供原始视频/音频/图像/文本内容的内容驱动微视频推荐数据集与基准。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2023-collaboration-transition-multi-query-self-attention]]:提出 MQSA-TED,用多查询自注意力建模协同信号、并把全局 item 转移模式蒸馏进 embedding,在序列推荐中平衡协同与转移信号。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。
- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度>=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。

## 相关

- [[self-attention]]
- [[transformer]]
- [[sequential-recommendation]]
- [[embedding-based-retrieval]]
- [[hyper-actor-critic]]
- [[recmamba]]
- [[mqsa-ted]]
