---
type: entity
subtype: model
tags: [model, language-model, google, dialogue]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# LaMDA

LaMDA(Language Models for Dialog Applications)是 Google 推出的面向对话应用的大型语言模型系列。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:作为评估 chain-of-thought prompting 的大模型之一。该论文表明在 few-shot 示例中加入中间推理步骤可显著提升大模型的多步推理能力,且该增益随模型规模涌现(PaLM 540B 在 GSM8K 达 57%);LaMDA 被用作其中一个被测模型家族。
- [[2022-star-self-taught-reasoner]]:作为 STaR 方法可应用的大模型之一。STaR 用少量 CoT 示例让模型自己生成推理过程,只保留答对的 rationale(并用 rationalization 从答错题反向补全)反复微调自身来 bootstrap 推理能力。
- [[2022-constitutional-ai]]:作为对话/助手类语言模型的代表之一出现在相关讨论语境中。该论文中 Anthropic 提出 Constitutional AI:用一套人类书写的原则替代人类有害性标注,通过模型自我批评修改与 AI 反馈(RLAIF)训练既无害又非回避的助手。

## 相关

- [[palm]]
- [[chain-of-thought-prompting]]
- [[google]]
- [[dialogue-systems]]
- [[large-language-model]]
