---
type: concept
subtype: method
tags: [prompting, llm, reasoning, baseline]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# Input-Output Prompting

Input-Output Prompting(IO Prompting)是最基础的 LLM 提示方法:把任务输入直接喂给模型,让其一步到位地产生最终答案,中间不显式生成任何推理过程。

## 在本 wiki 中的出现

- [[2023-tree-of-thoughts]]:IO Prompting 在该工作中作为最朴素的对照基线出现。Tree of Thoughts 将 LLM 推理建模为在「思考」树上的搜索(支持前瞻、自评估与回溯),其表现远超只产生单一答案的 IO Prompting,以及逐步生成中间推理的 Chain-of-Thought。在 24 点(Game of 24)任务上,GPT-4 配合 ToT 的成功率达到 74%,而 CoT 仅为 4%,IO Prompting 作为更弱的基线进一步衬托了显式搜索带来的提升。

## 相关

- [[chain-of-thought]]:在输入与最终答案之间显式生成一连串中间推理步骤,是对 IO Prompting 的直接增强。
- [[2023-tree-of-thoughts]]:将推理拓展为可搜索的思考树,相对 IO Prompting 与 CoT 的进一步泛化。
