---
type: source
subtype: paper
tags:
  - llm-user-simulation
  - recommender-system
  - reinforcement-learning
  - user-simulation
  - cold-start
  - prompt-engineering
created: 2026-05-29
updated: 2026-05-29
arxiv: 2405.13362
raw: raw/2405.13362.pdf
authors:
  - Danial Ebrat
  - Eli Paradalis
  - Luis Rueda
year: 2024
---

# Lusifer: LLM-based User Simulated Feedback Environment For online Recommender systems

提出 [[lusifer]]:一个基于 LLM 的用户模拟环境,在每次交互后增量更新用户画像并给出可解释说明,为 RL-based [[recommender-systems|recommender-system]] 生成动态、真实的用户反馈。

## 问题

[[reinforcement-learning]](RL)推荐系统通常依赖**静态历史数据集**训练,无法刻画真实场景中用户偏好的流动与持续变化。离线环境会带来分布漂移与探索不足;在线环境虽能动态交互,却面临样本效率与真实世界泛化的难题。已有模拟环境(RecSim NG、RecoGym、Virtual-Taobao)各有局限:RecSim NG 可定制但计算开销大、扩展性差;RecoGym 易上手但无法模拟复杂用户行为;Virtual-Taobao 真实但局限于电商领域。

[[large-language-models]] 作为模拟环境提供了一个兼具灵活性、广适用性与生成细腻真实反馈能力的替代方案,有望同时解决真实性、领域专一性与可扩展性问题。

## 方法

Lusifer 用 [[movielens]] 数据集(100K 与 1M 版本)做案例研究,只抽取每个用户**最近 40 次评分交互**(约占训练数据 30%),并用 TMDB API 补充电影 overview、tags 等文本元数据。用户画像编码为 user_info(年龄、性别、职业),电影编码为 movie_info(标题、类型、overview)。流程分两阶段:

- **Phase 1 创建用户画像**:把最近 40 次交互按时间序拆成 4 个 batch(每 batch 10 条),让 LLM 顺序处理,逐 batch 更新一段用户行为摘要,并存储每个中间画像状态与一段简明的"为什么变化"的解释,形成可解释的偏好演化记录。
- **Phase 2 生成模拟评分**:基于更新后的用户摘要加最近 10 条评分,让 LLM 扮演该用户,对测试集中被推荐的电影打分,输出 JSON(movie_ID + rating)。

实现上使用 [[gpt-4o-mini]] 以及 Ollama 上的开源模型 Gemma3:4B、Gemma3:12B,模型可在配置中替换。采用 one-shot [[prompt-engineering]],并加入输出校验层、解析失败重试机制与错误处理,保证 JSON 格式与流程鲁棒性。训练 RL agent 时,agent 的推荐以 item ID 的 dataframe 传入,Lusifer 返回模拟评分并据新评分更新用户行为。

基线为 ALS、SVD++、NCF、RNN4Rec,统一只用每用户最近 40 次交互、embedding 维度 16,以保证公平比较。评测指标:RMSE、MAE、Pearson 相关系数。

## 结果

整体预测精度上,传统协同过滤基线优于 Lusifer。Table 1(MovieLens 100K / 1M):

- SVD++:RMSE 1.05 / 1.14,MAE 0.76 / 0.83,Pearson 0.395 / 0.383(基线中最强)。
- ALS:RMSE 1.11 / 1.10,Pearson 0.392 / 0.423。
- Lusifer:GPT-4o-mini RMSE 1.57 / 1.73;Gemma3:4B RMSE 1.39 / 1.50;Gemma3:12B RMSE 1.19(100K,Pearson 0.259),1M 为 N/A。

**Cold-start 场景**(MovieLens 100K,交互少于 10 次的用户,Table 2):Lusifer 用 Gemma3:12B 在多数指标上超过基线——RMSE 1.18、MAE 0.88,优于 NCF(1.29/0.99)、RNN4Rec(1.19/0.9)、ALS(1.35/1.04),接近 SVD++(1.11/0.83)。

关键观察:引入非结构化文本元数据(overview、tags)显著提升 Lusifer 精度;而在画像中显式包含数值评分有时反而降低精度(LLM 对数值推理较弱),因此把数值仅限于最近 10 条评分、主要依赖文本元数据效果最佳。结论:Lusifer 不以预测精度取胜,其价值在于动态可解释的偏好演化建模、cold-start 处理、对稀疏/OOD 数据的适应,以及作为替代真人实验的可扩展、合伦理的环境。

## 在本 wiki 中的位置

本文属于 [[user-simulation]] 与 [[llm-agents|llm-agent]] 在 [[recommender-systems|recommender-system]] 中的交叉应用,与 wiki 中 [[recagent]]、[[user-simulation]]、[[llm-based-agents]] 等条目同源——都用 LLM 模拟用户行为以支撑 RL 推荐训练与评估。相关方法/概念:[[reinforcement-learning]]、[[prompt-engineering]]、[[in-context-learning]]、[[cold-start]]、[[collaborative-filtering]]、[[movielens]]、[[gpt-4o-mini]]。
