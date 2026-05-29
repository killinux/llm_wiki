---
type: concept
subtype: method
tags: [reasoning, self-reflection, multi-agent, LLM]
created: 2026-05-29
updated: 2026-05-29
sources: 2
---

# Degeneration-of-Thought

Degeneration-of-Thought(DoT)指 LLM 在自我反思(self-reflection)过程中,一旦对自身答案建立起自信,便难以再生成新颖的想法、跳出原有思路的退化现象。

## 在本 wiki 中的出现

- [[2023-multi-agent-debate]]:该论文将 Degeneration-of-Thought 作为单一智能体自我反思的核心局限提出,并以此作为引入 Multi-Agent Debate(MAD)框架的动机。在 MAD 中,多个 LLM 智能体以"针锋相对"(tit for tat)的方式辩论,再由裁判(judge)仲裁,从而缓解 DoT 问题并激发发散性思维。
- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,缓解单 Agent 反思中的思维退化,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。

## 相关

- [[self-reflection]]
- [[self-critique]]
- [[multi-agent-debate]]
- [[large-language-models]]
- [[divergent-thinking]]
- [[chain-of-thought]]
- [[reflexion]]
