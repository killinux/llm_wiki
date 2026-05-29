---
type: entity
subtype: lab
tags: [lab, industry-research, NLP, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 3
---

# Facebook AI Research

Facebook AI Research(FAIR)是 Facebook(现 Meta)旗下的人工智能基础研究实验室,专注于机器学习、自然语言处理与检索增强生成等方向的开放研究。

## 在本 wiki 中的出现

- [[2020-rag]]:FAIR 是 RAG(Retrieval-Augmented Generation)工作的提出方/研究机构。该工作将预训练的 seq2seq 生成器与可检索的 Wikipedia 稠密索引相结合,统一微调用于知识密集型 NLP 任务,并在多项任务上取得 SOTA。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,GPT-4 评估 win-rate 53-87%,与 ChatGPT 媲美。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,显著降低幻觉。

## 相关

- [[bart]] —— RAG 采用的 seq2seq 生成器(参数化记忆)。
- [[douwe-kiela]] —— RAG 论文作者之一。
- [[patrick-lewis]] —— RAG 论文第一作者。
- [[dpr]] —— RAG 使用的稠密检索器(Dense Passage Retriever)。
- [[retrieval-augmented-generation]] —— RAG 所属的研究方向。
- [[seq2seq]]
- [[knowledge-intensive-nlp]]
- [[llama]]
- [[hallucination]]
