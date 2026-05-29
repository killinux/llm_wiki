---
type: source
subtype: paper
tags: [generative-agents, llm-agent, social-simulation, user-simulation, interactive-evaluation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2411.10109
raw: raw/2411.10109.pdf
authors: [Joon Sung Park, Carolyn Q. Zou, Jonne Kamphorst, Niles Egan, Aaron Shaw, Benjamin Mako Hill, Carrie Cai, Meredith Ringel Morris, Percy Liang, Robb Willer, Michael S. Bernstein]
year: 2024
---

# LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals

用基于真人自述(深度访谈 + 结构化问卷)构建的 [[generative-agents]],可对单个个体在多种社会科学结果上进行通用模拟,在留出题目上的预测精度可接近个体自身两周后的重测一致性。

## 问题

机器学习在拥有大量结构化数据、目标明确的领域能很好预测人类行为,但这些模型通常局限于特定结果、难以迁移到新领域。社会科学家和政策制定者关心的许多场景缺乏所需的个体背景信息。[[large-language-models]] 提供了一条新路径:给定对个体的描述,同一个底层模型可被查询用于多种结果,而无需为每个结果训练新模型。关键在于如何用关于具体个体的可靠信息有效"接地"(grounding),并降低 LLM 依赖人口统计学刻板印象的倾向。

## 方法

招募了近似美国成年人分布(年龄、性别、种族、地区、教育、党派)的分层样本 N=1052。每位参与者:

- 完成约 2 小时的语音对语音 AI 访谈(采用 American Voices Project 访谈协议,半结构化:固定问题 + AI 访谈员实时生成的追问;转录平均 6491 词)。
- 完成结构化问卷:GSS(General Social Survey 核心模块,177 项)与 [[big-five]] 人格量表 BFI-44(44 项)。
- 参与 5 个真金白银的经济博弈(独裁者博弈、信任博弈、公共品博弈、囚徒困境)。
- 参与 5 个带对照/处理条件的社会科学复制实验。

两周后重做同一套问卷与实验,作为 ground truth 与重测一致性基线。

基于这些数据构建三类 [[generative-agents]]:
- **Interview agent**:仅用访谈转录。
- **Survey agent**:仅用 GSS + BFI-44 结构化作答。
- **Survey+Interview agent**:两者结合。

查询时将相应输入注入 prompt,指示模型模仿该个体作答。基线对照:**demographic-based**(仅人口统计属性,类似以往工作)与 **persona-based**(参与者自写简短个人简介段落)。

核心指标 **normalized accuracy** = agent 预测精度 / 个体自身重测一致性;1.0 表示 agent 预测与个体两周后自我复现一样准。连续变量用 normalized correlation。为防直接答案泄露,从 survey agent 输入中剔除被评测的题目;并过滤掉 27 个与访谈问题重合的 GSS 题(177→150 评测题)。核心分析已在 OSF 预注册。

## 结果

GSS(150 核心题,平均 3.31 个选项,随机基线精度 0.30):
- Interview agent normalized accuracy = 0.83(std 0.11;原始精度 65.67% ÷ 自我一致性 79.53%)。
- Survey agent = 0.82(std 0.11)。
- Survey+Interview agent = 0.86(std 0.09)。
- Demographic-based = 0.74;Persona-based = 0.71。三类自述 agent 显著优于两个基线(ANOVA 拒绝无差异零假设)。

Big-5 人格(BFI-44):
- Interview agent normalized correlation = 0.80(原始 r=0.78 ÷ 重测相关 0.95)。
- Demographic = 0.61,Persona = 0.75;Survey+Interview = 0.77。
- MAE 方面 Interview(0.665)优于 demographic(0.755)与 persona(0.737),但高于 survey agent(0.622)。

经济博弈(连续,标准化到 0-1):Interview agent normalized correlation = 0.66;Survey = 0.38;Survey+Interview = 0.49(MAE 各 agent 间无显著差异)。

实验复制(5 个研究):各类 agent 估计的效应量与参与者高度相关(r 从 0.91 到 0.99),整体模式与以往观察一致。

消融:随机删除 80% 访谈转录(去掉 96/120 分钟),interview agent 仍达 GSS 0.79、Big-5 0.73;将访谈转为去除语言风格的要点摘要(interview-summary agent)得 GSS 0.84、Big-5 0.70,说明预测力主要来自信息内容而非语言线索。

公平性:用 Demographic Parity Difference(DPD)度量按政治立场、种族、性别分组的最优组与最差组的性能差距;更丰富的自述数据相对仅用人口统计 prompt 的方法降低了精度上的群组差异。

## 在本 wiki 中的位置

本文是 [[generative-agents]] / [[social-simulation]] / [[user-simulation]] 方向的代表作,延续了 [[joon-sung-park]]、[[michael-s-bernstein]]、[[percy-liang]] 等 [[stanford-university]] 与 [[google-deepmind]] 团队的研究线。与早期 generative agents 侧重沙盒行为不同,本文聚焦"以个体真人自述接地"以实现可评测的通用个体模拟,并引入"以个体重测一致性归一化"的评测框架。可与 [[llm-agent]]、[[role-playing-agent]]、[[interactive-evaluation]] 等条目互参。
