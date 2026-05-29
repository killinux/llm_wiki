---
type: source
subtype: paper
tags: [recommender-systems, exploration, exposure-bias, debiasing, off-policy-evaluation, cost-aware, candidate-generation, streaming-tv]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2512.14733
raw: raw/2512.14733.pdf
authors: [Qiang Chen, Venkatesh Ganapati Hegde]
year: 2025
---

本文提出一种"reach 与 cost 感知"的内容级探索(exploration)部署方法:不改排序逻辑,而是把随机化内容放进一个根据用户滚动深度(scroll-depth)触发、经验上低成本高触达的专用 UI 容器("Something Completely Different"行),从而在不损害短期业务指标的前提下大规模收集无偏(unbiased)交互数据,并把这些数据回灌到候选生成阶段提升长期推荐质量。

## 问题

推荐系统从用户交互(播放、停留、观看时长)中学习,但这些反馈被系统已经曝光的内容所塑造,导致 feedback loop 与 presentation bias(曝光偏差):内容可见性而非内在相关性主导了交互。探索(exploration)是缓解此偏差、提升长期推荐质量的关键,但通常会损害短期业务指标——尤其在以遥控器为主的流媒体电视(remote-first streaming TV)环境中,用户被动滚动、期望即时相关、几乎不用搜索、也很少导航到次级界面,因此在首屏显眼位置或对错误人群引入随机化内容会显著降低短期参与度。

已有方法的不足:算法级探索(epsilon-greedy、UCB、Thompson Sampling、active learning)在模型层操作,抽象掉了 UI 因素、行为模式与平台业务约束;UI 级干预(YouTube 固定位探索槽、"New to You"标签、Netflix "Top 10"行)依赖静态位置、启发式摆放或用户主动 opt-in,且未说明探索位置如何选择、也未就用户曝光/参与度权衡做评估。核心缺口:不只是"探索什么内容",而是"在 UI 的哪里、如何"以行为对齐、成本敏感、可扩展的方式交付探索。

## 方法

作者把探索建模为"交付(delivery)"问题而非排序问题,在不修改排序逻辑、不建模用户意图的前提下,把探索内容的出现条件绑定到 session 上下文(用 scroll-depth 作为"用户对新颖内容接受度"的代理):用户滚得越深,越脱离顶部排序结果,越愿意接受新颖内容。

- **成本敏感的交付策略**:用两个经验因子评估每一行的机会成本(opportunity cost)——Reach(该行可见的用户 session 比例)与 User Engagement Contribution(该行贡献的用户参与度)。选取满足"约贡献 1% 首页参与度"且"约在 10% 的 session 中可见"的行作为放置位置(低风险、高触达)。Fig. 1 显示首页各行的归一化 reach 从第 1 行 100% 快速衰减(第 2 行 64.8%、第 4 行 36.7%……第 14 行 10.5%)。
- **"Something Completely Different"(SCD)行**:一个随机化、轻度过滤的内容容器,放在成本-reach 分析定位的 scroll-depth 前沿附近,只在用户滚到该区域(被解读为脱离顶部内容的行为信号)时才出现。SCD 行不做 re-ranking 或个性化,而是从一个高质量、可参与的探索池中均匀采样,以收集 off-policy / 无偏交互信号。
- **部署护栏(guardrails)**:所有放置决策先经 A/B 测试验证才上线,要求核心指标无显著回退、信号质量正向或中性,否则移除或重新放置。
- **无偏数据的利用——Unbiased Co-Occurrence Recaller**:用从均匀曝光容器收集的交互信号,离线批处理计算物品对 (A,B) 的归一化共同参与(co-view)统计;服务时对用户最近观看的标题查表取 top-K 关联标题并聚合,作为候选生成(candidate generation)的一路召回,用于首页推荐。

训练/系统基于 Qwen2.5-VL 之外无关——本文不微调大模型,主体是 UI 部署策略与召回构建,部署于一个月活超 1 亿(100M+ MAU)的大型流媒体平台(作者来自 Tubi)。

## 结果

- **探索位置对比实验(Table I,三组 A/B)**:Control(无探索)为基线;在个性化"Recommended"行中插入随机标题(Recommended Row insertion)产生 −0.13% 参与度(p=0.431),即轻微负面;专用 SCD 行(dedicated)产生 +0.28% 参与度提升(p=0.062,刚低于常规显著性阈值)。结论:同样的随机标题,通过专用、行为触发的 UI 行交付比嵌入核心个性化行更受用户接受,说明交付机制(delivery mechanism)对用户反应起关键作用。
- **无偏数据的分布特性(Fig. 3 + Gini)**:对 top 500 节目的归一化流行度分布,无偏推荐列表的 Gini 系数为 **0.203**,而整体(有偏)流行度列表为 **0.494**,定量证明无偏方法对内容的曝光更均衡、popularity bias 更低。
- **Unbiased Co-Occurrence Recaller 的线上收益(Table II)**:把该无偏召回器接入候选生成后,关键用户参与度指标提升 **+0.94%**(p<0.001),在百万级活跃用户规模上属可观增益,并可转化为下游广告收入等业务收益,验证了无偏信号回灌排序栈的可操作性与价值。

未来工作:用更动态的模型驱动信号(如反复右滑、连续多次观看)替代固定 scroll-depth 来推断探索就绪度;把探索从节目级扩展到 genre/演员/主题等细粒度属性;用收集到的无偏数据训练更公平、更鲁棒的推荐模型并支持离线评估。

## 在本 wiki 中的位置

本文属于 [[recommender-systems]] 中的 exploration / 无偏数据收集方向,核心动机是缓解 [[exposure-bias]](presentation bias)与 feedback loop,从而服务 [[debiasing]] 与 [[off-policy-evaluation]]。它在相关工作中对比了算法级探索方法 [[contextual-bandit]]、[[thompson-sampling]]、[[active-learning]] 与 epsilon-greedy/UCB 等,定位为 UI 级、成本敏感的互补方案;其无偏召回器服务于 [[candidate-generation]]。与 [[kuairand]] 等通过随机曝光获取 [[missing-at-random]] 数据的工作思路相通,但本文强调"在哪里/如何交付探索"的部署工程层面,部署平台为 [[tubi]] 旗下流媒体电视产品。
