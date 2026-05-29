---
type: source
subtype: paper
tags:
  - user-simulation
  - recommender-system
  - llm-agent
  - recommendation-simulator
  - personality
created: 2026-05-29
updated: 2026-05-29
arxiv: 2506.04551
raw: raw/2506.04551.pdf
authors:
  - Chenglong Ma
  - Ziqi Xu
  - Yongli Ren
  - Danula Hettiachchi
  - Jeffrey Chan
year: 2025
---

# PUB: An LLM-Enhanced Personality-Driven User Behaviour Simulator for Recommender System Evaluation

PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入到用户建模中,从行为日志推断人格并生成高保真的合成交互,用于[[recommender-systems|recommender-system]]的离线评估。

## 问题

传统的[[recommender-systems|recommender-system]]离线评估方法难以捕捉现代平台用户交互的动态复杂性:离线数据集普遍存在行为信号稀疏、日志含噪、缺乏细粒度行为信号以及受 confounding 变量偏置等问题,限制了对推荐系统的鲁棒优化能力。真实用户实验虽然有价值,但资源密集且涉及隐私顾虑。已有的[[user-simulation]]框架(如 [[recsim]]、[[recagent]])存在两大局限:(1) 低保真——生成的行为常偏离真实统计分布;(2) 人格建模过度简化——基于协同过滤或 Markov 决策过程的方法无法捕捉用户特质与行为之间的细致关联。论文要解决的核心问题是:如何利用 [[large-language-models]] 结合心理学上有效的 Big Five 人格特质,生成多样化且保真的用户行为以支撑可靠的推荐系统评估。

## 方法

PUB 是一个混合架构,分四个阶段运行:

1. **User Profile Aggregator(用户画像聚合器)**:从异构行为日志中分层构建统计用户画像。包含两个子阶段——Behavioural Signature Extraction(把各类别交互聚合为统一数据集,提取购买频率、购买节奏、类别偏好、价格分布等聚合特征;例如用圆形统计/角度变换刻画购买节奏的周期性,用 Shannon entropy 度量购买间隔的规律性)和 Temporal Stratified Sampling(用指数增长的时间窗口把交互划分为 K 个时间桶进行采样,时间窗按经验阈值设为 1 周/1 月/1 季度)。

2. **Metadata Enhancer(元数据增强器)**:把物品元数据(标题、描述、价格)纳入 LLM 提示引导的上下文,并用用户特定统计特征进行调制,通过 prompt-guided fusion 函数生成强调人格相关信号的动态表示。

3. **Personality Inference Module(人格推断模块)**:用心理测量映射函数从增强后的上下文估计用户的 Big Five 特质。基于已建立的心理语言学相关性来引导推断:Openness 对应类别熵与隐喻密度;Conscientiousness 对应评论长度一致性、评分偏差与购买节奏规律性;Extraversion 对应社交参照频率(用 LIWC-22 词典统计 "we"、"gift" 等);Agreeableness 对应正向情感比例(VADER)与礼貌标记;Neuroticism 对应负向情绪波动。

4. **User Behaviour Simulator(用户行为模拟器)**:基于推断出的特质分布生成合成交互,LLM agent 可完成多种下游任务(如 Q&A、对推荐提供反馈),本文聚焦推荐任务,生成的交互用标准指标(如 [[ndcg]])对照真实数据评估。

实验使用 [[amazon-reviews]](571.54 million 交互,30 个类别,1996–2023),经过三阶段预处理(跨类别聚合、过滤交互少于 20 的用户/物品、按时间划分训练/测试集)。

## 结果

围绕四个研究问题:

- **RQ1(能否生成接近真实的行为序列)**:用 Jaccard similarity 衡量合成序列 S_u 与真实序列 P_u 的对齐度。PUB 取得平均 0.31 的 Jaccard similarity,优于 Random Sampling、[[recsim]]、NEST、[[recagent]] 等 baseline(RecAgent 在 top case 表现尚可但整体更不稳定)。把用户按交互频率分为 10 组后,Jaccard similarity 随交互频率上升而提高,说明更丰富的交互历史带来更准确的人格建模。

- **RQ2(能否准确评估不同推荐算法)**:在合成测试集与真实测试集上评估 [[matrix-factorization]]、[[bpr]]、NeuMF、[[lightgcn]]、[[gru4rec]]、[[sasrec]] 及 Pop,用 nDCG@20。各算法在合成集上的表现趋势与真实集高度吻合。值得注意的是,MF、BPR、NeuMF、LightGCN 等依赖协同过滤的方法在合成集上整体表现更差,而 Pop、GRU4Rec、SASRec 等(聚焦序列/注意力模式)表现更好;这是因为合成数据基于推断的人格特质而非真实协同信号生成。

- **RQ3(Big Five 分布及与行为关系)**:Amazon 平台上 Big Five 分布相对均衡,Extraversion 最突出;Neuroticism 平均分显著低于其它特质,即留评论的用户情绪更稳定。极端购买体验的用户更倾向留评论并表达情绪(与较低 Neuroticism 相关)。

- **RQ4(哪些特质受推荐算法青睐)**:以 [[gru4rec]] 为推荐器,选取 nDCG@20 前 10%/后 10% 的用户。高 Agreeableness 与高 Conscientiousness 的用户获得更好推荐;但高 Openness 用户准确率反而更低——开放性高的用户更愿尝试新体验、偏离既有行为模式,干扰算法推断。

## 在本 wiki 中的位置

本文属于 LLM 驱动的[[user-simulation]]与[[recommendation-simulator]]方向,与 [[recagent]]、[[recsim]]、[[lusifer]] 等模拟器形成对照,但独特之处在于引入 Big Five 人格特质作为生成行为的心理学锚点。它服务于 [[recommender-systems|recommender-system]] 的离线[[evaluation]],并与序列推荐模型([[sasrec]]、[[gru4rec]])及协同过滤模型([[matrix-factorization]]、[[bpr]]、[[lightgcn]])的对比评估相关。作者来自 RMIT,与其前作 NEST、面向 confounding 与推荐去偏的工作([[debiasing]])一脉相承。
