---
type: source
subtype: paper
tags:
  - retrieval-augmented-generation
  - self-reflection
  - factuality
  - llm
created: 2026-05-29
updated: 2026-05-29
arxiv: "2310.11511"
raw: raw/2310.11511.pdf
authors:
  - Akari Asai
  - Zeqiu Wu
  - Yizhong Wang
  - Avirup Sil
  - Hannaneh Hajishirzi
year: 2023
---

Self-RAG 训练单个 LLM 通过特殊的 reflection token 实现"按需检索 + 自我反思批判",在推理时自适应决定是否检索、并对检索段落与自身生成进行评估,从而同时提升生成质量、事实性与引用准确率。

## 问题

标准的 [[retrieval-augmented-generation]](RAG)无论是否需要、是否相关都固定检索若干段落并拼接进输入,存在两个缺陷:(1)不加区分地检索会引入无关或离题段落,降低 [[large-language-models]] 的灵活性,生成低质量回答;(2)模型未被显式训练去遵循检索到的事实,输出不保证与所引段落一致(即仍可能 [[hallucination]])。如何让 LLM 在需要时才检索、并能判断检索内容相关性与自身输出是否被证据支持,是本文要解决的核心问题。

## 方法

提出 **Self-Reflective Retrieval-Augmented Generation (Self-RAG)**,核心是把四类 *reflection token* 统一进模型词表,作为下一个 token 预测的一部分:

- **Retrieve**(输入 x 或 x,y → {yes, no, continue}):决定何时调用 retriever。
- **IsRel**(x,d → {relevant, irrelevant}):判断段落 d 是否提供有用信息。
- **IsSup**(x,d,y → {fully supported, partially supported, no support}):判断输出 y 中可验证陈述是否被 d 支持。
- **IsUse**(x,y → {5,4,3,2,1}):判断 y 对 x 的整体有用性。

训练分两步:先用 GPT-4 蒸馏出一个 critic 模型 C(在 4k-20k 监督数据上训练,与 GPT-4 一致率超 90%),用 C 离线地把 reflection token 插入到原始语料,得到 D_gen;再用标准语言建模目标训练 generator 模型 M,使其无需在推理时托管 critic 即可自行生成 reflection token。训练时对 `<p>...</p>` 包裹的检索文本块做 loss mask。

推理时(见 Algorithm 1):每段先预测 Retrieve;若需检索则用 retriever R 取 top-K 段落并行处理,对每段预测 IsRel、生成对应输出、预测 IsSup/IsUse,再做 **segment-level beam search**(beam size B),用各类 critique token 的归一化概率加权和作为段落得分进行 re-ranking(Eq. 3-4)。权重 w^G 是可在测试时调整的超参,可实现软约束(如提高 IsSup 权重重视引用)或硬约束(过滤 IsSup=No support 的续写),无需额外训练即可定制行为。这与 [[rlhf]] 用独立 reward 模型在训练期对齐不同,Self-RAG 把批判离线插入语料,大幅降低训练成本。

基座为 [[llama-2]] 7B 和 13B,retriever 默认用 Contriever-MS MARCO,训练数据共 150k 指令-输出对。

## 结果

在六个任务上零样本评测(Table 2)。Self-RAG 7B / 13B 显著超越同规模的预训练与指令微调 LLM 及主流 RAG 方法,并在多项任务上超过 ChatGPT 与检索增强的 Llama2-chat:

- **PopQA**(短答 acc):Self-RAG 13B 55.8,7B 54.9,均高于 ChatGPT 29.3、Ret-ChatGPT 50.8、Llama2-chat13B+检索 45.7。
- **PubHealth**(事实核查 acc):13B 74.5,7B 72.4,优于 ChatGPT 70.1。
- **ARC-Challenge**(多选推理 acc):13B 73.1。
- **TriviaQA**(短答 acc):13B 69.3。
- **Biography**(长文 FactScore 事实性):7B 81.2,超过 ChatGPT 71.8,并优于迭代提示的 CoVE65B(71.2)。
- **ASQA**(长文 QA,含引用):citation precision 7B 66.9 / 13B 70.3,citation recall 7B 67.8 / 13B 71.3,引用准确率在所有非专有模型中最佳,引用精度甚至超过 ChatGPT。

消融(Figure 3a)显示:去掉 retriever、去掉 critic、推理时不检索、硬约束、只取 top1、移除 IsSup re-ranking 均带来明显下降,证明各组件均关键;Llama2-FT(同数据训练但无反思)落后于 Self-RAG,说明增益并非仅来自训练数据。调整 IsSup 权重可在引用精度与流畅度(MAUVE)间权衡,调整 Retrieve 阈值可控制检索频率与准确率的折中。

## 在本 wiki 中的位置

Self-RAG 属于 [[retrieval-augmented-generation]] 与 [[self-reflection]] / [[self-critique]] 的交叉工作,与 [[react]]、[[reflexion]] 等"生成时自我评估"思路相关,但聚焦于检索与事实性而非 agent 行动。它用 reflection token 实现可控解码,思想上承接 RLHF 与 controllable generation(如 [[ppo]]、[[constitutional-ai]]),但把批判离线化以降低成本。基座为 [[llama-2]],critic 蒸馏自 [[gpt-4]],并以 [[chatgpt]] 作为专有模型基线对比。可作为缓解 [[hallucination]]、提升 [[grounding]] 与引用质量的代表性方法参考。
