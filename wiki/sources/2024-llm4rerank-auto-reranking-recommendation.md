---
type: source
subtype: paper
tags:
  - recommender-system
  - reranking
  - large-language-models
  - chain-of-thought
  - diversity
  - fairness
created: 2026-05-29
updated: 2026-05-29
arxiv: "2406.12433"
raw: raw/2406.12433.pdf
authors:
  - Jingtong Gao
  - Bo Chen
  - Weiwen Liu
  - Xiangyang Li
  - Yichao Wang
  - Wanyu Wang
  - Huifeng Guo
  - Ruiming Tang
  - Xiangyu Zhao
year: 2024
---

# LLM4Rerank: LLM-based Auto-Reranking Framework for Recommendations

把推荐系统的 reranking 阶段里 accuracy、diversity、fairness 等多个目标(aspect)抽象成"全连接图"中的不同 node,让 LLM 以 Chain-of-Thought 方式自动跳转、按用户/部署方给定的 "Goal" 个性化地综合多目标重排候选列表。

## 问题

Reranking(重排)是 [[recommender-systems|recommender-system]] 中的关键后处理环节:在 ranking model 生成候选列表后,reranking 进一步分析 item 间关系,从 N 个候选中选出 K 个(K < N)更优的列表。实际应用中,reranking 不仅要看 accuracy(准确率),还要兼顾 diversity(多样性)与 fairness(公平性)等多个 aspect。

现有 reranking 模型存在三个核心局限:

- **难以在模型层面综合并平衡多个 aspect**:每个 aspect 关注推荐列表的不同语义维度,彼此之间存在很大的语义鸿沟(semantic gap),难以在一个模型里协调。
- **scalability(可扩展性)差**:单一模型难以适配不同推荐场景下千变万化的 aspect 组合或功能规则(如 backward、stop 等在设计时未预料到的规则)。
- **缺乏 personalization(个性化)**:模型一旦部署,其在各 aspect 上的输出倾向就被固定,无法随业务或用户偏好的演变而智能调整。

虽然 zero-shot LLM 在处理超长上下文(成千上万 item)时受 token 限制影响,但已有研究表明:在较短、item 数量有限的上下文(reranking 正是这种场景)中,LLM 凭借强语义理解能力可媲美甚至超越有监督模型。因此本文尝试用 LLM 来弥合不同 aspect 间的语义鸿沟。

## 方法

论文提出 **LLM4Rerank**,把各种 aspect 需求抽象为图中不同的 **node**,并构建一个供 LLM 遍历的**全连接 function graph**,以 [[chain-of-thought]](CoT)多跳方式自动重排。

**问题形式化**:用户 u、item i,ranking model(本文统一用 Generalized Matrix Factorization,GMF)先生成候选列表 I^r(每用户 20 个 item),reranking 从中选出 K 个得到 I^re,目标是优化相关性评分函数 R(u, i)。

**三类输入**:
- user info(用户信息,如 gender、age 等特征)
- candidate list I^r(候选 item 列表)
- **Goal**(目标句):一句人工输入的自然语言,描述本次重排优先关注哪些 aspect(如 "Mainly focus on accuracy, followed by diversity")。LLM 通过解读 Goal 与各 node 的语义关联,自动选择最合适的下一个 node。

**node 结构**(generic node,统一模板):每个 node 执行一步重排,公式为 `CN, CR = Function(CN)(u, I^r, Goal, Pool)`,输出重排结果 CR 与下一个 node 名 CN。node 分两类:

- **Aspect Nodes(aspect 节点)**,通过 prompt 模板 `Function(CN)() = LLM(Temp(CN)())` 实例化,本文实现三个:
  - **Accuracy Node**:聚焦 user-item 匹配的准确性;它是整个框架的固定起点(每次重排都从 Accuracy 出发)。评测指标用 Hit Ratio(HR)与 NDCG。
  - **Diversity Node**:提升最终列表中 item 某一属性的多样性,用 α-NDCG 衡量。
  - **Fairness Node**:用 Mean Absolute Difference(MAD)度量两个分组间的平均得分差异,追求公平。
- **Functional Nodes(功能节点)**:
  - **Backward Node**:当 LLM 判断上一步重排次优时,删除 historical reranking pool 中最近一次结果并回退,实现类似 reflection 的 [[self-reflection]] 能力。
  - **Stop Node**:终止重排,从 historical reranking pool 取最新结果作为最终输出;它不需要调用 LLM,也无 prompt 模板。

**Historical Reranking Pool(H,历史重排池)**:记录每个 node 的输出,作为后续重排的辅助参考,防止"记忆丢失",支撑对历史选择的整体性(holistic)评估。

