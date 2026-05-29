---
type: concept
subtype: method
tags: [self-correction, prompting, feedback, reasoning, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Intrinsic Self-Correction

内在自我纠错（Intrinsic Self-Correction）指 LLM 仅依靠自身能力（如 prompting），在没有外部反馈、工具或真值标签的情况下，对自己生成的初始答案进行复审并修正错误的过程。

## 在本 wiki 中的出现

- [[2024-when-can-llms-correct-mistakes]]：批判性综述，细分自我纠错的三类研究问题并提出实验检查清单，论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错，瓶颈在于反馈生成，而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-score-self-correct-via-rl]]：SCoRe 用完全自生成数据的多轮在线强化学习（两阶段 + 奖励塑形）训练单个 LLM，在 MATH 上把内在自我纠错 Δ(t1,t2) 从 -11.2% 提到 +4.4%（整体提升 15.6%）、HumanEval 上达 12.2%。

## 相关

- [[self-correction]]
- [[external-feedback]]
- [[self-refine]]
- [[chain-of-thought]]
- [[reinforcement-learning]]
- [[reward-shaping]]
