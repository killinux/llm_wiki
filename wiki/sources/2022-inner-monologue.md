---
type: source
subtype: paper
tags: [embodied-ai, robotics, llm-planning, closed-loop-feedback, grounding]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2207.05608
raw: raw/2207.05608.pdf
authors: [Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tompson, Igor Mordatch, Yevgen Chebotar, Pierre Sermanet, Noah Brown, Tomas Jackson, Linda Luu, Sergey Levine, Karol Hausman, Brian Ichter]
year: 2022
---

Inner Monologue 提出让 LLM 在机器人规划中通过持续注入自然语言环境反馈,形成"内心独白",从而在不做任何额外训练的前提下实现闭环、可重新规划的具身推理。

## 问题

把 LLM 的推理能力用于机器人等具身任务时,规划者不仅要决定"做什么技能",还要决定"何时做、怎么做",这些答案会随智能体自身的行动结果不断变化。此前用 LLM 做规划的工作(如 [[saycan]]、Huang et al. 的 zero-shot planner)大多是单向的:LLM 一次性吐出技能序列,无法根据执行中产生的失败、场景变化或人类反馈来修正或重规划。因此在动态、随机扰动或低层策略不可靠的环境中,这类开环系统鲁棒性差。本文研究:在不微调的情况下,LLM 能在多大程度上读懂并利用通过自然语言提供的各类反馈来"闭合"智能体-环境回路。

## 方法

核心思想是把多种来源的环境反馈持续地以文本形式注入 LLM 的规划提示中,形成一段随交互不断增长的"内心独白"。系统只用 frozen 的预训练 LLM 配合少样本提示(few-shot prompting),不做任何额外训练,并配合一组预训练、语言描述的机器人技能 π_k。

研究的反馈来源分为三类:
- Success Detection(成功检测):对低层技能是否成功的二分类,以语言形式("Action was successful / not successful")反馈,称为 Success 反馈。
- Passive Scene Description(被动场景描述):每步都自动注入的结构化场景信息,典型形式是物体识别(Object 反馈),以及仿真重排任务中描述任务进度子目标的 Scene 反馈。
- Active Scene Description(主动场景描述):LLM 主动提问、由人或 [[vqa]] 模型回答的非结构化反馈,本文只用人类回答(Human 反馈)。

在 Object + Scene 变体中,因推理复杂度更高,加入 [[chain-of-thought]] 可提升推断目标与已达成目标的一致性。系统在三个域中分别实例化:仿真桌面重排(用 InstructGPT + CLIPort 类拾放原语)、真实桌面重排(用 InstructGPT + MDETR 开放词表识别)、真实厨房移动操作(用 [[palm]] + SayCan 的价值函数做 affordance grounding)。

## 结果

- 仿真桌面重排(Ravens,50 episodes,带测试时扰动):Inner Monologue(Object + Scene)在所有任务上表现最佳。已见任务"Pick and place"达 94%、"Put all the blocks in the [x] bowl"达 56%;未见任务"Put the blocks on mismatched bowls"达 86%、"Put the blocks in their matching bowls"达 82%。对比之下纯 CLIPort 在未见任务上全部为 0%,LLM + Object 单一反馈也明显更低。
- 真实桌面拾放(每任务 10 次):Inner Monologue(Object + Success)整体成功率 90%,其中"Finish 3-block stacking"达 100%、"Sort fruits from bottles"达 80%;而仅用 LLM + Object 的开环基线整体仅 20%。两类具身反馈互补。
- 真实厨房移动操作(120 次评估,基线为 [[saycan]]):无扰动时 Inner Monologue(Object + Success)在 Manipulation 75%、Mobile Manipulation 75%、Drawers 100%;加入对抗性扰动后,SayCan 因无显式重试行为成功率接近 0%,而 Inner Monologue 整体从 SayCan 的 30.8% 提升到 60.4%。
- 涌现能力(均无对应提示样例):对中途变更的高层目标做持续适应、在原目标不可行时自主提出替代目标(如"换一个更轻的积木")、多语种交互(用中文给的新指令也能被正确解读并重规划)、以及结合历史行动回答场景问题。

## 在本 wiki 中的位置

本文是 LLM 用于具身规划/机器人控制谱系中的关键一环,直接建立在 [[saycan]] 的 affordance grounding 之上,并把单向的 LLM 规划扩展为闭环、可重规划的范式。它依赖 [[chain-of-thought]] 提升推理一致性,使用 [[instructgpt]] 与 [[palm]] 作为规划骨干,并与 [[vqa]]、grounding 等概念相关,可与 ReAct 等"推理-行动交错"工作对照阅读。
