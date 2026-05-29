---
type: concept
subtype: method
tags: [alignment, rlhf, rlaif, self-critique, harmlessness]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Constitutional AI

一种对齐方法:用一套人类书写的原则(constitution)替代人类的有害性标注,让模型自我批评并修改自身回复,再以 AI 反馈进行强化学习(RLAIF),训练出既无害又不回避的助手。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:Anthropic 提出 Constitutional AI,用一套人类书写的原则替代人类有害性标注,通过模型自我批评修改与 AI 反馈(RLAIF)训练既无害又非回避的助手。
- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。

## 相关

- [[rlhf]] — Constitutional AI 在反馈来源上对其改造,用 AI 反馈替代部分人类反馈
- [[rlaif]] — Constitutional AI 强化学习阶段所采用的反馈范式
- [[alignment]] — Constitutional AI 服务于对齐目标
- [[reward-model]] — RLAIF 阶段用 AI 偏好训练的偏好/奖励模型
- [[self-improvement]] — 模型通过自我批评与修改实现自我改进
