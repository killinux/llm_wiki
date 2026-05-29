---
type: source
subtype: paper
tags:
  - recommender-system
  - cold-start
  - meta-learning
  - online-recommendation
  - matthew-effect
created: 2026-05-29
updated: 2026-05-29
arxiv: "2411.11225"
raw: raw/2411.11225.pdf
authors:
  - Yunze Luo
  - Yuezihan Jiang
  - Yinjie Jiang
  - Gaode Chen
  - Jingchi Wang
  - Kaigui Bian
  - Peiyi Li
  - Qi Zhang
year: 2024
---

# Online Item Cold-Start Recommendation with Popularity-Aware Meta-Learning (PAM)

提出 PAM:一种 model-agnostic 的 popularity-aware meta-learning 框架,用预设的物品热度阈值把流式数据切分成固定的 meta-learning 任务,在线流式训练中解决新物品 [[cold-start]] 问题,并在三个公开数据集与 Kuaishou 亿级用户在线 A/B 上验证有效。

## 问题

在线 [[recommender-system]](短视频、电商、流媒体)需要在严格时延约束下、以单 epoch 流式训练持续更新模型并分发新物品。新物品的 [[cold-start]] 问题(交互稀疏)持续损害推荐效果,且面临两大挑战:

- **[[matthew-effect]](马太效应)**:线上线下数据由热门物品主导,模型对热门越来越准、对冷门越来越差,热门数据占比随时间增大,加剧冷启动。
- **流式约束下旧方法失效**:传统冷启动方案(基于 fine-tuning / 知识迁移 / side-information)多在离线表现好;但在流式数据管线上,因训练方式、计算开销与时延限制,无法为每个新物品实时生成个性化参数。

## 方法

PAM 由三部分组成,基座是一个 model-agnostic 的 dual-tower(双塔)模型,embedding 经多层全连接得到 user/item 顶层表示,用 InfoNCE / log loss 训练。

- **Popularity-Aware Meta-Learning(固定任务切分)**:用分段常数函数 F(v_i) 按物品热度(点击/销量等)把每个 batch 切成 N 个固定任务 {T_1,...,T_N}(最冷的 5% 为 cold-start 任务,其余分 4 个热度任务)。采用 gradient-based meta-learning 的 bi-level 优化:
  - **Local update**:从共享网络初始化 Θ_t 出发,在每个任务的 support set 上做内循环梯度更新得到任务专属网络参数 Ω_t^n(用 LSLR 为每个权重维护自适应学习率,缓解过拟合);
  - **Global update**:在 query set 上对所有共享参数 {Φ_t, Θ_t} 做外循环更新,损失为各任务加权和(冷启动任务权重更高,如 2,其余 0.5)。
  - 固定切分使在线推理无需对每个物品 fine-tuning(提前存好各任务参数),大幅降低传统 meta-learning"每条样本一个任务"的计算/存储开销;冷启动任务更依赖 content 特征,热门任务更依赖 popularity/反馈特征。
- **Cold-start Task Enhancer(冷启动任务增强器)**:把 item embedding 分为 behavior-based(含 ID embedding、序列 embedding)与 content-based;系统在物品处于冷启动期时把其 behavior-based embedding 存入参数 Φ̂。
  - **Cold-start Embedding Simulation**:对当前的热门物品,用其曾经存下的冷启动期 behavior embedding 拼接当前 content embedding,模拟出"冷启动状态"的物品 embedding ê_i。
  - **Data Augmentation**:用模拟的 ê_i 配上真实热门交互标签构造额外冷启动样本(L^A),直接扩充稀缺的冷启动训练量。
  - **Self-supervised Instructor**:用热门物品训练充分的真实 ID embedding 作监督,训一个映射层使冷启动网络输出的顶层表示逼近真实 ID embedding(MSE 损失 L^S),无需标签即提升冷启动特征抽取能力。
- **总损失**:L^T = γ_M·L^M + γ_S·L^S + γ_A·L^A(γ 取 1/3/2),联合更新共享参数与映射参数。

## 结果

- **数据集**:MovieLens(43,181 用户 / 51,142 物品 / 6,840,091 交互)、Yelp(1,987,929 用户 / 150,346 物品 / 6,990,280 交互)、Book(Amazon,351,487 用户 / 581,717 物品 / 6,402,728 交互);各数据集等分为 31 个 period,从第 24 个 period 开始测试,报告 [[ndcg]]@K 与 Recall@K 在冷启动物品上的平均。
- **冷启动物品(Table 2)**:PAM 全面、大幅超越 PF / s2Meta / IncCTR / SML / ASMG / MeLON / IMSR 等 baseline。相对最优 baseline 的提升幅度:
  - MovieLens:Recall@5 +32.73%,NDCG@5 +57.81%;
  - Yelp:Recall@5 +64.51%,NDCG@5 +74.09%;
  - Book:Recall@5 +20.06%,NDCG@5 +20.23%。
  - 在小 K 值上优势最明显,说明 PAM 能把冷启动物品准确推给最偏好它的用户;ASMG 在 Yelp 上因存储开销 OOM。
- **消融(Table 2 中 PAM-M / PAM-S / PAM-A / PAM-F)**:self-supervised 模块与 data augmentation 模块各自都能提升,完整增强器 PAM-F 最佳;PAM-S 在 content 特征丰富的 MovieLens 上提升较小、在 Yelp 上提升显著。
- **热门物品(Table 3)**:PAM 在热门物品上不如其在冷启动上的优势明显(说明参数偏好确实倾向冷启动任务),但仍优于部分 baseline。
- **在线 A/B(Table 4,Kuaishou 亿级用户线上)**:相比 PF,Show% +41.39%、点赞 LTR +60.45%、评论 CMTR +4.26%、收藏 CLTR +6.34%。
- 代码开源:https://github.com/Sycamoretail/PAM 。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] / [[cold-start]] 方向,核心手段是 meta-learning 而非 LLM。它把 [[matthew-effect]] 视为在线冷启动的根因,用"按热度固定切分任务 + 跨任务共享 meta-knowledge"在流式约束下解决新物品冷启动,可与同主题的 [[2024-prompt-tuning-item-cold-start]] 互为对照(后者侧重 prompt-tuning 思路的物品冷启动)。出品方为 [[kuaishou]] 与北京大学,使用了 [[movielens]]、[[yelp-dataset]] 等常见推荐数据集,评测指标用 [[ndcg]]。与本 wiki 中大量 LLM-for-recommendation 工作相比,本文提供了一个"工业级在线流式 + meta-learning"的非 LLM 基线视角。
