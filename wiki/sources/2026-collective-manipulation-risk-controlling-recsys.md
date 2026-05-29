---
type: source
subtype: paper
tags: [recommender-system, conformal-risk-control, algorithmic-collective-action, adversarial-attack, content-moderation, ai-safety, ndcg, kuairand]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.28476
raw: raw/2603.28476.pdf
authors: [Giovanni De Toni, Cristian Consonni, Erasmo Purificato, Emilia Gomez, Bruno Lepri]
year: 2026
---

# With a Little Help From My Friends: Collective Manipulation in Risk-Controlling Recommender Systems

这篇论文对"risk-controlling recommender systems"(用 [[conformal-risk-control]] + 二元 "Not Interested" 负反馈来可证明地约束不想要内容曝光的推荐系统)做了一次部署前审计,证明仅占 1% 的协同对抗用户即可让非对抗用户的 [[ndcg]] 最多下降 20%,并提出把风险保证从群体级改为个体级的缓解方案。

## 问题

[[recommender-system]] 已是在线信息的"守门人",用户越来越多地组织协同行动(collective action),利用点赞、评分、"Not Interested" 等平台 affordance 去操控算法结果。其中一类新系统——risk-controlling recommender systems([[conformal-risk-control]] 之上构建,见 De Toni et al. 的原工作)——直接用用户的二元负反馈("Not Interested")在期望意义上约束不想要内容(unwanted content)的曝光频率,提供 distribution-free、model-free 的形式化保证。核心研究问题:如果一群用户协同地、策略性地使用 "Not Interested" 来改变推荐系统行为会发生什么?即这种把用户反馈直接接入安全保证的设计,是否反而打开了被协同对抗操控([[adversarial-robustness]] / 类似 shilling attack / crowdturfing)的新杠杆。

## 方法

- **形式化**:采用两阶段推荐架构。ranker 给出相关性序;risk predictor r(i,u) 给每个 item 一个风险分(被用户标 "Not Interested" 的概率)。过滤条件为 1 − r(i,u) ≥ λ,阈值 λ 在一个校准集(calibration set,Q 个 user-item 交互)上选取,使期望风险 ≤ 平台设定的目标水平 α。被过滤位置用 "repeated safe items" 回填以维持推荐集大小 k。
- **建模协同攻击**:假设校准集中有 K 个对抗用户(比例 β = K/Q),采用弱协同模型——共享同一目标与动作(对一组预设 item 标记 "Not Interested"),不需细粒度同步,既覆盖去中心化运动也覆盖集中编排(如 crowdturfing 雇佣)。攻击者只用平台允许的正常 affordance,不注入伪造/投毒数据(区别于经典 shilling / profile-injection attack)。
- **理论结果(Theorem 1 与 Corollary 2)**:在 data exchangeability 下,非对抗用户的期望风险上界为 max{0, α − K/(Q+1)·r^adv_λ}。即每个对抗用户消耗一部分"风险预算",使针对普通用户的风险下降被推向零;效应随对抗用户数线性增长。要持续有效,攻击者必须在阈值升高时仍维持高 empirical adversarial risk r^adv_λ。
- **上报策略**:LowRisk(γ)(白盒,优先举报低风险 item,worst-case);以及三种基于可观测代理的现实策略——Likes(按点赞数)、TopRanker(按排名位置)、Tag(g)(按 item 标签/类别),外加 Random 基线。γ 为每个用户举报 item 的比例。
- **缓解**:把风险保证从 population-level(全局单一阈值)改为 individual-level(每用户单独校准阈值),以隔离对抗反馈对其他用户的污染。

## 结果

- **小群体大破坏**:仅约 40 个对抗用户(占用户总体约 1%)、每人最多举报其遇到 item 的 1%,即可在最坏情况下使标准 [[ndcg]] 下降最多 20%。
- **不对称性**:对风险保证的改变随协同用户数线性增长,但即使很小的群体也能让"降低非对抗用户期望风险"变得困难得多(disproportionate degradation,Figure 2 中 Reduction 值可远大于 1)。
- **数据集与模型**:实验用 [[kuairand]] 数据集(来自 [[kuaishou]] 的真实 user-item 交互,论文称其是唯一公开含真实 "Not Interested" 反馈的数据集;该反馈极稀疏,平均每用户约 0.002% 举报率),沿用原工作的两阶段架构与预训练 LightGCL recommender;评测 nDCG@20 与 [[recall]]@20。
- **RQ1**:LowRisk 策略一致地维持最高 empirical risk(即便只举报 0.1% 的 item);Tag 策略具竞争力但需多约两个数量级的举报量;Likes 与 TopRanker 接近 Random,因为高排名 item 未必低风险、点赞也只是 unwantedness 的不完美代理。关键是"举报对的 item"而非"举报更多"。
- **RQ3 / 局限**:对抗者无法选择性压制某一目标 item 组的曝光,因为底层风险控制过程对组成员身份(group membership)是 agnostic 的(但若底层推荐器本身有组偏见,仍可能产生 disparate impact)。
- **缓解有效性**:用 individual-level 阈值校准能成功削弱协同对抗行为的影响,同时为个体维持个性化安全。
- 论文将该工作定位为面向真实部署的 pre-deployment audit,并呼应 EU Digital Services Act(DSA Article 34(2))对系统性风险评估、应对蓄意/协同操控的要求。代码、数据与脚本已开源(GitHub: geektoni/collective-action-recsys)。

## 在本 wiki 中的位置

本文处在 [[recommender-system]] 安全、[[adversarial-robustness]] 与 [[ai-safety]] 的交叉点,核心机制是 [[conformal-risk-control]] 在推荐过滤中的应用,以及 algorithmic collective action 的对抗变体(与经典 shilling / profile-injection attack、crowdturfing 相关但只用合法 affordance)。它与 [[content-creator-incentive]]、[[provider-fairness]]、[[popularity-bias]] 等"推荐系统社会影响"议题相邻,评测指标用 [[ndcg]] 与 [[recall]],数据来自 [[kuairand]] / [[kuaishou]]。机构上来自 Fondazione Bruno Kessler 与 European Commission Joint Research Centre,属于 [[responsible-ai]] / 算法审计方向。
