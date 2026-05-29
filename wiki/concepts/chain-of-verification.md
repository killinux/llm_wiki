---
type: concept
subtype: method
tags: [hallucination, verification, prompting, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Chain-of-Verification

Chain-of-Verification (CoVe) 是一种降低大语言模型幻觉的方法:让模型先生成初始草稿回答,再自我规划一组验证问题并独立作答以核查事实,最后据此修订生成更可靠的最终答案。

## 在本 wiki 中的出现

- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。

## 相关

- [[hallucination]]
- [[self-consistency]]
- [[chain-of-thought]]
- [[self-refine]]
