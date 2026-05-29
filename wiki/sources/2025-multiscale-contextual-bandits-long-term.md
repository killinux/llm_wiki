---
type: source
subtype: paper
tags: [contextual-bandit, off-policy-learning, long-term-recommendation, user-retention, pac-bayes, multi-objective, recommender-system, conversational-system]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2503.17674
raw: raw/2503.17674.pdf
authors: [Richa Rastogi, Yuta Saito, Thorsten Joachims]
year: 2025
---

# MultiScale Contextual Bandits for Long Term Objectives

提出 MultiScale Policy Learning 框架与其实例化算法 MSBL,用分层的 off-policy [[contextual-bandit]] 在多个相互依赖的时间尺度上协调短期反馈(点击/参与)与长期目标(用户留存/订阅续费),让低尺度的丰富数据作为高尺度稀疏数据的先验,从而更快地为长期目标优化策略。

## 问题

许多交互式 AI 系统([[recommender-systems|recommender-system]]、对话系统)依赖大量收集到的**短期反馈**(点击、参与度)来训练,但过度优化短期反馈不一定能达成期望的**长期目标**([[user-retention]]、订阅续费),反而可能导致 reward hacking、用户操纵、clickbait/有毒内容等问题。

核心障碍在于**时间尺度的脱节(disconnect in timescales)**:短期干预(如排序)发生在快时间尺度,而长期反馈(如每月续费)发生在慢时间尺度且更稀疏。直接用 [[markov-decision-process]] / [[reinforcement-learning]] 建模序列依赖在实践中受困于巨大状态空间、信用分配(credit-assignment)和长期反馈稀疏,难以直接应用。本文聚焦 contextual bandit 设定来解决这一脱节。

## 方法

**MultiScale Policy Framework(多尺度策略框架)**:观察到 AI 系统在不同时间尺度上观测到不同反馈,作者把上下文与策略空间在每个层级上做分解。以两层为例,微观层(micro,快尺度 t1)观测短期奖励 r^L1(如点击),宏观层(macro,慢尺度 t2)观测长期奖励 r^L2(如周回报率/续费)。

- **PAC-Bayesian 动机**:用 [[pac-bayes]] generalization bound 论证,只要后验 Q 与先验 P 的 KL 散度小,学习宏观策略所需样本数就少。把微观层学到的最优策略 π̂^L1 构造成宏观层的**数据相关的分层先验** P^L1(centered on π̂^L1),宏观层所需训练样本的节省正比于参数空间中的 Mahalanobis 距离。文中数值例子:θ∈R^50 时,若 49 个参数已在微观层学好、宏观仅需调 1 个参数,可节省约 98% 训练样本(把收集宏观数据从"数年"降到"数周")。
- **多尺度上下文/策略分解**:上下文 p(x)=p(x^L2)·p(x^L1|x^L2);策略空间 Π=Π^L1·Π^L2。宏观动作 a^L2 对应一个微观策略 π_{a^L2}^L1,即宏观动作空间 A^L2 同构于一族在低层学到的策略 Π̂^L1。
- **学习一族微观策略**的两种构造:(1) **Policy Modification**:先用 Eq.(2) 学单一微观策略 π̂^L1,每个 a^L2 作为对其的扰动(如 LLM 的 decoding 策略、对推荐排序加 boost);(2) **Feedback Modification**:每个 a^L2 是把向量反馈(点击/点赞/购买/加购)组合成标量损失的不同函数,据此学不同微观策略。
- **学习宏观策略**:固定 Π̂^L1 后,用 off-policy policy-gradient,以 [[inverse-propensity-scoring]] 加权的经验平均估计宏观奖励 V^L2(Eq.(7)),可用 SGD 训练。
- **MSBL(MultiScale Off-Policy Bandit Learning)**(Algorithm 1):自底向上递归——收集微观 logged 数据 → 学微观策略族 → 收集宏观 logged 数据 → 学宏观策略;部署时自顶向下推理。框架自然推广到 3 层及更多层。

## 结果

在三个场景上验证(均报告 5 个随机种子):

- **多轮对话(2 层)**:基于 [[anthropic]] Helpful Assistant 数据,微观层是 LLM 策略,宏观层学 harmless/helpful 偏好权重向量 a^L2(feedback modification),模拟 5 轮 prompt-response。即使奖励高度非线性([[llama-3]] Llama-3-70b 评估),MSBL 在长期(多轮用户满意度)上取得最佳长期回报,而仅优化单轮响应会因 harm-inducing 回答损害整轮对话。
- **会话式推荐系统(3 层)**:模拟 1500 训练用户、300 测试用户;微观层用预训练 LLM 策略生成 cuisine 建议,宏观层选 decoding temperature a^L2∈{0.0,0.2,0.4,0.6,0.8,1.0}(policy modification),第三层为不同用户组学 feedback modification。结果:greedy decoding(a1^L2)短期最优但长期回报低;Level 3 opt.(MSBL 3 层)取得最佳长期回报且对中/短期牺牲很小;随机干预严格落在 Level 3 策略内部。
- **推荐系统(KuaiRand,真实数据)**:使用 [[kuairand]] 数据集模拟两层短/长期反馈;训练集 7,829、测试随机选 1,174 用户,每用户 T=5 次交互,transformer 模型预测排序分数,微观奖励为人均平均点击;宏观干预 a^L2 为对排序分数的 boost(policy modification)。在用户/物品组数量 ∈{2,3,4,5} 时,MSBL 在 top-10 排序下均保持高长期回报率,优于所有基线,仅对短期点击有少量牺牲,对微观策略扰动和排序大小变化稳健。

基线对比:单阶段策略、随机均匀干预 baseline、oracle skyline。整体显示**宏观层学习是必要的**,且 MSBL 能在长期奖励高度非线性时仍有效优化长期目标。

**局限**:公开领域缺乏真实多尺度数据集;聚焦 contextual bandit,向 stateful 策略的扩展留作未来工作。

## 在本 wiki 中的位置

本文连接 [[off-policy-evaluation]] / [[inverse-propensity-scoring]] / [[doubly-robust]] 的离线 bandit 学习传统与 [[long-term-recommendation]]、[[user-retention]] 的研究线,提供一个不依赖完整 [[reinforcement-learning]] / [[markov-decision-process]] 的、用分层先验弥合短期与长期反馈时间尺度脱节的框架。它与 [[reward-design]]、[[multi-task-learning]]、provider/multi-stakeholder 优化相关,并把 [[large-language-models]] 的 decoding 控制纳入宏观动作空间,与 [[rlhf]] 中的 helpful/harmless 权衡呼应。作者来自 [[cornell-university]](Thorsten Joachims、Yuta Saito 等),延续其 [[off-policy-evaluation]] / logged bandit feedback 的工作脉络。