**Automatic Reranking Process** 含三个子过程:设定 "Goal" → 跨 node 自动转移(每个 node 返回下一 node 名)→ 停止条件(LLM 自主选择 Stop,或经过超参 MC 设定的最大 node 数后强制经 Backward 结束)。

本工作把 [[large-language-models]] 用作推荐 reranking 的统一推理引擎,与 zero-shot LLM ranking(如 [[react]] 之外的 RankGPT、GoT/Graph of Thoughts)相关,但区别在于:LLM4Rerank 用全连接 function graph 做动态多跳路由并引入历史池,而非沿固定路径推理。

## 结果

**数据集**(Table 1):ML-1M(1,000,209 interactions / 6,040 users / 3,883 items)、KuaiRand(102,433 / 10,494 / 7,583)、Douban-Movie(759,652 / 2,606 / 34,893)。采用 leave-one-out 划分,每个候选集 20 个 item。LLM backbone 默认用 [[llama-2]] 13B(Llama-2-13B,zero-shot)。

**baseline**:GMF、DLCM、PRM、MMR、FastDPP、FairRec、RankGPT、GoT(graph-of-thought,固定路径 Accuracy-Diversity-Fairness-Stop 的 zero-shot LLM baseline)。

**RQ1 整体性能**(Table 2,"-A/-D/-F" 表示 Goal 聚焦 Accuracy/Diversity/Fairness;↑越高越好,↓越低越好):
- ML-1M:LLM4Rerank-A 取得 HR **0.7031**、NDCG **0.3320**(最高);LLM4Rerank-D 取得 α-NDCG **0.2407**(diversity 最高);LLM4Rerank-F 取得 MAD **0.0193**(fairness 最优)。对比 GMF(HR 0.4156、NDCG 0.1853)有大幅提升。
- KuaiRand:LLM4Rerank-A HR **0.8252**、NDCG **0.4229**;LLM4Rerank-D α-NDCG **0.2223**;LLM4Rerank-F MAD **0.0271**。
- Douban-Movie:LLM4Rerank-A HR **0.7041**、NDCG **0.4301**;LLM4Rerank-F MAD **0.1696**。

结论:LLM4Rerank 在对应 Goal 下,于 accuracy、diversity、fairness 三个维度均能取得各自最优或领先表现,验证其能用一个框架综合多目标。

**RQ2 aspect 组合分析**(Table 3,MC=5):不同 Goal(DF / D-F / F-D)会让 LLM 自动调整重排路径。例如 D-F 的最常用路径为 A-D-D-F(占 19%),平均推理长度约 3.3 步,印证"3 个 aspect node 下 3–4 步思考已足够"。Accuracy node 始终出现在所有重排结果中(每次都从 accuracy 起步)。

**RQ3 消融实验**(Table 4,ML-1M):
- 完整 LLM4Rerank-A:HR 0.7031 / NDCG 0.3320 / α-NDCG 0.2294 / MAD 0.0434。
- w/o historical pool(-H):HR 0.6410——去掉历史池性能明显下降,说明整体性视角的重要性。
- w/o automatic reranking(-AR,固定路径 Accuracy-Accuracy-Stop):HR 0.6413——自动重排带来显著增益。
- w/o other aspect nodes(-N,仅保留 Accuracy 与 Stop):HR 0.6533——去掉其他 aspect / 功能节点同样下降。

**Case Study**(Figure 7):展示 A-D-F 与 A-A-B-D 两条常见路径,说明 Backward 节点能让 LLM 在感知到 diversity 无改善时回退到上一步,做出更系统化的决策。

## 在本 wiki 中的位置

本文位于 **LLM 用于推荐系统 / reranking** 这一交叉脉络:

- 数据集方面直接使用了本 wiki 已有的 [[kuairand]];任务对象是 [[recommender-systems|recommender-system]] 的重排阶段,与 [[sequential-recommendation]]、[[listwise-recommendation]] 相关。
- 方法上把 [[chain-of-thought]] 与图结构推理引入推荐,并通过 Backward 节点体现 [[self-reflection]] 思想;LLM backbone 用 [[llama-2]],属于 [[large-language-models]] 应用。
- 与 diversity / fairness 优化的传统 reranking(MMR、FastDPP、FairRec、DLCM、PRM)形成对比;同时以 GoT、RankGPT 等 zero-shot LLM ranking 方法为 baseline。
- 概念上呼应推荐中的 fairness / [[debiasing]] 话题(用 MAD 度量分组公平),可与本 wiki 因果推荐类条目(如 [[deep-causal-reasoning-for-recommendations]])对照阅读。

作者来自 [[huawei-noahs-ark-lab]] 与 City University of Hong Kong,通讯作者包括 Ruiming Tang 与 Xiangyu Zhao([[xiangyu-zhao]])。
