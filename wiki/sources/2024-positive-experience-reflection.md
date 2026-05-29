---
type: source
subtype: paper
tags:
  - llm-agent
  - reflection
  - self-reflection
  - text-based-games
  - agent-memory
  - reasoning
created: 2026-05-29
updated: 2026-05-29
arxiv: 2411.02223
raw: raw/2411.02223.pdf
authors:
  - Philip Lippmann
  - Matthijs T.J. Spaan
  - Jie Yang
year: 2024
---

# Positive Experience Reflection for Agents in Interactive Text Environments

提出 Sweet&Sour:让 [[llm-agents|llm-agent]] 在交互式文本环境中不仅从失败中反思,还从**成功经验**(positive experience)中反思,并配合双缓冲“managed memory”管理短期/长期记忆,从而缓解既有 [[self-reflection]] 方法“初始成功后失效”和“小模型上效果差”的两大局限。

## 问题

text-based games(TBGs,文本冒险游戏)是评测智能体 [[reasoning]]、适应性与学习能力的高难场景,要求 planning、记忆、空间推理与常识。基于 [[large-language-models]] 的 agent 配合内部 [[reflection]] 改进 planning 已展现潜力,但作者指出现有 [[self-reflection]](与 self-refinement 相关,基于环境的二元/标量反馈做事后推理,如 [[reflexion]])存在三大局限:

1. 当 agent 初始就成功时,反思反而带来 underwhelming 的收益(无错可纠);
2. 在更小的 LLM 上效果显著变差;
3. 依赖外部反馈。

根本原因在于,既有方法只从**失败**中学习,忽视了像人一样“强化成功行为”的重要性。

## 方法

把 LLM 视作 actor model,在每个 time step $t$ 从策略 $\pi_\theta$ 采样动作 $a_t$ 并接收观测 $o_t$;每个任务由若干 sub task 组成,完成 sub task 给予稀疏奖励累加到 $r_t$,最多 150 步。两大组件:

- **Sweet&Sour 反思**:在 self-reflection 中同时纳入正向(sweet)与负向(sour)经验。当当前策略正在获得奖励时,主动 query agent 去 verbalize“是什么让当前策略成功、可以泛化出什么”;失败时仍按传统方式反思。区别于 [[reflexion]] 仅在一轮失败后跨 attempt 反思,Sweet&Sour 在**每个 sub goal 完成后**即时反思,使其反思立刻可用于下一 timestep(见论文 Figure 1 与 [[react]]、[[reflexion]] 的对比)。
- **Managed memory(双缓冲记忆)**:用短期/长期两类 [[agent-memory]] 按结果(成功/失败)与 recency 存取相关反思。sub goal 达成时,把 $(\text{reflection}_t, o_t, a_t, r_t)$ 元组存入短期缓冲;任务完成或 attempt 结束时,短期记忆全部转入长期记忆;失败 attempt 的反思则立即写入长期记忆供下一 attempt 使用。

作者称该方法广泛适用于带反馈、用 self-reflection 的交互式文本 agent,包括在反思 loop 之上叠加 grounding 或 gradient learning 的复杂方法。

## 结果

在 [[scienceworld]] benchmark 上评测(10 个互联场景、200+ 物体、25 个 action template,30 个任务各最多 10 个变体,平均最优决策深度约 50 步;success score 0–100)。基线含 CALM(DRRN + 因果语言模型重排)、[[react]] 与 [[reflexion]](最多 4 轮)。模型按参数量从大到小:[[gpt-4o]](gpt-4o-2024-08-06)、Mistral Large 2(mistral-large-2407)、[[llama-3]] 8B(llama-3.1-8b-instruct)。

主要数字(各方法的平均 success score):

- Sweet&Sour 在所有 LLM 上均优于基线,**GPT-4o 上平均 54.6** 为最高(对比 ReAct 36.0、Reflexion 45.3、CALM 5.07)。
- 模型越小,优势越大:Mistral Large 2 上 **44.6 vs Reflexion 27.6**;Llama 8B 上 **32.5 vs 21.7**,说明该方法更适合算力受限场景。
- 消融:若改为仅从失败采样,性能跌回 Reflexion 水平(Llama 8B 24.6、Mistral Large 2 31.1、GPT-4o 44.9),证实纳入正向经验确有增益。
- **Anti-Tilt**:在中等难度任务(如 3-2、3-3)上差距最明显——传统方法不反思早期成功,失去推进动量而“tilt”(持续下滑);例如任务 3-2,Sweet&Sour 用 GPT-4o 得 68.0,远超 Reflexion 的 24.7,也优于 ReAct 的 55.6。

局限:LLM 推理能力无保证;仅在单一环境(ScienceWorld)上评测。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 的 [[self-reflection]] / [[agent-memory]] 方向,可与 [[reflexion]](仅从失败跨 attempt 反思)、[[react]](reasoning+acting 基线)、[[self-refine]] 对照阅读。其核心论点——反思应同时强化成功经验、并用结构化记忆管理——延伸了 verbal reinforcement 一脉;评测基准 [[scienceworld]] 优先于更简单的 [[alfworld]]。涉及模型 [[gpt-4o]]、[[llama-3]] 与 Mistral Large 2。
