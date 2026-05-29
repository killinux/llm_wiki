---
type: entity
subtype: person
tags: [researcher, agents, reasoning]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# Shunyu Yao

LLM 智能体与推理方向的研究者(论文署名时在 Princeton),本 wiki 中多篇核心方法论文的第一作者。

## 在本 wiki 中的工作
- [[react|ReAct]]——推理 + 行动交替([[2022-react-reasoning-and-acting]],第一作者)
- [[tree-of-thoughts|Tree of Thoughts]]——对推理做搜索(arXiv 2305.10601,第一作者;原文尚未 ingest)
- [[2023-fireact-language-agent-fine-tuning]]:提出用多任务、多 prompting 方法(ReAct/CoT/Reflexion)生成的轨迹微调 backbone LM 来构建语言智能体,在性能、鲁棒性、泛化与成本上全面优于 few-shot prompting。
- [[2023-memgpt-llms-as-operating-systems]]:MemGPT 借鉴操作系统的分层内存与虚拟内存分页,用函数调用让 LLM 自主管理上下文内外的多级存储,在固定上下文模型上制造"无限上下文"的假象。

这两条线后续都被 [[language-agent-tree-search|LATS]] 综合吸收。

> 占位页(stub)——补充机构、主页、其他相关工作待资料。
