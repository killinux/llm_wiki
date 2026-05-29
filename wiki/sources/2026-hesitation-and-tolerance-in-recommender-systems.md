---
type: source
subtype: paper
tags:
  - recommender-system
  - user-behavior
  - user-retention
  - watch-time
  - ctr
  - human-computer-interaction
created: 2026-05-29
updated: 2026-05-29
arxiv: "2412.09950"
raw: raw/2412.09950.pdf
authors:
  - Kuan Zou
  - Aixin Sun
  - Yitong Ji
  - Hao Zhang
  - Jing Wang
  - Zhuohao (Jerry) Zhang
  - Xuemeng Jiang
year: 2026
---

提出并形式化推荐系统中介于"接受"与"拒绝"之间的两种被忽视的交互状态——hesitation(犹豫:用户带着不确定性犹豫不决地点击)与 tolerance(容忍:犹豫升级为不情愿地持续参与直至失去兴趣),通过两次大规模问卷、离线行为日志分析与线上 A/B 实验,论证容忍是一种消耗用户时间、侵蚀信任、降低 [[user-retention]] 的"低价值参与",并主张将 tolerance 信号作为"弱正/负"反馈重新建模。

## 问题

主流 [[recommender-systems]] 把用户交互压缩为简单的接受/拒绝二元信号,[[ctr]]、[[watch-time]] 等指标把所有点击同等看待,抹去了点击前后真实的好奇、怀疑与后悔。作者指出存在被忽视的中间状态:hesitation(犹豫,带不确定性地权衡后才点击)和 tolerance(容忍,犹豫升级为已意识到不感兴趣却仍勉强参与)。这些状态引入隐性的交互成本、时间与认知负担及负面情绪,却对现有优化目标不可见。论文提出三个研究问题:RQ1 兴趣与无兴趣之间是否存在中间状态;RQ2 若存在,如何系统识别与建模;RQ3 推荐系统能否利用这些信号提升用户留存。

## 方法

采用问卷 + 离线日志 + 线上实验的多方法研究:

- **两次大规模问卷**:通过中国开发者社区 CSDN 发放,第一次 6,644 份(17 天)、第二次 3,864 份(5 天),筛选后分别得 5,556 / 2,879 有效样本。采用场景化提问(避免直接询问抽象概念),用 Q1–Q9 的"是/否"率刻画 hesitation 与 tolerance 的普遍性与后果(信任下降、疲劳、流失)。
- **离线行为日志分析**:在电商 [[steam-dataset|Taobao]] 与短视频 [[kuairand|Kuaishou]] 两个域上分析 tolerance 行为。Taobao 将"点击但无后续动作(加购/收藏/购买)"定义为 tolerance;Kuaishou 将"观看时长比例低于个人平均"定义为 tolerance。比较"参考周"与"调查周"的活跃度变化,验证高 tolerance 与参与度下降的相关性。
- **线上 A/B 实验**:在一个拥有数千万活跃用户的中文视频流媒体平台上,微调排序模型 SIM 的正样本判定标准。重构推荐模型的交叉熵目标(式 1),提出两种策略——把 tolerance 样本当作**负样本**(式 2),或当作**弱正样本**并用折扣系数 β∈(0,1) 降权(式 3)。其中 β 由用户实际观看时长低于其历史完成基线的程度确定性计算得出,而非可调超参。开展两轮各含两组(共四组)实验,每组约 100 万次曝光,主指标为 Day-2 留存率变化(ℛ)。

## 结果

- **问卷发现**:仅 6% 用户从不犹豫,64% 表示当信息不足以判断时常犹豫;94%(Q1)曾对推荐内容犹豫,90%(Q2)承认"点击查看但无后续动作"不代表真正感兴趣;60% 偏好没有犹豫过程的物品;59% 在浪费时间后感到沮丧,80% 表示重复经历会加剧负面情绪;70%(Q9)称持续遭遇此类情况最终会停止使用平台。
- **离线分析**:在 Taobao 与 Kuaishou 上,tolerance 越高,调查周活跃度下降越明显(Figure 4),证实 tolerance 是兴趣的"弱信号",其累积预示脱离与流失。
- **线上 A/B**:四组实验在 7 天窗口内 Day-2 留存均提升。Tolerance 作负样本两组平均 +0.670% / +0.360%;作弱正样本两组平均 +0.15% / +0.58%。论文总结平均 7 天留存提升达 **0.67% 与 0.36%**(两次独立实验),在工业规模下属显著改进。Dwell time(停留时间)却普遍下降(如组 1 平均 −1.18%),表明缩短"无效观看时间"不降反保留存——说明参与的**质量比时长更重要**。
- **概念贡献**:提出 low-regret satisfaction(低后悔满意度)视角,以及三项新评估指标——Time-to-Disinterest(TTD)、Hesitation Tax(犹豫税)、Regret-Adjusted CTR(rCTR),倡导评估从"计数动作"转向"度量体验质量"。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 与 HCI 交叉方向,核心关切是 [[user-retention]] 与对 [[ctr]]、[[watch-time]] 等表层指标的反思,与 [[duration-bias]]、[[noisy-watching]]、[[debiasing]] 等"重新解读隐式反馈"的工作一脉相承(参见 [[2023-d2co-watch-time-debias]])。其离线分析使用了 [[kuairand]] 数据集,线上实验在 [[kuaishou]] 类短视频平台上进行。不同于面向长期奖励的 [[rl-based-recsys]]/[[long-term-recommendation]],本文主张通过轻量级的标签重定义(把 tolerance 当作弱正/负样本)来兼顾用户时间成本与平台留存。
