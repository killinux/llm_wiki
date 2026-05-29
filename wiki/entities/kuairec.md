---
type: entity
subtype: dataset
tags: [recommendation, dataset, kuaishou, debiasing, offline-rl]
created: 2026-05-29
updated: 2026-05-29
sources: 16
---

# KuaiRec

KuaiRec 是源自快手(Kuaishou)短视频平台的推荐系统数据集,常用于去偏与离线推荐研究。

## 在本 wiki 中的出现

- [[2022-kuairand]]:与该数据集同源的快手数据生态。KuaiRand 是快手发布的无偏序列推荐数据集,通过在推荐流中随机插入视频来收集百万级无偏交互(含 12 种反馈信号、完整用户/物品 ID 与特征),支持去偏与离线评估研究。
- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:作为交互式推荐离线评估的数据来源之一。该论文提出 DORL,在 model-based offline RL 的悲观惩罚上加入熵惩罚以缓解推荐中的马太效应(Matthew effect),提升交互式推荐的用户长期满意度。
- [[2024-llm-tags-vs-classical-text-features]]:在统一协议下对照评估 LLM 生成语义标签与 TF-IDF/LDA/BERT 三类经典文本特征用于短视频推荐用户兴趣建模,发现 LLM 标签下游精度最优(CTR AUC 较 TF-IDF +0.9~1.6 点、SASRec HR@10 +2.1~3.4 点)且因稀疏化在在线成本上 Pareto 支配稠密嵌入,但离线生成贵约 40 倍。
- [[2023-microlens-micro-video-recommendation-dataset]]:MicroLens:一个含 10 亿交互、3400 万用户、100 万微视频并提供原始视频/音频/图像/文本内容的内容驱动微视频推荐数据集与基准。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-sigformer-sign-aware-graph-transformer]]:用 Transformer 替代 GNN 做 sign-aware 推荐,通过谱编码(SSE)与路径编码(SPE)两种为带符号图设计的 positional encoding 统一利用正负反馈,在 5 个数据集上超越 SOTA。
- [[2024-fairness-recommendation-missing-labels]]:证明大规模推荐系统在缺失标签下 REO 公平性指标不可识别,提出用小比例 random traffic 无偏估计公平性指标并给出误差上界,首次公开 TikTok 公平性数据集。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2025-debias-can-be-unreliable]]:揭示用随机曝光数据集传统评估去偏推荐不可靠,提出 URE 方案无偏估计全曝光数据上的 Recall@K。
- [[2026-pdqubo-quantum-feature-selection]]:PDQUBO 用反事实分析量化单特征与特征对的推荐性能影响,构造性能驱动的 QUBO 系数矩阵,在量子退火器上做模型无关、指标无关的推荐系统特征选择。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2024-generative-regression-watch-time-prediction]]:提出 Generative Regression (GR),把短视频 watch time 预测从 ordinal regression 重构为 token 序列生成任务,配合 dynamic quantile 词表与 CLEM(curriculum learning + embedding mixup),在 KuaiRec/CIKM16/工业数据集及 Kuaishou 线上 A/B 上超过 SOTA,并可迁移到 LTV 预测。
- [[2026-diffusion-models-in-recommendation-survey]]:以"推荐任务为本"的三正交轴 taxonomy 系统综述扩散模型在推荐系统中的应用,覆盖 188 篇论文,涵盖协同过滤、序列推荐、数据模态/领域与可信目标。
- [[2025-policy-guided-causal-state-representation]]:PGCR:面向离线 RL 推荐的两阶段因果状态表示框架,用策略引导的因果特征选择隔离因果相关分量,再用 encoder 学习紧凑状态表示。
- [[2025-fine-grained-skip-micro-video-recommendation]]:将 micro-video 中的 skip 行为细分为 highly positive、less positive、negative 三类,用双层图与分层 BPR ranking loss 建模,在 MVA 与 KuaiRand-Pure 的八项指标上超越 FRAME/LightGT/BM3。

## 相关

- [[kuairand]]
- [[kuaishou]]
- [[offline-reinforcement-learning]]
- [[matthew-effect]]
- [[debiasing]]
- [[recommendation-system]]
- [[recflow]]
- [[watch-time-prediction]]
