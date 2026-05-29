---
type: concept
subtype: method
tags: [debiasing, recommendation, causal-inference, bias, unbiased-evaluation]
created: 2026-05-29
updated: 2026-05-29
sources: 20
---

# Debiasing

Debiasing 指在推荐系统等场景中,识别并矫正由数据收集或反馈机制引入的各类偏差(如曝光偏差、选择偏差、时长偏差等),以还原用户真实兴趣并获得无偏估计的一系列方法。

## 在本 wiki 中的出现

- [[2022-kuairand]]:作为支撑去偏研究的数据基础。该数据集通过在推荐流中随机插入视频收集百万级无偏交互(含 12 种反馈信号、完整用户/物品 ID 与特征),为 debiasing 与离线评估提供随机曝光数据。
- [[2023-idcf-debiasing-recommendation]]:提出 iDCF,借助代理变量(用户特征)与近端因果推断,在存在未观测混杂变量时为推荐反事实反馈提供可识别性保证,代表基于因果推断的 debiasing 路线,在 Coat/Yahoo!R3/KuaiRand 上优于现有去混杂方法。
- [[2023-d2co-watch-time-debias]]:提出 D²Co,从统一因果视角同时矫正视频推荐中观看时长的时长偏差(duration bias)与噪声观看,是面向 watch-time 的具体 debiasing 方法。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2024-causal-discovery-recommender-systems]]:以 KuaiRand 数据集为例,用 Hill-Climbing + 先验知识从观测数据学习推荐系统的因果图,结果显示只有 video duration 与 upload type 等少数变量真正影响用户反馈,反思"特征越多越好"的建模趋势。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL，让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作，同时提升推荐（平均 +11.52%）与用户模拟（平均 +21.12%），且不放大流行度/位置偏差。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2026-hesitation-and-tolerance-in-recommender-systems]]:提出并验证推荐系统中介于接受与拒绝之间的 hesitation(犹豫)与 tolerance(容忍)两种中间交互状态,通过问卷、离线日志与线上 A/B 实验论证容忍侵蚀用户留存,并主张将其作为弱正/负信号重新建模。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。
- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]]:一个 post-hoc、模型无关、distribution-free 的方法,用 conformal risk control 给推荐中"不想要内容"的比例提供可证明上界,并以用户曾看过的安全重复内容替换有害项以保住推荐质量。
- [[2025-where-to-explore-reach-cost-aware-unbiased-data]]:提出按用户 scroll-depth 触发、低成本高触达的专用 UI 行("Something Completely Different")来交付随机化探索内容,在不损害短期参与度的前提下大规模收集无偏交互数据,并回灌候选生成提升长期推荐质量(线上 +0.94% 参与度,无偏数据 Gini 0.203 vs 0.494)。

## 相关

- [[exposure-bias]]
- [[selection-bias]]
- [[duration-bias]]
- [[causal-inference]]
- [[counterfactual-learning]]
- [[unbiased-evaluation]]
- [[sequential-recommendation]]
- [[watch-time-prediction]]
- [[backdoor-adjustment]]
- [[fairness]]
- [[ctr-prediction]]
- [[recommendation-reranking]]
