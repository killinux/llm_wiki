---
type: concept
subtype: method
tags: [debiasing, causal-inference, recommendation]
created: 2026-05-29
updated: 2026-05-29
sources: 13
---

# Selection Bias

由于观测数据并非随机抽样(missing-not-at-random),用户与物品的交互数据在分布上系统性偏离真实分布,从而导致估计产生偏差。

## 在本 wiki 中的出现

- [[2023-conservative-doubly-robust]]:作为推荐数据缺失非随机(MNAR)的根本原因,是 CDR 等去偏方法所要校正的目标。CDR 在 Doubly Robust 框架上通过过滤高方差的"有毒"插补值来降低偏差与方差。
- [[2026-generative-social-simulation-validation]]:系统性文献综述(AI Review 2026, 59:15),梳理 LLM 驱动的生成式 Agent-Based Models 在社会模拟中的应用,论证引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了 ABM 长期的"验证"难题。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF 用协作式多智能体 RL 最大化短视频会话累计 WatchTime,并以 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。

## 相关

- [[debiasing]]
- [[doubly-robust]]
- [[inverse-propensity-scoring]]
- [[poisonous-imputation]]
- [[missing-at-random]]
- [[exposure-bias]]
- [[causal-inference]]
- [[recommender-systems]]
- [[2023-conservative-doubly-robust]]
