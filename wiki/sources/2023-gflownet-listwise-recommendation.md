---
type: source
subtype: paper
tags: [recommender-systems, gflownet, listwise-recommendation, generative-model, online-learning, diversity]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2306.02239
raw: raw/2306.02239.pdf
authors: [Shuchang Liu, Qingpeng Cai, Zhankui He, Bowen Sun, Julian McAuley, Dong Zheng, Peng Jiang, Kun Gai]
year: 2023
---

GFN4Rec 把 [[gflownet]] 引入 listwise 推荐,用流匹配损失让生成一个推荐列表的概率正比于其 list-wise 奖励,从而在保持高推荐质量的同时显著提升列表多样性与在线探索能力。

## 问题

个性化推荐需要生成一个与用户兴趣匹配的物品列表。多数方法学习 pointwise 评分模型,独立地给每个物品打分;但已有证据表明 listwise 方法能建模同时曝光物品之间的相互影响([[listwise-recommendation]]),从而进一步提升推荐质量。然而 listwise 推荐面临两大挑战:一是要在巨大的组合动作空间中高效搜索;二是现有使用交叉熵损失的生成式方法存在**多样性偏低**的问题——物品列表往往聚合了高质量物品的曝光概率,模型会迅速区分出高分物品并陷入局部最优,难以探索那些效用略低的列表。本文目标是学到一个能生成足够多样、同时保持高质量推荐的策略。

## 方法

- 提出 [[gfn4rec]] 框架,基于 [[gflownet]] 的流匹配学习范式,把列表生成建模为在**生成树**(generation tree)上的自回归过程:从空列表出发,每步用 item selection model 选一个物品加入列表,根到叶的一条轨迹对应一个长度为 K 的推荐列表(slate)。
- 核心学习目标是让 `P(O|u) ∝ R(u,O)`,即列表生成概率正比于其 list-wise 奖励。采用两类流匹配损失:Trajectory Balance(TB)损失整体优化轨迹;Detailed Balance(DB)损失逐步(step-wise)优化每个位置,方差更低、更适合大动作空间。
- 关键洞见:**log-scale reward matching**(对数尺度奖励匹配),使 `log P(O|u) → log R`,让高分物品与略低分物品不那么容易被区分开,从而提升在线探索时生成的多样性;以及自回归 item selection model 在捕捉物品相互影响的同时优化列表的未来奖励。
- 针对大动作空间引入 bias 项:全局归一化偏置 b_z、奖励平滑偏置 b_r、前向概率偏移 b_f,以稳定训练。
- 用 Transformer-based user request encoder 编码用户画像与最近交互历史;flow estimator φ 与 item selection model θ 联合学习。
- 设计了在线/离线两种学习框架(见 Algorithm 1),并支持多行为(multi-behavior)反馈。

## 结果

- 数据集:[[movielens]](ML1M,6400 用户 / 3706 物品)与 [[kuairand]](KR1K,1000 用户 / 69219 物品),列表长度 K=6。
- 在线学习(Table 2):GFN4Rec 取得最佳奖励指标,在 KR1K 上平均奖励 2.414(最强基线 CF 2.253),领先约 10%;ML1M 平均奖励 2.172。其在线采样变体 GFN4Rec(Explore)在保持较高奖励的同时,item Coverage 与 ILD(intra-list diversity)显著更高——相比 CF/PRM 把 item coverage 提升约 4×;ML1M ILD 0.617、KR1K ILD 0.591。ListCVAE 虽能达到相近多样性但奖励严重下降(准确性-多样性 trade-off)。
- 离线评估(Table 3/4):GFN4Rec 在 ML1M 上 R-NDCG(online) 0.665、R-MRR(online) 0.0848 最佳;在 KR1K 上 R-NDCG(test) 0.362、R-MRR(test) 0.0421 取得最佳测试集指标。在线与离线 ranking 指标一致,验证了在线模拟器的可行性。
- 消融:TB vs DB——DB 逐步学习方差更低,更适合更大的候选物品集合。

## 在本 wiki 中的位置

本文位于**推荐系统 × 生成模型 × 强化/流匹配**交叉处,是把 [[gflownet]] 从分子生成等领域迁移到 [[listwise-recommendation]] 的代表作。它与生成式列表方法(如 ListCVAE)和 reranking 方法(如 PRM)形成对比,核心卖点是用 log-scale 奖励匹配缓解准确性-多样性 trade-off。作者来自快手([[kuaishou]])与 UCSD,包括 [[julian-mcauley]]、[[kun-gai]] 等。可与 [[reinforcement-learning]] 在推荐中的应用相互参照。
