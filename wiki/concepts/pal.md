---
type: concept
subtype: method
tags: [reasoning, code-generation, tool-use, prompting]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# PAL

PAL(Program-Aided Language models)是一种让 LLM 把自然语言推理问题分解为可执行程序步骤,再交由代码解释器(如 Python)运行以得到最终答案的方法,从而将求解过程从模型的不可靠计算中卸载到外部解释器。

## 在本 wiki 中的出现

- [[2023-critic]]:CRITIC 强调外部工具反馈对 LLM 自我改进的重要性,其中代码解释器(code interpreter)正是这类外部工具之一;PAL 作为"借助程序/代码解释器辅助语言模型求解"的代表性方法,与这一以代码执行作为外部验证与计算手段的思路相一致。

## 相关

- [[code-interpreter]]
- [[2023-critic]]
- [[chain-of-thought]]
- [[program-of-thoughts]]
- [[tool-use]]
