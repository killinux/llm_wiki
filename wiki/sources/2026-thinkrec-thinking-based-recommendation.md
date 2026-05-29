---
type: source
subtype: paper
tags: [llm-for-recommendation, reasoning, lora, mixture-of-experts, sequential-recommendation, large-language-models]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2505.15091
raw: raw/2505.15091.pdf
authors: [Qihang Yu, Kairui Fu, Zheqi Lv, Shengyu Zhang, Xinhui Wu, Chen Lin, Feng Wei, Bo Zheng, Fei Wu]
year: 2026
---

# ThinkRec: Thinking-based Recommendation via LLM

ThinkRec 提出一个"思考激活 + 实例级专家融合"框架,把 [[llm-for-recommendation]] 从依赖点击相似度的 System 1 直觉模式,推进到带有显式 [[chain-of-thought]] 推理的 System 2 理性模式。

## 问题

现有的 LLM4Rec 方法(item scoring / item generation / hybrid modeling)本质上都类似认知科学中的 **System 1**:依赖点击历史的表层特征去匹配相似 item,而不通过更深层的行为逻辑进行推理。论文用一个例子说明其缺陷——用户随时间"不喜欢 Dune、喜欢 The Three-Body Problem 与 Foundation"(都属科幻),System 1 直觉会推断用户也会喜欢同为科幻的 Hyperion,但用户实际厌恶小说中的哲学/形而上学主题,导致错误推荐。

作者提出两个核心挑战:
- **Challenge 1**:推荐任务的数据与优化目标(hit rate / ranking 等指标)无法在 LLM 中"激活思考";盲目用 RL 强化思考会退化为简单 next-token 预测。
- **Challenge 2**:用户行为分布高度多样,统一建模会淹没个性化偏好、削弱推理能力;且仅从高分 item 与通用世界知识推断意图,信息基础不足。

## 方法

ThinkRec 基于 [[llama]]-3-8B,主要由三部分组成(见论文 Figure 2):

- **思考增强推荐(数据构建 + 思考激活)**
  - **Reasoning data construction**:用预训练摘要模型 PolyLM-Qwen-7B 从冗长/含噪的 item metadata 中抽取至多 10 个关键词,增强 item 语义;并把低分(dislike)交互也加入历史序列以建模完整偏好。每个 item 被增强为 `title + feature emb (label) + description(keywords)`。
  - 由于推荐数据缺乏显式推理轨迹,用强推理模型 **QwQ-32B** 合成解释:对若干千条训练样本反复 query,直到产出正确预测,记录最新解释作为 reason(含 reflect/reanalysis turn)。
  - **Thinking activation**:对常规推荐数据(二元标签)与合成推理数据做 **mixed sampling**,把 prompt 与对应输出(label `i_l` 或 reason `r_{u,t}`)拼成一个语言建模实例联合训练。损失含两部分:思考的 token 级交叉熵 `L_think` 与推荐的 BCE 损失 `L_rec`(从 "Yes" token 的 logit 计算相关性分数 `î`),按实例类型用权重 α/β/η/γ 加权组合。
  - 通过把 [[collaborative-filtering]] embedding 经 projector 注入 LLM 语言空间(类似 [[p5]]、CoLLM),融合协同信号。

- **推荐专家融合(Recommendation Experts Fusion)**
  - **Base expert fine-tuning**:用预训练协同模型得到的 user embedding 做无监督聚类,把用户划分为 N 组;先在全量数据上训练 global LoRA(`LoRA_global`),再用分组数据微调其最后 8 层,得到一组 base experts `{LoRA_1..N}`,用 [[lora]] 实现个性化。
  - **Instance Wise Expert Fusion**:用各组 user 特征均值作为专家表示,计算 user 特征与专家的 cosine 相似度并经 softmax 得参与分数 `w^u`;用熵阈值的 gating 机制——高熵(>0.95N)用 global LoRA,集中型(max>0.5+0.6/N)用单一专家,其余做加权融合。这样把"思考难度"通过信息分类与个性化机制降低。

- **Staged Training**:先在全量纯文本条件下训 `LoRA_global`,并行训 ID 条件的协同模型 → 用 user 特征分组数据微调 `LoRA_global` 最后 8 层得 base experts → 固定 `LoRA_global` 训练 projector 投影协同 embedding。
- 部署时,因推理能力已内化进参数,在 ranking 阶段把输出约束为单个 token,可一次前向产出 batch 级结果,效率友好。

## 结果

在三个真实数据集上评估(按时间戳划分以避免数据泄露,过滤交互数 <20 的用户/item):
- **ML1M**(MovieLens-1M):5,945 users / 3,687 items;**Yelp**:40,617 users / 60,014 items;**Book**(Amazon Book 子集):22,686 users / 47,059 items。

指标:AUC、UAUC、NDCG@5、MAP@5(推荐质量),METEOR、BLEURT(生成解释质量)。Baselines 含 [[matrix-factorization|MF]]、[[lightgcn]]、[[sasrec]]、gSASRec、Prompt4NR、[[tallrec]]、CoLLM(均扩展为 Llama3-8B + LoRA 以公平对比)。

主要数字(Table 2,ThinkRec 记为 Ours):
- **ML1M**:AUC 0.7764、UAUC 0.6775、NDCG@5 0.7747、MAP@5 0.4774(多数指标最优)。
- **Yelp**:AUC 0.6955、NDCG@5 0.8585、MAP@5 0.2826(AUC 最优)。
- **Book**:AUC 0.8302、NDCG@5 0.6858、MAP@5 0.2977(AUC 最优)。
- 相比此前 SOTA **CoLLM**:Yelp AUC +0.0582(+9.13%)、ML1M AUC +0.0623(+8.72%)。
- 摘要性结论:ThinkRec 平均比 SOTA baseline 在 AUC 上高 7.96%、在 METEOR 上高 56.54%(解释质量),BLEURT 平均提升 23.35%。
- SASRec 在非 LLM baseline 中表现较强(ML1M UAUC/MAP@5 领先);TALLRec 在 ML1M NDCG@5(0.7683)在非 ThinkRec 方法中最高。ThinkRec 在几乎所有数据集/指标上取得最均衡且鲁棒的表现。

三个研究问题:RQ1 整体性能优势、RQ2 思考激活机制的必要性、RQ3 专家融合对性能的影响。

## 在本 wiki 中的位置

本文属于 [[llm-for-recommendation]] 方向,把 [[large-language-models]] 的 [[reasoning]] 能力(System 2 / [[chain-of-thought]] 风格)引入 [[recommender-system]],与 [[tallrec]]、[[p5]] 等 LLM4Rec 工作以及 [[sasrec]]、[[lightgcn]]、[[matrix-factorization]] 等传统推荐方法构成对比。技术上结合了 [[lora]] 个性化、[[mixture-of-experts]] 思想的实例级专家融合、[[collaborative-filtering]] embedding 注入,以及用强推理模型(QwQ-32B)做的推理数据合成与蒸馏,与 [[reflection]]、[[self-improvement]] 等推理增强范式相关。由 [[zhejiang-university]] 与 Ant Group 合作完成。
