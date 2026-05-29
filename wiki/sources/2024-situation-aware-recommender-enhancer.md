---
type: source
subtype: paper
tags: [recommender-system, context-aware-recommendation, situation-aware-recommendation, personalized-ranking, conditioning-neural-network]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2403.18317
raw: raw/2403.18317.pdf
authors: [Jiayu Li, Peijie Sun, Chumeng Jiang, Weizhi Ma, Qingyao Ai, Min Zhang]
year: 2024
---

提出 SARE(Situation-Aware Recommender Enhancer),一个可插拔模块,把"情境(situation)"视为用户交互的前置条件而非普通特征,以个性化方式建模情境对用户-物品偏好的动态影响。

## 问题

用户与 [[recommender-systems|recommender-system]] 交互时,当前情境(situation)——如时间、地点、环境、情绪、活动——会显著影响其偏好。情境是交互发生的"背景",使用户-物品关系随情境变化而动态演化。但已有 [[context-aware-recommendation]] 方法把情境与用户、物品**置于同一层级**:或像 [[factorization-machines]]、xDeepFM、DIN、DIEN 那样把情境与其他属性拼接作为输入,或单独设计模块建模情境与用户/物品属性的关系。它们只能分别建模情境与用户/物品的关联,而**忽略了情境对用户-物品关联(即用户偏好)的动态影响**;同时由于情境与用户被联合建模,情境的"个性化感知与影响"也未被充分刻画。

两个关键事实:(1) 用户偏好对情境敏感,情境在比用户/物品固有特征更高的层级上影响偏好;(2) 用户对情境的感知是个性化的(如 11 点对早起者很晚、对夜猫子尚早),情境带来的偏好变化也是个性化的。

## 方法

核心视角:**把情境作为推荐的前置条件(precondition)**,而非又一种特征。基于此提出 **SARE(Situation-Aware Recommender Enhancer)**,一个轻量两塔结构的可插拔模块,可嵌入各类 backbone RecSys(包括 context-aware 与 ID-based)。

- **情境定义**:情境是交互前即可获得、独立于 RecSys、反映用户动态状态的属性(时间、地点、天气、当下活动、情绪等);用户画像、历史交互、社交网络、物品特征均不属于情境。
- **两个核心组件**:
  - **UCPE(User-Conditioned Preference Encoder,用户条件偏好编码器)**:一个 conditioning neural network,把物品 i_s(及序列推荐中的历史 h_s)用以用户嵌入 u_s 为条件的个性化嵌入编码,得到个性化偏好 p_u,建模情境影响的个性化。受 conditioning sequence modeling 启发,用一组 K 个基础激活函数 {sigmoid, relu, tanh, ...} 的有序集合,从用户向量学习个性化加权,对激活输出做集成。
  - **PSF(Personalized Situation Fusion,个性化情境融合)**:用 cross-attention 从用户嵌入与各情境属性嵌入中学习融合权重,把 N 个情境属性自适应聚合为单一表示 s_u,建模用户对情境的个性化感知。
- **概率组合器(combiner)**:把 backbone 的无情境得分 Sc(i|u) 与 SARE 的情境得分 Sc(i|u,s) 经 softmax 转为概率后,用加权调和平均(weighted harmonic mean)自适应融合;权重由两侧的置信度决定,置信度借鉴 uncertainty-based 方法、由模型不确定性量化。这样情境不可靠时可退化为 backbone 预测。
- **学习**:端到端训练,backbone 与 SARE 各用 session 级 pairwise BPR loss,并对最终概率施加 Cross-Entropy 约束损失以对齐两侧输出。任务被定义为 impression 列表上的排序问题(M+ 正样本、M- 负样本)。

## 结果

- 在**两个真实数据集**上,将 SARE 应用于**七个 backbone**(论文摘要称 seven backbones;正文为五个 context-aware RecSys + 两个 ID-based RecSys)。
- 实验结果表明,相比各 backbone 本身以及 SOTA 的 situation-aware baseline,SARE 都能**显著提升**推荐性能(personalized ranking 指标)。
- 在两个 ID-based RecSys 上的提升进一步验证了 SARE 的**灵活性**(可插拔、跨 backbone 通用),且只引入极少量额外参数。

(注:本文为方法/实验型论文;具体指标数值在所读取页面之外的实验章节,此处不臆造。)

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 中 [[context-aware-recommendation]] / situation-aware 方向。与把情境当作普通特征拼接的 [[factorization-machines]] 等不同,它把情境抬升为"前置条件",强调情境感知与影响的个性化建模,可与序列推荐、conditioning network 等线索对照。与 [[large-language-models]] 主线关系较弱,属于推荐系统专题的补充节点。
