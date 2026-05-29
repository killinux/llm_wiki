---
type: entity
subtype: model
tags: [recommendation, ctr-prediction, factorization-machine, deep-learning]
created: 2026-05-29
updated: 2026-05-29
sources: 13
---

# DeepFM

DeepFM 是一种用于 CTR 预测的推荐模型,将 Factorization Machine (FM) 与深度神经网络结合在共享 embedding 之上,同时建模低阶与高阶特征交互。

## 在本 wiki 中的出现
- [[2026-smes-scalable-multi-task-expert-sparsity]]:SMES 是 Kuaishou 提出的可扩展稀疏 MoE 多任务推荐框架,用 progressive expert routing 与 multi-task load-balancing 解决多任务稀疏路由的 exploded activation 与 load skew,使参数 scaling 在工业延迟约束下带来稳定收益。
- [[mixture-of-experts]]
- [[multi-task-learning]]
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干(含 DeepFM 等)的 CTR 预测。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[nfm]]
- [[microvideo-recommendation]]
- [[2024-bi-level-user-modeling-deep-recommenders]]
- [[2025-causality-constraint-debiasing-recommender]]

- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:该论文提出 DORL,在 model-based offline RL 的悲观惩罚上加入熵惩罚以缓解推荐中的马太效应,提升交互式推荐的用户长期满意度;DeepFM 作为推荐场景中的相关模型出现。
- [[2023-d2co-watch-time-debias]]:该论文提出 D²Co,从统一因果视角同时矫正视频推荐中观看时长的时长偏差与噪声观看,以还原用户真实兴趣;DeepFM 作为推荐场景中的相关模型出现。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。
- [[2026-pdqubo-quantum-feature-selection]]:PDQUBO 用反事实分析量化单特征与特征对的推荐性能影响,构造性能驱动的 QUBO 系数矩阵,在量子退火器上做模型无关、指标无关的推荐系统特征选择。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2024-prompt-tuning-item-cold-start]]:PROMO 用高价值正反馈(pinnacle feedback)替代内容描述作 prompt,并为每个 item 构造个性化 prompt network,同时缓解 item cold-start 推荐的数据成本与热门偏置,已在快手十亿用户级平台部署。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent——一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户的多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 来评估推荐模型(如 DeepFM)并做数据增强。

## 相关

- [[factorization-machine]]
- [[ctr-prediction]]
- [[recommender-systems|recommendation-system]]
- [[wide-and-deep]]
- [[feature-selection]]
