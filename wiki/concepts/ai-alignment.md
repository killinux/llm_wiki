---
type: concept
subtype: method
tags: [alignment, safety, RLHF, RLAIF, supervision]
created: 2026-05-29
updated: 2026-05-29
sources: 5
---

# AI alignment

AI alignment 指让 AI 系统(尤其是大语言模型)的行为、目标与输出与人类的意图、价值观和安全规范保持一致的研究与方法。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:把 alignment 作为核心目标。Anthropic 提出 Constitutional AI,用一套人类书写的原则(constitution)替代人类对有害性的逐条标注,让模型通过自我批评进行修改,并用 AI 反馈(RLAIF)进行训练,从而对齐出一个既无害又不回避问题的助手。该工作展示了用更少人类监督实现 alignment 的路径。
- [[2023-lets-verify-step-by-step]]:从监督信号的角度服务于 alignment。OpenAI 比较了过程监督(PRM)与结果监督(ORM),证明在 MATH 多步数学推理上过程监督显著更优(best-of-N 达 78.2%),并开源步骤级标注数据集 PRM800K。过程监督因奖励可解释、可定位错误步骤,被视为更利于对齐与可信推理的训练方式。
- [[2024-generative-ai-as-economic-agents]]:立场/理论论文,主张把生成式 AI 本身建模为有独立信息与(可能错位的)偏好的经济主体,并给出一个把 AI agent 嵌入博弈的形式化框架。
- [[2024-mitigating-false-refusal-single-vector-ablation]]:提出 training-free、零推理开销的方法,通过正交化并消融单个 false refusal vector 来缓解 LLM 的过度拒绝,同时保持安全性与通用能力。
- [[2025-multi-agent-llm-value-diversity]]:通过 Schwartz 价值观给 LLM 智能体注入价值多样性的多智能体社会模拟,发现价值多样性提升集体行为的价值稳定性、涌现与自发规则创造,但极端异质带来边际递减与不稳定。

## 相关

- [[alignment]]
- [[rlhf]]
- [[reward-model]]
- [[constitutional-ai]]
- [[rlaif]]
- [[process-supervision]]
- [[scalable-oversight]]
- [[helpfulness-and-harmlessness]]
- [[human-values]]
- [[multi-agent-systems]]
