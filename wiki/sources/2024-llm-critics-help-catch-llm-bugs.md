---
type: source
subtype: paper
tags: [scalable-oversight, rlhf, critic, code-generation, ai-safety, llm-as-judge]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2407.00215
raw: raw/2407.00215.pdf
authors: [Nat McAleese, Rai (Michael) Pokorny, Juan Felipe Cerón Uribe, Evgenia Nitishinskaya, Maja Trębacz, Jan Leike]
year: 2024
---

# LLM Critics Help Catch LLM Bugs

OpenAI 训练了名为 **CriticGPT** 的 GPT-4 级别 critic 模型,用 RLHF 让 LLM 写出指出代码错误的自然语言批评,从而帮助人类更准确地评估模型生成的代码——这是 [[scalable-oversight]] 在真实助手任务上的首次实证。

## 问题

[[rlhf]] 从根本上受限于人类正确评估模型输出的能力。随着模型能力增强,即使是经验丰富的专家也将无法可靠判断输出的质量或正确性,这是 RLHF 的根本性缺陷。若评估中存在系统性偏差且被强优化,可能导致危险策略。[[scalable-oversight]](可扩展监督)领域旨在通过训练模型帮助人类正确评估模型输出来解决该问题。本文聚焦于 LLM 助手最重要且经济价值高的应用之一:写代码,demonstrate scalable oversight 能帮助人类更全面地评估模型写出的代码方案。

## 方法

核心思路沿用 Saunders et al. 的 [[self-critique]] 路线:训练一个自回归策略,接受 (question, answer) 对作为输入,输出指出该答案中错误的文本批评(critique)。批评以 markdown 引用的形式高亮答案片段并附上对应评论。与前人不同,本文在更具挑战性的真实数据上用 RLHF 训练,得到 GPT-4 系 critic 模型 CriticGPT,在 bug 检测任务上超越代表性人类承包商。

训练流程类似 [[chatgpt]] 的 [[rlhf]] pipeline:
- **Step 0(Tampering / 篡改)**:让承包商在模型写的答案中植入 subtle bug,并记录如同代码评审般的 bug 说明。篡改对抗式收集——承包商可访问 LLM critic,被要求验证其植入的 bug 至少在三次采样中有一次被 critic 漏掉,使 bug 更难被发现。
- **Step 1-2**:对每个 (question, answer) 对采样若干 critique,由承包商按属性(comprehensiveness、critique-bug inclusion CBI、是否含 hallucinated bug 或 nitpick、整体 helpfulness,1-7 序数量表)评分。
- **Step 3**:训练 [[reward-model]] 预测人类整体质量排序。
- **Step 4**:用 [[ppo]] 针对 reward model 优化策略。
- **Step 5**:推理时采用 **Force Sampling Beam Search (FSBS)** 采样策略。

**FSBS**:利用 reward model 配合 test-time search,通过强制采样带高亮的片段并按 `rm_score + LENGTH_MODIFIER * num_highlights` 选最优批评。本文每输入搜索 28 个样本,通过调节长度惩罚在 comprehensiveness 与 hallucination 之间建立 [[pareto]] 曲线。除非特别说明,CriticGPT 指 RL+FSBS(50 分位,平均四个高亮)。

评估在两类已知 bug 的数据上进行:**Human Inserted Bugs**(篡改植入,更难更严重)与 **Human Detected Bugs**(ChatGPT 标注流程中原评分者发现并指出的真实 bug)。批评对比采用四份匿名批评同屏比较,用 BFGS 拟合 pairwise 模型计算 **Elo / win-rate**。还研究了 Human+CriticGPT 人机协作团队(预填充 critic 输出供承包商编辑)。

## 结果

- **偏好率**:在含 Human Inserted Bugs 的代码上,模型写的批评在 **63%** 的情况下优于人类批评;CriticGPT 与 ChatGPT 的批评被标注者偏好超过 **80%** 的时间,CriticGPT 显著优于 prompted ChatGPT。
- **抓 bug 率(Human Inserted Bugs)**:人类承包商约抓住 **25%** 植入 bug,ChatGPT 约 **70%**,CriticGPT 约 **86%**。
- **模型规模**:对 RLHF 模型家族扫描预训练算力,naive 外推估计要让 ChatGPT 匹配 CriticGPT (RL only) 的表现,需约 **30x** 预训练算力。
- **人机团队**:Human+CriticGPT 团队写出比人类单独更 comprehensive 的批评,同时比 LLM 单独更少 hallucinate / nitpick,移动到 model-only Pareto frontier 之外。
- **泛化(超出代码)**:对一大批被首位标注者评为 "flawless" 的 ChatGPT 训练数据采样 CriticGPT 批评,在 **24%** 的案例中承包商确认批评找到了实质性降低答案评分的问题(无批评对照下第二位标注者仅 6% 给出同样低分),即 CriticGPT 能识别被评为完美任务中数百个错误,尽管多数为非代码、对 critic 而言 out-of-distribution 的任务。
- **局限**:nitpick 与 hallucinated bug 的绝对率仍偏高;评估代码片段较短、无多文件/仓库导航;植入 bug 分布与自然 LLM 错误分布不同;单步 critique 可能弱于 debate / consultancy 等多步交互。

## 在本 wiki 中的位置

本文是 [[openai]] [[scalable-oversight]] / superalignment 团队的代表作,由 [[jan-leike]] 等人完成,把 [[rlhf]]、[[reward-model]]、[[ppo]] 与 [[llm-as-judge]] / [[self-critique]] 结合到代码评审场景。它与 [[constitutional-ai]]、[[self-refine]]、[[reflexion]] 等 [[self-correction]] 路线形成对照(scalable oversight 目标是提升 human judge 而非 base model 能力),并是 recursive reward modeling 的第一步。CriticGPT 是建立在 [[gpt-4]] 之上、用于评审 [[chatgpt]] 写代码的 critic,可作为 [[ai-safety]] 与 [[code-generation]] 评估主题的核心来源。
