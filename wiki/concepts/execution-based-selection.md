---
type: concept
subtype: method
tags: [code-generation, self-debugging, llm, execution-feedback]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Execution-based Selection

Execution-based Selection 指利用代码的实际执行结果(而非仅靠模型对代码的静态判断)来选择、验证或修正 LLM 生成的程序。

## 在本 wiki 中的出现

- [[2023-self-debugging]]:SELF-DEBUGGING 通过 few-shot prompting 让 LLM 执行自己生成的代码并解释执行结果,从而在无人工反馈的情况下完成自我调试。这里 execution-based 的思路体现在:模型不只是凭文本推理判断代码是否正确,而是借助实际执行(及对执行结果的解释)来发现并修正错误,进而选出更可靠的解。

## 相关

- [[2023-self-debugging]]
- [[self-debugging]]
- [[few-shot-prompting]]
- [[execution-feedback]]
- [[code-generation]]
