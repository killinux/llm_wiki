---
type: source
subtype: paper
tags:
  - decision-transformer
  - generative-recommendation
  - offline-rl
  - recommender-system
  - state-abstraction
  - kuaishou
created: 2026-05-29
updated: 2026-05-29
arxiv: 2507.20327
raw: raw/2507.20327.pdf
authors:
  - Xiang Gao
  - Tianyuan Liu
  - Yisha Li
  - Jingxin Liu
  - Lexi Gao
  - Xin Li
  - Haiyang Lu
  - Liyin Hong
year: 2025
---

TADT-CSA 是一个面向工业级生成式推荐的 [[decision-transformer]] 改进框架,通过引入 Temporal Advantage 信号和 Contrastive State Abstraction 模块,解决 DT 在高噪声、随机推荐环境下轨迹拼接弱与状态空间过大的问题。

## 问题

在工业 [[recommender-systems|recommender-system]] 中,序列推荐常被建模为无限时域的 [[markov-decision-process]],并用 [[reinforcement-learning]] 求解。传统基于 [[temporal-difference]] / TD 误差 bootstrapping 的方法在真实 RS 环境中面临两大困难:数据分布波动剧烈(尤其流量高峰到低谷的过渡),采集到的 $(s_t, a_t, r_t, s_{t+1})$ 样本高噪声、强随机,使 RL agent 难以学到准确的 Q 值估计。

[[decision-transformer]](DT)作为一种 return-conditioned 的序列建模方法被引入生成式推荐(如 DT4Rec、CDT4Rec、DT4IER),相比 [[large-language-models]] 更轻量、推理开销低,适合工业部署(如自动出价场景)。但 DT 本身存在两个缺陷:

- 缺乏轨迹拼接(trajectory stitching)能力,只在 offline 数据上做 [[behavior-cloning]],当高回报轨迹稀缺或环境随机时容易学到次优策略。
- 工业 RS 中用户数达数千万、物品达数十亿,状态空间是高维特征的笛卡尔积,极其庞大且稀疏。已有 DT 推荐模型多依赖简单 embedding 层或浅层 encoder 学状态表示,效果不佳。

## 方法

模型称为 **Temporal Advantage Decision Transformer with Contrastive State Abstraction (TADT-CSA)**,由 TADT 与 CSA 两部分组成。

**Temporal Advantage Score(TA score)**:在标准 Return-To-Go(RTG)$R_t^{\text{RTG}}=\sum_{i=t}^{T}\gamma^{i-t}r_i$ 之外,定义 TA score $R_t^{\text{TA}}=\sum_{i=2}^{t}\gamma^{t-i}(R_i^{\text{RTG}}-R_{i-1}^{\text{RTG}})$,即对 RTG 差分的折扣累积,捕捉时间趋势信息。新的 return-conditioned 信号是二者拼接 $R_t=[R_t^{\text{RTG}}, R_t^{\text{TA}}]$。这样即使两条轨迹 RTG 相同,稳步增长与快速骤增的不同 TA 模式也能提供更强的判别梯度信号。

**Pairwise ranking loss**:为缓解纯 BC 的局限,提出基于分位数的成对排序损失。利用量化后的 codebook 索引 $c_t$ 做子轨迹哈希分组,组内按 RTG 的 $\beta$-quantile 划分正/负样本(用 QuickSelect 把复杂度从 $O(n\log n)$ 降到 $O(n)$),损失 $\mathcal{L}_{\text{pair}}(i,j)=-\log(\sigma(\ell_{a_t^{(i)}}-\ell_{a_t^{(j)}}-\delta))$。作者将其解释为隐式策略改进机制,概念上类似 policy gradient 与 [[bpr]]/Bradley-Terry 偏好学习。TADT 的总损失为多任务:动作预测损失 + 排序损失 + return 回归损失 $\mathcal{L}_{\text{TADT}}=\mathcal{L}_a+\lambda_1\mathcal{L}_{\text{rank}}+\lambda_2\mathcal{L}_R$。

**Contrastive State Abstraction(CSA)**:用 MLP state encoder 把高维状态压成低维潜表示 $e_t$,再做向量量化。

