---
type: entity
subtype: product
tags: [short-video, recommendation, reinforcement-learning, dataset, industry, watch-time, debiasing]
created: 2026-05-29
updated: 2026-05-29
sources: 17
---

# Kuaishou

Kuaishou(快手)是中国领先的短视频与直播平台,其推荐系统是大量序列推荐、强化学习与召回研究的真实工业场景与数据来源。

## 在本 wiki 中的出现

- [[2022-kuairand]]:作为数据集发布方,快手通过在推荐流中随机插入视频收集百万级无偏序列交互,发布无偏序列推荐数据集 KuaiRand(含 12 种反馈信号、完整用户/物品 ID 与特征),支持去偏与离线评估研究。
- [[2023-two-stage-constrained-actor-critic]]:作为生产部署平台,TSCAC 两阶段约束式 actor-critic 在最大化短视频 WatchTime 主目标的同时软约束平衡 Like/Share 等稀疏交互,已在快手生产系统全量上线。
- [[2023-rlur-user-retention-short-video]]:作为问题来源与部署平台,RLUR 把短视频用户留存建模为无限时域请求级 MDP,用强化学习直接最小化累计回访时间,在 KuaiRand 上优于 TD3/CEM,并在快手全量上线提升留存与 DAU。
- [[2023-divide-and-conquer-ebr]]:作为线上部署平台,将推荐召回的 embedding-based retrieval 拆为"物料聚类 + 簇内并行检索 + 可控合并"并辅以 prompt-like 多任务适配,公开数据集 Recall 最高提升约 40%,已在快手线上部署。
- [[2023-multi-task-recommendations-with-rl]]:作为实验数据来源,RMTL 用 actor-critic 强化学习按 session 级序列动态生成多任务损失权重,在 RetailRocket 与 KuaiRand 上提升 CTR/CTCVR 的 AUC。
- [[2023-hyper-actor-critic-recommendation]]:作为短视频推荐场景背景,HAC(Hyper-Actor Critic)把推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,并用对齐与监督模块稳定大动作空间下的 RL 推荐策略学习。
- [[2023-gflownet-listwise-recommendation]]:作为 list-wise 推荐场景背景,GFN4Rec 用 GFlowNet 流匹配让推荐列表的生成概率正比于其 list-wise 奖励,在保持高质量的同时提升列表多样性与在线探索。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度>=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。

## 相关

- [[kuairand]]
- [[short-video-recommendation]]
- [[sequential-recommendation]]
- [[reinforcement-learning-for-recommendation]]
- [[actor-critic]]
- [[user-retention]]
- [[watchtime]]
- [[embedding-based-retrieval]]
- [[multi-task-learning]]
- [[gflownet]]
- [[recommendation-debiasing]]
- [[wechat]]
