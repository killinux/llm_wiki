---
type: source
subtype: paper
tags: [recommender-system, embedding-based-retrieval, diffusion-models, two-tower, candidate-generation, kuaishou]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2502.20687
raw: raw/2502.20687.pdf
authors: [Yihan Wang, Fei Xiong, Zhexin Han, Qi Song, Kaiqiao Zhan, Ben Wang]
year: 2025
---

# T2Diff:基于扩散模型的双塔交叉交互大规模召回

T2Diff(发表于 WWW '25,来自 [[kuaishou]])提出了一种"生成式交叉交互解耦架构",在 [[recommender-system]] 的召回(matching)阶段用 [[diffusion-models]] 在用户塔内重建用户的"下一个正向意图",并通过 mixed-attention 模块在保持双塔低延迟的同时打破双塔的"晚交互(Late Interaction)"瓶颈。

## 问题

工业级 [[recommender-system]] 通常采用两阶段架构:召回(matching)阶段从数十亿候选语料中快速筛选,排序(ranking)阶段再精排。召回阶段对延迟和吞吐要求极高,因此 two-tower(双塔)模型成为主流 [[embedding-based-retrieval]] 范式——用户塔与物品塔独立编码为低维 embedding,再做内积打分以支持高效 top-k 检索。

但双塔的解耦导致两塔在最后一刻之前都无法利用用户-物品的交叉特征/交互,即所谓"Late Interaction(晚交互)"问题。已有解决思路存在权衡困境:

- COLD/FSCD 类方法把双塔改造成单塔(加一层浅层全连接),但效率受限,且只能用于排序阶段;
- DAT 类方法把另一塔的历史正向交互信息作为输入特征(adaptive-mimic 机制),但后续研究表明因缺乏对"下一个用户正向意图"的引导,增益有限。

当前 SOTA 难以同时兼顾模型效果与推理效率。

## 方法

T2Diff 在用户塔内部引入两个核心模块,实现完整的交叉交互,同时保持双塔结构以满足大规模语料的效率要求:

- **Diffusion 模块(重建下一个正向意图)**:不直接对原始行为序列做扩散,而是先做 drift preparation——对相邻行为做元素级差分得到"兴趣漂移(interest drift)" `z0 = X(2:n+1) − X(1:n)`,认为对漂移做扩散/还原比对原始序列更容易。训练时随机加 r 步高斯噪声,采用 **指数噪声调度(exponential β schedule)**,以 U-Net 作为 approximator,并以原始行为序列 `X(1:n)` 作为 condition 引导还原;损失用 KL 散度(`L_KL`),区别于 DiffuRec 采用的 cross-entropy 损失。推理时从标准高斯采样反向 T 步,最终经 drift utilization 还原出预测的下一个正向行为 `x̂(n+1)`。
- **Mixed-attention 模块(交叉交互)**:把最近 session 行为 `X_session` 与重建的 `x̂(n+1)` 沿时间维拼接,经 [[transformer]] encoder + average pooling 得到当前兴趣 `h_s`("Early Interaction");再以 `h_s` 为 query 用 target-attention(activation units,输入含 `x_j`、`x_j − h_s`、`x_j * h_s` 与外积)从历史行为 `X_history` 抽取相似兴趣,二者拼接生成用户 embedding `e_u`。
- **优化**:总损失 = softmax 双塔召回损失 `L_TOWER` + λ·`L_KL`(λ 取 1 或 10);因扩散模块与召回任务的梯度方向不一致易相互抵消,采用 **stop-gradient** 隔离扩散模块的梯度更新。

## 结果

离线在两个公开数据集 [[kuairand]](25,828 用户 / 108,025 物品)与 [[movielens-1m]](6,040 用户 / 3,648 电影)上评测,指标为 Recall@K 与 MRR@K。

- 对比 9 个 SOTA 基线([[sasrec]]、Caser、[[gru4rec]]、Bert4Rec、DAT+、Mamba4Rec、ContrastVAE、STOSA、DiffuRec),T2Diff 全面领先。相对最优基线:ML-1M 上 Recall@2 +11.84%、MRR@20 +22.27%;KuaiRand 上 Recall@100 +10.94%、MRR@100 +4.08%。所有增益在 p < 0.05 下显著。
- ML-1M 上 T2Diff 取得 Recall@2=0.07738、Recall@20=0.27727、MRR@2=0.06076、MRR@20=0.08730。
- 消融:仅加 mixed-attention 模块即在多项指标超过所有基线;再加扩散模块后 recall 在 ML-1M 提升 22.67%、KuaiRand 提升 25.90%;去掉 drift preparation(DP)步骤性能明显下降,佐证建模兴趣漂移的重要性。
- 超参:指数噪声调度 > linear > log(ML-1M:exp 的 Recall@20=0.27727 vs linear 0.27519 vs log 0.25151);扩散步数 T=50 在效果与效率间最优(T 从 50 增到 200,MRR 略升但单样本推理时间增加 238%)。效率上 T2Diff 参数量(0.187 MB)与推理时间(0.68 ms,5×Tesla T4)与基线相当。
- 在线 A/B(2024-03-27 至 04-03,某大型短视频平台,逾 300 万用户):相对常规双塔召回,EVR +10.98%(24.6% vs 17.2%)、FTR +11.67%、平均播放时长 +37.42%(20.96s vs 11.4s);App 人均使用时长 +0.143%(95% CI:+0.02%~+0.26%)。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 召回阶段与 [[embedding-based-retrieval]] 方向,把 [[diffusion-models]] 用于序列推荐中的目标物品/意图重建,与 [[diffurec]] 一脉相承但改用 KL 损失、指数噪声调度并显式建模兴趣漂移。它针对双塔模型固有的 [[candidate-generation]] 效率-效果权衡,可与 [[sasrec]]、[[gru4rec]]、[[recmamba]] 等 [[sequential-recommendation]] 方法对照;实验依托 [[kuairand]]、[[movielens-1m]] 数据集,来自工业界 [[kuaishou]]。
