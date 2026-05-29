---
type: source
subtype: paper
tags:
  - recommender-system
  - interactive-recommendation
  - provider-fairness
  - popularity-bias
  - deep-reinforcement-learning
  - long-term-recommendation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2603.03094"
raw: raw/2603.03094.pdf
authors:
  - Chongjun Xia
  - Xiaoyu Shi
  - Hong Xie
  - Xianzhi Wang
  - Yun Lu
  - Mingsheng Shang
year: 2026
---

# HRL4PFG:面向交互式推荐 item-side 公平的主动引导策略

本文提出 HRL4PFG,一个分层强化学习框架,通过"主动引导"用户偏好逐步转向长尾物品,在不损害用户满意度的前提下提升交互式推荐中的 item-side 公平。

## 问题

交互式推荐系统中存在 [[popularity-bias]]:少量热门物品吸引绝大部分曝光,大量长尾物品曝光不足。已有 [[provider-fairness]]/item-side 公平方法直接把长尾物品塞进推荐结果(公平正则、re-ranking、把公平约束加进 [[reinforcement-learning]] 奖励),但这种"生硬注入"会造成推荐结果与用户偏好错位,降低长期参与度与满意度。

作者主张采用**主动引导(proactive guiding)**策略:不强行推送长尾物品,而是在交互过程中**逐步、个性化地把用户偏好引导向长尾物品**,同时保持满意度,使用户偏好分布从长尾形态平滑过渡到更均衡的形态。实现这一策略面临三个挑战:(1) 用户偏好随交互动态演化,静态/规则方法难以适配;(2) 随机选长尾物品会推荐低质内容、损害整体效果;(3) 引导偏好与保持满意度之间难以权衡。

## 方法

HRL4PFG([[deep-reinforcement-learning]] 分层框架,基于 [[actor-critic]])把引导过程分为两个阶段:

- **Macro-learning(高层智能体 HRA)**:由 high-level actor 与 critic 组成。high-level state $s^h_t$ 编码最近 N 次交互,经 embedding 后用 self-attention 得到状态表示。high-level actor 输出一个高斯分布,采样出 **fairness-guided target $g_t$**(一个"虚拟长尾物品"),用于在接下来的 M 步引导用户偏好。为防止采样的 target 偏离真实物品空间太远,引入约束 $\|g_t - v_{center}\|_2 \le \max_i \|v_i - v_{center}\|_2$。高层奖励 $r^h_t$ 同时考虑推荐准确性 $r^a_j$ 与 item-side 公平奖励 $r^f_j = -\log(pop_j)$($pop_j = N_j/|U|$,即物品流行度),用权重 $\lambda_f$ 平衡。

- **Micro-learning(低层智能体 LRA)**:由 low-level actor 与 critic 组成。low-level state 同样用 attention 得到当前偏好 embedding $p_t$,再与 target $g_t$ 拼接。actor 在物品空间上输出推荐概率,但为应对海量物品空间,引入**过滤机制(filtering mechanism / Mask)**:先算每个物品与 $g_t$ 的 L2 距离,取最近的 L 个作为候选,再在候选上采样。低层奖励 $r^l_t = r^a_t + \lambda_g r^g_t$,其中引导奖励 $r^g_t = Distance(p_t, g_t) - Distance(p_{t+1}, g_t)$,鼓励偏好朝 target 移动;$\lambda_g$ 控制引导强度。两层 critic 均用 Actor-Critic 训练。

核心思想:高层生成"该把用户引向哪"的公平目标,低层在保证贴合当前偏好的同时把用户**渐进式**地引导过去(图示中 Step_t 最优是 Item 2,Step_{t+1} 偏好移动后最优变成 Item 1)。

## 结果

在基于 [[easyrl4rec]] 库搭建的交互式模拟环境上评测,使用 [[kuairec]] 与 [[kuairand]] 两个数据集(KuaiRec 训练 12530.8k / 测试 4676.5k 交互;KuaiRand 训练 1436.6k / 测试 1186.1k)。设最大交互长度 Max Len = 30 与 50,并设流行度感知退出机制:连续推荐 W 个 top-20% 流行物品则会话终止(默认 W=3)。指标:单步奖励 R_single、累积奖励 R_cum、交互长度 Len(用户满意度),以及 [[gini-coefficient|Gini Index]](越低 item-side 公平越好)。

基线包括 SQN、PG、DDPG、[[td3]]、C51、SAC4IR、DNAIR。主要结果(Table 2):

- **KuaiRec, Max Len 30**:HRL4PFG R_cum = 29.99,R_single = 1.07,Len = 27.82,Gini Index = 98.20%,均优于所有基线(如 DNAIR R_cum=17.40、Gini=99.20%;SAC4IR Len=23.39)。
- **KuaiRec, Max Len 50**:HRL4PFG R_cum = 43.37,Gini = 97.20%。
- **KuaiRand, Max Len 30**:HRL4PFG R_cum = 10.03,Len = 27.90,Gini = 95.50%(基线 Gini 多在 98%-99%)。
- HRL4PFG 在所有设置下**同时取得最高累积奖励、最长交互长度与最低 Gini Index**,说明公平提升没有以牺牲满意度为代价。

**RQ2(鲁棒性)**:在退出参数 W ∈ {2,3,4,5,6}(W 越大对公平要求越低)下,HRL4PFG 仍持续最优。

**消融(RQ3,Max Len 30, W=3)**:HRL4PFG-wo-hie(去掉分层、只留低层)表现最差,说明分层必要;HRL4PFG-wo-tc(去掉对 target 的约束 Eq.6)与 HRL4PFG-wo-fm(去掉过滤机制)均劣于完整版,说明 target 约束与过滤机制都有正向贡献。

**超参(RQ4)**:$\lambda_g$ 增大时准确性与公平先升后降,$\lambda_g = 0.1$ 最佳;高层更新间隔 $M$ 在 $M=3$ 时最优(太短缺乏前瞻、太长目标过易达成而失去引导力)。

**局限/未来工作**:扩展到 demographic fairness、纳入更丰富用户行为、开展真实场景研究。

## 在本 wiki 中的位置

本文处于 [[recommender-system]] 的 [[provider-fairness]]/item-side 公平与 [[interactive-recommendation]] 交叉,用 [[deep-reinforcement-learning]] 的 [[hierarchical-representation|分层]] [[actor-critic]] 实现。与直接注入长尾物品的公平方法(re-ranking、公平正则、把约束加进 RL)不同,它属于 [[proactive-recommendation|主动推荐]] 思路——渐进引导用户偏好。评测沿用 [[easyrl4rec]] + [[kuairec]]/[[kuairand]] 的 [[rl-based-recsys]] 标准设置,公平用 [[gini-coefficient|Gini Index]] 度量,可与 [[long-term-recommendation]]、[[minimum-exposure-guarantee]]、[[matthew-effect]] 等条目互参。
