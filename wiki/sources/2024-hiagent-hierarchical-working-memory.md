---
type: source
subtype: paper
tags:
  - llm-agent
  - working-memory
  - long-horizon-tasks
  - subgoal-decomposition
  - agent-memory
  - hierarchical-planning
created: 2026-05-29
updated: 2026-05-29
arxiv: 2408.09559
raw: raw/2408.09559.pdf
authors:
  - Mengkang Hu
  - Tianxing Chen
  - Qiguang Chen
  - Yao Mu
  - Wenqi Shao
  - Ping Luo
year: 2024
---

# HiAgent: Hierarchical Working Memory Management for Solving Long-Horizon Agent Tasks with Large Language Model

HiAgent 借鉴人类问题求解中的"分块(chunking)"思想,用 subgoal 作为 memory chunk 分层管理 [[llm-agents|llm-agent]] 的 working memory(in-trial memory),在五个长程任务上将成功率提升约一倍。

## 问题

[[llm-based-agents]] 作为交互系统处理环境 observation 并生成可执行 action,其表现高度依赖 memory 机制。memory 分为两类:cross-trial memory(跨多次尝试累积,见 [[agent-memory]])与 in-trial memory(即 **working memory**,单次尝试内累积)。已有大量工作优化 cross-trial memory(如 [[reflexion]]),但对 working memory 的高效利用研究不足。

主流范式 STANDARD(如 [[react]] / [[react|react-reasoning-and-acting]])把**所有历史 action-observation pair** 全部直接塞进 working memory 作为 LLM 上下文。在 long-horizon agent tasks(任务通常需 20 步以上)中,这导致 working memory 冗长冗余,阻碍 LLM 维持连贯策略、做出准确预测,并随步数增加而性能下降。

## 方法

HiAgent 受认知科学(Newell & Simon、Anderson、Miller 的 chunking 理论)启发,用 subgoal 作为 working memory 的 chunk 进行分层管理:

- **Subgoal-based hierarchical working memory**:每个时间步,LLM 先生成一个 subgoal(里程碑),再生成具体 action 去完成它;对应的 action-observation pair 存入一个 memory chunk。当前 subgoal 保留完整 action-observation pair 提供细节上下文;过去的 subgoal 只保留**汇总后的 observation**。
- **Observation Summarization(§3.3)**:子目标完成后,用 LLM 把该 chunk 内的历史 observation/action 合成为一条简洁的 summarized observation s_i,并判定该 subgoal 是否达成;随后用 s_i 替换(obscure)chunk 内的明细 pair。工作记忆形式化为 m_t = (g_0, s_0, ..., g_{n-1}, s_{n-1}, g_n, a_{n0}, o_{n1}, ...)。
- **Trajectory Retrieval(§3.4)**:当某过去 subgoal 的明细信息对当前决策(如失败溯因)仍然必要时,LLM 主动生成检索函数,把该 subgoal 的完整 action-observation pair 召回上下文,实现按需访问。
- 形式化为 POMDP (S, O, A, T, R),agent 作为策略 π(a_t | I, o_t, a_{t-1}, ...)。

## 结果

- 任务:AgentBoard 上五个 long-horizon 任务——Blocksworld、Gripper、Tyreworld、Barman、Jericho(文本冒险,见 [[blocksworld]])。
- backbone:[[gpt-4]](gpt-4-turbo),temperature=0、top_p=1,最大步数 30,每任务 1 个 in-context 示例。
- 指标:Success Rate(SR)、Progress Rate(PR)、Average Steps、Context Efficiency、Run Time。
- **整体**:相对 STANDARD,SR 从 21.00 提升到 **42.00(+21,约翻倍)**,PR 从 38.61 提升到 **62.55(+23.94%)**,平均步数减少 3.8,context token 减少 35.02%,run time 减少 19.42%。
- 分任务:Blocksworld SR 30→60、Tyreworld 10→60、Barman 10→30。Tyreworld 中 SR +50% 且平均步数减 9.4;Gripper 任务 SR 持平但 context 减少约 50%。
- **消融(Table 2, tyreworld)**:去掉 Observation Summarization(w/o OS)SR -30、context +10.8%;去掉 Trajectory Retrieval(w/o TR)SR -10;两者皆去 SR -30。
- **task decomposition 对照(Table 3)**:仅做子目标分解(w. TD)SR=40,仍比 HiAgent(60)低 20,且 runtime +5.7%、context +12.8%——说明增益不仅来自任务分解,更来自 working memory 管理。
- **统计显著性**:Wilcoxon signed-rank test,PR 检验统计量 144.0(p=2.38e-5),Average Steps 112.5(p=0.0016)。
- HiAgent 在更长步数下仍保持 >80% 的 action 可执行率,而 STANDARD 在步数超 20 后可执行率跌破 10%。

## 在本 wiki 中的位置

本文属于 [[llm-based-agents]] 的 memory 管理方向,聚焦少被研究的 in-trial / working memory(区别于 [[agent-memory]] 中常见的 long-term/cross-trial memory 如 [[reflexion]]、Memorybank)。方法上把 [[llm-planning]] 的 subgoal 分解与认知科学 chunking 结合,可与 [[react]]、[[llm-planning]]、least-to-most / plan-and-solve 等条目互链;HiAgent 被定位为可嵌入其他 agent 框架(含 [[llm-multi-agent]])的通用 working memory 管理组件。
