---
type: source
subtype: paper
tags: [recommender-systems, multi-task-learning, survey, CTR, CVR, mixture-of-experts]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2302.03525
raw: raw/2302.03525.pdf
authors: [Yuhao Wang, Ha Tsz Lam, Yi Wong, Ziru Liu, Xiangyu Zhao, Yichao Wang, Bo Chen, Huifeng Guo, Ruiming Tang]
year: 2023
---

这是一篇关于多任务深度推荐系统(Multi-Task Deep Recommender Systems, MTDRS)的系统性综述,从任务关系与方法论两个维度建立了完整的分类体系(taxonomy),梳理了该领域的代表性模型、应用场景、公开数据集与未来方向。

## 问题

推荐系统(RS)在实际场景中往往需要同时完成多种预测任务,例如视频推荐中用户对同一视频会有点击、点赞、转发等多种行为,广告中需要联合估计 CTR 与 CVR。把这些相关任务放进一个统一模型里联合学习,就是多任务学习([[multi-task-learning]], MTL)在推荐中的应用,即多任务推荐(MTR)。借助深度神经网络([[deep-neural-network]])对高阶特征交互和复杂用户-物品交互的建模能力,MTDRS 相比传统 MTR 框架展现出更好的效果。

相比单独处理多个任务,MTDRS 有两大好处:一是跨任务共享数据与知识实现互相增强,二是计算与存储效率更高。但它也面临三个挑战:(1) 如何有效且高效地捕捉任务间有用信息与相关性;(2) 数据稀疏性(尤其转化信号稀疏);(3) 推荐中独特的序列依赖(用户跨任务行为的顺序模式)。尽管 MTL 已被广泛研究,推荐社区一直缺乏系统性综述,本文旨在填补这一空白。

## 方法

论文先给出 MTDRS 的形式化定义:给定 K 个任务的数据集,学习任务专属参数 {θ¹,...,θᴷ} 与共享参数 θˢ,目标是最小化各任务损失的加权和(通常为 BCE 损失);[[ple]] 进一步提出可随训练步更新的损失权重。随后建立两大维度的分类体系:

任务关系(Task Relation):
- 并行(parallel):各任务相互独立计算,无序列依赖,代表工作有 [[dupn]](结合 MTL、attention 与 RNN)、MSSM、CFS-MTL(因果视角的特征选择)等。
- 级联(cascaded):任务间存在序列依赖,如 CTCVR = CTR × CVR。代表为 [[esmm]](impression→click→conversion,共享 embedding、在全空间建模),以及 ESM²、AITM、ESCM² 等,主要解决样本选择偏差(SSB)与数据稀疏(DS)。
- 主辅任务(auxiliary with main task):指定主任务,其余辅助任务帮助提升主任务表现,如 Multi-IPW/Multi-DR、MTRec、PICO 等。

方法论(Methodology):
- 参数共享:硬共享(shared-bottom)、稀疏共享(如 LT4REC 基于 [[lottery-ticket-hypothesis]] 的神经元级 mask)、软共享、专家共享。专家共享受 [[mixture-of-experts]] 启发,[[mmoe]] 用 softmax 门控装配专家被视为里程碑,后续有 [[ple]](提出 Customized Gate Control 显式分离共享与任务专属专家)、SNR、DSelect-k、MoSE(用 [[lstm]] 建模序列行为)等。
- 优化:针对负迁移(negative transfer,含 seesaw 现象,源于梯度主导与参数冲突)与多目标权衡([[pareto-optimality]] 前沿)。代表方法有 AdaTask、MetaBalance(平衡梯度幅度)。
- 训练机制:联合训练、强化学习(将用户行为建模为 [[markov-decision-process]] 优化长期满意度)、辅助任务学习。

## 结果

作为综述,本文不报告单一实验数字,而是给出结构化的归纳结果:

- 模型层面:在 Table 1 中系统总结了 9 个级联任务关系模型(ESMM、ESM²、Multi-IPW & DR、ESDF、HM³、AITM、MLPR、ESCM²、HEROES、APEM),逐一列出其针对的问题与行为序列(如 ESMM 的 impression→click→conversion,AITM 的 impression→click→application→approval→activation)。
- 趋势:Figure 1 显示主流 MTDRS 同时考虑任务关系与参数共享两个因素,其中超过一半的工作采用硬共享(shared-bottom 结构应用最广),专家共享是热点且多在并行任务关系下讨论。
- 数据集:Table 2 汇总了 8 个公开数据集,包括 Ali-CCP、Criteo、AliExpress(排序阶段,任务为 CTR/CVR/CTCVR),以及 [[movielens]]、Yelp、[[amazon-reviews]]、KuaiRand、Tenrec(召回+排序,涵盖 watch/rating/explanation/click/like/follow/comment 等任务)。
- 应用:MTDRS 已落地电商、广告、社交媒体等领域,并通过线上 A/B test 验证,如 MMoE 用于 YouTube(权衡 engagement 与 satisfaction)、LT4REC 用于腾讯视频、BatchRL-MTF 用于腾讯短视频。
- 未来方向:负迁移机理、多任务+多场景统一建模(M2M、AESM²)、使用大规模预训练模型(指出 [[p5]] 基于 [[t5]]、M6-Rec 基于 M6、UniMIND 等用预训练语言模型统一推荐任务)、AutoML/NAS、可解释性、任务特定偏差等。

## 在本 wiki 中的位置

本文是连接推荐系统与多任务学习的纵览性入口。它系统化了 [[mmoe]]、[[ple]]、[[esmm]] 等推荐领域多任务架构,并在"未来方向"中明确指向用 [[p5]]、[[t5]] 等大规模预训练/语言模型统一推荐任务,可作为理解 LLM 时代生成式推荐(generative recommendation)与传统判别式 MTDRS 之间过渡的背景文献。其涉及的 [[mixture-of-experts]]、负迁移、[[pareto-optimality]] 等概念也与 LLM 训练中的多任务/多目标问题相通。
