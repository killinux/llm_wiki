---
type: source
subtype: paper
tags: [recommender-systems, graphrag, inverse-reinforcement-learning, llm-for-recommendation, knowledge-graph, learning-to-rank, persona]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2604.19128
raw: raw/2604.19128.pdf
authors: Siqi Liang, Xiawei Wang, Yudi Zhang, Jiaying Zhou
year: 2026
---

# 2026-graphrag-irl

GraphRAG-IRL 是一个混合推荐框架,把 graph-grounded 特征构造、Maximum Entropy 逆强化学习(IRL)预排序与 persona-guided 的 [[large-language-models]] re-ranking 结合起来:LLM 只对 IRL 选出的短候选列表做语义重排,而非充当独立排序引擎。

## 问题

个性化推荐需要在稀疏、含噪、随时间演化的交互历史中捕捉序列偏好。传统 [[collaborative-filtering]] 与 [[sequential-recommendation]] 擅长结构化信号,但难以纳入"为什么某 item 匹配用户兴趣"的语义证据。近期工作把 [[large-language-models]] 当作 recommender 或 zero-shot ranker,但纯 prompt-based 排序存在校准差、对候选顺序敏感、以及 [[popularity-bias]] 等问题——LLM 是好的语义推理者,却是不可靠的独立排序引擎。作者要解决的是:如何在保留学习型排序模型稳定性的同时,利用 LLM 的语义推理能力。

## 方法

完整流水线:用户历史 → 知识图构造 → GraphRAG 检索 → 特征工程 → IRL reward 打分 → top-N 选择 → persona-guided LLM 重排 → α-blended 融合。

- **异构知识图**:构造含 Item / Category / Concept 三类节点的图 G,边包括 Item→Category、Item→Concept、Item↔Item(共享至少 2 个 concept 节点的共现边),并额外建一个 item 文本的 TF-IDF 索引做内容检索。
- **GraphRAG 检索**:对每个用户状态检索两类上下文——个体上下文(近期高评分 item、category 分布、concept affinity)和社区上下文(用 category profile 的 cosine 相似度取 top-M 近邻构成轻量社区,得到 community support、社区平均评分、shared concepts)。
- **特征工程**:每个候选构造 φ(s,a),含行为特征(用户 category 分布、活跃度、recency、候选 category 向量、popularity、交互相似度)和 4 个图衍生特征(user-retrieval similarity、community support、shared concepts、community average rating)。
- **IRL reward 模型**:用 [[inverse-reinforcement-learning]] 把推荐建模为从 expert demonstration(用户正反馈轨迹)恢复 latent reward。reward 为两层 MLP(隐藏维 64),策略采用 Boltzmann/softmax 分布,训练用 listwise softmax 目标最大化专家动作的对数似然——这等价于 single-step Maximum Entropy IRL,也形式等同于生存分析中 Cox 比例风险模型的偏似然。
- **Persona-guided LLM 重排**:对 top-N=20 短列表构造个性化 prompt(user persona、社区上下文、候选详情、IRL 置信度 high/medium/low 信号),让 LLM 一次性返回 listwise 排序,temperature=0。
- **Score Fusion**:rank-level 融合 score(c)=α·rank_LLM(c)+(1−α)·rank_IRL(c),α 在验证集上按 NDCG@10 grid search 调,强 LLM 得到更高 α。

## 结果

数据集为 MovieLens(过滤后 608 测试用户)与 KuaiRand-Pure([[kuairand]],10,877 测试用户);评测在每条样本 1 正 + 99 负的 100-候选任务上,报告 HR/NDCG/MRR。

- **IRL + GraphRAG(非 LLM)**:IRL-MLP+GraphRAG 在 MovieLens 上 NDCG@10=0.258(比 Supervised LogReg 的 0.223 提升 +15.7%),在 KuaiRand 上 N@10=0.351(比 0.301 提升 +16.6%)。IRL-MLP 单独比监督基线提升 +6.3%(MovieLens)/+11.6%(KuaiRand),而 IRL-Linear 与监督相当,说明增益来自非线性 MLP reward + listwise 目标。
- **超可加性(superadditive)**:MovieLens 上 IRL(+0.014)与 GraphRAG(+0.005)的单独贡献之和为 +0.019,但合并实际增益 +0.035,接近翻倍——因为 listwise 目标能利用候选间图特征的相对差异。
- **LLM 重排(KuaiRand,2000 用户,Claude Opus 4.6,top-20)**:Persona 上下文是关键——去掉 persona 时 IRL+plain LLM 的 N@10 仅 0.246(比 IRL-only 的 0.351 暴跌 28%);IRL+Persona LLM 恢复到 0.347,full pipeline 达 0.354,温和但稳定地超过非 LLM 基线。
- **预排序质量主导**:GraphRAG-only 检索 top-20 召回仅 34.8%(IRL 为 77.3%),导致 65% 用户的正样本根本进不了短列表,GraphRAG+plain LLM 因此很差(N@10=0.158)。
- **多 LLM(MovieLens ml-1m,608 用户,tuned α)**:所有 4 个前沿模型经 α 融合后均超过 IRL-only(N@10=0.292):Claude 4.6(α=0.8)N@10=0.341,+16.8%;DeepSeek(α=0.7)+4.5%;Qwen3-235B(α=0.4)+2.7%;GPT-5.2(α=0.6)+1.4%。增益随 LLM 质量上升,验证融合的模型无关性。
- **消融**:去 GraphRAG 特征 −8.1%、去非线性 reward −11.6%、去 listwise 目标 −11.6%、退化为 Supervised flat −13.6%。在缺乏用户标签的 ml-1m 上 shared_concepts 特征恒为零、增益约 0%,说明图的价值来自细粒度语义元数据流经 concept 节点,而非图结构本身。

## 在本 wiki 中的位置

本文连接了 [[llm-for-recommendation]]、[[graphrag]]、[[inverse-reinforcement-learning]] 与 [[learning-to-rank]] 四条线:它把 LLM 定位为对短列表做语义精炼的 re-ranker 而非独立排序器,与 wiki 中关于 [[popularity-bias]]、prompt 敏感性的讨论呼应,并给出"把建模容量投入检索/候选生成、用 LLM 做定向精炼"的设计原则。与 [[lightgcn]]、[[collaborative-filtering]]、[[sequential-recommendation]]、[[kuairand]] 等条目相邻,可作为 IRL-based recsys 与 GraphRAG-grounded 推荐的实证参考。
