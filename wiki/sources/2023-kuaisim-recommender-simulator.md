---
type: source
subtype: paper
tags:
  - recommender-system
  - user-simulation
  - reinforcement-learning
  - benchmark
  - user-retention
created: 2026-05-29
updated: 2026-05-29
arxiv: "2309.12645"
raw: raw/2309.12645.pdf
authors:
  - Kesen Zhao
  - Shuchang Liu
  - Qingpeng Cai
  - Xiangyu Zhao
  - Ziru Liu
  - Dong Zheng
  - Peng Jiang
  - Kun Gai
year: 2023
---

# KuaiSim: A Comprehensive Simulator for Recommender Systems

KuaiSim 是一个面向 [[recommender-system]] 的综合性 [[user-simulation]] 环境,提供 multi-behavior 与 cross-session 的用户反馈,统一支持 request 级 list-wise 推荐、whole-session 级 sequential 推荐与 cross-session 级 retention 优化三类任务,并配套 baseline 与 benchmark。

## 问题

基于 [[reinforcement-learning]] 的 [[recommender-system]] 能学到最优推荐策略、最大化长期用户回报,但直接在线上部署 RL 模型并通过 A/B test 产生真实数据代价高、风险大(未训练好的模型会损害用户体验)。User simulator 作为 pre-online 验证手段应运而生,但现有模拟器存在若干局限:

1. **反馈过于简化**:多数只模拟单一即时反馈,而真实 web 服务中用户反馈是 multi-behavior 的(短视频场景下用户可 click、like、forward、download)。
2. **缺乏长期/延迟行为建模**:用户可能离开 app 后再回来,产生 leave 信号与 retention 信号,而 retention 与 DAU(daily active users)这一核心指标紧密相关,却被严重低估。
3. **场景受限**:许多 rule-based 模拟器([[recsim]])为特定场景定制,难以迁移。
4. **分布不一致**:近期模拟器([[rl4rs]]、Virtual-Taobao)虽用 log data 预训练,但在线交互时还需额外用 user generator 采样用户,放大了模拟环境与真实分布的不一致。
5. **缺乏对模拟器本身的评估**:如何确认在模拟器上更优的 RL 方法在真实环境也更优,研究仍有限。

## 方法

KuaiSim 把 RL 推荐建模为 recommender system(agent)与用户(environment)之间的 multi-behavior、cross-session 序列交互。在第 t 步,系统根据静态用户画像 U 和动态历史 H 生成大小为 K 的推荐列表 A_t,用户返回三类反馈:即时反馈 Y^(I)(b 种行为信号)、leave 信号 Y^(L)∈{0,1}、return time / retention 信号 Y^(R)。据此定义三个层次的任务:

- **Request level**:单次请求的 [[listwise-recommendation]] 优化,关注列表内 item 间相关性;传统 Recall/NDCG 在此失效,需模拟器补位。
- **Whole-session level**:把整个 session 视为标准 [[markov-decision-process]],优化整段会话的长期表现。
- **Cross-session level**:引入 user return time 信号,优化 retention(降低用户回访间隔),直接关联 DAU,但不确定性与延迟使其极具挑战。

模拟器由三个反馈生成模块构成(Algorithm 1):

- **User immediate response module (UIRM)**:用 Transformer 编码历史得到 ground-truth user state,输出各行为的 likelihood;引入 item_correlation 函数抑制同列表中高相关 item 的正向行为(模拟用户对多样性的需求)。需在 log data 上用 binary cross-entropy 预训练。
- **User leave module**:维护 user temper(耐心)因子,每步用 UIRM 推断的即时反馈计算 immediate reward,temper 随交互下降,低于阈值则产生 leave 信号;不满意的推荐使 temper 下降更快。
- **User retention module**:预测 next-day return probability p_ret(由 global retention bias、personal retention bias、response retention bias 组合而成),return time 服从几何分布;return day 限制在 {1,...,D},D=10(超过 10 天回访占比近乎为零)。

数据上,KuaiSim 基于 [[kuairand]] 的无偏序列数据集 [[kuairand-pure]] 构建(在随机曝光 item 上采集),并通过迁移到 [[movielens-1m]] 展示灵活性。

## 结果

数据集统计(Table 2):KuaiRand-Pure 含 27077 用户、7551 item、1,436,609 次交互、246738 个 session,密度 0.70%;ML-1m 含 6,400 用户、3,706 item、1,000,208 次交互。KuaiRand 用 6 个正向信号(click、view time、like、comment、follow、forward)与负向信号 hate。

- **与现有模拟器对比(Table 1)**:KuaiSim 是唯一同时满足"真实数据集 + request/whole-session/cross-session 三类任务"的模拟器(RecoGym、[[recsim]] 仅 whole-session;[[rl4rs]]、Virtual-Taobao 不覆盖 cross-session)。
- **Request level(Table 3)**:[[matrix-factorization]] 类 CF 平均 L-reward 最高 2.253;ListCVAE 在 max L-reward(4.042)与 ILD 多样性(0.565)、Coverage(446.100)最佳;PRM 表现最差。
- **Whole-session level(Table 4)**:HAC 在多数长期指标上最优(Depth 14.98、Average reward 0.6895、Total reward 10.1742、ILD 0.9874);A2C 最差且最不稳定;[[ddpg]]、[[td3]] 次之。
- **Cross-session level(Table 5)**:[[reinforcement-learning]] 的 RLUR 为 SOTA,Return day 3.481(越低越好)、User retention 0.607(越高越好),优于 TD3(3.556 / 0.581)与 CEM(3.573 / 0.572)。
- **模拟器定量对比(Table 6)**:用 DDPG 在不同模拟器上训练 agent,KuaiSim 在 Depth(14.86)、Average reward(0.679)、Total reward(10.081)、AUC(0.7234)上均显著优于 RL4RS、RecoGym、RecSim、VirtualTaobao(p<0.05)。
- **数据迁移(Table 7)**:在 ML-1m 上 HAC 仍在多数指标领先(Total reward 7.5791),验证 KuaiSim 适配不同数据集的能力。
- **参数分析(Figure 3)**:max time step 与 slate size 均在设为 20 时最优。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 的 [[user-simulation]] 与 [[offline-rl]] 评估方向,与 [[recsim]]、[[rl4rs]] 等模拟器形成对照,首次统一覆盖 request/whole-session/cross-session 三层任务并强调 [[user-retention]] 优化。其用到的 [[kuairand]]/[[kuairand-pure]] 数据集、HAC/[[td3]]/[[ddpg]] 等 RL 方法,以及对 [[listwise-recommendation]] 与 [[sequential-recommendation]] 的建模,可与 wiki 中相关 RL4Rec 工作互相参照。
