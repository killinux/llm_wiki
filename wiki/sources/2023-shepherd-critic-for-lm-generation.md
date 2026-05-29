---
type: source
subtype: paper
tags:
  - critic
  - self-correction
  - llm-as-judge
  - feedback
  - fine-tuning
created: 2026-05-29
updated: 2026-05-29
arxiv: "2308.04592"
raw: raw/2308.04592.pdf
authors:
  - Tianlu Wang
  - Ping Yu
  - Xiaoqing Ellen Tan
  - Sean O'Brien
  - Ramakanth Pasunuru
  - Jane Dwivedi-Yu
  - Olga Golovneva
  - Luke Zettlemoyer
  - Maryam Fazel-Zarandi
  - Asli Celikyilmaz
year: 2023
---

# Shepherd: A Critic for Language Model Generation

Shepherd 是 Meta AI / FAIR 提出的一个专门用于**批判(critique)**语言模型输出的 7B 模型:它经过针对性微调,能指出模型回答中的事实性、逻辑、连贯性、对齐等错误并给出可执行的改进建议,虽仅 7B 参数,其 critique 质量却可与 [[chatgpt]] 媲美甚至更受偏好。

## 问题

随着 [[large-language-models]] 能力增强,人们越来越希望利用模型自身能力来**精炼/修正其输出**([[self-correction]] / [[self-refine]])。但 LLM 仍常生成虚假、不可靠、不连贯的内容([[hallucination]])。已有用 LLM 生成反馈的工作存在局限:有的只给多维度评分,有的在 math/reasoning 等复杂任务上只能给出泛泛的通用反馈,无法精确定位错误。论文要解决的核心问题是:如何训练一个**鲁棒、跨领域**的 [[critic]] 模型,能对任意 LLM 生成文本给出既有正确判断、又有深度领域知识和可执行建议的自然语言反馈。

## 方法

核心是构建一份高质量 **feedback dataset** 并用其微调出 Shepherd:

- **Community Critique Data(社区反馈)**:从 Stack Exchange 与 Pushshift Reddit Dataset 抓取。把帖子标题/副标题视为 question,顶层评论视为 answer,对评论的回复视为 critique;每条带 community vote score。通过关键词过滤(区分"答案基本正确需改进"的 Case #1 与"答案有错被指出"的 Case #2)、用户编辑历史、投票分数阈值、脏话过滤、去除含 URL/图片/视频的样本等手段筛选有效 critique。
- **Human-Annotated Feedback(人工标注反馈)**:覆盖 8 个需复杂推理且有 step-by-step 解释的数据集([[gsm8k]]、PIQA、CosmosQA、ECQA、e-SNLI、Entailment Bank、Proofwriter、Adversarial NLI)及两个摘要数据集(GPT-3 summarization、DeFacto)。为每个问题提供 context、正确输出、候选输出(部分用 [[llama]]-65B / LIMA-30B 以 zero/few-shot 生成带错的候选),由专家标注员(RWS Moravia)标注错误。最终得到 1,317 条高质量样本。
- **训练**:以 [[llama]]-7B 为 base model,AdamW 优化器,学习率 1e-5、2000 warmup steps、batch size 64、max length 2048,共 3,000 steps;用 [[gpt-4]] 评估协议在 held-out set 上挑选最佳 checkpoint。Shepherd 仅用约 **8K** 微调样本(对比 SelFee 用 178K)。

评估上采用两套:用 [[gpt-4]](GPT-4-0613)做自动评估(包括 1-7 Likert 绝对打分与 pairwise 比较)和 human evaluation,把 Shepherd 与 Alpaca-7B、SelFee-7B、ChatGPT(GPT-3.5 Turbo)做对比。

## 结果

- **GPT-4 评估总体 win-rate 53-87%**(对各竞品的平均)。详细(Table 3,GPT-4 pairwise win rate%,跨 7 个数据集均值):Shepherd vs Alpaca = **87.0**,vs SelFee = **53.0**,vs ChatGPT = **56.0**。
- **Human 评估**(Table 4,均值):Shepherd vs Alpaca = **72.4**,vs SelFee = **59.7**,vs ChatGPT = **49.6**(与 ChatGPT 基本打平)。
- 评估数据覆盖 6 个公开数据集:AlpacaFarm、FairEval、CommonsenseQA、OBQA、PIQA、[[truthfulqa]],各采样 50 条共 300 条;并额外构建 **CritiqueEval**(52 条 2022.06-2023.06 的 Pushshift 新问题,用于防数据污染),总评估集 352 条。Shepherd 在 ChatGPT/LLaMA 都没见过的 CritiqueEval 上始终表现更好,体现 critique 与泛化能力。
- **数据质量胜过数据量**:Shepherd 仅 8K 微调样本即超过用 178K 样本的 SelFee;加入更多高质量人工标注数据可持续提升 critique 模型(Figure 7)。
- **LLM-as-judge 的局限观察**:作者发现 [[gpt-4]] 的 Likert 绝对打分不可靠——它倾向给所有反馈高分(Alpaca 平均 4.7 vs 人工 2.91),且偏好特定格式、存在 knowledge barrier;因此推荐用 **pairwise 比较**方式让 GPT-4 评估,这与人工判断更一致。

## 在本 wiki 中的位置

Shepherd 属于"训练专门 [[critic]] 模型为生成提供反馈"的方向,是 [[self-correction]] / [[self-refine]] / [[self-critique]] 生态中的关键一环,可与 [[reflexion]]、[[constitutional-ai]]、[[rlaif]]、[[process-reward-model]] 等利用反馈/评判信号的工作互参。它也是 [[llm-as-judge]] 研究的重要案例,实证揭示了 GPT-4 作为评估者的偏差,主张用 pairwise 评估。模型基于 [[llama]]-7B 微调([[fine-tuning]]),对照基线含 [[chatgpt]] 与 Alpaca、SelFee。作者团队来自 [[facebook-ai-research]],包括 [[luke-zettlemoyer]] 等。
