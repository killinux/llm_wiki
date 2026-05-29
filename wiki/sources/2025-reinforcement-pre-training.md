---
type: source
subtype: paper
tags:
  - reinforcement-learning
  - pre-training
  - reasoning
  - scaling
  - large-language-models
created: 2026-05-29
updated: 2026-05-29
arxiv: 2506.06326
raw: raw/2506.06326.pdf
authors:
  - Qingxiu Dong
  - Li Dong
  - Yao Tang
  - Tianzhu Ye
  - Yutao Sun
  - Zhifang Sui
  - Furu Wei
year: 2025
---

# Reinforcement Pre-Training (RPT)

把 next-token prediction 重新表述为一个带可验证奖励的 next-token reasoning 任务,用 [[reinforcement-learning]] 在海量无标注文本上做通用预训练,从而把整个语料变成 RL 训练数据。

## 问题

[[large-language-models]] 的能力主要来自在海量文本上 scale [[fine-tuning|self-supervised]] 的 next-token prediction;而 [[reinforcement-learning]] 这条路线(包括 [[rlhf]] 与 RLVR / reinforcement learning with verifiable rewards)虽能显著增强 [[reasoning]] 能力,却面临 scalability 瓶颈——RLVR 依赖大规模、带可验证答案的标注数据,获取成本高昂。本文要回答:能否把 RL 的可验证奖励机制接到自监督预训练上,既保留 next-token prediction 的可扩展性,又获得 RL 带来的推理增益,同时避免 [[reward-model|reward hacking]]。

## 方法

核心思想是把标准 next-token prediction 改写成 next-token reasoning:对任意上下文,模型先生成一段 [[chain-of-thought]] 推理,再给出对下一个 token 的预测。

- **可验证的内在奖励(prefix matching reward)**:在字节级别比较模型预测与真实续写。若预测 token 的字节序列在合法 token 边界上是 ground-truth 续写的前缀,则奖励为 1,否则为 0。奖励信号直接来自数据本身,无需人工标注。
- **on-policy RL 训练**:对每个 token 位置采样 G 个 (thinking + prediction) 响应,用 GRPO(Group Relative Policy Optimization)做 on-policy 优化。
- **entropy-based token 过滤**:过滤掉低熵(容易预测)的位置,把训练集中在高熵、更难、更能从推理中受益的 token 上。
- **训练设置**:base model 为 Deepseek-R1-Distill-Qwen-14B([[llama|属 distilled reasoning 模型]]),训练数据为 OmniMATH(4,428 道竞赛级数学题与解答)。

这一重述把通常用于 next-token prediction 的无标注文本,转化为通用 RL 的大规模训练资源;同时通过给每一步预测分配更多"思考"([[test-time-compute|更多 compute]]),把语言建模准确率推得更高。

## 结果

- **next-token prediction 准确率(OmniMATH 验证集,按难度)**:RPT-14B 在 easy / medium / hard 上分别为 45.11 / 33.56 / 23.75,全面超过标准 NTP 基线(R1-Distill-Qwen-14B:41.60 / 29.46 / 21.32;Qwen2.5-14B:41.90 / 30.03 / 20.65)。
- **scaling 特性**:next-token prediction 准确率随训练 compute 呈 power-law 提升,easy/medium/hard 三档的 [[scaling-laws|scaling 曲线]] R-squared 均高于 0.98,表明可预测、可持续地随算力增长。
- **作为 RLVR 的初始化**:在 Skywork-OR1 上继续做 reinforcement fine-tuning,RPT-14B 由 RL 前 51.6 提升到 RL 后 58.3,显著优于"continual-NTP 再 RLVR"的基线(RL 后约 52.7)。
- **zero-shot 下游任务**:推理模式下,RPT-14B 在 SuperGPQA 上 39.0(vs R1-Distill-Qwen-14B 32.0)、在 [[mmlu|MMLU-Pro]] 上 71.1(vs 52.7)。
- **推理模式分析**:RPT 的 next-token reasoning 更多表现为 deliberation、hypothesis generation 与 verification,使用更多推断/演绎式推理,而非标准 reasoning 模型那种"解题式"模式。

局限:实验聚焦数学文本、规模限于 14B。

## 在本 wiki 中的位置

RPT 处在 [[reasoning]]、[[reinforcement-learning]] 与预训练 scaling 三者的交叉点。它与依赖人工偏好/标注的 [[rlhf]]、[[direct-preference-optimization]] 不同,用 [[reward-model|可验证内在奖励]]替代外部标注,可视为把 RLVR(如 [[process-reward-model]]、[[outcome-reward-model]] 等 [[reward-design]] 路线)从狭窄的标注数据扩展到全量语料的尝试。其 [[chain-of-thought]]+RL 的训练范式与 [[star-self-taught-reasoner]]、[[rejection-sampling-fine-tuning]]、[[self-improvement]] 等 bootstrapping 推理方法相关,并把 [[test-time-compute|test-time-scaling]] 的思路前移到预训练阶段。出自 [[microsoft-research]] 与 [[peking-university]]、[[tsinghua-university]]。
