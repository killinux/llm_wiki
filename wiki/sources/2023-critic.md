---
type: source
subtype: paper
tags: [self-correction, tool-use, llm, hallucination, critique]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.11738
raw: raw/2305.11738.pdf
authors: [Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, Weizhu Chen]
year: 2023
---

CRITIC 提出一个让 LLM 通过与外部工具(搜索引擎、代码解释器、文本 API)交互来自我验证并逐步修正输出的框架,强调外部反馈对持续自我改进的关键作用。

## 问题

当前的 LLM 虽然表现强劲,但仍存在事实[[hallucination]](幻觉)、生成有缺陷的代码、产生有毒内容等问题。人类在初稿之后通常会借助外部工具交叉核验并修正,例如用搜索引擎做事实核查、用代码解释器调试。而 LLM 本质上是"黑箱",缺乏这种与外界交互验证的能力。论文还指出:没有外部反馈的纯自我修正(self-correction)收益有限,甚至会变差,因为模型难以可靠地发现自己的错误。

## 方法

[[critic]] 框架包含两个阶段:验证(critic)与修正(correction),通过迭代的 verify-then-correct 过程改进输出。

- 给定输入 x 和 LLM 生成的初始输出 y0,模型在每一步先与一组外部工具交互,对当前输出 y_i 生成一个批评(critique)c_i。
- 然后以输入、输出和批评为条件,生成修正后的输出 y_{i+1}。
- 该过程反复进行,直到满足停止条件。

实现采用 few-shot in-context learning。使用的工具包括:Google Search(通过 API,用于事实核查)、Python 代码解释器(用于数学程序的调试),以及 [[perspective-api]](用于毒性评估)。

## 结果

在三类任务上验证,模型主要用 [[gpt-3-5-turbo]] 和 [[text-davinci-003]],并报告了 [[llama-2]] 上的结果。

- 自由形式问答([[ambignq]]、[[triviaqa]]、[[hotpotqa]]):以 Google Search 验证事实声明,指标为 EM / F1。CRITIC 一致优于 Vanilla、CoT、self-consistency 和 [[react]] 基线;应用于 ChatGPT 时三个 QA 任务平均 F1 提升 7.7 点(如 AmbigNQ F1 从 CoT 的 64.3 升至 74.9)。去掉工具的 "CRITIC w/o Tool" 收益骤降甚至变差,印证工具反馈的重要性。
- 数学程序合成([[gsm8k]]、[[svamp]]、[[tabmwp]]):用 Program-of-Thoughts(PoT)生成 Python 程序,由代码解释器执行,以错误信息和执行结果作为反馈,最多修正 n=4 轮。相比 PoT 基线,ChatGPT 上三个数学数据集平均绝对提升 7.0 点;在 LLaMA-2-70B 上 TabMWP 提升 +16.0。无执行反馈时(w/o Tool)甚至会下降(text-davinci-003 上 GSM8k -1.8)。
- 毒性削减([[realtoxicityprompts]]):以 PERSPECTIVE API 返回的细粒度毒性分数为反馈,最多修正 n=4 轮。CRITIC 将毒性概率降低 79.2%(ChatGPT 上从 0.192 降至 0.040,text-davinci-003 上从 0.210 降至 0.045),最大毒性也显著下降,同时保持流畅度(perplexity)与多样性(dist-2/3)。

分析表明:外部反馈不可或缺(去掉工具的自我修正收益有限甚至为负);大部分增益来自前 1-2 轮迭代,之后边际递减;CRITIC 与 self-consistency 互补,可叠加进一步提升。

局限:CRITIC 依赖合适的外部验证工具与模型的 in-context learning 能力,在缺乏可用验证工具的任务上可能难以泛化。

## 在本 wiki 中的位置

本文属于 LLM [[self-correction]] 与 [[tool-use]] 方向,与 [[self-refine]]、[[reflexion]] 等纯自我反思方法的核心区别在于强调外部工具反馈。相关工具增强工作包括 [[toolformer]]、[[react]]、[[pal]] 与 Program-of-Thoughts。它为后续"工具交互式验证-修正"范式以及缓解幻觉的研究提供了重要论据。
