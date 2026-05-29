---
type: entity
subtype: lab
tags: [industry-research, huawei, recommender-systems]
created: 2026-05-29
updated: 2026-05-29
sources: 15
---

# Huawei Noah's Ark Lab

华为旗下的人工智能与决策推理研究实验室,研究方向涵盖机器学习、推荐系统、自然语言处理与决策优化。

## 在本 wiki 中的出现

- [[2023-multi-task-deep-recommender-systems-survey]]:该综述从任务关系与方法论两个维度为多任务深度推荐系统(MTDRS)建立系统分类体系,梳理代表模型、数据集与未来研究方向;Huawei Noah's Ark Lab 为该工作的署名研究机构之一。
- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。
- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-rethinkmcts]]:一个面向代码生成的思路搜索框架,用 MCTS 探索写代码的推理过程,并通过 rethink 机制利用块级代码执行反馈直接精炼搜索树中的错误思路。
- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。
- [[2025-fuxi-gamma-efficient-sequential-recommendation]]:decoder-only 生成式序列推荐框架,用受 Ebbinghaus 遗忘曲线启发的指数幂时间编码器与对角稀疏位置剪枝,在 SOTA 推荐质量下把训练加速最多 4.74×、推理 6.18×。
- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent:一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强。
- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。
- [[2026-nestpipe-nested-pipelining]]:NestPipe 通过两层嵌套流水线(inter-batch 的 Dual-Buffer Pipelining 与 intra-batch 的 Frozen-Window Pipelining)在保持同步训练语义下隐藏大规模推荐 embedding 训练的 lookup 与 All2All 通信瓶颈,在 1,536 worker 上实现 3.06× 加速、94.07% 扩展效率。

## 相关

- [[multi-task-learning]] —— 多任务深度推荐系统(MTDRS)的核心范式
- [[recommender-systems]] —— 实验室相关研究领域
- [[mmoe]]、[[ple]] —— 多任务推荐中的代表性模型架构
- [[multi-scenario-ctr-prediction]] —— HierRec 所属的多场景 CTR 预测方向
- [[reranking]] —— BankFair / LLM4Rerank 涉及的重排序问题
- [[recommendation-fairness]] —— BankFair 关注的提供方公平性
- [[duration-bias]] —— CWM 旨在消除的观看时长偏差
- [[llm-for-recommendation]] —— LLM4Rerank 代表的 LLM 用于推荐方向
- [[code-generation]] —— RethinkMCTS 所属的代码生成方向
- [[large-recommendation-models]] —— scaling law 工作研究的对象
- [[feature-selection]] —— SELF 关注的深度推荐特征选择问题
- [[generative-recommendation]] —— FuXi-Gamma 等生成式序列推荐方向
- [[sequential-recommendation]] —— FuXi-Gamma / FuXi-Linear 所属的序列推荐方向
- [[conversion-rate-prediction]] —— KAML 关注的 CVR 预测问题
- [[llm-agents|llm-agent]] —— A/B Agent 代表的 LLM 智能体方向
- [[recommendation-system-training]] —— NestPipe 关注的大规模训练系统问题
