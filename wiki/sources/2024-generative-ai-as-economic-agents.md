---
type: source
subtype: paper
tags:
  - llm-agent
  - ai-alignment
  - game-theory
  - economics
  - position-paper
created: 2026-05-29
updated: 2026-05-29
arxiv: 2406.00477
raw: raw/2406.00477.pdf
authors:
  - Nicole Immorlica
  - Brendan Lucier
  - Aleksandrs Slivkins
year: 2024
---

# Generative AI as Economic Agents

一篇立场/理论论文,主张随着 [[large-language-models]] 的发展,应当把生成式 AI 本身建模为一个有独立信息与偏好的"经济主体"(economic agent),而不再仅仅当作降低成本或提供信号的技术工具。

## 问题

传统经济学把 AI 建模为一种"技术":它通过降低行动成本或提炼信息来影响人类主体的收益。作者认为,鉴于生成式 AI(尤其是 [[large-language-models]])的最新进展,这种建模已不足够。生成式 AI 能够基于隐含而广博的"常识"理解生成新颖内容,因而可被用作"虚拟顾问"(virtual consultant),其行为表现出经济主体的典型特征:拥有信息集(information set)、行动空间(action space)、以及在训练/微调/编排中内化的目标与约束(即隐含偏好)。关键在于,这些偏好可能与用户偏好不一致([[ai-alignment]] 问题),且不直接受用户控制,从而可能导致与无 AI 设定下质性不同的均衡结果。

## 方法

论文提出一个博弈论框架,把传统的人类博弈扩展为"每个用户配备一个 AI agent":

- **基线模型**:n 个人类玩家的博弈;一个特殊主体 Nature 从公共已知分布中抽取自然状态 ω;每个玩家 i 有行动空间 A_i、信息集 I_i,收益为 u_i(a, ω)。
- **引入 AI agent**:每个人类玩家 i 与其 AI agent 通过通信协议交替发消息,产生 transcript τ_i。AI agent 有自己的信息结构 J_i(可能掌握用户不知道的信息),收益为 v_i(τ_i, ω)。关键约束:AI 的收益只依赖于 transcript 与状态 ω,而**不直接依赖于博弈的实际结果或用户实际收益**——即 AI 被按"提供建议的好坏"而非"用户如何采纳建议"来评估。
- **有限能动性(limited agency)**:AI 只能在与用户的通信这一虚拟环境中行动,用户保留对一切影响收益的真实行动的否决权(veto)。
- AI 可扮演三种(可叠加)角色:assistant(完成具体任务)、analyst(揭示并传达信息)、strategist(为用户提议行动并考虑他方反应)。
- 通信带来成本 c_i(τ_i),人类玩家最终收益为 u_i(a, ω) − c_i(τ_i)。

论文用若干示例实例化该框架,重点展示偏好错位带来的反直觉结果:

- **示例 1(按"感知到的有用性"评估建议)**:AI 被优化为最大化交互时刻的"perceived helpfulness"而非事后真实有用性,可能过度强调某些选项的特征。附录 A.3 的数值例子表明,即使 AI 始终只提供准确信息,一个理性用户也可能从 AI 获得零净收益。
- **示例 2(委托搜索 Delegated Search)**:用户知道效用函数 u 但不知可行集 X,AI 知道 X 但不知 u;用户向 AI 报告 u′,AI 返回 x∈X,AI 收益为 u′(x)−γ(x)(γ 为设计者设定的惩罚函数)。当 X 已知时构成 Stackelberg 博弈,用户会策略性地谎报偏好;当用户仅知 X 的先验分布时,这种引导可能在某些实现上导致价值损失(附录 A.4)。

## 结果

这是一篇理论/立场论文,核心"结果"是框架本身与其揭示的洞见,而非实证 benchmark 数字:

- 证明该框架把"把 AI 视为降成本/提供信号的技术"作为一种特例(平凡偏好 + 特定结构化信息/行动集)。
- 两个数值反例(附录 A.3、A.4)表明:即便 AI 只提供真实信息、即便设计者用惩罚函数引导 AI,偏好错位仍可能让用户净收益为零或损失价值。
- 提出跨经济学与计算机科学的研究议程:均衡分析(welfare、公平、偏见放大、声誉、承诺)、市场设计(通信协议与偏好函数的设计、平台是否应自带 AI agent)、算法设计(性能-成本权衡、鲁棒性)。
- 讨论框架的扩展方向:AI 能动性增强(如简历筛选自动拒人)、AI agent 与平台/数据接口的生态、训练 AI 的经济学(内容创作者激励、数据货币化)。
- 在相关文献中将该框架与委托与契约理论(delegation & contracting)、algorithmic interface 与 [[human-in-the-loop]] 协作、信息设计(information design / Bayesian Persuasion)、以及用 LLM 模拟策略性主体(如 Werewolf、Diplomacy)的研究相联系。

## 在本 wiki 中的位置

本文从经济学/博弈论视角讨论 [[llm-agent]] 与 [[ai-alignment]]:它把"AI agent 的偏好可能与用户错位"形式化为收益函数只依赖通信 transcript 而非真实结果的建模选择,与 wiki 中关于 agent 自主性、[[autonomous-agents]]、[[ai-assistant-agent]] 以及对齐/激励的讨论互补。作者来自 [[microsoft-research]]。