- *TAC-SVQ*(Temporal Advantage-conditioned State Vector Quantization):受 [[variational-autoencoder]]/VQ-VAE 启发,定义相似度 $z(e_t,c_i,R_t^{\text{TA}})=\alpha\,c_i^\top e_t+(1-\alpha)\,c_i^\top R_t^{\text{TA}}$,即量化时同时考虑当前状态与历史 TA 信号,用 Gumbel-Softmax 生成可微 one-hot 赋值 $c_t=Cz_t$。
- 为缓解 codebook collapse,加入最大化 codebook 使用熵的正则项 $\mathcal{L}_{\text{reg}}$。
- *State Auxiliary Networks*:Reward Prediction(RP)网络 $\hat r_t=\text{MLP}(c_t,a_t)$ 与 Contrastive Transition Prediction(CTP)网络(受 SimCLR 启发,以 $(c_t,a_t,c_{t+1})$ 为正样本、随机 $c'_{t+1}$ 为负样本),保证压缩状态空间保留 MDP 的 reward 与 transition 信息。

最终所有 token 序列 $(R_1,c_1,a_1,\cdots)$ 喂入 Causal [[transformer]](GPT 架构)自回归生成动作。总损失 $\mathcal{L}=\mathcal{L}_{\text{TADT}}+\mathcal{L}_{\text{CSA}}$。

**理论分析**:Theorem 1 给出最优策略与抽象策略价值差的上界 $V_{\pi^*}(s)-V_{\pi_\Theta}(s)\le\frac{2}{(1-\gamma)^2}(\varepsilon_r+\kappa I^{\frac{d+2}{2d}}|\mathcal{C}|^{-\frac{1}{d}}+\frac{\gamma\varepsilon_{\mathcal{P}}|\mathcal{C}|}{1-\gamma})$,误差界与原始状态空间大小 $|\mathcal{S}|$ 无关,只依赖 codebook 大小、RP/CTP 预测误差和 embedding 集中度。

## 结果

离线评估用 4 个公开数据集:[[kuairand-pure]]、[[movielens]]-20M、Netflix、[[retailrocket]];指标 Recall@K、[[ndcg]]@K、MRR。baseline 含 [[cql]]、[[iql]]、[[sasrec]]、BERT4Rec、DT4Rec、CDT4Rec、DT4IER。

- TADT-CSA 在四个数据集上的 Recall/NDCG/MRR 大多取得最高或接近最高分。例如 KuaiRand-Pure:Recall@1 = 0.2704(优于 CDT4Rec 0.2402)、NDCG@10 = 0.4995、MRR = 0.4278;MovieLens-20M:Recall@1 = 0.2666、MRR = 0.4264;RetailRocket:Recall@1 = 0.4430、MRR = 0.4867。
- 实现细节:状态为 20 维观测向量,轨迹长度 30,学习率 5e-3,batch 128,codebook size 64,hidden dim 64,训练 50 epoch,PyTorch。
- **消融**(KuaiRand-Pure,Table 2):完整模型 Recall@1 = 0.2704;去掉 TAC 降到 0.2566;去掉 CSA 降到 0.2578;同时去掉 TAC、CTP、RP 暴跌到 0.0893,说明 RP/CTP 网络对 codebook 学习至关重要。
- **参数敏感性**:codebook size = 64、$\delta=0.3$ 时最佳。
- **在线仿真**:用 VirtualTaobao 环境,先训 [[ddpg]] 作为专家采集轨迹预训练各方法,再做在线微调对比 CTR,TADT-CSA 微调时 CTR 高于现有 DT 与传统 RL 方法。
- **在线 A/B**:部署于 [[kuaishou]](Kwai,超 1 亿用户)直播推荐排序阶段,2025 年 3 月做 5 天实验。SAC-CSA 相比 SAC 提升直播 watch time 10.322%、平均 watch time 12.947%;TADT-CSA 相比 SAC-CSA 再提升直播 watch time 2.830%、平均 watch time 15.307%。

## 在本 wiki 中的位置

本文属于 [[llm-for-recommendation]] / 生成式推荐与 [[offline-rl]] 交叉方向,是把 [[decision-transformer]] 应用到工业 [[recommender-systems|recommender-system]] 的延续工作,直接对标 DT4Rec、CDT4Rec、DT4IER 等 DT-based 推荐模型,并改进其 [[behavior-cloning]] 局限(类似 QT、ACT、QDT 等给 DT 注入策略改进的思路)。其状态压缩借鉴 VQ-VAE([[variational-autoencoder]])与 [[graph-contrastive-learning]] 式对比学习。来自 [[kuaishou]] 团队,与该团队在 [[user-retention]]、[[watch-time]] 优化方向上的工作(如强化用户留存的短视频推荐)一脉相承。
