---
type: source
subtype: paper
tags:
  - user-simulation
  - llm-agent
  - recommender-system
  - evaluation
  - persona
created: 2026-05-29
updated: 2026-05-29
arxiv: 2504.12722
raw: raw/2504.12722.pdf
authors:
  - Nicolas Bougie
  - Narimasa Watanabe
year: 2025
---

# SimUSER: Simulating User Behavior with Large Language Models for Recommender System Evaluation

SimUSER 提出一个基于 LLM 的 agent 框架,把从历史数据中推断出的 persona、记忆、感知与决策模块组合成可信且低成本的"合成用户",用来在离线环境中评估 [[recommender-system]]。

## 问题

[[recommender-system]] 的核心难题是评估:离线指标(非交互)与上线后真实用户行为之间存在鸿沟。线上 A/B 测试成本高、耗时且涉及伦理问题,而真实用户数据稀缺并受隐私限制。已有的 LLM 用户模拟工作(如 RecAgent、[[interecagent]]、[[agent4rec]])存在"孤立性"问题:主要依赖模型权重内的知识,忽视外部知识与 user-item 关系;且常常忽略 user persona 与视觉信号对用户体验和情绪的影响。

## 方法

SimUSER 分两个阶段构建合成用户:

- **Phase 1:Persona Matching via Consistency Check**。从用户历史交互推断最可信的 persona(包含 age、personality、occupation,personality 用 Big Five 五个维度按 1-3 打分)。先从 50 个抽样物品生成偏好摘要 s_u(评分≥4 为 liked,<3 为 disliked),为每个用户生成 m=5 个候选 persona,再用 self-consistency 打分函数 s(p,u)(目标用户交互子集打分减去其他用户交互子集打分)挑选最一致的 persona。
- **Phase 2:Engaging in Interactions with RS**,认知架构含四个模块:
  - **Persona Module**:在 persona 基础上加入 pickiness(not picky / moderately picky / extremely picky,按平均评分采样,纠正 LLM 的正向情感偏置)、habits、unique tastes。
  - **Perception Module**:用 GPT-4o 从物品 thumbnail 生成 caption(情绪基调、视觉细节、卖点),把视觉线索注入推理。
  - **Memory Module**:Episodic Memory(交互历史,self-ask 检索 + 余弦相似度 top-k1 向量检索)+ Knowledge-Graph Memory(用真实数据集初始化的三元组图,emulate 外部影响)。引入 Graph-Aware Dynamic Item Retrieval,扩展 PathSim 计算 item-item 相似度 s_{x,y} 与 user-item 相似度 s_{u,y},加权融合 α·s_{x,y}+(1-α)·s_{u,y}。
  - **Brain Module**:用 [[chain-of-thought]] 跨五个步骤推理,含 multi-round preference elicitation(逐页 WATCH/SKIP,带 pickiness 修饰)、item evaluation(给出 1-5 评分及理由,引用 KG 路径)、action selection([EXIT]/[NEXT]/[PREVIOUS]/[CLICK])、Causal Action Refinement(生成反事实问题如"如果现在退出会怎样"以校正过早退出)、Post-interaction Reflection(反思并把 insight 写回 episodic memory)。

实验用 [[gpt-4o-mini]] 驱动 agent,agent 数为 1000;有 SimUSER(zero) 与 SimUSER(sim)(先与 RS 交互填充记忆)两个版本。

## 结果

- **偏好对齐(Table 1)**:在 [[movielens]]、AmazonBook、[[steam-dataset]] 上,SimUSER 全面优于 RecAgent 与 [[agent4rec]]。如 1:1 distractor 下 MovieLens Accuracy 0.7912、F1 0.7771;AmazonBook Accuracy 0.8221;Steam Accuracy 0.7905(配对 t 检验 p<0.002)。
- **评分预测(Table 2)**:SimUSER 取得最佳 RMSE/MAE,且 SimUSER(sim) 通过 grounded 交互进一步降低 MAE(如 MovieLens RMSE 0.5020 / MAE 0.4460)。指出 [[agent4rec]] 因 niche 物品幻觉导致 RMSE 偏高。
- **推荐策略评估(Table 3)**:在 MovieLens 上比较 Random / Pop / [[matrix-factorization]] / [[lightgcn]] / [[variational-autoencoder]](MultVAE),SimUSER 给高级算法更高满意度(LightGCN P_view 0.557、S_sat 3.92),符合现实趋势。
- **人类相似度(Table 4,GPT-4o 5 点 Likert 评)**:SimUSER(persona) 在三域均显著最优(MovieLens 4.41、AmazonBook 3.99、Steam 4.02,p<0.05);persona 与 memory 模块为关键贡献因素。
- **离线 A/B(Table 5,Fig 1)**:基于 55 个真实线上 A/B 测试的专有数据集,SimUSER 与 ground truth 的 Spearman 相关性最高,显著超过 [[agent4rec]] 与 RecAgent;按 SimUSER 评估选参数比传统 nDCG@10(TRAD)带来更高线上 engagement 与满意度(P_view 0.561、S_sat 4.09)。
- 还做了 thumbnail 对点击率、exposure effect、review 对 engagement 影响的实验。

## 在本 wiki 中的位置

本文属于 [[user-simulation]] 与 [[llm-agent]] 在 [[recommender-system]] 评估方向的工作,与 [[agent4rec]]、[[interecagent]]、[[recagent]]、[[recsim]] 等模拟器同属一脉,但通过 persona 推断、[[perception]] 视觉模块与 knowledge-graph 检索强化了可信度。方法上复用 [[chain-of-thought]]、[[memory-module]]、[[reflection]] 与 [[causal-inference]] 思想,可与 [[llm-for-recommendation]]、[[interactive-recommendation]] 等概念互相参照。
