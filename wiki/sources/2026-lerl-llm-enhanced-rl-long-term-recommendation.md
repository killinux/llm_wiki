---
type: source
subtype: paper
tags: [interactive-recommendation, reinforcement-learning, large-language-models, filter-bubble, long-term-recommendation, hierarchical-rl]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2601.19585
raw: raw/2601.19585.pdf
authors: [Chongjun Xia, Yanchun Peng, Xianzhi Wang]
year: 2026
---

# LERL: LLM-Enhanced Reinforcement Learning for Long-Term User Satisfaction in Interactive Recommendation

LERL 是一个分层 [[interactive-recommendation]] 框架,把 [[large-language-models]] 的语义规划能力与 [[reinforcement-learning]] 的细粒度自适应结合,通过高层 LLM 规划类别、低层 RL 选物品来优化长期用户满意度并缓解 [[filter-bubble]]。

## 问题

[[interactive-recommendation]](IRS)能根据用户反馈实时调整,但常因过拟合用户短期偏好而陷入内容同质化与 [[filter-bubble]] 效应,导致用户反复接触语义相似内容、长期满意度下降。已有提升多样性的方法(belief-aware re-ranking、对回音室敏感的表示学习、diversity-aware candidate filtering)大多在静态/一次性(one-shot)设置下工作,忽略了用户兴趣的动态长期演化。

[[reinforcement-learning]] 通过把推荐建模为序列决策((Markov Decision Process))来优化长期累积奖励,天然适合长期目标;但在推荐中受限于用户-物品交互的稀疏性、长尾分布以及语义规划能力不足。[[large-language-models]] 擅长高层推理与长期规划,但难以在物品空间极大、极复杂的推荐场景中 grounding 到细粒度动作。本文要同时克服 RL 与 LLM 各自的短板。

## 方法

LERL((LLM-Enhanced Reinforcement Learning))把推荐分解为两层决策。优化目标为最大化折扣累积奖励 $\max_\pi \mathbb{E}_\pi[\sum_{t=1}^{N}\gamma^{t-1} r_t]$。

**High-Level Semantic Planner (HSP)**:由 LLM 驱动的宏观决策者,在类别粒度上规划。
- **High-Level Actor**:基于用户类别级交互历史 $H_t^c$ 和采样的 reflections,通过 prompt 让 LLM 从候选类别集 $\mathcal{C}$ 中选出子集 $c_t$,对过曝(overexposed)、近期饱和的内容类别降权,促进类别级多样性。输出严格为 Python 整数列表。
- **High-Level Critic**:一个基于语言的 reflective critic((reflection)),在每个用户会话结束时输出文本反思 $\mathcal{F}_u$,基于完整轨迹 $\mathcal{T}_u$ 与辅助统计(交互长度、累积奖励)总结提升长期满意度的可执行洞见,存入 reflection pool。
- **Reflection 采样**:维护 reflection pool $\mathcal{R}=\{(\mathcal{F}_u, S_u)\}$,按累积奖励经 softmax 分布 $P(u)=\exp(\alpha S_u)/\sum\exp(\alpha S_v)$ 优先采样高满意度用户的反思($N_r=200$,采样 $N_s=3$ 条),作为高层语义引导。

**Low-Level Policy Learner (LPL)**:由 RL 优化的细粒度物品选择器,在 HSP 给定的类别约束 $c_t$ 内工作。
- **Low-Level Actor**:用 [[transformer]] encoder 编码物品级交互历史得到偏好表示 $e_t^p$,经 MLP 参数化高斯分布并采样虚拟物品嵌入 $p_t \sim \mathcal{N}(\mu_t, \sigma_t^2)$(支持探索)。与候选物品嵌入点积得相似度,再用二值 item-category 映射矩阵 $W$ 构造 category mask $a^{mask}=W \cdot c_t$ 作为软过滤,$a^{score}=a^{sim}\odot a^{mask}$,取 top-$k$ 组成推荐列表。
- **Low-Level Critic**:状态值函数 $V_\varphi(s_t)$(MLP),用 TD 误差训练。
- 低层智能体用 [[ppo]](clipped surrogate objective)优化,兼顾学习效率与稳定性。

## 结果

**环境与数据**:在 [[kuaisim]] 模拟器上做 whole-session 实验,基于 [[kuairand]](pure,27,077 用户 / 7,551 物品 / 1,436,609 交互 / 密度 0.70%)与 [[kuairec]](7,176 用户 / 10,728 物品 / 12,530,806 交互 / 密度 16.3%)。最大交互长度 20,列表长度 6,引入 diversity-aware quit mechanism(连续推同类内容则剩余交互数减一)。高层 LLM 使用 [[llama-3]]-8B。

**指标**:交互长度 $\mathbf{T}_{int}$、累积奖励 $\mathbf{R}_{cum}$、单轮奖励 $\mathbf{R}_{sin}$。Baselines 包括 [[ppo]]、[[td3]]、[[ddpg]]、[[sac]]([[actor-critic]] A2C)、PG、[[hac]]、SAC4IR、DNaIR。

**RQ1 主结果(Table 2)**:LERL 在两个环境的 $\mathbf{T}_{int}$ 和 $\mathbf{R}_{cum}$ 上均最优。
- KuaiRand:$\mathbf{T}_{int}=17.238$(次优 PPO 14.352),$\mathbf{R}_{cum}=12.284$(次优 DNaIR 9.824),$\mathbf{R}_{sin}=0.719$(次优,DNaIR 0.720 最佳)。
- KuaiRec:$\mathbf{T}_{int}=16.400$(次优 A2C 13.305),$\mathbf{R}_{cum}=10.507$(次优 DNaIR 9.235),$\mathbf{R}_{sin}=0.637$(TD3 0.800 最佳)。
- 传统 RL(TD3、DDPG)单轮奖励尚可,但 $\mathbf{T}_{int}$、$\mathbf{R}_{cum}$ 显著偏低;DNaIR 因把多样性纳入奖励有中等提升,但长期增益有限。

**RQ2 案例研究**:在 KuaiRec 对用户(ID:5)连续三轮推荐对比 LERL 与 PPO。LERL 三轮间无重复物品类别;PPO 则出现 5 个、3 个类别重叠,说明 LERL 能在时间上分散类别曝光、缓解内容同质化。

**RQ3 消融**:去掉 HSP(w/o hsp)使交互长度与累积奖励大幅下降;去掉 high-level critic(w/o hc)使三项指标均变差,说明高层规划与语义反思都不可或缺。

## 在本 wiki 中的位置

LERL 处于 [[llm-for-recommendation]] 与 [[rl-based-recsys]] 的交叉点,采用分层 RL((actor-critic)+ [[ppo]])架构,延续 [[long-term-recommendation]] 与 [[filter-bubble]] 缓解线索(如 [[cirs]]、DNaIR)。它的"LLM 高层规划 + RL 低层执行"模式与 [[interecagent]] 等 [[llm-agent]] 推荐工作思路相关,但创新在于用 reflective language-based critic(类 [[reflexion]] 的 [[reflection]] 机制)替代标量奖励来指导高层决策。评测沿用 [[kuaisim]] 模拟器与 [[kuairand]]/[[kuairec]] 数据集,与 [[recommender-system]] 的 RL 评测生态(如 [[easyrl4rec]])一脉相承。
