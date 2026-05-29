---
type: source
subtype: paper
tags:
  - rlhf
  - ai-safety
  - alignment
  - harmlessness
  - self-critique
  - anthropic
created: 2026-05-29
updated: 2026-05-29
arxiv: 2212.08073
raw: raw/2212.08073.pdf
authors:
  - Yuntao Bai
  - Saurav Kadavath
  - Sandipan Kundu
  - Amanda Askell
  - Jackson Kernion
  - Jared Kaplan
  - 等(Anthropic 团队)
year: 2022
---

# Constitutional AI: Harmlessness from AI Feedback

Anthropic 提出 **Constitutional AI (CAI)**:用一套人类书写的原则("宪法",constitution)替代人类对有害性的标注,通过模型对自身输出的自我批评(self-critique)与修改、以及 AI 生成的偏好标签来训练一个既无害(harmless)又"非回避"(non-evasive)的助手,从而把人类监督需求降到只需提供少量原则。

## 问题

传统 [[rlhf]] 训练无害助手依赖大量人类对有害输出的标注,成本高、难以扩展,且对标注者心理负担大。更关键的是,纯粹追求无害的模型常常变得**回避(evasive)**:对任何敏感问题都回答"我不能帮你",拒绝解释自己反对的理由,既无用也不透明。作者希望:

- 用尽可能少的人类标签(理想情况下只需要一份原则清单)来控制模型行为;
- 让模型在拒绝有害请求时仍能解释原因(non-evasive),提升透明度;
- 利用 AI 自身能力随模型规模增长来扩展监督(scaling supervision)。

## 方法

CAI 包含两个阶段,均以一个已经过 [[rlhf]] 训练、只擅长"有用(helpful)"的助手模型为起点:

1. **监督学习阶段(SL-CAI,critique→revision)**:让 helpful-only 模型对"红队"有害提示(red teaming prompts)生成回答,然后依据宪法中随机抽取的某条原则,要求模型**批评(critique)自己的回答并加以修改(revise)**。可多次迭代修改。最后用修改后的回答对原始预训练模型做监督微调,得到 SL-CAI 模型。该步骤主要用于把模型分布拉近目标行为、缩短后续 RL 训练。

2. **强化学习阶段(RL-CAI,即 RLAIF)**:这是 [[rlhf]] 的变体,把人类偏好反馈替换为 **AI 反馈(RLAIF)**。对每个有害提示,用 SL-CAI 生成一对回答,再用一个独立的"反馈模型"依据宪法原则(以多选题形式)判断哪个回答更无害,得到 AI 生成的偏好标签;有用性(helpfulness)仍使用人类偏好标签。用这些标签训练偏好模型(PM),再用 PM 作为奖励做 RL。作者还发现在 RL 阶段对反馈模型加入 [[chain-of-thought]] 推理可提升偏好标注质量。

核心要点:
- "宪法"是一组自然语言原则,是**唯一**的人类无害性监督来源;
- 利用 self-critique 和 RLAIF 实现"AI 监督 AI";
- 目标是 Pareto 改进:在不牺牲有用性的前提下提升无害性,同时保持非回避。

## 结果

- **无害性显著提升且不回避**:RL-CAI(尤其带 [[chain-of-thought]] 的版本)在偏好模型打分上比标准 [[rlhf]] 训练的 helpful+harmless 模型更无害,且与纯 helpful 模型相比有用性几乎没有下降,实现 helpfulness 与 harmlessness 的更优 Pareto 前沿。
- **更少回避**:相比传统 RLHF 无害模型动辄回答"I can't help with that",CAI 模型会解释为何拒绝某个请求,透明度更高。
- **大幅减少人类标注**:无害性训练不再需要人类对有害输出打标签,仅需一份宪法原则清单 + 用于有用性的人类偏好数据。
- **scaling 趋势**:AI 识别有害行为的能力随模型规模增长而提升,使得用 AI 反馈替代人类反馈在更大模型上更可行。
- 论文同时给出了所用宪法原则示例、红队对抗评估,以及 SL/RL 各阶段对有害性 Elo 分数的影响曲线。

## 在本 wiki 中的位置

本文是 [[ai-safety]] / [[ai-alignment]] 方向的奠基性工作之一,由 [[anthropic]] 提出,直接启发了后续 [[claude]] 系列模型的对齐方法。它把 [[rlhf]] 推广为 [[rlaif]](用 AI 反馈替代人类反馈),与 [[self-critique]]、[[scalable-oversight]] 等概念紧密相关,并广泛使用 [[chain-of-thought]] 提升反馈质量。可与标准 [[rlhf]] / InstructGPT 类工作对照阅读,理解"如何用更少人类监督实现可扩展对齐"。
