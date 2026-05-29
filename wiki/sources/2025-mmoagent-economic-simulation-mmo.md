---
type: source
subtype: paper
tags:
  - llm-agent
  - agent-based-modeling
  - social-simulation
  - generative-agents
  - game-economics
  - multi-agent-systems
created: 2026-05-29
updated: 2026-05-29
arxiv: "2506.04699"
raw: raw/2506.04699.pdf
authors:
  - Bihan Xu
  - Shiwei Zhao
  - Runze Wu
  - Zhenya Huang
  - Jiawei Wang
  - Zhipeng Hu
  - Kai Wang
  - Haoyu Liu
  - Tangjie Lv
  - Le Li
  - Changjie Fan
  - Xin Tong
  - Jiangze Han
year: 2025
---

本文提出 **MMOAgent**——一个基于 LLM 的 Generative Agent-Based Modeling(GABM)框架,用 LLM 驱动的智能体来模拟 Massively Multiplayer Online(MMO)游戏中的微观经济活动,使其涌现出角色分化、价格波动等符合市场规律的宏观经济现象。

## 问题

在 MMO 游戏经济研究中,Agent-Based Modeling(ABM)是从微观个体交互自底向上分析复杂系统的有力工具,已从规则驱动智能体演进到 [[reinforcement-learning]] 驱动的智能体(如 MMO Economist)。但现有方法在模拟"类人经济活动"时存在三大局限:

- **Reliability(可靠性)**:RL 范式依赖人工设计的奖励函数来模拟多样人类行为,难以刻画玩家群体的人口学多样性;ABM 是自底向上方法,微观行为对真实性的任何偏离都会削弱模拟可信度。
- **Sociability(社交性)**:智能体之间通过语言进行的直接交互(讨价还价、谈判)是游戏内经济交易的根本驱动力,但常被忽视,导致模拟缺失关键社会动态。
- **Interpretability(可解释性)**:RL 智能体的决策机制不透明,难以理解模拟经济如何运行,削弱了对政策制定者的实用价值。

此外,以往虚拟环境的交易机制局限于伪 P2P(由游戏环境或 NPC/拍卖中介),无法刻画玩家间直接的、以语言谈判和议价为核心的真实交易。

## 方法

作者扩展了 MMO Economist 的虚拟环境,并构建 **MMOAgent**,核心由五个模块组成:profile、perception、reasoning、memory、action(见 [[generative-agents]] / [[memory-stream]] 思路)。

- **扩展的虚拟环境**:六类经济资源(Experience、Material、Token、Currency、Capability、Labor)与多种经济活动(Task、Upgrade、Auction、Shop、Recharge),并新增**完整的 P2P 交易**——支持 Public Chatting(向所有玩家广播交易要约)与 Private Chatting(买卖双方私下谈判议价),实现直接的玩家间语言谈判与 escrow-free 交易。
- **Data-driven Profile Design**:采集某 NetEase MMO 游戏 16,294 名真实玩家(2024-03-04 至 03-10)的脱敏日志,用 k-means 聚类提取代表性玩家画像,再用 [[gpt-4]] 生成个性化文字 profile(如 Engaged Grinder、Moderate Player、Spending Enthusiast、Casual Gamer、Steady Participant),每个特征分为 high/medium-high/medium/medium-low/low 五级。
- **Perception**:用 parser 把原始观测解析为语义文本(库存、拍卖托管、拍卖信息、附近资源、消息)。
- **Structured Actions with Execution Feedback**:把低层操作封装为带清晰语义的结构化动作(Task 用 DFS/A* 做资源探索与最短路径,其余为规则或 LLM call),并构建 verifier 对执行结果给出成功/失败反馈,避免 LLM 因 outcome unawareness 重复失败计划。
- **Feedback Enhanced Reasoning**:用 zero-shot [[chain-of-thought]] 结合 profile、观测、记忆、反馈来决策;周期性进行 [[reflection]](self-reflection),每 n 步评估近期动作以调整后续策略。
- **Numeric-aware Long Short Term Memory**:STM 保留最近 10 条轨迹;LTM 存储带 importance score 的重要经验,基于数值嵌入做 memory reading(相似度由数值方差决定),memory writing 用 recency-sensitive 打分,并按 [[ebbinghaus-forgetting-curve]] 做指数式遗忘(memory forgetting)。

## 结果

在 Rich / Moderate / Scarce 三种资源场景下,用两个指标评测:**Capability**(资源获取与管理水平,越高越好)与 **Diversity**(活动分布熵)。LLM backbone 用 GPT-3.5-turbo(对比 Llama3-8B)。

- **Capability(Table 1)**:MMOAgent(GPT-3.5)在三场景分别为 121.0 / 80.4 / 75.0,显著超过 SOTA 的 MMO-economist(92.4 / 72.6 / 51.8)以及 Random、Rule-based、[[react]]、[[reflexion]] 等基线(p < 0.05)。MMOAgent(Llama3)为 104.0 / 76.2 / 68.4,GPT-3.5 一致优于 Llama3,故后续分析基于 GPT-3.5。
- **Ablation**:去掉 STM / LTM / Reflect 任一模块性能均下降;去掉 LTM 在 Rich/Moderate 场景下降最多(115.2 / 77.0),凸显长期经验保留的重要性。
- **Profile Consistency(Table 2)**:用 GPT-4(与 3 名人工评估在 20% 样本上达 95% 一致)做 5 级一致性评分,五类智能体得分 3.75~3.89,接近 4,说明决策序列与所赋画像一致。
- **System-level 涌现现象**:30 个智能体跑 200 步;P2P 平均成交价(MAT 6.46 tokens)低于拍卖均价(6.86 tokens),符合 escrow-free 直接交易的特性;拍卖价与"Demand Supply Gap"的 Pearson 相关系数 0.67(p < 0.001),验证符合供需规律。还观测到 Equality-Profitability 权衡:资源越稀缺,profitability 升、equality 降。智能体涌现出明显**角色分化**(cost-averse 偏向 task/trade,愿花钱者演化为 Pay-to-Win)。

局限:LLM 的 hallucination 可能产生非法动作(资源不足时升级或超额竞拍);游戏知识使智能体偏好保守动作(task),降低动作多样性。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 用于 [[social-simulation]] / [[agent-based-modeling]] 的方向,是 Generative ABM(GABM)在 MMO 游戏经济中的应用,直接承接 [[generative-agents]] 的 profile-perception-reasoning-memory-action 架构,并与 social simulation 工作(如 S³、[[generative-agents]])相呼应。方法上整合了 [[chain-of-thought]]、[[reflection]]、[[react]]、[[reflexion]] 等推理/记忆机制,记忆模块借鉴 [[ebbinghaus-forgetting-curve]];基线对比 [[react]]、[[reflexion]] 及 RL 驱动的 MMO Economist。作者来自 NetEase Fuxi AI Lab、[[university-of-science-and-technology-of-china]]、[[national-university-of-singapore]] 等,使用 [[gpt-4]]、[[gpt-3-5-turbo]]、[[llama-3]] 作为模型主体。
