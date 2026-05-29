---
type: source
subtype: paper
tags: [feature-selection, deep-recommender-systems, llm-for-recommendation, ctr, large-language-models, prompt-engineering]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2412.08516
raw: raw/2412.08516.pdf
authors: [Pengyue Jia, Zhaocheng Du, Yichao Wang, Xiangyu Zhao, Xiaopeng Li, Yuhao Wang, Qidong Liu, Huifeng Guo, Ruiming Tang]
year: 2025
---

# SELF: Surrogate-light Feature Selection with Large Language Models in Deep Recommender Systems

本文提出 **SELF**(SurrogatE-Light Feature selection),通过让多个 LLM 用世界知识对特征做语义排序、再用轻量 bridge network 融合任务信号,缓解传统深度推荐系统(DRS)特征选择过度依赖 surrogate model 的问题。

## 问题

[[recommender-systems|recommender-system]] 中的 feature selection 对提升模型效率与预测性能至关重要。现有方法分三类:shallow(统计算法,如 Lasso/GBDT)、gate-based(可学习 gate 向量,如 AutoField/AdaFS/OptFS/LPFS)、sensitivity-based(梯度敏感度,如 SFS/SHARK)。

作者指出,这些方法都依赖训练一个 **surrogate model** 去逼近 feature-to-label 映射,其有效性取决于 surrogate 拟合得好不好。但在真实推荐场景中 surrogate 常常失效:

- cold-start / 深转化任务中,样本(尤其正样本)稀疏导致 underfitting;
- 高基数特征众多时容易 overfitting;
- surrogate 难以捕捉特征间依赖,忽略 collinearity 与互补性(例如「经度」与「纬度」必须同时出现才能定位,surrogate 往往只选其一)。

[[large-language-models]] 凭借预训练世界知识可天然理解这类语义关系,但仍面临三个挑战:特征复杂性、knowledge gap(通用知识与领域不对齐)、工业级效率约束。

## 方法

SELF 包含三阶段:

- **Feature Importance Extraction(prompt iteration)**:设计含 instructions / descriptions / feature sets / supplementary information / output formatting 五部分的 prompt,让 LLM 每步从候选集中**迭代地**挑出一个最重要特征(初始 selected 集含 user ID 与 item ID),逐步生成完整特征排序。为缓解单模型偏差,**并行使用 K 个不同 LLM**,得到一个 K×N 的特征选择序列矩阵 S。

- **Feature Importance Refinement(bridge network)**:引入可学习的 **bridge vector** w(长度为 LLM 数 K),经温度缩放 softmax 归一化后作为各 LLM expert 的融合权重,对齐语义先验与任务目标。训练时按 LLM 排序对每个 batch 做特征 masking:masking 数 r 从 U(0, N·β) 采样(β 为最大 masking ratio,从最不重要的特征开始 mask),据此对未被 mask 的特征 embedding 加权,送入 DRS。任务为 CTR 预测,用 BCE loss 端到端优化 bridge vector。

- **Retraining**:用训好的 w*,对第 k 个 LLM 排序在位置 t 的特征赋线性衰减重要度 fi = 1 − t/N,跨 expert 加权聚合得每个 feature field 的最终分 h*;选 top-d 特征,**从头重训** DRS。

整体只优化一个轻量 bridge vector(故称 surrogate-light / agency-light),无需重训大模型。

## 结果

在 Movielens-1M(9 特征)、Aliccp(23 特征)、Kuairand(96 特征)三个公开数据集上,以 AUC / Logloss 评估(CTR 任务中 AUC +0.001 即显著)。LLM 设置默认 K=3(GPT-4、GPT-4o、GPT-3.5),β=0.2,τ=4.0。

- **RQ1 总体**:SELF 在三数据集全部指标上达最优。Movielens-1M 上 AUC 0.80480 / Logloss 0.52703(No Selection 为 0.78854 / 0.54367,次优 LPFS 0.80339);Aliccp AUC 0.62015;Kuairand AUC 0.78002。特征越少的数据集(Movielens-1M)增益越大。
- **RQ2 迁移性**:把 SELF 选出的特征用于 FM / DeepFM / Wide&Deep / DCN(Aliccp),四个 backbone 均较 No Selection 提升,Wide&Deep 与 DCN 等更复杂模型提升更明显。
- **RQ3 消融**:去掉 multiple LLMs(w/o MM)、iterative prompt(w/o IP)、bridge vector(w/o BV)三个变体均逊于完整 SELF,且都优于 No Selection。
- **RQ4 数据稀缺**:训练/验证集缩到 5%,SELF 仍几乎全面领先;此时与 No Selection 的差距更大,且 Movielens-1M 上有 6 个 baseline 反而劣于 No Selection(过拟合)。
- **RQ5 超参**:K=1 即超过 No Selection,K=3 最优且性价比最高(>3 趋于稳定);β 在 0.2~0.5 表现稳定。
- **RQ6 线上**:在服务数十亿用户的工业搜索广告平台部署(用 Qwen 系列模型),移除 12 个最不重要特征后,相对 baseline 实现 **RPM +0.63%、CTR +3.01%、在线推理延迟 −13.6%**,已全量上线。
- **Case study**:Movielens-1M 中 LLM 识别出 title 与 movie_id 高度相关(冗余),给 title 低排名,从而比 LPFS 得到更合理的排序。

## 在本 wiki 中的位置

本文属于 [[llm-for-recommendation]] 方向,具体聚焦深度推荐系统的特征选择,把 [[large-language-models]] 的世界知识当作语义先验来补足纯数据驱动 surrogate 的不足。它与 gate-based 特征选择代表作 [[autofield]]、CTR 模型 [[deepfm]] / [[autoint]] / [[esmm]]、[[factorization-machines]] 等相关,数据集涉及 [[kuairand]]、[[movielens-1m]] 与 Aliccp。方法上以 [[prompt-engineering]] 的迭代提示获取语义排序,可与「LLM 增强推荐」「特征工程自动化」主题互链。
