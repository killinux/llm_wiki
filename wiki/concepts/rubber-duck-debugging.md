---
type: concept
subtype: method
tags: [debugging, code-generation, self-debugging, explanation, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Rubber Duck Debugging

Rubber Duck Debugging(小黄鸭调试)是一种调试方法:程序员通过向无生命的对象(如一只橡皮鸭)逐行讲解、解释自己的代码,在用自然语言把逻辑说清楚的过程中自行发现并定位 bug,无需外部帮助。

## 在本 wiki 中的出现

- [[2023-self-debugging]]:SELF-DEBUGGING 明确把 Rubber Duck Debugging 作为核心灵感——通过 few-shot prompting 教会 LLM 像程序员"对橡皮鸭讲解代码"一样,执行并用自然语言逐行解释自己生成的代码(Code Explanation feedback),从而在无人工反馈、无额外训练的情况下自行发现并修复代码错误。

## 相关

- [[2023-self-debugging]]
- [[self-debugging]]
- [[self-refine]]
- [[self-critique]]
- [[code-generation]]
- [[chain-of-thought]]
- [[few-shot-prompting]]
