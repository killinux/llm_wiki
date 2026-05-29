---
type: entity
subtype: dataset
tags: [recommendation, dataset, movie-rating, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 13
---

# MovieLens

MovieLens 是由 GroupLens 研究团队收集发布的电影评分数据集,广泛用作推荐系统研究的基准数据集。

## 在本 wiki 中的出现

- [[2022-deep-causal-reasoning-for-recommendations]]:作为评测数据集,用于验证 Deep-Deconf 通过深度 VAE 推断 substitute confounders、将推荐建模为 MCMO 因果推断以消除混杂偏差并降低方差的效果。
- [[2023-divide-and-conquer-ebr]]:作为公开数据集之一,用于评测将 embedding-based retrieval 拆为"物料聚类+簇内并行检索+可控合并"的方法,在公开数据集上 Recall 最高提升约 40%。
- [[2023-multi-task-deep-recommender-systems-survey]]:作为多任务深度推荐系统(MTDRS)综述中梳理的代表性数据集之一被收录。
- [[2023-gflownet-listwise-recommendation]]:作为评测数据集,用于验证 GFN4Rec 以 GFlowNet 流匹配让推荐列表生成概率正比于其 list-wise 奖励、在保持质量的同时提升列表多样性的效果。
- [[2023-recagent-user-behavior-simulation]]:作为用户行为数据来源,用于支撑 RecAgent 以 LLM-based agent 在沙盒中模拟用户推荐与社交行为的研究。
- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-microlens-micro-video-recommendation-dataset]]:MicroLens:一个含 10 亿交互、3400 万用户、100 万微视频并提供原始视频/音频/图像/文本内容的内容驱动微视频推荐数据集与基准。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。
- [[2024-lusifer-llm-user-simulation]]:提出 Lusifer:基于 LLM 的用户模拟环境,在每次交互后增量更新可解释的用户画像,为 RL-based 推荐系统生成动态真实的用户反馈,并在 cold-start 场景超越传统协同过滤基线。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-user-creator-feature-polarization]]:提出 user-creator feature dynamics 模型刻画推荐系统对用户与创作者的双向影响,证明非零推荐概率下系统必然极化,并发现 top-k 截断等效率优化反而能抑制极化、而多样性提升方法在动态环境下失效。

## 相关

- [[recommendation-system]]
- [[embedding-based-retrieval]]
- [[multi-task-learning]]
- [[collaborative-filtering]]
- [[user-behavior-simulation]]
- [[microlens]]
- [[merrec]]
