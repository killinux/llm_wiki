---
type: source
subtype: paper
tags: [reinforcement-learning, recommender-system, rl-based-recsys, code-library, benchmark, offline-rl, long-term-engagement]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2402.15164
raw: raw/2402.15164.pdf
authors: [Yuanqing Yu, Chongming Gao, Jiawei Chen, Heng Tang, Yuefeng Sun, Qian Chen, Weizhi Ma, Min Zhang]
year: 2024
---

# EasyRL4Rec: An Easy-to-use Library for Reinforcement Learning Based Recommender Systems

EasyRL4Rec 是一个面向 RL-based 推荐系统([[recommender-systems|recommender-system]])的易用代码库,围绕 Environment / Policy / StateTracker / Collector 四个核心模块,基于五个公开数据集构建轻量级 RL 环境,提供面向长期收益的统一训练与评测流程,并附带在经典 RL 与近期工作上的对照实验。

## 问题

基于 [[reinforcement-learning]] 的推荐系统因能优化用户长期参与度(long-term user engagement)而受关注:推荐被建模为多步决策的 [[markov-decision-process]],agent(推荐器)与环境(用户)交互、根据动作(item)反馈学习最大化累计奖励的策略。但该领域面临三大障碍:

- **缺乏易用框架**:已有资源既不直接用真实大规模数据、也不易复用模拟器,通用 RL 库(如 rllib)缺少推荐环境构建与状态建模,难以直接套用。
- **评测口径不一**:有的沿用传统 RS 指标(NDCG、HitRate),有的用 RL 指标(cumulative reward、interaction length),团队间无法公平比较。
- **可复现性差**:超过 60% 的现有工作未开源,自实现 baseline 细节差异大,阻碍后续研究。

## 方法

EasyRL4Rec 用 OpenAI Gymnasium API 实现环境,扩展 Tianshou 实现策略,核心由四个模块构成:

- **Environment**:从静态数据集构建轻量 RL 环境,核心是 step() 返回状态与奖励;离线评测时用一个在测试集上训练的 MF([[matrix-factorization]])模型预测缺失 user-item 对的奖励。
- **Policy**:支持离散与连续动作,内置"连续动作→离散 item"的转换机制;状态由 StateTracker 编码并与策略联合优化;提供 Remove Recommended Items(对 logits 加 mask)以支持多轮推荐。覆盖三类算法——Batch RL([[bcq]]、[[cql]]、CRR、[[sasrec]] 式的 SQN)、model-free off-policy([[ddpg]]、C51、DQN、[[td3]])、model-free on-policy(PG、A2C、[[ppo]])。
- **StateTracker**:对推荐场景中无法直接观测的状态做建模,实现五种序列推荐式编码器(Average、GRU、Caser、[[sasrec]]、NextItNet)。
- **Collector**:连接 Environment 与 Policy,把交互轨迹收集进 Buffer;Buffer 支持多环境并行的流式轨迹存储。

**统一流程**:两种训练范式——(1) 直接从离线日志学习([[offline-rl]] / batch RL,支持 Sequential / Convolution / Counterfactual 三种 buffer 构造);(2) 用预训练的 user model(reward model,类似 [[chatgpt]] 的 [[rlhf]] 思路,用 [[deepfm]] 作 user model)在线学习。评测在离线环境进行,引入 quit 机制模拟真实用户,提供三种评测模式 FreeB / NX_0_ / NX_X_。长期指标为 Cumulative Reward(R_cumu)、Average Reward(R_avg)、Interaction Length。

数据集:Coat、YahooR3、MovieLens(1M)、KuaiRec、KuaiRand,覆盖商品 / 音乐 / 电影 / 短视频等场景。

## 结果

在 Coat、MovieLens、KuaiRec 三个数据集上的实验给出若干结论:

- **离散动作 > 连续动作**:DQN、C51、PG、PPO 等离散方法在三数据集上 R_cumu 与 Length 普遍更高;连续方法(标 C)如 DDPG(C)、TD3(C) 表现较弱。例如 Coat 上 A2C 取得最高 R_cumu=81.7952,而 TD3(C) 仅 16.3232。
- **on-policy > off-policy**:同类型内 on-policy 更优,如 KuaiRec 上 PG 的 R_cumu=18.8922 高于 off-policy DQN 的 12.6543。
- **RS 专用方法有竞争力**:[[dorl](去偏、缓解 Matthew effect)与 Intrinsic(加内在奖励促探索)接近最优;MovieLens 上 DORL 取得 R_cumu=45.7708、Length=17.3440,均为最佳。
- **Batch RL**:从离线日志训练时 CRR 在三数据集全面最优(如 Coat R_cumu=28.96),BCQ 最差;受限于离线日志,batch RL 整体奖励低于带 user model 在线训练的 model-free baseline。
- **Coverage/Diversity/Novelty**(KuaiRec):off-policy 覆盖率更高(C51 coverage=0.1027),DQN diversity 最高 0.8981,on-policy 新颖性更好(PPO(C) novelty=3.5830)。
- **Preference Overestimation 问题**:类似 offline RL 的价值高估——用更少负样本训练的 user model 预测更准(MSE 更低)却导致策略高估稀有 item 的偏好;实验建议增加负样本数缓解。
- **StateTracker 与 buffer 构造方法**对性能影响都很小(GRU 略优;Sequential/Convolution/Counterfactual 三种构造表现相近)。

## 在本 wiki 中的位置

本文是 RL-based 推荐系统的基础设施类工作,把 [[reinforcement-learning]] 与 [[recommender-systems|recommender-system]] 的研究流程标准化,可作为 wiki 中各类 RL 推荐方法(如 [[dorl]]、[[ppo]]、[[bcq]]、[[cql]]、[[td3]]、[[ddpg]])的统一实验平台入口。其问题建模([[markov-decision-process]])、离线评测中用 [[matrix-factorization]] 补全奖励、以及用 [[deepfm]] user model + [[rlhf]] 式范式训练策略的做法,串联了 [[offline-rl]]、user simulation 与序列推荐([[sasrec]] 等)等多条线索;所用数据集 KuaiRec、KuaiRand、MovieLens-1M、YahooR3、Coat 也是 wiki 中反复出现的 [[recommender-systems|recommender-system]] 基准。
