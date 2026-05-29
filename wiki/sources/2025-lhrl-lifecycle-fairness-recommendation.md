---
type: source
subtype: paper
tags: [recommender-system, fairness, interactive-recommendation, hierarchical-reinforcement-learning, item-lifecycle, popularity-bias, short-video]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2511.16248
raw: raw/2511.16248.pdf
authors: [Yun Lu, Xiaoyu Shi, Hong Xie, Chongjun Xia, Zhenhui Gong, Mingsheng Shang]
year: 2025
---

一句话:本文把"物品生命周期(item lifecycle)"作为公平推荐的控制旋钮,提出分层强化学习框架 LHRL,根据短视频物品所处生命周期阶段动态调和长期公平与短期用户满意度。

## 问题

[[recommender-system|推荐系统]]中的公平性研究长期关注 [[popularity-bias|流行度偏置]]:少数热门物品垄断曝光,长尾内容被低估,而这种不公平在 [[interactive-recommendation|交互式推荐]](如 TikTok、KuaiShou 等短视频平台)中被反馈回路进一步放大。然而,绝大多数现有公平方法(无论是静态方法,还是基于 [[reinforcement-learning|RL]] 的方法,如 [[dorl|DORL]]、[[morec]] 等)都忽视了一个关键时间因素:物品生命周期。实践中物品的曝光需求会经历不同时间阶段,长尾分布(long-tail)假设并不总成立——对所有物品施加统一的公平约束,会导致曝光与需求错配:陈旧内容(decay 阶段)被过度推广,而新兴物品错失早期关键曝光窗口。

本文提出两个核心挑战:(1) 如何自动发现物品潜在的生命周期模式?(2) 如何根据生命周期阶段动态调整公平策略?

## 方法

作者首先在两个真实短视频数据集 [[kuairec|KuaiRec]] 与 [[kuairand|KuaiRand]] 上做实证分析,用 **play progress**(播放时长/视频时长)度量视频活力,发现短视频生命周期呈"压缩三阶段"模式,显著偏离经典四阶段产品生命周期(PLC)与 Gompertz 曲线:

- **Growth(成长)**:发布后播放进度快速上升;
- **Mature(成熟)**:相对稳定或缓慢下降;
- **Decline(衰退)**:陡峭加速下滑。

92.9%(KuaiRec,9524/10253)与 94.5%(KuaiRand,6400/6777)的视频在上传后 7 天内达到峰值;Kruskal–Wallis/ANOVA 检验确认三阶段间用户参与度差异显著(p < 0.001)。

在此基础上提出 **LHRL(Lifecycle-aware Hierarchical Reinforcement Learning)**,含三大模块:

1. **PhaseFormer 模块**:实时预测物品当前生命周期阶段。先用 STL(Seasonal-Trend decomposition with Loess)把 play progress 时间序列分解为趋势 $T_t$、季节 $S_t$、残差 $R_t$;再用 iTransformer 编码 $T_t$、$S_t$ 得到长程注意力表示,经 MLP + softmax 分类为 {Growth, Mature, Decline}。对历史稀疏的新物品用掩码自注意力 + 时间序列外推处理。
2. **High-level Recommendation Agent(HRA)**:基于用户状态生成公平权重 $w_{fair}$(从 MLP 参数化的多元正态分布采样)与生命周期权重 $w_{life}$;高层奖励组合点击反馈、生命周期感知奖励(用奖励系数矩阵 $\Lambda$ 关联流行度分组与阶段)与公平奖励;用 [[ppo|PPO]] 训练。
3. **Low-level Recommendation Agent(LRA)**:在 HRA 的公平/生命周期权重指导下,结合用户兴趣、物品流行度与公平权重计算最终推荐分数并 softmax 采样,奖励为即时交互反馈,同样用 PPO 优化。

这种 [[hierarchical-representation|分层]]设计将长期生态公平(高层)与短期用户参与(低层)解耦。实验在 [[kuaisim|KuaiSim]] 模拟器(最多 20 轮交互)中进行,公平用 Absolute Difference(AD)度量。

## 结果

在 KuaiRec 与 KuaiRand 上对比 11 个基线(RL 类:[[dorl|DORL]]、[[cql|CQL]]、[[bcq|BCQ]]、[[sqn|SQN]]、[[td3|TD3]]、[[ddpg|DDPG]];公平交互推荐类:MOFIR、FCPO、DNAIR、SAC4IR、HER4IF):

- **KuaiRec**:LHRL 在所有精度指标上最优,Len = 17.760,$R_{cum}$ = 15.613,相比最强基线长期用户参与提升约 10.5%、累计奖励提升 13.1%,同时 AD 仅 0.009(公平最优)。
- **KuaiRand**:$R_{cum}$ 达 12.655,较次优 HER4IF 提升 13.7%,AD 低至 0.184,公平性大幅领先。
- 表 2 汇总:LHRL 在 KuaiRec 上 Len/$R_{cum}$/AD 改进分别为 10.48% / 13.12% / 10.00%;KuaiRand 上为 10.03% / 13.74% / 16.36%。
- **消融(RQ2)**:去掉生命周期奖励(w/o L)使交互长度与累计奖励明显下降;去掉分层结构(w/o H)在约 10000 步后策略崩塌不稳定;完全扁平(w/o A)所有指标最差,证明生命周期感知与分层结构缺一不可。
- **泛化(RQ4)**:把生命周期感知奖励插入现有公平基线即插即用——SAC4IR+life 在 KuaiRec 上 $R_{cum}$ 提升 8.2%,FCPO+life 在 KuaiRand 上提升 5.7%。
- **策略分析(RQ5)**:随训练进行,LHRL 学会增加高价值 Mature 阶段物品曝光、逐步削减 Decline 物品、对 Growth 物品维持低水平稳定曝光以供探索。

代码与数据:https://github.com/luyunstar/LHRL ;KuaiRec/KuaiRand 数据集公开。

## 在本 wiki 中的位置

本页属于推荐系统中的公平性与交互式推荐方向。它把 [[item-lifecycle|物品生命周期]]作为新的控制信号,与 [[popularity-bias]]、[[matthew-effect]]、[[provider-fairness]]、[[two-sided-fairness-reranking]] 等公平概念相关;方法上属于 [[rl-based-recsys|基于 RL 的推荐]]与 [[hierarchical-representation|分层]] [[reinforcement-learning]],与 [[dorl]]、[[cirs]]、[[dorl]] 等长期推荐工作以及 [[ppo]]、[[constrained-mdp]] 等技术衔接;评测建立在 [[kuairec]]、[[kuairand]] 数据集与 [[kuaisim]] 模拟器之上,可与 [[easyrl4rec]]、[[recsim]] 等仿真评测环境对照。
