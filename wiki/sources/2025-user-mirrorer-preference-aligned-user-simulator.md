---
type: source
subtype: paper
tags:
  - user-simulation
  - recommender-system
  - llm-agent
  - preference-alignment
  - uncertainty
  - data-distillation
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.18142
raw: raw/2508.18142.pdf
authors:
  - Tianjun Wei
  - Huizhong Guo
  - Yingpeng Du
  - Zhu Sun
  - Huang Chen
  - Dongxia Wang
  - Jie Zhang
year: 2025
---

USERMIRRORER 是一个利用推荐系统 (RS) 中真实用户反馈来微调轻量级 [[large-language-models]] 用户模拟器的数据构造框架,通过生成显式决策过程来消歧、用不确定性分解来蒸馏高质量样本,使小模型在偏好对齐上超越更强的教师模型与商用 LLM。

## 问题

[[user-simulation]] 对开发与评估 [[recommender-systems|recommender-system]] 越来越重要。传统模拟器多为基于规则或 [[reinforcement-learning]] 的方法,只关注系统内偏好,忽略外部上下文与决策推理。基于 [[large-language-models]] 的模拟器有两大缺陷:(1) 过度依赖预训练知识而不在海量用户反馈上微调,导致任务适配差;(2) 依赖强大 LLM 后端,大规模模拟成本过高。

RS 中的原始用户反馈本身是一种被忽视的对齐资源,但难以利用,因为它具有两个特性:

- 用户反馈通常只记录可观测行为,缺失底层**决策过程**,带来 ambiguity,且难以检测 noisy 数据(如误点击)。
- RS 产生海量且质量参差的反馈,必须筛选高质量样本才能高效微调。

## 方法

框架分两阶段(见 Figure 4):

**1. 构建用户模拟场景 (User Simulation Scene)。** 把来自 8 个不同领域的反馈统一为一个 LLM agent 可理解的场景。核心元素是 **memory**(用户 profile 静态属性 + interaction history)与 **exposure**(用户做决策时看到的曝光列表)。采用 listwise 的 impression-aware 设定:用户对整个曝光列表 [A]、[B]、[C] 等选项做行为(如点击),而非逐项预测。对缺失真实曝光的数据集,用随机采样、[[collaborative-filtering]] 和基于内容的 [[approximate-nearest-neighbor-search]] 三种来源构造混合曝光列表(K=32,再随机采样 N=2~12 项并插入 ground truth)。形式化定义:模拟器参数 θ 在动作空间 A 上定义条件于场景 X 的类别分布 P_θ(a_i|X)。

**2. 决策过程生成 + 基于不确定性分解的数据蒸馏。**
- **Decision-process Generation:** 用强 LLM 生成显式决策过程作为预测行为的 rationale,以消歧。借鉴消费者行为学的 **Engel Kollat Blackwell (EKB)** 模型,改编为四阶段:Stimulus(触发因素,含时间/地点/社会上下文与需求/情绪)、Knowledge(从曝光中抽取相关属性)、Evaluation(用不同风格评估行为,从直觉到逻辑)、Decision。
- **Uncertainty-based Distillation:** 借鉴用 clarification 分解不确定性的思路,把总不确定性 H(P(Y|X)) 分解为 aleatoric(数据)不确定性 I(Y;C|X) 与 epistemic(模型)不确定性。对同一场景比较强模型 (Qwen2.5-32B-Instruct) 与弱模型 (Llama-3.2-3B-Instruct) 的 epistemic 不确定性差 Δ_EU,差距大的场景更复杂、更值得纳入训练集。每场景采样 N=10 个决策过程。
- **Sampling Denoised Behaviors:** 用 [[rejection-sampling-fine-tuning]] 式拒绝采样去噪——若 N 个决策过程无一匹配真实行为则判为 noisy 并丢弃;否则把行为标为 accepted/rejected,以最高置信度样本构成偏好对。

**3. 微调。** 主要微调 [[llama]]-3.2-3B-Instruct(也验证 [[qwen]]2.5-3B-Instruct)。两阶段:先用 accepted 响应做 [[supervised-fine-tuning]],再用 [[direct-preference-optimization]] 做偏好对齐;还实验了 [[grpo]] (GRPO)。

## 结果

- **数据规模:** 约 10,000 样本即达到数据质量与算力的最优平衡,之后增益边际化(Figure 5)。
- **主表 (Table 1, accuracy %):** Llama-3.2-3B-Instruct 基线 22.7 → +SFT 27.1 → +SFT+DPO **55.0**(Overall);Qwen2.5-3B-Instruct 基线 27.2 → +SFT+DPO **54.7**。微调后的轻量模拟器不仅超越基础 LLM 与更强的教师模型 (Qwen2.5-32B Teacher 39.7),在多数情况下还超过最先进的商用模型:[[gpt-4o]] 系列中的 GPT-5 (2025-08-07) 42.2、GPT-5.1 (2025-11-13) 42.6、[[gemini]]-2.5-Flash 42.5、Gemini-3.0-Pro-Preview 47.7。DPO 改进比 GRPO 更显著。
- **数据选择策略 (Table 2):** 本文 pipeline(55.0 Overall)优于随机采样 (with Decisions 53.9)、High/Low/Diff Accuracy 及 [[lima]] 同源的 IFD (Instruction-Following Difficulty) 分数 (52.7) 等基线,在真实曝光 (MIND) 与合成曝光上均更稳健。
- **决策过程分析 (Figure 6):** 用户表达 "thematic preferences" 比仅表达 "boredom" 时预测准确率更高;"logical" 评估风格优于 "intuitive";stimulus/knowledge 因子越多越详细,对齐越好。
- **对 RS 的反馈价值 (RQ2, Table 3):** 在 Movielens 与 Steam 上,用微调模拟器的反馈增强 [[lightgcn]]、[[diffrec]]、[[sasrec]]、[[narm]] 等 RS 训练,Recall/NDCG/MRR 三指标全面提升。例如 Movielens 上 DiffRec 的 R@5 相对 Backbone 提升 24.1%,N@5 提升 37.1%。

## 在本 wiki 中的位置

本文属于 [[user-simulation]] × [[llm-for-recommendation]] 交叉方向,与 [[recagent]]、[[agent4rec]]、[[lusifer]] 等 LLM-based 用户模拟器相关,但独特之处在于把 RS 真实反馈作为微调信号、用 EKB 决策过程消歧、并用不确定性分解做数据蒸馏。方法上联系 [[direct-preference-optimization]]、[[supervised-fine-tuning]]、[[rejection-sampling-fine-tuning]] 与 [[grpo]]。数据集涉及 [[mind]]、[[amazon-reviews]]、[[kuairec]]、[[movielens]]、[[steam-dataset]] 等。代码与数据开源 (USERMIRRORER / UserMirrorer-Llama-DPO)。
