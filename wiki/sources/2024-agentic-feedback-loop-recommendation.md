---
type: source
subtype: paper
tags: [llm-agent, recommender-system, user-simulation, feedback-loop, multi-agent-collaboration, agent-memory, reward-model, sequential-recommendation, debiasing]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.20027
raw: raw/2410.20027.pdf
authors: [Shihao Cai, Jizhi Zhang, Keqin Bao, Chongming Gao, Qifan Wang, Fuli Feng, Xiangnan He]
year: 2024
---

# Agentic Feedback Loop Modeling Improves Recommendation and User Simulation

提出 Agentic Feedback Loop(AFL):让 [[llm-for-recommendation]] 中的 recommendation agent 与 user agent 通过基于 [[memory-module]] 的多轮文本反馈相互协作,从而同时提升推荐与 [[user-simulation]],并且不放大流行度/位置偏差。

## 问题

基于 [[large-language-models]] 的 [[llm-agents|llm-agent]] 在推荐领域的应用主要分两类:一类是 **recommendation agent**(如 [[interecagent]] 类、RecMind、[[macrec]]),利用 LLM 的世界知识、[[tool-use]] 与 [[reasoning]] 提升推荐;另一类是 **user agent / [[user-simulation]]**(如 Agent4Rec/[[generative-agents]] 思路、RecLLM、[[recagent]]、[[agentcf]]),用 LLM 模拟用户的点赞、点踩、评论等行为,用于评测推荐系统、推断用户兴趣、生成训练数据。

以往研究**只单独优化其中一个 agent**,忽视了真实推荐场景中用户与推荐器之间的 **feedback loop(反馈回路)**:推荐器帮用户发现兴趣,用户通过多轮交互的反馈又让系统更懂自己。作者认为这种交互式、互惠的反馈回路恰好契合 LLM agent 在交互与记忆上的优势,因此提出把反馈回路引入双方的联合优化。注意真实世界的反馈回路常会放大 popularity bias 与 position bias(见 [[matthew-effect]]、[[filter-bubble]]),这是本文要规避的风险。

## 方法

**AFL** 同时构建一个 recommendation agent 和一个 user agent,用文本通信模拟反馈回路,核心仅依赖 memory,因此通用、可插拔(可接入几乎任何带记忆的推荐/用户 agent)。

- **Recommendation Agent**:由 [[gpt-4o-mini]] 驱动,含 memory module 与一个可替换的 recommendation module(基模型,提供数据集相关推荐知识);采用 [[role-playing]] 与 [[chain-of-thought]],综合 memory + 交互历史 + 基模型推荐项,输出推荐项 I_r 与理由 R_r。
- **User Agent**:含 memory module,同样用 role-playing + CoT;额外用一个**固定的 [[reward-model]]**(实现为 [[sasrec]])给候选项打相关性分;结合理由、memory、历史与该分数,判断是否喜欢(yes/no)并给理由。
- **Feedback Loop(Algorithm 1)**:推荐 agent 先建议一项;若 user agent 满意则终止;否则把推荐项、推荐理由、拒绝理由写入双方 memory,推荐 agent 可重新归纳用户兴趣、尝试说服或换项,user agent 则从中挖掘潜在兴趣,循环直至满意或达到 Max_Epoch。本文最大迭代数设为 4。

**实验设置**:三数据集 [[steam-dataset]](Steam,采样 200 条测试)、[[movielens]](MovieLens100k)、Lastfm;按时间 8:1:1 划分。推荐任务沿用 [[llara]] 设置,候选 20 项(1 正 + 19 负),用 HitRatio@1;用户模拟沿用 Agent4Rec 设置,正负比 1:k(k∈{1,3,9}),用 precision/recall/F1。基模型涵盖传统模型([[sasrec]]、[[gru4rec]]、Caser)与 LLM 类([[morec]]、[[llama-3]]-8B、[[gpt-4o-mini]]、[[llara]])。

## 结果

- **总体增益(abstract)**:agentic feedback loop 相对单一 recommendation agent 平均提升 **11.52%**,相对单一 user agent 平均提升 **21.12%**。
- **推荐性能(Table 4,HitRatio@1)**:AFL 在几乎所有基模型上优于 "Base Model" 与 "Rec Agent"。例:Lastfm 上 SASRec 0.2869→Rec Agent 0.3197→AFL **0.3770**;最强基模型 LLaRA 在三数据集分别达 **0.4836 / 0.4750 / 0.4947**(均为该列最佳)。
- **用户模拟性能(Table 5)**:AFL 在多数 1:k 设置下 precision/recall/F1 最佳,如 Lastfm 1:1 的 F1 由 User Agent 0.4865 提升到 **0.6297**;仅 MovieLens 1:3 的 recall 略低于 User Agent,但 AFL 的 F1 更高(说明 User Agent 倾向"全部喜欢"刷高 recall)。
- **消融**:
  - vs. 简单加 ranker(Table 6):"Rec Agent + SASRec/User Agent" 不一定有提升,AFL 因反馈可纠错而最优(Lastfm 0.3770 vs 0.3607)。
  - 模型组件(Table 7):去掉 Rec Model / Reward Model / 二者都去掉,性能依次下降(MovieLens:0.4316 → 0.4000 / 0.4211 / 0.2105),证明推荐模型与奖励模型协同有效。
  - 迭代数:推荐与模拟性能随迭代上升,但增益递减且 API 成本上升,需权衡(本文取 4)。
- **偏差(RQ3)**:AFL 不放大且能**缓解 popularity bias**(随迭代推荐更多长尾项),并对 **position bias** 有抵抗力("Random" 多数情况下优于 "First"/"Last",说明依赖用户偏好而非位置),体现其鲁棒性。
- 代码:https://github.com/Lanyu0303/AFL 。发表于 SIGIR '25。

## 在本 wiki 中的位置

本文位于 **[[llm-for-recommendation]] × [[multi-agent-collaboration]] × [[user-simulation]]** 的交叉点:它不是把 recommendation agent 与 user agent 分开做,而是用 [[memory-module]] 驱动的反馈回路让二者互惠协同,可视为对 [[macrec]]、[[recagent]]、[[agentcf]]、[[generative-agents]] 等 agent-based recommendation 工作的统一与延伸。其对 popularity/position bias 的关注与 [[matthew-effect]]、[[filter-bubble]]、[[cirs]]、[[debiasing]] 等反馈回路偏差研究相承接;作者团队([[university-of-science-and-technology-of-china]]、[[xiangnan-he]]、[[chongming-gao]] 等)亦活跃于交互式/长期推荐方向(参见 [[long-term-recommendation]]、[[interactive-recommendation]])。
