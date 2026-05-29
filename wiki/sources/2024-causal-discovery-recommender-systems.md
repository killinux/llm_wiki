---
type: source
subtype: paper
tags:
  - causal-discovery
  - recommender-systems
  - causal-inference
  - structure-learning
created: 2026-05-29
updated: 2026-05-29
arxiv: 2409.10271
raw: raw/2409.10271.pdf
authors:
  - Emanuele Cavenaghi
  - Fabio Stella
  - Markus Zanker
year: 2024
---

# Causal Discovery in Recommender Systems: Example and Discussion

本文以一个示例演示如何用 [[causal-discovery]](因果发现)从 [[recommender-systems]] 的观测数据中学习因果图(Causal Graph, CG),并结合先验知识讨论结果:学到的因果图显示只有少数几个变量真正影响所分析的反馈信号。

## 问题

[[causal-inference]] 在 AI 与机器学习社区日益受到关注,并被引入 [[recommender-systems]](RS)。因果图(Causal Graph / CG)能以图形化、人类可读的方式建模因素之间的因果关系,从而可用观测数据估计相当于 causal estimand 的 statistical estimand(无需受控实验)。然而,RS 领域很少有工作真正去**从数据中学习**一个因果图——手工构造的 CG 只编码了人对问题的认知,而没有利用数据中蕴含的信息。本文针对这一空白,尝试结合先验知识与观测数据来学习 RS 的因果图。

## 方法

基于开源数据集 [[kuairand]](具体为 [[kuairand-pure]],含 1,186,059 条交互、27,285 名被随机推荐视频的用户、30 个用户特征、62 个物品特征、12 个反馈信号),作者执行五步因果发现流程:

- **Remove features**:移除与目标无关的特征(交互日期/时间)、太稀疏的反馈信号,以及加密的(无语义)用户特征和 music ID。
- **Discretize features**:对特征离散化,因为所用结构学习算法只能处理离散数据;采用作者建议的离散化版本,并按语义合并类别以尽量少丢信息。
- **Build prior knowledge**:用 tiers(分层)方式注入先验——定义五个层级((i) 用户特征、(ii) 上下文特征 tab、(iii) 物品特征、(iv) 物品统计、(v) 反馈信号),低层节点不能成为高层节点的原因;也支持 forbidden/required edges。
- **Structure Learning**:用 bnlearn 中的 Hill-Climbing(HC)爬山算法搜索 CG 空间,以 [[bayesian-information-criterion]](BIC)作为评分函数(consistent scoring criterion)。
- **Average Causal Graph**:用 HC 学习 100 个 CG,只保留在至少 90% 的 CG 中出现的边,平均得到单一 CG。

随后用 [[markov-blanket]](Markov Blanket)将完整 CG 限制到反馈信号节点的相关子图进行分析。

## 结果

- 学到的完整 SCM(structural causal model)中,**只有极少数变量真正影响反馈信号**;根据反馈信号的 Markov blanket 子图,影响用户反馈的相关物品特征主要只有 **video duration(视频时长)** 和 **upload type(上传类型)** 两个,其余物品特征基本无关。
- 用户特征几乎只对 is_hate 反馈相关,且因可用用户特征大多被加密,可解释性受限。
- 这一结果与机器学习/RS 领域“纳入越来越多变量、构建越来越大模型”的趋势相反:作者认为大多数变量对决策无关、只贡献噪声,推荐决策应只考虑少数关键变量。
- 作者强调因果图的正确性无法由自动化流程保证,必须由领域专家结合知识与实验共同验证(引用 [[judea-pearl]] 关于“假设性共识”的论述),并指出需要更多数据,以及当前可用特征往往未捕捉推荐效果的关键因素。

## 在本 wiki 中的位置

本文连接 [[causal-inference]] 与 [[recommender-systems]] 两条主线,提供了一个把 [[causal-discovery]]/结构学习落地到真实 RS 数据集([[kuairand]])的具体示例。它与 wiki 中关于 [[debiasing]]、[[recommender-systems]] 因果建模的工作互补,并对“特征越多越好”的建模范式提出反思。
