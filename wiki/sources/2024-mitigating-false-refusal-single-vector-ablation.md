---
type: source
subtype: paper
tags:
  - false-refusal
  - ai-safety
  - activation-steering
  - representation-engineering
  - model-editing
  - refusal-vector
created: 2026-05-29
updated: 2026-05-29
arxiv: "2410.03415"
raw: raw/2410.03415.pdf
authors:
  - Xinpeng Wang
  - Chengzhi Hu
  - Paul Röttger
  - Barbara Plank
year: 2024
---

# Surgical, Cheap, and Flexible: Mitigating False Refusal in Language Models via Single Vector Ablation

本文提出一种 training-free、model-agnostic 的方法,通过提取并消融(ablation)单个「false refusal vector」来缓解 [[large-language-models]] 的过度拒绝(false refusal)行为,同时保持模型的安全性与通用能力。

## 问题

要让 LLM 既 helpful 又 harmless 需要在拒绝行为上做精细校准:模型应拒绝恶意请求(如 "how do I kill someone?"),但不应拒绝表面相似的安全请求(如 "how do I kill a Python process?")。这种 **false refusal(过度拒绝/错误拒绝)** 即使在最强的模型上也难以避免,会降低模型的可用性。

现有缓解方法各有局限:

- **基于训练的方法**:可有效降低 false refusal,但 inflexible,安全性只能在训练时校准。
- **训练自由的方法**:更灵活,但 costly(推理时需额外计算)且 imprecise(对通用能力有意外的负面影响)。

## 方法

核心思想是用 **single vector ablation** 进行精细的拒绝校准。基于 [[activation-steering]] / difference-in-means(Arditi et al. 2024、Zou et al. 2023)的 [[refusal-vector]] 提取思路:

- **提取 true refusal vector 与 false refusal vector**:用少量 harmful query 与 pseudo-harmful query(即 [[ORBench]] / OR-Bench-Hard 中诱发 false refusal 的查询),分别用 difference-in-means 计算 harmful/pseudo-harmful 与 harmless 激活的均值差;用 refusal score 作为过滤与选择标准。
- **关键发现**:单纯 ablate diff-in-means 的 false refusal vector 不够,因为 true refusal 与 false refusal 向量并不独立——消融任一个都会移除整体拒绝行为。
- **Orthogonalization(正交化)**:将候选 false refusal vector 对 true refusal vector 做正交化,得到 w'=w−λ·v·vᵀ·w,再消融正交化后的 false refusal vector。这样能在保持对 harmful 数据低 compliance 的同时,显著提高对 harmless 数据的 compliance。
- **Partial orthogonalization(部分正交化)**:引入系数 λ∈[0,1] 控制正交化强度,从而 fine-grained 地调节模型对 ambiguous 请求(如 "how to cut off the heads of a fish")的敏感度。λ 越小,false refusal vector 被修改越少,消融对 false refusal 的削弱越强,模型越 compliant。

方法可直接作用于模型权重(weight editing),推理时**无额外计算开销、无额外显存**,等价于推理时 steering。

## 结果

在四个 chat-tuned 模型上评估:[[gpt]] 之外的 Gemma-7B-It、[[llama-2]]-7B/13B/70B-Chat、[[llama-3]]-8B-Inst。评估三方面:safety(true refusal)、false refusal、general capability。

- **False refusal 大幅下降(compliance rate 上升)**:以 Llama2-7B-Chat 为例,OR-Bench-Hard 的 CR 从 14.8 → 65.6;XSTest-S(H) 从 13.6 → 42.4;OKTest 从 59.0 → 65.0。各模型在三个 false refusal 数据集上 CR 普遍提升。
- **安全性保持**:Harmful CR 与 JailbreakBench(JBB)CR 基本不变(均维持低位),true refusal 几乎不受影响。
- **通用能力几乎无损**:MMLU(5-shot)、ARC-C、Wikitext PPL 的绝对变化均小于 1.0。
- **正交化消融实验(Table 1, Llama2-7B-Chat)**:消融原始 r̂ 或 ŵ 会把 Harmful CR 推高到 46-93(破坏安全);而消融正交化后的 ŵ' 使 Harmful CR 仅 3.1,同时 ORBench-H CR 达 65.6、XSTest-S 达 57.6。
- **对比 SCAN(Cao et al. 2024)**:本方法 MMLU 更高(47.2 vs 40.5)、PPL 变化更小(+0.1 vs +1.56)、XSTest-Unsafe CR 更低(0 vs 6.5),且推理时间与显存均 unchanged,更 surgical 且 cost-efficient。
- **λ 的 fine-grained 控制**:降低 λ 可让模型对安全相关问题更不敏感、更 compliant;MMLU 准确率不随 λ 改变(因事先过滤了大幅改变首 token 分布的候选向量)。

## 在本 wiki 中的位置

本文属于 [[ai-safety]] / [[ai-alignment]] 中关于 helpfulness-harmlessness 权衡与 false refusal 缓解的方向,技术上属于 [[activation-steering]] / [[representation-engineering]] 与 [[model-editing]] 的交叉,使用单向量消融操作 [[refusal-vector]]。可与基于训练的对齐方法(如 [[rlhf]]、[[safety-fine-tuning]])对照,作为一种 training-free、推理零开销的替代方案。作者来自 LMU Munich、Bocconi University 与 Munich Center for Machine Learning。
