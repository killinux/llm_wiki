---
type: source
subtype: paper
tags: [self-play, multi-agent, reinforcement-learning, self-improvement, llm-reasoning, llm-as-judge]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.23595
raw: raw/2510.23595.pdf
authors: [Yixing Chen, Yiding Wang, Siqi Zhu, Haofei Yu, Tao Feng, Muhan Zhang, Mostofa Patwary, Jiaxuan You]
year: 2025
---

# Multi-Agent Evolve: LLM Self-Improve through Co-evolution

提出 Multi-Agent Evolve (MAE),让同一个 LLM 实例化为 Proposer / Solver / Judge 三个互动智能体,通过强化学习协同进化,在没有人工标注数据和可验证奖励的前提下提升通用推理能力。

## 问题

[[reinforcement-learning]] 已显著提升 [[large-language-models]] 的推理能力,但 RL for LLM 的成功严重依赖人工整理的数据集与可验证奖励(verifiable reward),这限制了其可扩展性与通用性。受 Go 等游戏启发的 [[self-play]] RL 方法(如 [[deepseek-r1]] 之外的 Absolute Zero Reasoner 等)试图在无人工标注下自我提升,但它们主要依赖一个有 grounding 的环境(如 Python 解释器、游戏引擎)来提供反馈,难以推广到开放式通用领域(自然语言推理、通用知识)。核心研究问题:能否构建一个无需人工标注、可在通用领域让 LLM 自我提升的 RL 框架?

## 方法

MAE 把单个基座 LLM 实例化为三个互动角色,形成闭环 propose-solve-judge 的自我进化循环,并用 RL 联合训练。

- **Proposer**:生成可解但有挑战性的问题。可选地以参考问题 q_ref(无 ground truth,从约 1K 种子数据采样)为条件,也可从零生成。奖励是三项加权和(λ 均为 1/3):**Quality Reward**(由 Judge 评问题清晰度/可解性)、**Difficulty Reward**(R_difficulty = 1 − 平均 solve score,Solver 越解不出奖励越高,形成对抗 co-evolution)、**Format Reward**(检查 `<question>` 标签唯一性)。
- **Solver**:对问题生成答案。奖励为 **Judge Reward**(Judge 评答案质量正确性)+ **Format Reward**(`<answer>` 标签),两者权重各 0.5。
- **Judge**:作为生成式 reward model,采用 [[llm-as-judge]] 范式,先在 `<think>` 标签内做 [[chain-of-thought]] 分析再输出 `<score>`。无任何 ground truth,用严格 rubric 给答案(1-10 分)和问题打分。也有 Format Reward。
- **Quality Filtering**:只有被 Judge 评为 Quality Score ≥ 0.7 的问题才进入持续演化的有效问题池,稳定训练。
- **Task-Relative REINFORCE++**:沿用 Absolute Zero Reasoner 的训练范式,对每个角色分别计算 baseline 与归一化 advantage A_role^norm = (r − μ_role)/σ_role,是 per-question 算法(如 GRPO)与单 baseline(REINFORCE++)的插值,然后对共享 backbone 做同步参数更新。

## 结果

基座模型为 [[qwen2-5-instruct]] 系列的 Qwen2.5-3B-Instruct。评测覆盖数学、代码、推理与通用知识共 14+ benchmark,含 [[gsm8k]]、MATH、ARC-Challenge、[[mmlu]]、GPQA、CommonsenseQA、OpenBookQA、NaturalQuestions、TriviaQA、SQuAD、BoolQ、[[humaneval]]、MBPP、[[truthfulqa]]、BBH、LiveBench Reasoning、AMC、Minerva、WinoGrande、Olympiad、MMLU-Pro。基线含 Base、SFT(LoRA 128-rank,用 ground truth)、AZR(Absolute Zero Reasoner)。

- 整体平均提升 4.54%。
- **MAE (zero)**(仅 16 条自生成种子、无真实数据)Overall Avg. 58.51,超过 Base 55.33 和 AZR 57.72;MATH 60.40 → 68.20,AMC 39.76 → 44.58,ARC-C 80.60 → 84.20,CQA 66.80 → 71.54,SQuAD 78.20 → 92.28;在 BBH(+4.94)、AMC(+9.64)等复杂推理上明显超过 AZR。
- **MAE (half reference)** 取得最佳整体结果:ID Avg. 68.95、OOD Avg. 43.96、Overall Avg. 59.87,优于 with/no reference 变体。
- 所有 MAE 变体均不使用 ground truth,却一致超过用 ground truth 训练的 SFT;SFT 反而相对 Base 退化(53.87 vs 55.33)。MAE (with reference) ID 65.07 vs SFT 63.28,OOD 43.18 vs 37.41。
- 训练稳定性:批大小 128 下稳定训练超过 250 步(对比 R-Zero 仅 45/15 步),Difficulty Score 随训练上升,问题质量持续保持;agent 多样性是稳定性基础,单一角色 collapse 会拖垮整个框架。

## 在本 wiki 中的位置

本文属于 [[self-improvement]] / [[self-evolving-agents]] 方向,把 [[self-play]] 从零和游戏推广到通用领域,关键在于用 [[llm-as-judge]] 替代可验证环境来提供奖励,使 zero-sum 不再是必需。与 [[rlhf]]、[[rlaif]] 不同,MAE 不依赖人工偏好或外部 verifier;与单纯的 [[multi-agent-reinforcement-learning]] 不同,三个角色从同一 backbone 实例化并联合训练。代码地址 github.com/ulab-uiuc/Multi-agent-Evolve。作者来自 [[university-of-illinois-urbana-champaign]]、[[peking-university]] 与 [[nvidia]]。
