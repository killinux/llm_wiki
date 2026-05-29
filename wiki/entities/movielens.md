---
type: entity
subtype: dataset
tags: [recommendation, dataset, movie-rating, benchmark]
created: 2026-05-29
updated: 2026-05-29
sources: 25
---

# MovieLens

MovieLens 是由 GroupLens 研究团队收集发布的电影评分数据集,广泛用作推荐系统研究的基准数据集。

## 在本 wiki 中的出现
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模,用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[deep-recommendation-system]]
- [[ctr-prediction]]
- [[user-modeling]]
- [[kuairand]]
- [[tenrec]]

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
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2024-online-item-cold-start-popularity-aware-meta-learning]]:提出 PAM,一种按物品热度固定切分 meta-learning 任务的 model-agnostic 框架,在流式在线推荐中解决新物品冷启动并缓解马太效应。
- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。
- [[2026-vk-lsvd-short-video-dataset]]:迄今最大的公开短视频推荐工业数据集,来自 VK,含 400 亿交互、1000 万用户、近 2000 万视频,跨 6 个月。
- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。
- [[2026-graphrag-irl]]:GraphRAG-IRL 把 graph-grounded 特征、Maximum Entropy 逆强化学习预排序与 persona-guided LLM 重排融合,LLM 只对 IRL 短候选列表做语义重排,在 MovieLens/KuaiRand 上 NDCG@10 比监督基线提升 15.7%/16.6%。

## 相关

- [[recommender-systems|recommendation-system]]
- [[embedding-based-retrieval]]
- [[multi-task-learning]]
- [[collaborative-filtering]]
- [[user-behavior-simulation]]
- [[microlens]]
- [[merrec]]
