---
type: source
subtype: paper
tags: [user-simulation, recommender-system, llm-for-recommendation, reinforcement-learning, llm-agent]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2412.16984
raw: raw/2412.16984.pdf
authors: [Zijian Zhang, Shuchang Liu, Ziru Liu, Rui Zhong, Qingpeng Cai, Xiangyu Zhao, Chunxu Zhang, Qidong Liu, Peng Jiang]
year: 2024
---

# LLM-Powered User Simulator for Recommender System

用 LLM 显式建模用户偏好逻辑、蒸馏用户情感,并与统计模型集成,构建可解释、低幻觉的用户模拟器,为基于 [[reinforcement-learning]] 的 [[recommender-systems|recommender-system]] 提供高保真训练数据。

## 问题

基于 RL 的推荐系统需要在线交互训练,但真实在线用户数据存在采集成本高、隐私顾虑、采集慢等问题,因此 [[user-simulation]] 成为加速评估与迭代的关键。现有用户模拟器有两个主要缺陷:

- **偏好建模不透明**:VirtualTaobao 用 GAN、KuaiSim 用离线 transformer 来模拟用户响应,均未**显式**建模用户偏好,决策过程黑盒、不可解释。
- **缺乏保真度评估框架**:难以评估模拟交互与真实用户行为的一致性。

而直接用 LLM 推断用户交互(如 [[agentcf]]/Agent4Rec、SUBER)又面临两大障碍:训练时频繁调用 LLM 的**计算成本**高,以及 LLM [[hallucination]] 带来的错误推断。

## 方法

论文首先提炼出用户与推荐物品交互的显式逻辑:用户对一个物品的判断分为"它**是什么**(what,识别 genre/特征)"和"它与我过往偏好**有多契合**(how)"两步(图 1)。据此设计了一个**集成模型**,把 LLM 用于**离线**分析而非在线推断,从而规避计算成本与幻觉。

**物品描述收集(用 LLM,离线)**

- **客观描述 D_obj**:用 LLM 结合物品的 name/attributes/categories,生成 pros/cons 及对应 evidence 与 keywords,提取正面关键词集 D_pos^obj 与负面 D_neg^obj。采用 [[chain-of-thought]] 引导 LLM 先找出具体理由再总结为关键词,并要求附 evidence 以降低幻觉。
- **主观描述 D_sub**:基于用户评论(comments),用 LLM 提取代表喜欢/不喜欢倾向的关键词 D_pos^sub、D_neg^sub。
- 合并得 D_pos = D_pos^obj ∪ D_pos^sub,D_neg 同理,并过滤过于常见/罕见的关键词。

**集成模拟(三个基模型,在线推断时不调用 LLM)**

- **关键词匹配模型 f_mat(逻辑)**:在与候选物品 i_c 同类别的历史交互中,分出喜欢集 I_pos(评分=1)与不喜欢集 I_neg(评分=0),统计候选物品 pros 关键词与历史喜欢物品 pros 的重叠度 α_pos,以及 cons 重叠度 α_neg;α_pos > α_neg 输出 1,相等则随机,否则 0。
- **相似度计算模型 f_sim(逻辑)**:用 BERT 将关键词嵌入语义空间,平均池化得 E_pos/E_neg,以余弦相似度比较候选物品与历史正/负子集的接近度 β_pos、β_neg,同样按大小输出。
- **统计模型 f_sta**:用 [[sasrec]](Kang & McAuley 2018)在用户历史交互上预训练,推断对候选物品的参与度,提供协同过滤式的回退与正则。
- **集成**:最终交互推断 y_c 由三者共识决定。

**MDP 与奖励**:把 RL 推荐建模为 [[markov-decision-process]],推荐系统为 agent,用户模拟器给出奖励。奖励函数 R(s, i_c, s') = 1 当 f_mat + f_sim + f_sta ≥ 2,否则 0(三基模型多数投票)。

LLM 使用 [[chatglm]] ChatGLM-6B。

## 结果

**数据集**:5 个公开数据集,跨 POI/音乐/游戏/电影/动漫领域——[[yelp-dataset]]、Amazon Music、Amazon Games、Amazon Movie、Anime;评分 ≥3 记为 1,<3 记为 0。规模从约 16 万到 611 万 instances,稀疏度 97.80%–99.99%。

**RL 算法对比(表 2)**:在模拟器上训练 [[a2c]]、[[dqn]]、[[ppo]]、[[trpo]] 四种 RL 算法,报告平均奖励/总奖励/Top-10 中喜欢物品比例(Liking%)。[[dqn]] 在多数数据集上表现最好(离散动作空间优势),例如 Yelp 上 DQN 平均奖励 27.56、总奖励 330.98、Liking% 49.43;所有算法都呈现良好的 liking 比例,说明模拟器能提供一致稳定的训练环境。

**与现有模拟器对比(表 6)**:在 Yelp 上对比 SUBER 与 KuaiSim,本方法在 A.Rwd 27.56、T.Rwd 330.98、AUC 0.674 上均最优;推断时间 0.76s,介于 SUBER(2.42s)与 KuaiSim(0.53s)之间——相比 LLM-based 的 SUBER 大幅提速,精度高于二者。

**案例研究(表 3/4)**:展示 Yelp 上 DQN 的推荐推断过程,逻辑模型对带新 genre 的物品(如 i_c^{t+1})匹配度下降时,统计模型 f_sta 作为关键回退保证推断准确。

**局限**:当前只推断二元的 like/dislike;未来将加入 duration、rating、retention 等更丰富的交互信号。

## 在本 wiki 中的位置

本文属于 [[user-simulation]] 与 [[llm-for-recommendation]] 的交叉,与 [[recsim]]、RecGym、VirtualTaobao、[[lusifer]] 等 [[recommendation-simulator]] 同属一脉,但区别于纯统计/GAN 模拟器(不可解释)与纯 LLM 模拟器([[agentcf]]/Agent4Rec、SUBER,成本高且易幻觉),其核心创新是把 LLM 限定在**离线**关键词蒸馏、在线用 逻辑+统计 集成推断。可与 [[interactive-recommendation]]、[[rl-based-recsys]]、[[long-term-recommendation]] 等条目互参。作者来自 [[kuaishou]](Kuaishou Technology)及相关高校,与 [[kuairec]]/[[kuairand]] 等快手数据集生态相关。
