---
type: source
subtype: paper
tags:
  - recommender-system
  - reinforcement-learning
  - actor-critic
  - listwise-recommendation
  - user-modeling
created: 2026-05-29
updated: 2026-05-29
arxiv: 2401.16108
raw: raw/2401.16108.pdf
authors:
  - Xiaobei Wang
  - Shuchang Liu
  - Xueliang Wang
  - Qingpeng Cai
  - Lantao Hu
  - Han Li
  - Peng Jiang
  - Kun Gai
  - Guangming Xie
year: 2024
---

# Future Impact Decomposition in Request-level Recommendations

提出 ItemA2C 框架,在 request-level MDP 下对 list-wise reward 做 item-wise 分解,并用 actor-critic 优化每个 item 的长期未来影响,从而提升推荐的长期效果。

## 问题

工业推荐系统(尤其是短视频、新闻、博客等用户高频连续浏览的场景)出于效率考虑,policy 的动作通常是一次性推荐一个 list(大小为 K),用户状态在每个 request 后才更新,对应一个 **request-level MDP**。然而这种 list-wise 表述与用户真实的 **item-level 行为**存在根本性的不一致:用户实际上一次只关注一个 item,状态随每个 item 变化,但系统只能观测到 request 级的状态转移,item-level 的状态转移不可观测。

直接在 request-level MDP 下优化 list-wise 累积 reward(如标准 [[reinforcement-learning]] 方法)会丢失 item 特性对未来 reward 估计的信息。论文用一个例子说明:Tom 收到包含体育和纪录片两类的电影列表,对体育给出正反馈、对纪录片无反馈;若只做 list 级优化,系统无法发现 item 间差异和 Tom 对体育的偏好。因此需要一种既能在 list-wise 状态转移下优化 policy,又能利用 item-level reward 与 item-level 未来影响的 RL 方案。

## 方法

论文先把推荐问题形式化为带 item-wise reward 的 request-level MDP,做出三个核心假设:1) request-level 状态转移;2) 可观测的 item-wise reward;3) list-wise reward 是 item-wise reward 的线性聚合(R(s_t,a_t)=Σ r(s_t, i_{t,k}))。

- **Request-level [[actor-critic]] (A2C)**:作为 backbone,含一个 actor π_θ(a_t|s_t)(推荐 policy)和一个 critic V(s_t)(估计长期累积 reward),critic 走 TD loss、actor 走 advantage-boosting loss。
- **Item-wise Decomposition of A2C(ItemA2C)**:利用 R 的线性关系,把 request-level 的 target 函数信用分配到每个 item,得到 item-wise target Ψ(s_t, i_{t,k}) = r_{t,k} + (1/K)·γ(1-d)V(s_{t+1}),即每个 item 平均分担未来价值 V(s_{t+1}),actor 改为对每个 item 做优化。理论上该分解仍能在目标函数上还原 request-level A2C。
- **Future Impact Re-weighting**:平均分配 V(s_{t+1}) 无法区分 item 的不同未来影响。论文假设即时反馈更好的 item 更可能正向改善用户未来行为,提出带权重 w_{t,k} 的 target(Eq.5),权重由超参 α 控制纯 re-weighting 与纯 reward-based 策略的平衡(α=0 退化为均分,α=1 为纯 reward-based)。该策略记为 **itemA2C-W**。
- **Model-based Re-weighting(itemA2C-M)**:将启发式权重泛化为可学习的 weight model w(i_{t,k}, s_t, s_{t+1}, r_{t,k}),输入还包含 item 特征和下一状态,输出经 softmax 归一化;用**对抗学习**(目标与 actor loss 相反,Eq.7)训练,迫使 actor 在"更难"的样本上学习,从而探索更广的 re-weighting 空间。

整体框架:critic 用 TD learning(保持在 request-level),actor 用带 re-weighting 的 item-level advantage learning,weight model 用对抗学习,见 Algorithm 1。

## 结果

**离线模拟实验**:基于 KuaiSim 在两个公开数据集 [[movielens-1m]](ML1M,3706 items)和 [[kuairand]](KuaiRand1K,11643 items)上构建 session-based 模拟器,list 大小 K=6,episode 最大深度 20,batch 64 用户;reward 为点击 1.0 / 缺失 -0.2。Baseline 含 [[ppo|DDPG]]、A2C、SlateQ、Supervision、以及 SOTA 的 HAC。

- 主结果(Table 1):itemA2C-M 取得最佳综合表现,显著(p<0.05)在 KuaiRand1K 上把 total reward 提升约 **27%**、depth 提升约 **20%**;在 ML1M 上 reward 提升约 **2.3%**、depth 提升约 **1.8%**(边际,非统计显著)。ML1M 上 itemA2C-M 的 Average Total Reward 17.94 ± 0.47、Max 20.00、Min 9.79;KuaiRand 上 16.03 ± 0.53。所有 ItemA2C 变体均优于 request-level A2C,且 reward 方差更小、学习更稳定。
- list 大小实验(Table 2):K∈{1,2,4,8,16,32},所有方法性能随 K 增大而下降(印证 request-level 与 item-level 视角不一致),itemA2C-M 在不同 K 下均取得最佳,且 K>2 时持续优于 HAC。
- α 消融(Fig.7):α 在 [0.0, 2.0] 搜索,最佳设置出现在 [1.0, 1.5],验证 future impact re-weighting 的有效性;α>1.0 的"over-weighting"会负向影响。
- 权重相关性(Fig.5):itemA2C-M 学到的权重与启发式 reward-based 权重(Eq.5)呈高 cosine 相似度和正 Pearson 相关,验证 model-based 设计的合理性,但训练中逐渐发散,说明存在更优、不唯一的 re-weighting 形式。

**线上 A/B 实验**(工业级视频推荐平台,日活 100M+,部署于 refined ranking 阶段,候选 500、输出 K=6,reward 为 watch time/like/follow/collect/comment 的线性组合,Eq.9):结果均统计显著(Table 3)。ItemA2C 相对 request-level A2C:like +1.103%、follow +0.300%、collect +0.963%、comment +0.221%、watch time +0.129%;itemA2C-W(α=1) 相对 ItemA2C 进一步提升 like +0.451%、follow +0.636%、collect +0.616%、comment +0.258%(watch time 微降 0.013%,不显著)。ItemA2C 还使 DAU 提升 0.028%、次周用户留存(user retention)提升 0.016%。

## 在本 wiki 中的位置

本文是 [[reinforcement-learning]]-based [[recommender-system]] 方向的工作,聚焦 [[listwise-recommendation]] 在 [[markov-decision-process]] 下的建模不一致问题。其 backbone 是 [[actor-critic]],与 [[ppo]] 类方法及 list 表示方法 HAC 同属一脉。它强调 item-level 的长期价值估计与未来影响分解,与本 wiki 中关注 [[watch-time]]、[[user-retention]] 的快手系推荐工作([[kuairand]]、KuaiSim、[[qingpeng-cai]]、[[peng-jiang]]、[[kun-gai]] 等作者)相承接。实验数据集涉及 [[movielens-1m]] 与 [[kuairand]]。
