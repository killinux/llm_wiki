---
type: entity
subtype: benchmark
tags: [text-to-sql, semantic-parsing, benchmark, code-generation]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Spider

Spider 是一个大规模、跨领域的 text-to-SQL 语义解析基准,要求模型将自然语言问题转换为可在多个数据库上执行的 SQL 查询。

## 在本 wiki 中的出现

- [[2023-self-debugging]]:作为评测 SELF-DEBUGGING 方法的基准之一。该工作通过 few-shot prompting 让 LLM 执行并解释自己生成的代码,实现无需人工反馈的自我调试;在 text-to-SQL 任务上,Spider 被用来衡量自我调试对生成代码正确性的提升。

## 相关

- [[text-to-sql]]
- [[self-debugging]]
- [[code-generation]]
- [[2023-self-debugging]]
