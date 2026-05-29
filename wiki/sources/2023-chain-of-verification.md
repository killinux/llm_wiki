---
type: source
subtype: paper
tags:
  - hallucination
  - prompting
  - reasoning
  - self-correction
  - factuality
created: 2026-05-29
updated: 2026-05-29
arxiv: 2309.11495
raw: raw/2309.11495.pdf
authors:
  - Shehzaad Dhuliawala
  - Mojtaba Komeili
  - Jing Xu
  - Roberta Raileanu
  - Xian Li
  - Asli Celikyilmaz
  - Jason Weston
year: 2023
---

Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再自我规划并独立回答一组验证问题来事实核查自己,从而在多种任务上显著降低 [[hallucination]]。

## 问题

[[large-language-models]] 经常生成看似合理但事实错误的内容(即 [[hallucination]]),尤其在长尾、低频实体上;长文本生成因 [[exposure-bias]] 会进一步放大该问题。本文研究语言模型能否通过对自身回答进行"审议"(deliberation)来发现并纠正错误,且不依赖外部工具或检索。

## 方法

[[chain-of-verification]](CoVe)由四个核心步骤组成,均通过对同一个 LLM 的不同 few-shot 提示完成:

1. **生成基线回答**(Generate Baseline Response):像往常一样对查询生成初始回答。
2. **规划验证**(Plan Verifications):基于查询与基线回答,生成一组用于核查事实声明的验证问题。
3. **执行验证**(Execute Verifications):逐一回答这些验证问题,与基线回答比对以发现不一致。
4. **生成最终验证后回答**(Generate Final Verified Response):综合发现的不一致,产出修正后的回答。

针对第 3 步(执行验证),论文比较了四种变体:
- **Joint**:规划与执行用一个提示完成。
- **2-Step**:规划与执行分两个提示,执行时上下文只含验证问题、不含基线回答。
- **Factored**:每个验证问题作为完全独立的提示分别回答,彼此与基线回答均不交叉。
- **Factor+Revise**:在 factored 基础上,额外增加一个显式 cross-check 提示来推理不一致。

关键设计动机是:让验证问题不去 attend 原始基线回答,可避免模型重复(copy/repeat)自身的幻觉,这与 [[self-correction]] / [[self-refine]] 的思路相关,但通过分解为更简单的子问题实现。本文不使用 [[tool-use]] 或 [[retrieval-augmented-generation]],仅靠 LLM 自身的 [[reasoning]]。

## 结果

基座模型为 [[llama]] 65B(greedy decoding),与 [[llama-2]] 70B Chat(zero-shot / CoT)等基线对比。

- **列表类任务(Wikidata)**:precision 从 Llama 65B few-shot 的 0.17 提升到 CoVe (factored) 的 0.32,超过两倍;CoVe (two-step) 达 0.36。幻觉实体(负例)从 2.95 降到 0.68,而正例仅小幅下降(0.59 → 0.38)。
- **Wiki-Category list(更难)**:precision 从 0.12 提升到 0.22(factored)。
- **闭卷 MultiSpanQA**:F1 从 few-shot 基线 0.39 提升到 CoVe (factored) 0.48,约 23% 提升,precision 与 recall 均有增益。
- **长文本传记生成(FactScore)**:CoVe (factor+revise) 达 71.4,显著高于 few-shot 基线 55.9(提升 28%),并超过 [[instructgpt]](41.1)、[[chatgpt]](58.7)和 PerplexityAI(61.6,基于检索),平均事实数仅从 16.6 略降到 12.3。
- factored / 2-step 一致优于 joint,验证了"验证问题不应 attend 基线回答"的假设;factor+revise 的显式推理进一步把 FactScore 从 63.7 提升到 71.4。
- 量化观察:在 Wikidata 上 few-shot 基线整体列表答案仅约 17% 正确,但逐个用验证问题查询时约 70% 能被正确回答——短问答比长文本查询更准确,这正是 CoVe 有效的根源。
- [[instruction-tuning]] 与 [[chain-of-thought]] 在这些任务上均未降低幻觉;LLM 生成的验证问题优于模板化的 yes/no 启发式问题,开放式验证问题优于 yes/no 形式。

局限:CoVe 不能完全消除幻觉,改进上界受模型自身能力(是否"知道自己知道")约束,且会增加推理开销。

## 在本 wiki 中的位置

CoVe 是用 [[prompt-engineering]] 与 [[self-correction]] 缓解 [[hallucination]] 的代表方法,与 [[self-refine]]、[[self-consistency]]、[[react]] 等推理/自纠正路线同属一脉,但强调"分解验证 + 独立作答"以避免重复幻觉。作者团队来自 [[facebook-ai-research]](Meta AI),[[jason-weston]] 等参与。它与基于检索的 [[retrieval-augmented-generation]] 路线互补——论文明确指出给验证步骤加上 [[tool-use]] / 检索是值得探索的扩展。
