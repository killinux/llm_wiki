---
type: source
subtype: paper
tags:
  - sequential-recommendation
  - system-exposure
  - offline-rl
  - decision-transformer
  - data-augmentation
  - exposure-bias
created: 2026-05-29
updated: 2026-05-29
arxiv: "2504.13482"
raw: raw/2504.13482.pdf
authors:
  - Ziqi Zhao
  - Zhaochun Ren
  - Jiyuan Yang
  - Zuming Yan
  - Zihan Wang
  - Liu Yang
  - Pengjie Ren
  - Zhumin Chen
  - Maarten de Rijke
  - Xin Xin
year: 2025
---

CaseRec 通过对 system exposure(系统曝光序列)做 counterfactual augmentation,并用 Decision Transformer 式的 offline RL 建模不同用户反馈,从而改进 [[sequential-recommendation]] 并缓解 exposure bias。

## 问题

在 [[sequential-recommendation]](SR)中,**system exposure**(系统曝光)指推荐系统展示给用户的物品列表,而用户通常只与其中极少数交互。现有 SR 方法主要存在两个局限:

- **只建模已交互物品**:大量"曝光但未交互"的物品被忽略。常见做法把未交互物品简单当作负反馈 [11],但这一假设未必成立——曝光未交互的物品(图 1a 中的 v2)可能也符合用户兴趣,只是受时间等限制未被点击,其中蕴含潜在用户兴趣。
- **即便建模完整曝光,也只用 logged 曝光序列训练**,忽略了"未被曝光"的用户兴趣,导致 **exposure bias**(曝光偏差,又称 previous model bias)。已有 debiasing 方法(基于 [[inverse-propensity-score]] 的惩罚、或 [[distributionally-robust-optimization]])会对不当物品施加惩罚,可能损害模型性能。

作者主张:把包含已交互与未交互物品的完整曝光序列纳入建模,并用 counterfactual(反事实)曝光序列来发掘未见过的用户兴趣,是缓解 exposure bias 的另一条路径。

## 方法

CaseRec(**c**ounterfactual **a**ugmentation over **s**ystem **e**xposure for sequential **rec**ommendation)由三个部分组成(图 2):

**1. 基于 Decision Transformer 的序列推荐器。** 把 [[offline-rl]] 视作条件序列建模问题,采用 [[decision-transformer]](DT)。输入轨迹 τ = (R̂₁, s₁, a₁, …, R̂_T, s_T, a_T):

- **state** s_t = (v₁, b₁, …, v_t, b_t):同时含曝光物品与用户反馈,经 GRU 状态编码器([[gru4rec]] 风格的 [[gru4rec|GRU]] encoder)映射为隐状态;物品与行为分别用两套 embedding 编码再相加。
- **action** a_t:第 t 步曝光的物品。
- **reward** r_t:依用户反馈定义,b_{t+1}=0 取 r_uni、=1 取 r_int(也支持按 watch-time 等更细粒度反馈赋奖)。
- **RTG** R̂_t:从 t 到 T 的累计奖励(return-to-go)。

关键改造:原始 DT 的目标是预测每一步 action,而 SR 要预测用户**会交互**的下一个物品。CaseRec 把 ground-truth action 重定义为"当前 t 之后第一个被交互的物品"(ā_t = v_k,k = min{k | k>t ∧ b_k=1}),用 cross-entropy loss 训练,使模型只预测高回报 action,弥合 DT 与 SR 目标的差距。

**2. 用户模拟器(user simulator)。** 受 model-based offline RL 启发,用一个 transformer-based [[user-simulation|user simulator]] 预测"若把曝光序列中某物品换成反事实物品,用户会给出什么反馈"。它与推荐器共享 state/action encoder 与 transformer block,输出经全连接层 + 二元交叉熵优化。

