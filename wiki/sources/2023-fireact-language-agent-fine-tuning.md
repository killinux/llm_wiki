---
type: source
subtype: paper
tags: [llm-agent, fine-tuning, react, language-agent, question-answering]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2310.05915
raw: raw/2310.05915.pdf
authors: [Baian Chen, Chang Shu, Ehsan Shareghi, Nigel Collier, Karthik Narasimhan, Shunyu Yao]
year: 2023
---

# FireAct: Toward Language Agent Fine-tuning

FireAct 系统性地研究了对 LLM 进行 fine-tuning 以构建 [[llm-agents|llm-agent]] 的方向,提出用多任务、多 prompting 方法生成的 [[react]] 轨迹来微调 backbone LM,使语言智能体在性能、鲁棒性、泛化、效率与成本上全面优于仅依赖 few-shot prompting 的现成模型。

## 问题

目前大多数 language agent 直接对现成 LLM 做 [[few-shot-prompting]],存在三个问题:(1) LLM 并非为 agentic 用例(生成动作、自我评估)设计,few-shot 提供的学习支持有限,导致小模型性能与鲁棒性差;(2) 一些高级 agent 方法(如 [[reflexion]]、[[react]])只能由 [[gpt-4]] 支撑,带来高成本、高延迟以及可控性/可复现性问题;(3) 尽管 language agent 与 LM [[fine-tuning]] 各自都是热门话题,二者交叉(即面向 agent 用途的微调)却被严重忽视,已有工作仅局限于 web navigation 或 API 工具使用的单一模型族,缺乏系统研究。

## 方法

FireAct 基于 [[react]] 框架(thought-action-observation 多轮循环),核心是用**强 LM 生成多样化的微调数据**来蒸馏出更小的智能体 LM:

- **数据生成**:用 [[gpt-4]] 在多个 QA 任务上、用多种 prompting 方法生成 task-solving 轨迹,只保留答对的轨迹,统一 reformat 成 [[react]] 格式后用于微调较小的 LM(如 [[llama-2]])。
- **混合 prompting 方法**:除 [[react]] 外,纳入 [[chain-of-thought]](单轮 ReAct,thought=中间推理,action=返回答案,适合无需工具的简单问题)与 [[reflexion]](在第 6 和第 10 轮加入反思,使长轨迹能调整策略)。显式提倡数据多样性。
- **推理时**:微调后的 agent 无需 few-shot prompting,可隐式地根据任务复杂度自适应选择方法,生成长度灵活的 [[react]] 轨迹。
- **任务/工具**:在 [[hotpotqa]]、Bamboogle、[[strategyqa]]、[[mmlu]] 四个 QA 数据集上训练与评测;工具为基于 SerpAPI 的 Google 搜索。
- **模型与微调**:数据生成用 GPT-4,微调与 prompting 对比用 [[gpt-3-5]]、[[llama-2]](7B/13B)、CodeLlama(7B/13B/34B);大多用 [[lora]],部分用 full-model 微调。

## 结果

- **微调显著提升性能**:在 HotpotQA 上,GPT-3.5 用 [[react]] prompting 的 EM 为 31.4,用 500 条 ReAct 轨迹微调升至 39.2(+25%),混合 ReAct+CoT 进一步升至 41.0(+31%)。[[llama-2]]-7B 从 14.8 提升到 26.2(相对 +77%),Llama-2-13B 从 21.2 到 34.4(+62%)。微调后的 Llama-2-13B 可超过所有 GPT-3.5 的 prompting 方法。
- **更便宜更快的推理**:无需 few-shot 上下文,微调 GPT-3.5 相比 prompting GPT-3.5 推理时间减少约 70%(9.0s → 2.7s/trial),即便微调推理单价贵 8 倍,总成本仍更低(2.6×10⁻³ → 2.2×10⁻³ 美元/trial)。
- **更鲁棒**:在搜索 API 有 0.5 概率返回 "None" 或随机响应的噪声设定下,[[react]] 的 EM 下降 33.8%(None)/28.0%(random),而 FireAct 仅下降 14.2% / 5.1%。
- **更好泛化**:在 HotpotQA 上微调的 GPT-3.5 在 Bamboogle 上取得 44.0 EM,超过 prompting 的 40.8 EM。
- **数据规模**:GPT-3.5 样本效率高,100 条即可达 EM ≈ 35;Llama 模型需 500 条才"涌现"出非平凡分数,1000 条 Llama-2-13B 可匹敌 100 条微调的 GPT-3.5。
- **方法选择空间**:HotpotQA 上随机选方法仅得 32.4 EM,而 oracle(每题选最佳方法)可达 52.0 EM,显示方法选择仍有大量改进空间。
- **多任务微调**:加入 StrategyQA/MMLU 数据不损害 HotpotQA/Bamboogle 性能,且多任务+多方法微调能提升所有任务表现,暗示可用单个多任务 LM 替代多个单任务 agent。

## 在本 wiki 中的位置

本文位于 [[llm-agents|llm-agent]] 与 [[fine-tuning]] 的交叉点,是 [[react]]、[[chain-of-thought]]、[[reflexion]] 等推理-行动范式的延伸:它不再仅靠 prompting,而是把这些方法生成的轨迹蒸馏进更小的 backbone LM。可与同样基于 ReAct 的 [[reflexion]]、自我改进类工作对照阅读;在"何时 fine-tune vs. prompt"这一议题上提供了实证依据(prompting 适合探索/新任务,fine-tuning 适合已知任务的大规模工业落地)。作者 [[shunyu-yao]] 亦是 [[react]] 的提出者。
