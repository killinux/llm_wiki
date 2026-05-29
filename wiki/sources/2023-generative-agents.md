---
type: source
subtype: paper
tags: [llm, agents, simulation, memory, social]
created: 2026-05-29
updated: 2026-05-29
arxiv: "2304.03442"
raw: raw/2304.03442v2.pdf
authors: [Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein]
affiliations: [Stanford University, Google Research, Google DeepMind]
venue: "UIST 2023"
base_model: ChatGPT
published: 2023-04-07
revised: 2023-08-06
---

# Generative Agents：可交互的人类行为仿真体

一句话:提出 [[generative-agents]]——一种扩展 LLM 的智能体架构,能用自然语言**完整记录经历**
([[memory-stream|记忆流]])、随时间把记忆**综合成更高层的反思**、并**动态检索**以规划行为,从而
产生可信的个体行为与**涌现的社会行为**。作者:[[joon-sung-park|Joon Sung Park]] 等(Stanford +
Google,含 Percy Liang、Michael S. Bernstein)。

- **arXiv**:[2304.03442](https://arxiv.org/abs/2304.03442) · 2023-04-07 提交,2023-08-06 修订 · cs.HC / cs.AI / cs.LG · UIST 2023
- **基础模型**:ChatGPT(论文 footnote)
- **本地原文**:`raw/2304.03442v2.pdf`
- **代码 / Demo**:https://github.com/joonspk-research/generative_agents · https://reverie.herokuapp.com/UIST_Demo/

## 问题
可信的人类行为"代理"能赋能沉浸式环境、人际沟通排练、原型工具等交互应用。难点在于:让软件
智能体在**长时间跨度**上保持连贯、可信,能随不断累积的记忆、冲突、事件而**检索→反思→规划**,
并处理多智能体间级联的社会动态。

## 方法:智能体架构(三组件)
在 LLM(ChatGPT)之上扩展:
- **记忆流([[memory-stream]])**——以自然语言完整存档经历;记忆检索综合 相关性·近因·重要性。
- **反思 (reflection)**——周期性把记忆综合成更高层结论,反哺决策。
- **规划 (planning)**——把结论 + 环境转为高层日程,再递归细化为行动;反思与计划回灌记忆流。

## 实验:沙盒小镇
在受《模拟人生 (The Sims)》启发的可交互沙盒里部署 **25 个智能体**,用户可用自然语言观察与干预。

## 结果:涌现社会行为
仅给定"某智能体想办情人节派对"这一个设定,智能体们在两天内**自发**传播邀请、结识新朋友、
互相约对方做舞伴,并协调在正确时间到场。**消融实验**表明 **观察 / 规划 / 反思** 三者各自对
行为可信度有关键贡献。

## 在本 wiki 中的位置
为 [[llm-agents|LLM 智能体]] 开辟"**可信行为仿真 / 社会模拟**"分支,区别于以 [[react|ReAct]] →
[[language-agent-tree-search|LATS]] 为代表的"任务求解 + 搜索"分支。其"反思"机制与
[[reflexion|Reflexion]] 同名但目的不同(前者综合长期记忆以维持可信人格,后者从失败中纠错)。

> 待深入:记忆检索打分的具体公式、规划/反思的提示结构、沙盒交互细节——可在后续单独建页。