**3. Counterfactual augmentation(两种策略)。**
- **Random**:把 logged 曝光序列中的物品替换成从物品集 V 中**均匀采样**的新物品,再用 user simulator 预测反馈,自回归地生成长度 h 的反事实曝光序列。意在摆脱先前部署策略的影响、增加训练多样性。
- **Self-Improving**:对某个历史曝光物品的 embedding 加小幅 Gaussian noise(扰动),取与扰动 embedding 余弦相似度最高的物品作为替换,再用**当前推荐器**自回归生成后续序列、user simulator 给反馈。让模型探索历史曝光物品附近的物品空间,迭代自我改进。

最终把 logged 曝光序列与反事实增强序列**混合**训练 DT 推荐器(Algorithm 1)。

## 结果

在三个真实数据集上实验:[[zhihurec|ZhihuRec]]、[[steam-dataset|Tenrec]](注:Tenrec 视频推荐场景)与 [[kuairand|KuaiRand]](含 KuaiRand-15policies 与无偏的 KuaiRand-Random)。指标为 Recall@K 与 [[ndcg|NDCG]]@K(K=5/10/20),5 次重复取均值,8:1:1 划分。Baselines 含 [[gru4rec|GRU4Rec]]、[[sasrec|SASRec]]、[[sasrec|BERT4Rec]]、CORE、FEARec、[[inverse-propensity-score|IPS]]、ReLMF、[[distributionally-robust-optimization|DRO]]、vanilla [[decision-transformer|DT]]、SQN。

- **整体性能(RQ1):** CaseRec-S 与 CaseRec-R 在三个数据集全部指标上均超过所有 baseline(p<0.01)。例如 ZhihuRec 上 Recall@20:CaseRec-S 0.1470 vs 最佳 baseline(FEARec)0.0445;Tenrec Recall@20:0.2459 vs DRO 0.1701;KuaiRand-15policies NDCG@20:0.1579 vs DRO 0.0770。Self-Improving 普遍优于 Random(在物品空间附近探索质量更高);在密度更高的 KuaiRand 上提升最显著。
- **Debiasing 性能(RQ2):** 在无偏 KuaiRand-Random 上评估(用有偏 KuaiRand-15policies 训练),只有 CaseRec 取得令人满意的结果,如 Recall@10:CaseRec-R 0.0139 vs 最佳 baseline(SQN)0.0028;说明反事实增强能捕捉原数据集之外的新兴趣。此处 CaseRec-R 反而优于 CaseRec-S,因随机曝光模拟更能削弱先前策略的影响。
- **推荐多样性:** 用 Coverage@K 衡量,CaseRec-R 在三数据集上 coverage 最高(图 3),说明其探索了更广物品空间,可作为缓解 exposure bias 的替代方案。
- **增强比 δ 的影响(RQ3):** δ 从 0.2 增到 10,性能先升后降(δ 过大引入过多噪声);各 δ 下 CaseRec 仍优于最佳 baseline,显示鲁棒性。
- **消融(RQ4,Tenrec / Self-Improving):** No-Aug(去掉反事实增强)、No-Enc(用 embedding 均值替代 state encoder)、No-Des(去掉对学习目标的改造)均劣于完整 CaseRec,验证三个模块的有效性。

代码:https://github.com/ZiqiZhao1/CaseRec(SIGIR '25)。

## 在本 wiki 中的位置

本文位于 [[recommender-systems|recommender-system]] 与 [[offline-rl]] 的交叉点,把 [[decision-transformer]] 与 [[rl-based-recsys|RL-based RecSys]] 引入 [[sequential-recommendation]]。它与 [[exposure-bias]] / [[debiasing]] 主题相关:不同于基于 [[inverse-propensity-score]] 或 [[distributionally-robust-optimization]] 的惩罚式 debiasing(如 DRO),CaseRec 改用 [[counterfactual-reasoning|counterfactual]] 数据增强 + [[user-simulation]] 来发掘未见兴趣。其 user simulator 思路属 [[model-based-rl]];Self-Improving 策略呼应 [[self-improvement]] 与 [[recommendation-simulator]] 的相关工作。基线层面与 [[gru4rec]]、[[sasrec]]、SQN、[[decision-transformer|DT]] 形成对照。
