---
type: source
subtype: paper
tags: [llm-agent, context-aware-guidelines, offline-learning, web-navigation, in-context-learning, self-reflection]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2403.08978
raw: raw/2403.08978.pdf
authors: [Yao Fu, Dong-Ki Kim, Jaekyeom Kim, Sungryull Sohn, Lajanugen Logeswaran, Kyunghoon Bae, Honglak Lee]
year: 2024
---

# AutoGuide: Automated Generation and Selection of Context-Aware Guidelines for Large Language Model Agents

AUTOGUIDE 从离线经验中自动生成并按当前情境检索"上下文感知指引"(context-aware guidelines),从而帮助 [[large-language-models]] 智能体在网页导航等陌生领域做出更好的序列决策。

## 问题

[[llm-agents|llm-agent]] 在序列决策任务中主要依赖 demonstration-based [[in-context-learning]],即把示范轨迹作为 in-context 示例。但在 web navigation 等 LLM 缺乏先验知识的目标领域,这种范式效果有限:成功率低,且把全部离线经验当作示范又会受 context 长度限制、prompt 敏感性以及复杂推理困难的影响。论文要解决的核心挑战是:如何有效地从离线数据中抽取出隐含的可执行知识,以指导智能体决策。

## 方法

AUTOGUIDE 把离线轨迹中的隐含知识压缩为简洁的自然语言指引,且每条指引带有条件结构(明确说明"在什么情境下适用")。包含两个核心模块:

- 上下文识别模块(context identification module):把部分轨迹 τ:t 抽象为一段简洁的自然语言 CONTEXT,描述智能体当前所处状态。
- 指引抽取模块(guideline extraction module):利用一对对比轨迹 τ⁺(高回报)与 τ⁻(低回报),找到二者开始分叉的偏离时间步 t,对共享前缀生成 CONTEXT,再对比这对轨迹抽取出对应的指引(例如"在 Reddit 主页上,若想导航到某个具体 forum,应点击位于 'link Wiki' 上方的 'link Forums'")。

生成的指引以 CONTEXT 为 key、指引为 value 组织成字典 G,并用 LLM 判断新 context 是否与已有 context 重复以去冗余(Algorithm 1)。测试时(Algorithm 2),对当前轨迹识别 CONTEXT,用 selection 模块按 top-k 选取相关指引,把 context 与指引一起注入动作生成 prompt。相较于 [[expel]],AUTOGUIDE 的指引选择是 contextual 的(按当前状态检索),而非把所有指引一股脑提供给智能体。

实现上:WebShop/ALFWorld 用 [[gpt-3-5-turbo]] 作为基座([[react]] 智能体),WebArena 用 [[gpt-4]];指引抽取统一用 GPT-4-turbo;多模态实验用 GPT-4V 配合 Set-of-Marks (SoM)。

## 结果

在三个序列决策 benchmark 上(Table 1),AUTOGUIDE 显著超过 [[react]] 与 [[expel]]:

- [[alfworld]] 成功率 79.1%(ReAct 54.5%,ExpEL 59.0%)。
- [[webshop]] reward 73.4 / SR 46%(ReAct 66.4/30%,ExpEL 60.9/35%)。
- [[webarena]](Reddit 域)SR 47.1%(ReAct 8.0%,ExpEL 21.8%)。

与自反馈方法 [[reflexion]] 结合时进一步提升:ALFWorld 88.1%、WebShop reward 81.4 / SR 57%,说明上下文感知指引提供的 inter-task 知识与 Reflexion 的 intra-task 知识互补(ExpEL+Reflexion 反而不如 ExpEL 单独,可能因引入无关指引干扰反馈)。

多模态真实网站实验(Table 2,GPT-4V + SoM 基座):GitHub SR 19/30(基线 SoM 2/30),Flights 9/20(5/20),Coursera 14/20(1/20)。消融实验显示:增加 ReAct in-context 示例数(1→6-shot)收益有限(SR 30%→38%),仍低于 AUTOGUIDE 的 46%(Table 3);top-k 在 k=2 左右最优(WebShop SR 46%,Table 4)。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 通过经验学习提升决策的方向,与 [[expel]](从离线经验抽取指引但非上下文感知)和 [[reflexion]](测试时 intra-task 自反馈)形成对照与互补,基座方法为 [[react]]。评测覆盖 [[alfworld]]、[[webshop]]、[[webarena]] 等智能体 benchmark,可与 [[self-reflection]]、[[experiential-learning]]、[[in-context-learning]] 等概念页互相参照。作者来自 [[university-of-michigan]] 与 [[lg-ai-research]]。
