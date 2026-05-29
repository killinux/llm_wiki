---
type: source
subtype: paper
tags:
  - llm-agent
  - recommender-system
  - long-term-recommendation
  - actor-critic
  - reflexion
  - llm-planning
created: 2026-05-29
updated: 2026-05-29
arxiv: 2403.00843
raw: raw/2403.00843.pdf
authors:
  - Wentao Shi
  - Xiangnan He
  - Yang Zhang
  - Chongming Gao
  - Xinyue Li
  - Jizhi Zhang
  - Qifan Wang
  - Fuli Feng
year: 2024
---

# Large Language Models are Learnable Planners for Long-Term Recommendation

一句话:提出 BiLLP(Bi-level Learnable LLM Planner)框架,用一组 [[large-language-models]] 实例以宏观/微观双层学习的方式承担长期推荐中的规划任务,在稀疏推荐数据上超越从零训练的 [[reinforcement-learning]] 方法与现有 LLM agent 基线。

## 问题

长期推荐(long-term recommendation)需要在即时收益(如点击)与长期用户参与(long-term engagement)之间权衡,以缓解 filter bubble / echo chamber 问题。主流做法把交互式推荐建模为 [[markov-decision-process]] 并用 RL 最大化累积奖励(cumulative reward),但推荐数据天然稀疏且呈 long-tail 分布,从零训练 RL 容易不稳定、过拟合,对长尾物品与用户规划能力差,导致次优表现。

作者主张利用 LLM 在稀疏数据上的强规划与世界知识能力来做长期推荐。难点有二:LLM 预训练与推荐场景差异大,LLM 本身不天然掌握"增强长期参与"的指导原则;且面向个体用户的推荐需要个性化、到具体物品(item-specific)的策略,仅有原则意识不够。因此需要"教会"LLM 获得这些原则并使其个性化。

## 方法

采用 interactive recommendation 设置:每步 n 向用户 u 推荐一个物品 a_n,先生成问题求解计划(thought t_n),再给出物品推荐。整条交互 episode 记为 H = {s_1,t_1,a_1,r_1,...,s_N,t_N,a_N,r_N}。因在线收集反馈成本高,沿用前人构造 Simulated Environment(基于离线日志,用 [[deepfm]] 拟合在线奖励并计算物品相似度)做训练与测试,并引入 quit 机制(推荐物品与近期列表相似度超过阈值 β、或单轮奖励低于 2 则终止)模拟 filter bubble 退出。

BiLLP 通过层次机制把学习拆为 macro-learning 与 micro-learning,含四个 LLM 模块:

- 宏观层(Macro-learning):
  - **Planner**:冻结的 LLM 实例,带记忆库 M_P 存历史高层经验(指导原则)。新 episode 用 [[faiss]] 按欧氏距离检索 K 条最相关 reflection,结合历史轨迹与当前状态生成 forward-looking 的高层计划(thought)。
  - **Reflector**:类似 [[reflexion]],对完成的整条 episode 反思,抽取指导原则(如"用户因重复推荐相同物品退出 → 应强调多样性"),生成 reflection ℓ 更新到 Planner 记忆。这是无需 fine-tuning 的 [[self-improvement]]。
- 微观层(Micro-learning),借鉴 [[actor-critic]](A2C):
  - **Actor**:带记忆 M_A 与工具库 Tl(如 Category Analysis Tool),把高层计划 grounding 成可执行动作。先检索经验、调用工具分析用户历史、再 prompt LLM 生成候选动作 a'_n,最后用 [[llama-2]]-7b 编码做 embedding 相似度(L2)把 a'_n grounding 到物品池中实际物品。
  - **Critic**:LLM 实现的评估器,带记忆 M_C。用 in-context learning 估计 state-value V(s_n),再算 advantage A(s_n,a_n)=r_n+γ·V(s_{n+1})−V(s_n),取 σ(A)(A≥0 时为 1 否则 0)作为 advantage v_n,以低方差方式更新 Actor,缓解 Q-value 高方差问题。

讨论指出:传统梯度更新提升某状态-动作的采样概率,而 BiLLP 把状态-动作记入外部记忆,再遇相似状态时检索概率上升,达到类似梯度更新的效果而无需训练。

## 结果

数据集:**Steam**(6,012 用户 / 190,365 物品)与 **Amazon-Book**(3,109 用户 / 13,864 物品)。指标:轨迹长度 Len、单轮奖励 R_each、累积奖励 R_traj(越长/累积越高代表长期参与越好;但 R_each 过高可能是过度偏重即时奖励)。

实现:所有 RL 基线用 100,000 episode 训练,LLM 方法仅用 100 episode;LLM backbone 默认 gpt-3.5-turbo-16k,temperature=0.5,γ=0.5,reflection K=2,阈值 τ_A=0.01、τ_C=0.1。RL 基线含 DQN、SQN、[[bcq]]、[[cql]]、CRR、A2C、[[dorl]];LLM 基线含 ActOnly、[[react]]、[[reflexion]]。

主结果(Table 3,三随机种子均值):

- **BiLLP 在 Len 与 R_traj 上均最佳**。Steam:Len 15.367、R_traj 69.193(次优 Reflexion 57.423);Amazon:Len 9.413、R_traj 42.443(次优 Reflexion 40.670)。
- R_each 上 BiLLP 适中(Steam 4.503、Amazon 4.507),不靠拉高即时奖励取胜。
- ActOnly 弱于部分含规划的方法,说明显式 thinking/planning 重要;ReAct 弱于 Reflexion 与 BiLLP,凸显 self-improvement 的价值。
- 频率分析(Figure 3):A2C 倾向过拟合热门物品、缺乏对 long-tail 的规划;BiLLP 在长尾物品上规划更好,缓解 filter bubble。

消融(Table 5):去掉 Macro(w/o Macro)或 Micro(w/o Micro)均使 R_traj 下降(Steam BiLLP 69.193 vs w/o Macro 64.960、w/o Micro 64.720),两种学习机制都有贡献。

Critic 有效性(RQ3, Figure 4):以 1000 条轨迹的蒙特卡洛估计为参照,Critic 的 in-context 估计能有效降低 state-value 估计方差(存在小偏差)。

鲁棒性(RQ4):随 quit 窗口 W 增大所有方法指标下降,但 BiLLP 始终领先(Figure 5)。不同 backbone(Table 6):GPT-4-32k > GPT-3.5-16k > Llama-2-7B,说明 backbone 越强 BiLLP 提升越大;Steam 上 GPT-4-32k 的 R_traj 达 118.235。

## 在本 wiki 中的位置

本文是 [[llm-agents|llm-agent]] 与 [[recommender-systems|recommender-system]] 交叉的代表工作,把 [[reflexion]] 式 [[self-improvement]] 与 [[actor-critic]] 结合用于 [[long-term-recommendation]]。它延续了 [[dorl]]、CIRS 等缓解 filter bubble / [[matthew-effect]] 的交互式推荐线索,又把 [[react]]、[[reflexion]]、ExpeL、AdaPlanner 等 agent 规划范式落到推荐场景。与从零训练的 [[reinforcement-learning]] 方法相比,它展示了 LLM 在稀疏数据上的 [[llm-planning]] 优势,并用 [[experiential-learning]] / [[agent-memory]] 替代梯度更新。作者团队来自 [[university-of-science-and-technology-of-china]] / Meta AI,核心作者包括 [[xiangnan-he]]、[[chongming-gao]]。
