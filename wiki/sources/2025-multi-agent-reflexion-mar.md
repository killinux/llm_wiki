---
type: source
subtype: paper
tags:
  - llm-multi-agent
  - reflexion
  - self-reflection
  - multi-agent-debate
  - reasoning
  - code-generation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2512.20845"
raw: raw/2512.20845.pdf
authors:
  - Onat Ozer
  - Grace Wu
  - Yuchen Wang
  - Daniel Dosti
  - Honghao Zhang
  - Vivi De La Rue
year: 2025
---

# MAR: Multi-Agent Reflexion Improves Reasoning Abilities in LLMs

一句话:本文复现了 [[reflexion]] 框架,指出其"同一模型既行动又自评又反思"导致确认偏误与思维退化,并提出 Multi-Agent Reflexion(MAR)——用一组多 persona 的批评者加一个 judge 来合成反思,从而在 [[hotpotqa]] 与 [[humaneval]] 上稳定超过单 Agent Reflexion。

## 问题

[[reflexion]](Shinn et al. 2023)是一种无需更新参数的轻量级"语言强化"方法:[[llm-agent]] 在失败后用自然语言反思错误,把反思作为 episodic memory([[memory-stream]] 式记忆)指导下一次尝试。它在多跳问答与代码生成上相对 baseline 有明显提升。

但作者在复现中发现 Reflexion 的单 Agent 设计存在系统性缺陷:Actor(行动)、Evaluator(评估)、Self-Reflector(反思)是同一个模型,导致:

- 确认偏误(confirmation bias):反思往往只是重述错误推理、用更多错误逻辑为其辩护、或做表面修改。
- 思维退化([[degeneration-of-thought]])/ mode collapse:多次重试产出近乎相同的解,反复在同一概念错误上失败。

作者还观察到 [[hotpotqa]] 的 Exact Match([[exact-match]])指标过于严苛,会把语义正确但格式/同义词不同的答案判为错误(如 "women's interest magazines" 对 "women interest magazine";"Stone Brewing Co" 对 "Stone Brewing"),反而把 Agent 的反思引向错误方向直至超时。

## 方法

MAR 用一支协调的多 persona 批评团队替换 Reflexion 的单 Agent 自我批评,核心受 Society of Mind 与 [[multi-agent-debate]](MAD)启发。流程为:

1. Actor Attempt:Actor 用与标准 Reflexion 相同的 baseline 模型先作答。
2. Evaluation:若错误则触发 debate 模块(评估器同 Reflexion)。
3. Initial Diagnosis:把 Actor 的失败 scratchpad 传给 judge,judge 让每个 persona 写出失败诊断。
4. Debates:各 persona 互相同意/反对并精炼批评(最多 2 轮)。
5. Consensus & Reflection:judge 把辩论综合成一条可执行的 "Consensus Reflection"。
6. Retry:把这条反思注入 Actor memory 指导下一次尝试。

persona 沿三条轴设计以保证推理多样性:Evidence Exploitation、Exploration、Specification strictness。HotPotQA 用 4 个 debater(Skeptic、Logician、Creative、Verifier),HumanEval 用 3 个(Senior Engineer、QA Engineer、Code Reviewer)。所有角色均用 [[gpt-3-5-turbo]],以隔离"多 Agent 推理"本身的贡献。HotPotQA 每题最多 5 次试(初始 + 4 次 MAR 引导重试),HumanEval 最多 3 次。

## 结果

复现与 MAR 实验均在 100 道困难 HotPotQA 题与 HumanEval 上进行:

- HotPotQA Exact Match(GPT-3.5):ReAct baseline 32.0 → Reflexion+ReAct 44.0 → MAR 47.0(相对 Reflexion +3 分)。原 Reflexion 论文报告 ReAct 34 / Reflexion 51。
- HumanEval pass@1:GPT-3.5 baseline 67.1 → Reflexion(GPT-3.5)76.4 → MAR 82.6(相对 Reflexion +6.2 分);GPT-4 baseline 81.7。复现的 Reflexion(GPT-4)为 89.4,原论文 91.0。
- MAR 减少了单 Agent Reflexion 的停滞(stagnation):跨 5 个 trial,MAR(图 3 红线)持续高于 Reflexion(蓝线)与 baseline(灰线)。

作者强调:HotPotQA 上 MAR 增益小于 HumanEval,主要归因于 EM 指标对格式敏感(附录 A/B/E 给出具体失败案例),更宽容的指标(F1、语义匹配 / [[llm-as-judge]])预计会显示更强的 MAR 优势。

局限:MAR 每个任务约需 300–400 次 API 调用,约为单 Agent Reflexion 的 3 倍,计算成本与延迟显著上升,在大规模 benchmark 或真实 Agent 系统上可扩展性受限。

## 在本 wiki 中的位置

本文是 [[reflexion]] 的多 Agent 扩展,把 [[self-reflection]] / [[self-refine]] 路线与 [[multi-agent-debate]] / [[llm-multi-agent]] 路线结合,直接关联 [[degeneration-of-thought]] 这一失败模式,以及 [[react]]、[[chain-of-thought]] 等 Actor 提示策略。评测上挂靠 [[hotpotqa]] 与 [[humaneval]] 两个基准,并对 [[exact-match]] 指标的局限提出了实证批评,可作为"无需训练的自我改进 Agent"专题下的一个具体案例研究。
