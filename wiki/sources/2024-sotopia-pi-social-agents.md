---
type: source
subtype: paper
tags: [llm-agent, social-intelligence, self-improvement, behavior-cloning, llm-as-judge, role-playing]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2403.08715
raw: raw/2403.08715.pdf
authors: [Ruiyi Wang, Haofei Yu, Wenxin Zhang, Zhengyang Qi, Maarten Sap, Graham Neubig, Yonatan Bisk, Hao Zhu]
year: 2024
---

SOTOPIA-π 提出一种交互式学习方法,通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交互动数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4 水平,同时提升安全性并保持 MMLU 通用问答能力。

## 问题

机器社交智能(machine social intelligence)对人机交互至关重要,但当前 [[large-language-models]] 在 theory-of-mind、遵守社会规范、应对目标驱动的社交场景等方面仍落后于人类。人类通过模仿(imitation)与社交互动(social interaction)习得社交技能,而现有构建 language agent 的研究对这一社会学习过程理解不足。作者提出三个研究问题:(RQ1) 该方法能否提升 language agent 的社交目标完成能力与整体社交智能?(RQ2) LLM 评分能否作为人类评分的有效代理用于训练?(RQ3) 该训练如何影响 agent 的其它能力(知识、安全)?

## 方法

SOTOPIA-π 基于 [[sotopia]] 环境(社交任务由场景、两个角色 profile 及各自私有社交目标构成,在 [[sotopia]]-EVAL 的 7 个社交维度上评估:believability、relationship、knowledge、secret、social rules、financial/material benefits、goal completion)。框架分三步:

1. Social task generation:用 [[gpt-4]] 从 Social Chemistry、Social IQa、Normbank 采样关键词,自动合成多样化社交任务(涵盖 negotiation、collaboration、competition),复用 [[sotopia]] 中 40 个角色 profile;采用自动化、可扩展、不做人工筛选的方式批量生成。
2. Training data collection:收集多轮社交对话轨迹。Behavior cloning(BC,[[behavior-cloning]])使用专家策略 π_expert(两个 GPT-4 agent 角色扮演)的互动;self-reinforcement(SR)收集 agent 策略 π_ref 自身角色扮演的互动。
3. Agent policy update:用 [[gpt-4]] 对 agent 表现的 7 个维度评分并给出推理,专注于 goal completion 维度(该维度与人类评分相关性最高),设阈值过滤正例,再以 supervised [[fine-tuning]] 更新 agent。还探索先 BC 再 SR 的序列训练(BC+SR)。SR 采用 ratio-based 数据过滤,避免 ReST 式 threshold 调参与多轮迭代。

实现上以 Mistral-7B 为 base model,GPT-4 为专家,GPT-3.5-turbo 为固定 partner,用 QLoRA([[lora]])做量化高效微调;每轮生成 100 个社交任务,每任务 10 对角色各跑 10 次互动。该方法属于离线方法,无需人类介入与在线 reward model,区别于 [[rlhf]]。

## 结果

在 [[sotopia]] 的 14 个 hard 社交任务子集上(goal completion 维度,GPT-4 自动评分):base Mistral-7B 为 3.25,SR 为 3.96,BC 为 4.82,BC+SR 为 5.71,接近 GPT-4 的 5.89。人类评分上 base 0.36、SR 0.64、BC 1.27、BC+SR 4.29,GPT-4 为 5.25。

- 全部 90 个社交任务(GPT-4 评分,Table 2):Expert(GPT-4)GOAL 7.62 / Overall 3.31;Base 5.07 / 2.33;SR 5.83 / 2.57;BC 7.27 / 3.41;BC+SR 7.62 / 3.44,与专家模型相当。
- 其它社交维度(BC+SR 相对 base 的人类评分提升 Table 1):BEL +2.05、REL +1.91、SOC +1.11、Overall +0.91 显著提升,KNO/SEC/FIN 影响很小。
- 安全(RQ3,Table 3):在 "injure third person" 任务中,BC+SR 的 engagement rate 100%,proceed-to-injure 44%(低于 base 100%),toxic 词数 0.9(低于 base 3.6);Character 2 的 prevention rate 100%、alternative solutions 2.9,且未显式做 RLHF 对齐即更安全。
- 通用能力(Table 4,MMLU,5-shot):base 49.21、BC+SR 48.57,差异不显著,未出现 catastrophic forgetting,表明社交互动能力与问答能力近乎正交。

关键发现:GPT-4 评分与人类评分的差距随训练增大(0.36 增至 1.42),说明 [[llm-as-judge]] 会高估专门为社交训练的模型,需更鲁棒的评估模型。

## 在本 wiki 中的位置

本文是 [[llm-agents|llm-agent]] 在社交智能方向的代表工作,与 [[generative-agents]]、[[role-playing-agent]] 同属 agent 行为/对话研究脉络。其训练方法属 offline [[self-improvement]]:behavior cloning + self-reinforcement,与 [[expert-iteration]]、ReST、RAFT([[rejection-sampling-fine-tuning]])、SIL 等离线 self-training 同源,区别于在线 [[rlhf]]/[[ppo]]/[[dpo]]。使用 [[gpt-4]] 作为评分器属 [[rlaif]]/[[llm-as-judge]] 思路,并实证揭示其作为训练信号的局限。来自 [[stanford-university]] 之外的 Carnegie Mellon University(Language Technologies Institute)。
