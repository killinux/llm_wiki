---
type: entity
subtype: dataset
tags: [recommendation, dataset, short-video, unbiased, debiasing, offline-rl]
created: 2026-05-29
updated: 2026-05-29
sources: 34
---

# KuaiRand

KuaiRand 是快手(Kuaishou)发布的无偏序列推荐数据集,通过在正常推荐流中随机插入视频来收集百万级的无偏交互数据,广泛用于去偏(debiasing)、强化学习推荐与离线评估研究。

## 在本 wiki 中的出现

- [[2022-kuairand]]:数据集的发布论文。通过在推荐流中随机插入视频收集百万级无偏交互,包含 12 种反馈信号、完整的用户/物品 ID 与特征,支持去偏与离线评估研究。
- [[2023-two-stage-constrained-actor-critic]]:作为短视频多目标推荐(WatchTime 主目标与 Like/Share 等稀疏交互软约束)的实验/评估场景,相关方法 TSCAC 已在快手生产系统全量上线。
- [[2023-rlur-user-retention-short-video]]:作为评估基准,RLUR 在 KuaiRand 上优于 TD3/CEM,并在 Kuaishou 全量上线提升留存与 DAU。
- [[2023-divide-and-conquer-ebr]]:作为 embedding-based retrieval 召回方法的公开评估数据集之一,Recall 最高提升约 40%。
- [[2023-multi-task-recommendations-with-rl]]:作为 RMTL 多任务推荐的评估数据集(与 RetailRocket 并列),用于验证 RL 动态损失权重对 CTR/CTCVR AUC 的提升。
- [[2023-hyper-actor-critic-recommendation]]:作为 Hyper-Actor Critic(HAC)框架在列表生成式 RL 推荐中的实验场景。
- [[2023-idcf-debiasing-recommendation]]:作为去混杂方法 iDCF 的评估数据集(与 Coat、Yahoo!R3 并列),用于验证近端因果推断下的可识别性。
- [[2023-gflownet-listwise-recommendation]]:作为 GFN4Rec(基于 GFlowNet 的 list-wise 推荐)的实验场景,用于评估列表多样性与在线探索。
- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:作为 model-based offline RL 推荐(缓解马太效应)的交互式推荐评估环境。
- [[2023-d2co-watch-time-debias]]:作为 D²Co 矫正观看时长偏差与噪声观看的视频推荐评估场景。
- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2024-llm-tags-vs-classical-text-features]]:在统一协议下对照评估 LLM 生成语义标签与 TF-IDF/LDA/BERT 三类经典文本特征用于短视频推荐用户兴趣建模,发现 LLM 标签下游精度最优(CTR AUC 较 TF-IDF +0.9~1.6 点、SASRec HR@10 +2.1~3.4 点)且因稀疏化在在线成本上 Pareto 支配稠密嵌入,但离线生成贵约 40 倍。
- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度>=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。
- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2024-dfei-large-scale-multi-domain-recommendation]]:DFEI 是 Meituan 提出的大规模多域推荐框架,自动把用户行为聚合为域特征并为每个用户个性化整合跨域特征,在 Dianping 与 KuaiRand 上的多场景 CTR 预测显著优于 MMoE/PLE/STAR/HiNet 等基线。
- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。
- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-recommendation-editing]]:提出 recommendation editing 新任务:不重训练、不访问训练数据地修正已部署推荐系统的已知不当推荐,给出形式化定义、ES/EC/EP/EA 评估指标、E-BPR 损失与综合 benchmark。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。

## 相关

- [[kuairec]]
- [[kuaishou]]
- [[debiasing]]
- [[unbiased-recommendation]]
- [[short-video-recommendation]]
- [[offline-reinforcement-learning]]
- [[sequential-recommendation]]
- [[watch-time-prediction]]
- [[multi-task-recommendation]]
- [[embedding-based-retrieval]]
