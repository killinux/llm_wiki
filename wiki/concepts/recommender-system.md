---
type: concept
subtype: method
tags: [recommendation, ranking, reinforcement-learning, user-modeling]
created: 2026-05-29
updated: 2026-05-29
sources: 76
---

# Recommender System

Recommender System(推荐系统)是根据用户的历史行为、上下文与候选内容特征,预测用户偏好并为其筛选、排序与呈现内容的系统。

## 在本 wiki 中的出现

- [[2023-rlur-user-retention-short-video]]:以短视频推荐系统为应用场景,将用户留存优化建模为无限时域的请求级 MDP(每次请求为一步),提出 RLUR(Reinforcement Learning for User Retention)用强化学习直接最小化累计回访时间。该工作把推荐系统从单步即时反馈的优化目标,转向对长期留存这一稀疏、延迟信号的直接优化;在 KuaiRand 数据集上优于 TD3、CEM 等基线,并在 Kuaishou 全量上线,带来用户留存与 DAU 的提升。
- [[2026-transformers-graph-recommender-survey]]:首篇系统综述把 transformer 引入 graph-based 推荐系统的研究,提出 GTRS 形式化定义并建立含 4 大功能类(GUTM/GATM/GTSAM/HM)、6 子类的分类体系。
- [[2024-llm-tags-vs-classical-text-features]]:在统一协议下对照评估 LLM 生成语义标签与 TF-IDF/LDA/BERT 三类经典文本特征用于短视频推荐用户兴趣建模,发现 LLM 标签下游精度最优(CTR AUC 较 TF-IDF +0.9~1.6 点、SASRec HR@10 +2.1~3.4 点)且因稀疏化在在线成本上 Pareto 支配稠密嵌入,但离线生成贵约 40 倍。
- [[2023-video-length-debiasing-microvideo-rec]]:VLDRec 通过 play-progress 去偏标注、视频长度条件采样与多任务学习缓解微视频推荐中长视频被偏好的 video-length bias,以 NFM 为基座在 View_Time@120 上较最佳基线提升 1.81%(Kuaishou)与 11.32%(WeChat)。
- [[2023-recmind-llm-agent-for-recommendation]]:RecMind 是一个由 LLM 驱动的自主推荐 agent,通过规划、记忆与外部工具实现 zero-shot 个性化推荐,并提出 Self-Inspiring 规划算法保留所有已探索状态以增强规划能力。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2023-hierrec-scenario-aware-hierarchical-dynamic-network]]:HierRec 用分层 dynamic-weight 网络同时建模显式与隐式场景,在 Ali-CCP/KuaiRand 多场景 CTR 预测上显著超越 MMoE、PLE、STAR 等基线。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2023-microlens-micro-video-recommendation-dataset]]:MicroLens:一个含 10 亿交互、3400 万用户、100 万微视频并提供原始视频/音频/图像/文本内容的内容驱动微视频推荐数据集与基准。
- [[2023-agentcf-collaborative-learning-agents-recsys]]:把推荐系统中的用户和物品都建模为 LLM agent,通过自主交互与协同反思实现无梯度的协同过滤式优化。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建电影推荐用户模拟器,探究其能否忠实模拟真实用户行为并复现 filter bubble 与 popularity bias。
- [[2023-collaboration-transition-multi-query-self-attention]]:提出 MQSA-TED,用多查询自注意力建模协同信号、并把全局 item 转移模式蒸馏进 embedding,在序列推荐中平衡协同与转移信号。
- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-feature-level-bias-ctr]]:自上而下分析揭示 CTR 模型的 feature-level bias 主要源自线性部分,并提出移除/重建线性权重的极简非侵入式去偏策略。
- [[2024-merrec-mercari-c2c-recommendation-dataset]]:首个面向 C2C 电商的大规模推荐数据集 MerRec,来自 Mercari,含约 556 万用户、8307 万商品、12.7 亿交互,配套 CTR/SBR/MLR/IAR 四类任务基准与三塔模型 Mercatran。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-macrec-multi-agent-recommendation]]:清华提出的多 agent 协作推荐框架(SIGIR'24 demo),用 Manager、Analyst、Reflector、Searcher、Task Interpreter 等角色各异的 LLM agent 直接协作完成评分预测、序列推荐、解释生成与对话推荐。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-recmamba-lifelong-sequential-recommendation]]:提出 RecMamba,用带选择机制的状态空间模型 Mamba 替换 Transformer 层来建模长度>=2k 的终身用户行为序列,在 KuaiRand 与 LFM-1b 上达到与 SASRec 相当的推荐效果,同时训练时长降低约 73%、推理时间约 61%、显存约 80%,并在 5k 长度下避免 SASRec 的 OOM。
- [[2024-touch-the-core-hybrid-targets-recommendation]]:首次研究"离散转化任务 + 连续核心目标(如 watch time)"的 hybrid targets 多任务学习,提出 HTLNet 用 label embedding 显式传递任务依赖并设计梯度调整策略稳定优化。
- [[2024-situation-aware-recommender-enhancer]]:提出 SARE,一个把情境视为交互前置条件的可插拔模块,以个性化方式建模情境对用户-物品偏好的动态影响,可嵌入各类推荐系统 backbone 并显著提升性能。
- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2024-dfei-large-scale-multi-domain-recommendation]]:DFEI 是 Meituan 提出的大规模多域推荐框架,自动把用户行为聚合为域特征并为每个用户个性化整合跨域特征,在 Dianping 与 KuaiRand 上的多场景 CTR 预测显著优于 MMoE/PLE/STAR/HiNet 等基线。
- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-crocodile-cross-experts-covariance]]:Crocodile 用多嵌入架构 + cross-experts covariance loss(CovLoss)解耦各 expert 表示,并以 Prior Informed Element-wise Gating(PEG)路由,平衡多域推荐中"保持域差异性"与"充分学习参数"的两难,公开数据集与 Tencent 线上 A/B 均取得提升。
- [[2024-lusifer-llm-user-simulation]]:提出 Lusifer:基于 LLM 的用户模拟环境,在每次交互后增量更新可解释的用户画像,为 RL-based 推荐系统生成动态真实的用户反馈,并在 cold-start 场景超越传统协同过滤基线。
- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2024-counterfactual-watch-time]]:提出 counterfactual watch time (CWT) 与 Counterfactual Watch Model (CWM),从经济学视角建模观看行为以消除视频推荐中的 duration bias。
- [[2024-llm4rerank-auto-reranking-recommendation]]:把推荐 reranking 的 accuracy/diversity/fairness 等目标抽象为全连接图中的 node,让 LLM 以 Chain-of-Thought 多跳方式按用户给定的 "Goal" 自动综合多目标重排候选列表。
- [[2024-robust-recommendation-decision-boundary-gcl]]:提出 RGCL:用决策边界感知的对抗扰动约束 graph contrastive learning 增强视图,平衡语义不变性与对比难度并最大化间隔,在 5 个数据集上一致超越 12 个 baseline(Kuaishou Recall@10 +14.14%)。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2024-deconfound-release-interval-bias]]:将 release interval 识别为短视频推荐中的 confounder,提出模型无关的因果框架 LDRI,通过 backdoor adjustment 阻断后门路径并按视频自身 recency sensitivity 个性化去偏。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。
- [[2024-diit-domain-invariant-information-transfer]]:DIIT 通过 gating 域级聚合 + 对抗表示对齐双抽取器和 multi-spot 知识蒸馏迁移器,把多个 source domain 模型的 domain-invariant 信息注入 target domain 模型,实现推理只需 target 模型的高效工业跨域推荐。
- [[2024-mitigating-dual-latent-confounding-biases]]:IViDR 联合工具变量(IV)与 identifiable VAE,同时缓解推荐系统中 item-feedback 与 exposure-feedback 两类潜在混淆偏差。
- [[2026-pdqubo-quantum-feature-selection]]:PDQUBO 用反事实分析量化单特征与特征对的推荐性能影响,构造性能驱动的 QUBO 系数矩阵,在量子退火器上做模型无关、指标无关的推荐系统特征选择。
- [[2024-agentic-feedback-loop-recommendation]]:提出 AFL,让 recommendation agent 与 user agent 通过基于 memory 的多轮文本反馈回路相互协作,同时提升推荐(平均 +11.52%)与用户模拟(平均 +21.12%),且不放大流行度/位置偏差。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2024-online-item-cold-start-popularity-aware-meta-learning]]:提出 PAM,一种按物品热度固定切分 meta-learning 任务的 model-agnostic 框架,在流式在线推荐中解决新物品冷启动并缓解马太效应。
- [[2024-oasis-million-agent-social-simulation]]:通用、可扩展的 LLM-agent 社交媒体模拟器,在 X 与 Reddit 上模拟最多 100 万个 agent,复现信息传播、群体极化与从众效应,并发现规模越大群体动态越丰富、意见越多样有用。
- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2026-hesitation-and-tolerance-in-recommender-systems]]:提出并验证推荐系统中介于接受与拒绝之间的 hesitation(犹豫)与 tolerance(容忍)两种中间交互状态,通过问卷、离线日志与线上 A/B 实验论证容忍侵蚀用户留存,并主张将其作为弱正/负信号重新建模。
- [[2024-llm-powered-user-simulator-for-recommender-system]]:用 LLM 离线蒸馏用户偏好关键词与情感,在线用逻辑+统计集成模型显式推断 like/dislike,构建可解释、低幻觉、低成本的推荐系统用户模拟器。
- [[2024-prompt-tuning-item-cold-start]]:PROMO 用高价值正反馈(pinnacle feedback)替代内容描述作 prompt,并为每个 item 构造个性化 prompt network,同时缓解 item cold-start 推荐的数据成本与热门偏置,已在快手十亿用户级平台部署。
- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。
- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。
- [[2025-hyperzero-auto-tuning]]:Meta 的端到端超参数自动调优系统 HyperZero,利用推荐系统小时级反馈,通过 semi-i.i.d. delta 信号 + GP/Thompson Sampling 零阶约束优化 + 异步并行,把 value model 权重调优从数周压缩到 2-3 天,合成数据上 Gain 4.951% 远超 Bayesian optimization。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[2025-t2diff-two-tower-diffusion-matching]]:T2Diff 在双塔召回的用户塔内用扩散模型重建用户"下一个正向意图"并以 mixed-attention 实现交叉交互,在保持低延迟的同时打破双塔的 Late Interaction 瓶颈,离线/在线均显著超越 SOTA。
- [[2025-fine-grained-skip-micro-video-recommendation]]:将 micro-video 中的 skip 行为细分为 highly positive、less positive、negative 三类,用双层图与分层 BPR ranking loss 建模,在 MVA 与 KuaiRand-Pure 的八项指标上超越 FRAME/LightGT/BM3。
- [[2025-segment-level-user-interest-modeling]]:把短视频拆成时间片段,用混合表示+多模态用户-视频编码器+片段兴趣解码器建模用户沿时间线动态演变的片段级兴趣,用于 video-skip 预测与推荐。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2025-socioverse-world-model-social-simulation]]:SocioVerse 是一个由 LLM agents 驱动、依托 1000 万真实用户池与四个对齐模块的社会模拟 world model,在政治、新闻、经济三大领域复现大规模人群行为。
- [[2025-simuser-llm-user-simulation-recsys]]:基于 LLM 的 agent 框架,用从历史数据推断的 persona、记忆、感知与决策模块构建可信合成用户来低成本评估推荐系统。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。
- [[2025-deep-interest-life-cycle-network]]:提出 DILN,显式建模用户兴趣生命周期(emergent/stable/declining)并用 VQ 聚类离散化、注入 MMOE 排序模型,Lofter 线上 CTR +0.38%、CVR +1.04%、时长 +0.25%。
- [[2026-thinkrec-thinking-based-recommendation]]:ThinkRec 通过思考激活(推理数据合成+联合训练)与实例级 LoRA 专家融合,把 LLM 推荐从 System 1 直觉匹配推进到 System 2 推理,在 ML1M/Yelp/Book 上 AUC 平均超 SOTA 7.96%。
- [[2025-causality-constraint-debiasing-recommender]]:LCDR 用 identifiable VAE (iVAE) 作为因果约束去对齐标准 VAE 的潜在表征,即使 proxy variable 低质/有噪声也能恢复 latent confounder,从而缓解推荐系统中的潜在混杂偏差。
- [[2025-gnolr-progressive-implicit-preference]]:提出 GNOLR,用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进又把多路检索简化为单次最近邻搜索。
- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。
- [[2025-perscen-multi-scenario-matching]]:首个将用户个性化建模引入多场景匹配(召回)的两塔方法,用 user-specific 特征图+轻量 GNN、向量量化的场景偏好与渐进式 GLU,在 KuaiRand-Pure 与 Alimama 上以高效率刷新召回性能。
- [[2025-reward-balancing-revisited]]:提出 R3S,用 diffusion world model 显式建模 reward 不确定性并配合带衰减的多样性惩罚,在 offline RL 推荐中同时平衡 world model 偏差与策略多样性,在 Coat/Yahoo/KuaiRand 上超越 DORL、ROLeR 等 11 个 baseline。
- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]]:一个 post-hoc、模型无关、distribution-free 的方法,用 conformal risk control 给推荐中"不想要内容"的比例提供可证明上界,并以用户曾看过的安全重复内容替换有害项以保住推荐质量。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。
- [[2025-hid-vae-interpretable-generative-recommendation]]:HiD-VAE 用层次化监督量化 + uniqueness loss 学习可解释、解耦的 semantic ID,消除 ID 碰撞并显著提升生成式推荐性能。

## 相关

- [[recommender-systems]]
- [[sequential-recommendation]]
- [[reinforcement-learning]]
- [[markov-decision-process]]
- [[constrained-mdp]]
- [[off-policy-evaluation]]
- [[user-retention]]
- [[short-video-recommendation]]
