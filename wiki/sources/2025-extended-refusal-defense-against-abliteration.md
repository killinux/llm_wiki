---
type: source
subtype: paper
tags: [llm-safety, abliteration, refusal-direction, alignment, jailbreak-defense, fine-tuning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2505.19056
raw: raw/2505.19056.pdf
authors: [Hareth Abu Shairah, Hasan Abed Al Kader Hammoud, Bernard Ghanem, George Turkiyyah]
year: 2025
---

# An Embarrassingly Simple Defense Against LLM Abliteration Attacks

通过 **extended-refusal**(扩展式拒绝)微调,把安全信号从单一潜在方向分散到多个 token 位置与表示维度,使模型在遭受 abliteration(refusal direction 消融)攻击后仍能保持 >90% 的拒绝率。

## 问题

[[large-language-models]] 通常通过 [[alignment]](SFT 或 [[rlhf]])学会拒绝有害指令,但这种对齐往往很"浅":拒绝行为高度集中在 residual stream 的**单一潜在方向(refusal direction)**上,且只出现在开头少数 token 位置。最近提出的 **abliteration** 攻击(Arditi et al., 2024)正是利用这一弱点——它识别出最负责拒绝行为的单一方向,通过对每层输出投影矩阵做正交投影(weight surgery)将该方向消除,从而在几乎不影响通用 perplexity 的情况下,把 [[llama-2]]-7B-Chat 的拒绝率从 100% 打到约 20%。问题核心是:常规安全对齐产生的拒绝既简短又句式单一(formulaic),形成易被定位和中和的"集中激活签名"。

## 方法

核心思路:不改变模型"是否拒绝",而是改变"如何拒绝"。

- **Extended-Refusal (ER) 数据集**:从 Beavertails、AdvBench、StrongReject、TDC-2023 合并出 4,289 条有害 prompt,用 [[gpt-4o-mini]] 之外的 GPT-4o 生成结构化拒绝,每条回复含三部分:(i) 中性主题概述 explanation,(ii) 明确拒绝 refusal,(iii) 简短伦理说明 justification。再混入 5,711 条来自 Alpaca-GPT4-en 的良性指令对(保持通用能力),共 10,000 条样本组成 D_FT。
- **微调**:对 [[llama-2]]-2-7B-Chat、Qwen2.5-3B-Instruct、Qwen2.5-1.5B-Instruct 在 D_FT 上微调 3 epoch,学习率 1e-6。
- **Abliteration 复现**:对每个 (layer ℓ, position p) 计算有害集 H 与良性集 B 的均值激活之差作为候选 refusal direction;选出使拒绝准确率下降最多的方向 r̂,归一化后用正交投影 P = I − r̂r̂ᵀ 从每层输出矩阵中投影掉该分量。
- 攻击时筛选条件:在保持 coherence ≥ 70% 的前提下最大化拒绝退化。

通过把拒绝信号在时间(更多 token 位置)和语义上"延展、延迟",安全方向被分散到多个维度,使单方向消融难以奏效。

## 结果

- **抗 abliteration**:基线模型遭 abliteration 后拒绝率暴跌 70–80 个百分点([[llama-2]]-7B 100%→20.7%,Qwen2.5-1.5B 93.8%→13.6%,Qwen2.5-3B 93.1%→15.1%);ER 模型则保持 >90%([[llama-2]]-7B-Extended 100%→92.7%,Qwen2.5-3B-Extended→90.9%,Qwen2.5-1.5B-Extended→96.7%),最大下降仅约 9.1%。
- **通用性能代价小**:ER 微调前 [[mmlu]] 仅下降 0.5–1.3%;perplexity(C4 子集 1000 段)有中等上升。Coherence 用 Qwen-2.5-14B 作 [[llm-as-judge]] 评估。
- **拒绝评估**:用 CatQA(550 题)+ Qwen-2.5-14B judge(附录另用 Llama-Guard-3-8B)。
- **泛化到更多 jailbreak**(Table 2,越低越好):[[llama-2]]-7B 的 DAN 3.7→1.3、HarmBench 8.1→1.6;Qwen2.5-1.5B 的 WildJailbreak 90.5→44.1、TrustLLM 22.8→8.3;Qwen2.5-3B 的 WildJailbreak 93.8→41.0、TrustLLM 39.0→10.3。
- **抗 benign fine-tuning drift**:在 Databricks Dolly 15k 上微调,base 模型拒绝率几百步内跌破 60%,ER 模型 1400+ 步后仍 >90%。
- **特征空间分析(PCA)**:abliteration 对标准模型显著拉近有害/良性表示(Euclidean 距离降 28.8/33.9/28.7),对 ER 模型影响小得多(降 10.0/7.7/13.7);如 Qwen2.5-1.5B,标准模型距离降 37.8% 而 ER 仅降 13.4%——说明 ER 的分散表示阻止了类别边界塌缩。
- **组件消融**(Qwen2.5-3B,Table 3):仅用 Refusal 部分微调,abliteration 后拒绝率 90.9→17.8(降 73.1),而完整 ER 保持 90.9;Explanation/Justification 单独训练能保留较高拒绝但都不及完整三件套。

结论:安全表达的**形式本身就是一种安全机制**——把主题语境与伦理推理融入拒绝,模型不仅更难被攻击,拒绝也更透明可解释。

## 在本 wiki 中的位置

本文属于 [[ai-safety]] / [[alignment]] 中"对齐鲁棒性与攻击防御"分支。它针对 abliteration 这类权重手术式(weight-surgery)攻击,与 [[rlhf]]、[[instruction-tuning]] 等对齐方法、以及 [[hallucination]]、[[constitutional-ai]] 等安全主题相关。被测模型涉及 [[llama-2]] 与 Qwen2.5 系列,评测用到 [[mmlu]]。研究机构为 [[kaust]]。其揭示的"浅层对齐 / 集中激活签名"问题,与 [[fine-tuning]] 导致安全退化的现象一脉相承。
