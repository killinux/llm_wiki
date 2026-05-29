---
type: source
subtype: paper
tags:
  - reasoning
  - introspection
  - ai-welfare
  - machine-consciousness
  - self-reflection
  - evaluation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2512.04588"
raw: raw/2512.04588.pdf
authors:
  - Robert Long
year: 2025
---

# The Mirror Loop: Recursive Non-Reasoning and the Collapse of Cognitive Depth in Large Language Models

提出 **mirror loop**(镜像循环)这一极简递归探针:让模型反复审视自己上一轮输出并"找出新东西",结果在所有模型家族上语义新颖度都在第 10 轮前坍缩到 0.05 以下,支持"模式补全(pattern completion)而非真正推理"的假说。

## 问题

[[large-language-models]] 能产出看似有推理、有反思、有内省的流畅文本。当被要求审视自身推理时,它们会生成关于自身内部过程的第一人称叙述。核心问题是:这些系统是在进行真正的认知/认识论处理(genuine epistemic processing),还是在做模仿推理表面形式的复杂模式补全?这一问题与机器意识、AI welfare([[ai-safety]] 相关的道德地位讨论)以及内省自我报告(introspective self-report)的可信度密切相关——若模型能准确报告丰富的内部状态,可能影响其道德地位的判断。作者需要一种能区分"真实认知"与"表面模仿"的可证伪的经验方法。

## 方法

**Mirror loop 协议**:从种子提示开始得到响应 r0;此后每一轮 t,把上一轮响应 r(t-1) 喂回模型,要求其审视并"找出新东西",响应 r(t) 成为下一轮输入,迭代 T 轮。协议刻意极简——不引入外部信息、无任务目标、无反馈信号,从而隔离出模型"自生成新颖性"的能力。

**四个互补度量**:
- **语义新颖度(semantic novelty)**= 1 − 连续响应嵌入间的 cosine similarity(用句向量模型生成嵌入);
- **词汇新颖度(lexical novelty)**= 连续响应词集间的 Jaccard distance;
- **自指频率(self-reference frequency)**= 每条响应中自指词("I"、"my"、"this response"等)的频率;
- **抽象漂移(abstraction drift)**= 基于抽象词词表,跟踪抽象词频率随轮次的变化。

**实验设计**:40 次运行,每次 50 轮,跨四个模型家族——OpenAI [[gpt-4]] 级模型([[openai]])、Anthropic [[claude]]([[anthropic]])、Google [[gemini]]([[google]])、本地 [[qwen]] 模型([[local-model]])。

**三种干预**:温度提升(temperature elevation)、显式反重复指令(anti-repetition instructions)、语义距离奖励(semantic distance rewards)。

**可证伪框架(falsifiability framework)**:事先声明若为真实推理应观察到——持续的语义新颖度、抽象度增长、新概念结构涌现、非收敛轨迹;若为模式补全应观察到——语义新颖度快速衰减、收敛到不动点、近乎逐字重复、抽象度稳定或下降。

## 结果

- **新颖度坍缩**:语义新颖度在所有条件下快速坍缩,第 10 轮前跌破 0.05 并维持到结束,连续响应近乎逐字重复。最后 10 轮各模型家族的平均语义新颖度均低于 0.05。
- **模型差异**:OpenAI、Anthropic、Google 模型呈单调衰减到单一不动点;本地 [[qwen]] 模型呈独特的振荡模式,在少量响应间来回摆动产生周期性的新颖度尖峰,但绝对值仍很低。
- **词汇新颖度**:Jaccard distance 同样快速衰减,衰减略慢于语义新颖度。
- **自指频率**:全程保持高且稳定——内省的表面形式(第一人称自指)持续存在,而实质新颖度消失。即流畅的自指不等于真正的自我审视。
- **抽象漂移**:幅度很小,没有持续的抽象度增长证据。
- **干预效果**:三种干预均无法阻止坍缩。温度提升使早期新颖度略高、衰减略慢;反重复指令几乎无效(模型口头承认但仍收敛);语义距离奖励效果最大,提高了渐近新颖度并减缓衰减,但仍最终坍缩到低值。

数据一致支持模式补全假说。作者认为 mirror loop 是区分"生成式重组"与"真正认识论处理"的诊断探针,对 [[self-refine]]、[[reflexion]]、[[constitutional-ai]] 等自我改进方法构成警示:缺乏外部反馈或新信息时,递归自我审视会收敛而非改进,自我改进系统可能需要外部 grounding。

## 在本 wiki 中的位置

本文属于 [[reasoning]] 与 [[evaluation]] 交叉的方法/批判性研究,与"LLM 是否真在推理 vs 模式匹配"的争论直接相关,可与 [[chain-of-thought]]、[[self-reflection]]、[[self-correction]]、[[self-improvement]] 对照阅读。它对依赖模型内省的 [[self-refine]]、[[reflexion]]、[[constitutional-ai]] 给出经验限制,并与机器意识/AI welfare 讨论([[ai-safety]])相联系。作者 Robert Long 为独立研究者。
