---
type: source
subtype: paper
tags: [recommendation, dataset, debiasing, exposure-bias, sequential-recommendation, off-policy-evaluation, kuaishou]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2208.08696
raw: raw/2208.08696.pdf
authors: [Chongming Gao, Shijun Li, Yuan Zhang, Jiawei Chen, Biao Li, Wenqiang Lei, Peng Jiang, Xiangnan He]
year: 2022
---

KuaiRand 是从快手 App 收集的一个无偏序列推荐数据集,通过在正常推荐流中随机插入随机视频来获取无偏的用户反馈,首次支持在大规模推荐场景下做无偏离线评估与去偏(debiasing)研究。

## 问题

现实中的推荐系统存在固有的曝光偏差(exposure bias):离线日志只记录了系统曾经曝光过的物品的交互,对海量"未曝光"物品的用户偏好一无所知,导致离线评估与线上结果不一致、产生过滤气泡(filter bubble)。从根本上解决这一问题需要收集 missing-at-random(MAR)数据,即用户对均匀随机抽样物品的反馈。已有的随机曝光数据集(如 Yahoo!、Coat、Open Bandit)要么规模太小(Yahoo! 仅 54,000 条随机评分,Coat 仅 4,640 条),要么缺失关键信息(无用户 ID、无用户/物品特征、无时间戳),无法满足序列推荐等任务的需要。

## 方法

作者从快手(中国最大短视频平台之一,日活超 3 亿)采集数据,核心是干预线上推荐策略:在两周内(2022.04.22~2022.05.08),每当推荐系统给用户出列表时,以固定概率插入一条从候选池(共 7,583 个物品)中均匀随机抽样并替换的视频,用户对此无感知,从而获得真正无偏的反馈。要点:

- 记录每次交互的 **12 种反馈信号**(如 click、like、hate、view time、收藏、关注作者、写评论等),覆盖多种 UI 场景(共 15 种推荐策略/scenario)。
- 同时回溯采集这些用户在随机曝光前两周(2022.04.08~2022.04.21)的正常交互历史,以支持序列建模。
- 保留所有用户 ID、物品 ID,以及丰富的用户/物品侧特征(用户 30 维、物品 62 维特征)。
- 过滤掉随机曝光少于 10 次的用户,最终保留 27,285 名用户。

发布三个版本:**KuaiRand-27K**(完整版,23GB 日志 + 23GB 特征)、**KuaiRand-1K**(均匀抽 1,000 用户,829MB + 3.5GB)、**KuaiRand-Pure**(只保留候选池内 7,582 个视频的日志,184MB + 10MB)。

## 结果

这是一份数据集论文,主要"结果"是数据集本身的规模与特性(见 Table 1):

- **KuaiRand-27K**:27,285 用户,正常交互部分含 32,038,725 个物品、322,278,385 条正常推荐交互;随机干预总次数为 1,186,059。
- **KuaiRand-1K**:1,000 用户,4,369,953 个物品,正常交互 11,713,045 条,随机交互 43,028 条。
- **KuaiRand-Pure**:27,285 用户,7,551 个物品,正常交互 1,436,609 条,随机交互 1,186,059 条。
- 所有 7,583 个候选物品都至少被随机插入一次。每个用户平均拥有数千条历史交互,适合长序列建模。

相比已有数据集,KuaiRand 是**首个**包含百万级随机曝光干预、且保留完整用户/物品 ID、特征、时间戳、12 种反馈信号的无偏序列推荐数据集。它可支撑去偏推荐、off-policy evaluation(OPE)、交互式推荐(基于强化学习)、长序列行为建模、多任务学习等方向。数据发布于 kuairand.com。

## 在本 wiki 中的位置

本文是 [[recommender-systems]] 领域的数据集贡献,核心解决 [[exposure-bias]] 问题,通过随机曝光获得 [[missing-at-random]] 数据以支持 [[debiasing]] 与 [[off-policy-evaluation]]。它服务于 [[sequential-recommendation]] 与长序列行为建模研究,数据来自 [[kuaishou]] 平台。同组作者还发布过全观测数据集 [[kuairec]],二者互为补充。与 [[yahoo-r3]]、[[coat]]、[[open-bandit-dataset]] 等随机曝光数据集相比,KuaiRand 在规模与信息完整度上是新的基准。
