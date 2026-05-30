---
type: concept
subtype: method
tags: [game-theory, multi-agent, social-simulation, reinforcement-learning, cooperation]
created: 2026-05-30
updated: 2026-05-30
sources: 8
---

# 博弈论 (Game Theory)

博弈论是研究**多个理性决策者(玩家)在策略互动中如何选择行动**的数学框架:每个玩家的收益(payoff)不仅取决于自己的动作,
还取决于其他玩家的动作。它为多智能体系统、社会模拟与对齐研究提供了刻画**合作 / 竞争 / 协调**的标准语言。

## 核心概念
- **博弈要素**:玩家、动作/策略空间、收益函数、信息结构(完全/不完全信息)。
- **均衡 (equilibrium)**:无人能通过单方面改变策略获益的稳定状态,最常用的是 **Nash 均衡**;序贯博弈用子博弈完美均衡。
- **博弈类型**:
  - **零和 vs 非零和**;**合作 vs 非合作**;一次性 vs **重复博弈**(repeated game,可支撑合作涌现)。
  - 经典范式:**囚徒困境 (Prisoner's Dilemma)**、**协调博弈 (Coordination Game)**、公共品博弈、独裁者/信任博弈、社会困境 (social dilemma)。

## 在 LLM 智能体与社会模拟中的角色
博弈论是 [[generative-social-simulation]] 一条主线的分析工具——用来检验 LLM 智能体是否表现出类人的策略行为:
- **协调与约定涌现**:[[2025-emergent-llm-behaviors-data-leakage]] 复测的 "naming game" 即一个**协调博弈**,争议在于 LLM 的"涌现约定"
  是否只是复述了预训练中的博弈论知识。
- **合作 / 社会困境**:[[2025-llm-agents-cooperate-social-dilemma]]、[[2025-emergent-coordination-multi-agent-language-models]] 研究
  LLM agent 在重复社会困境中能否维持合作。
- **竞争 / 策略识别**:[[2025-llm-agent-game-theory-strategy-recognition]]、[[2026-llm-agents-competition-cooperation-games]];
  [[2023-waragent-world-war-simulation]] 把国家建模为博弈玩家研究开战条件。
- **经济博弈作为评测**:[[2024-generative-agents-self-reports]] 用独裁者/信任/公共品/囚徒困境等真金博弈检验 agent 对真人选择的复刻度。

## 与强化学习的关系
[[reinforcement-learning]] 的多智能体扩展(MARL)与博弈论深度交叉:[[alphago]] 用自博弈(self-play)逼近最优策略;
[[2025-llm-collaboration-marl-magrpo]] 等把 MARL 用于 LLM 协作。重复博弈中的合作/背叛动态也是 [[multi-agent-systems]] 的核心议题。

## 相关页
[[multi-agent-systems]]、[[reinforcement-learning]]、[[social-simulation]]、[[generative-social-simulation]]、[[alphago]]
