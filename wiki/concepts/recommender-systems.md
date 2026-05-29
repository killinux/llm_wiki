---
type: concept
subtype: method
tags: [recommender-systems, recommendation, debiasing, causal-inference, ranking]
created: 2026-05-29
updated: 2026-05-29
sources: 8
---

# Recommender Systems

Recommender Systems(推荐系统)是一类根据用户历史行为、特征与上下文,从海量候选物品中预测用户偏好并排序推荐的方法体系,广泛用于内容流、电商与视频平台。

## 在本 wiki 中的出现
- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。
- [[2025-fuxi-gamma-efficient-sequential-recommendation]]:decoder-only 生成式序列推荐框架,用受 Ebbinghaus 遗忘曲线启发的指数幂时间编码器与对角稀疏位置剪枝,在 SOTA 推荐质量下把训练加速最多 4.74×、推理 6.18×。
- [[2025-no-one-left-behind-asymmetric-multi-label-cvr]]:KAML 框架针对广告主只上报部分转化行为导致的非对称多标签数据,用归因掩码 ADM、层级知识抽取 HKE 与排序标签利用 RLU 改进 MMoE 基座,工业数据与线上 A/B(RPM +12.11%、CVR +0.92%)均超越现有 MTL 基线的 CVR 预测方法。
- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。
- [[2026-tencent-advertising-algorithm-challenge-2025]]:腾讯广告算法大赛 2025 发布两个真实工业广告日志构建的大规模全模态生成式推荐数据集(TencentGR-1M/10M)、基线模型与含转化加权的评测协议。
- [[2601-dsmoe-scenario-adaptive-moe-matching]]:DSMOE 将 MMOE 迁移到多场景推荐召回阶段,用低秩场景自适应投影(SAP)缓解头部场景统治专家,并用 user-item 联合特征 teacher 蒸馏指导双塔 student,在保持检索效率的同时显著提升长尾稀疏场景的召回质量。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent:一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强。
- [[2026-vk-lsvd-short-video-dataset]]:迄今最大的公开短视频推荐工业数据集,来自 VK,含 400 亿交互、1000 万用户、近 2000 万视频,跨 6 个月。
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。
- [[2026-fuxi-linear]]:线性复杂度的时间感知序列推荐模型,解耦时间与语义信号、用可学习核近似相对位置编码,在数千 token 长序列上提升推荐质量并实现最高 21× 推理加速。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。
- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段,在用户意图模糊时兼顾追问效率与残余不确定性驱动的多样化推荐。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是一个基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化。
- [[2026-collective-manipulation-risk-controlling-recsys]]:审计基于 conformal risk control 与二元 Not Interested 负反馈的推荐系统,证明仅 1% 协同对抗用户即可让非对抗用户 nDCG 最多降 20%,并提出个体级阈值校准作为缓解。
- [[2026-nestpipe-nested-pipelining]]:NestPipe 通过两层嵌套流水线(inter-batch 的 Dual-Buffer Pipelining 与 intra-batch 的 Frozen-Window Pipelining)在保持同步训练语义下隐藏大规模推荐 embedding 训练的 lookup 与 All2All 通信瓶颈,在 1,536 worker 上实现 3.06× 加速、94.07% 扩展效率。
- [[2026-cs3-capability-synergy-two-tower]]:CS3 是快手提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块让 two-tower 召回模型感知自身、对侧塔与下游 cascade 模型,提升容量与跨阶段一致性,线上广告收入最高提升 8.36%。
- [[2026-compressed-video-aggregator]]:CVA 用冻结视觉基础模型的帧 embedding 加 self-attention 压缩成紧凑视频 embedding,在 MicroLens 与 Short-Video 上提升微视频推荐精度,同时把训练时间与 GPU 显存降低数个数量级。
- [[two-tower-model]]
- [[mixture-of-experts]]
- [[llm-agent]]
- [[conversational-recommendation]]
- [[retrieval]]
- [[short-video-recommendation]]
- [[online-ab-testing]]
- [[recommendation-dataset]]
- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。
- [[recommendation-editing]]
- [[bpr]]

- [[2022-kuairand]]:作为**数据集贡献**。快手发布的无偏序列推荐数据集,通过在推荐流中随机插入视频收集百万级无偏交互(含 12 种反馈信号、完整用户/物品 ID 与特征),为推荐系统的去偏与离线评估研究提供数据基础。
- [[2023-causal-inference-for-recommendation]]:作为**综述主题**。系统梳理如何将因果推断引入推荐系统,涵盖因果记号/假设/效应/估计方法,以及推荐系统中可解释性、公平性、鲁棒性、uplift、无偏性等实际问题。
- [[2023-idcf-debiasing-recommendation]]:作为**去偏方法的应用场景**。提出 iDCF,借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证,在 Coat/Yahoo!R3/KuaiRand 上优于现有去混杂方法。
- [[2023-data-heterogeneity-recommendation]]:作为**预测与去偏对象**。提出双层聚类方法 BHE 显式挖掘推荐数据中的预测机制异质性与协变量分布异质性,用于多子模型预测与去偏,在 Yelp/MovieLens-1M 上 NFM 骨干 NDCG@20 从 14.01 提升到 22.57。
- [[2024-causal-discovery-recommender-systems]]:以 KuaiRand 数据集为例,用 Hill-Climbing + 先验知识从观测数据学习推荐系统的因果图,结果显示只有 video duration 与 upload type 等少数变量真正影响用户反馈,反思"特征越多越好"的建模趋势。
- [[2024-residual-multi-task-learner-resflow]]:ResFlow:轻量多任务学习框架,通过跨任务网络对应层的残差连接高效传递信息;部署于 Shopee Search pre-rank,线上 OPU 提升 1.29% 且无额外延迟。

## 相关

- [[debiasing]]
- [[causal-inference]]
- [[proximal-causal-inference]]
- [[unobserved-confounding]]
- [[counterfactual-inference]]
- [[sequential-recommendation]]
- [[offline-evaluation]]
- [[ndcg]]
- [[data-heterogeneity]]
- [[uplift-modeling]]
- [[multi-task-learning]]
- [[causal-discovery]]
