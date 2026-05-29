---
type: concept
subtype: method
tags: [alignment, rlhf, ai-feedback, harmlessness, preference-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# RLAIF

RLAIF(Reinforcement Learning from AI Feedback)是一种用 AI 模型生成的反馈来替代人类标注、为强化学习提供偏好信号的对齐方法。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:Anthropic 在 Constitutional AI 中提出并使用 RLAIF。其核心是用一套人类书写的原则(constitution)替代人类的有害性标注:模型先对自身回答进行自我批评与修改,再基于 AI 生成的反馈进行强化学习训练,从而得到一个既无害又非回避的助手。在该工作中,RLAIF 是 RLHF 在无害性偏好上的替代方案。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。

## 相关

- [[rlhf]]
- [[constitutional-ai]]
- [[harmlessness]]
- [[preference-model]]
- [[self-critique]]
