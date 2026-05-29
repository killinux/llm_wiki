---
type: entity
subtype: lab
tags: [lab, ai-safety, alignment]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Anthropic

Anthropic 是一家以 AI 安全与对齐研究为核心的人工智能实验室。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:Anthropic 作为提出方,提出了 Constitutional AI 方法——用一套人类书写的原则(constitution)替代人类对有害性的标注,通过模型自我批评、自我修改以及基于 AI 反馈的强化学习(RLAIF),训练出既无害又不回避问题的助手。
- [[2025-multiscale-contextual-bandits-long-term]]:提出 MultiScale Policy Learning 框架与 MSBL 算法,用分层 off-policy contextual bandit 在多个时间尺度上协调短期反馈与长期目标,让低尺度数据作为高尺度稀疏数据的 PAC-Bayes 先验。
- [[2025-mem0-scalable-long-term-memory]]:Mem0 是一个以记忆为中心的架构,从持续对话中动态抽取、整合与检索关键信息,并提出图记忆变体 Mem0^g,在 LOCOMO 基准上以约 91% 更低延迟和逾 90% token 节省超越多种基线。

## 相关

- [[constitutional-ai]]
- [[rlaif]]
- [[rlhf]]
- [[ai-alignment]]
