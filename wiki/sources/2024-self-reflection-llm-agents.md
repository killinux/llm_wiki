---
type: source
subtype: paper
tags:
  - self-reflection
  - llm-agent
  - self-correction
  - reasoning
  - benchmark
created: 2026-05-29
updated: 2026-05-29
arxiv: 2405.06682
raw: raw/2405.06682.pdf
authors:
  - Matthew Renze
  - Erhan Guven
year: 2024
---

# Self-Reflection in LLM Agents: Effects on Problem-Solving Performance

通过把 self-reflection 拆解成 8 种类型并在 9 个 LLM、1000 道多选题上做对照实验,本文证明所有类型的自我反思都能显著提升 [[llm-agent]] 的解题准确率。

## 问题

[[large-language-models]] 驱动的 agent 在多步问题上表现出色,但仍受限于知识不足、[[reasoning]] 出错、[[hallucination]],并容易陷入无效循环。研究者希望通过赋予 agent 认知能力(如 [[chain-of-thought]]、外部记忆、从反馈中学习)来改进表现。

[[self-reflection]](又称 introspection)是一种元认知策略:让 LLM 反思自己的 CoT,识别错误、解释原因并生成改进建议。但既有文献分歧很大——有研究认为 LLM 能借自我反思识别并纠正错误,也有研究([[self-correction]] 持怀疑观点)认为 LLM 无法在没有外部反馈时发现自身推理错误。本文的核心问题是:**self-reflection 究竟能否提升解题性能?哪些类型的反思贡献最大?哪些模型、哪些题型受益最多?**

## 方法

- **数据**:从 10 个流行 LLM benchmark(ARC、AQUA-RAT、HellaSwag、LogiQA、LSAT-AR/LR/RC、MedMCQA、SAT-English、SAT-Math,多来自 AGIEval)各随机抽 100 题,组成 1000 题的多领域多选题(MCQA)考试。

- **模型**:9 个 LLM,包括 [[gpt-4]]、[[gpt-3-5-turbo]]、[[claude]] 3 Opus、Gemini 1.0 Pro、Gemini 1.5 Pro (Preview)、Cohere Command R+、[[llama-2]] 7B/70B Chat、Mistral Large;temperature 设为 0.0 以提高可复现性。

- **8 种反思 agent + 基线**:
  - **Baseline**:无反思(对照,准确率下界)。
  - **Retry**:仅被告知答错,直接重答。
  - **Keywords**:列出错误类型关键词。
  - **Advice**:给出通用改进建议。
  - **Explanation**:解释为何出错。
  - **Instructions**:给出有序解题步骤。
  - **Solution**:给出逐步解答。
  - **Composite**:以上六种反思全用。
  - **Unredacted**:六种反思但不遮蔽答案(准确率上界)。

- **流程(批处理实现的 virtual 多步 agent)**:Baseline 先答全部 1000 题,答错的进入队列;反思 agent 用"正确答案"作为外部反馈信号生成各类反思,再做 find-and-replace **遮蔽(redact)答案标签与描述**以防答案泄漏(Unredacted 除外);最后用各自反思重答。为省成本,反思 agent 只重答 Baseline 答错的题,再把正确重答数加回 Baseline 分数。

- **统计**:用 McNemar 检验比较配对二元结果,报告 χ² 检验统计量与 p 值。

## 结果

- **总体**:所有类型的 self-reflection 在所有 LLM 上都**显著**提升准确率(p < 0.001)。

- **GPT-4 为例(Table 3)**:Baseline 准确率 0.786;Retry 0.827、Keywords 0.832、Advice 0.840、Instructions 0.849、Explanation 0.876、Solution 0.925、Composite 0.932、Unredacted 0.971。即提升幅度从 +0.041(Retry)到 +0.146(Composite),上界 Unredacted +0.185(χ²=183.005)。

- **规律**:信息量更大的反思(Instructions/Explanation/Solution/Composite)优于信息量小的(Retry/Keywords/Advice)。即使是仅"知道自己答错"的 Retry 也能显著提升,作者推测是 agent 二次作答更谨慎或选择次优答案。

- **按模型(Table 4)**:所有 9 个模型均呈相似上升趋势。例如 Llama 2 7B 从 Baseline 0.297 升到 Composite 0.427;Claude 3 Opus 从 0.792 升到 Composite 0.947、Unredacted 0.971。

- **按题型(Table 5)**:LSAT-AR(分析推理)提升最大(GPT-4 从 0.33 升到 Composite 0.72、Unredacted 0.92);而 SAT-Math、ARC Challenge 等基线已高(>0.9)的题型提升被天花板压缩。

- **局限**:实验只针对单步问题(非真正多步 agent),API 内容安全过滤偶发误差(Gemini 1.0 Pro、Mistral Large 误差可达 2.8%),高分题型存在天花板压缩。未来工作建议用更难题集、多步问题、外部工具与外部记忆([[retrieval-augmented-generation]])。

## 在本 wiki 中的位置

本文是 [[self-reflection]] / [[self-correction]] 主题的实证基准研究,把抽象的"自我反思"细化为可量化的 8 种反馈类型,与 [[reflexion]]、[[self-refine]]、[[self-critique]] 等方法形成对照,也呼应 [[self-correction]] 关于"LLM 能否独立纠错"的争论(本文反思依赖正确答案作为外部信号)。它在 [[gpt-4]]、[[claude]]、[[llama-2]] 等多个 [[large-language-models]] 上验证,可作为评估 [[llm-agent]] 元认知能力的参考。作者来自 Johns Hopkins University。
