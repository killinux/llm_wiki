---
type: source
subtype: paper
tags: [diffusion-model, recommender-system, survey, collaborative-filtering, sequential-recommendation, generative-model]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2501.10548
raw: raw/2501.10548.pdf
authors: [Ting-Ruen Wei, Yi Fang]
year: 2026
---

# Diffusion Models in Recommendation Systems: A Survey

一篇关于扩散模型(diffusion model)在 [[recommender-systems|recommender-system]] 中应用的系统性综述,提出以"推荐任务为本"的三正交轴 taxonomy,覆盖 188 篇相关论文。

## 问题

扩散模型在计算机视觉中展现出强大的生成与复杂分布建模能力,自 2022 年起被大量引入推荐系统,论文数量快速增长(2022 年 1 篇,2023 年 14 篇,2024 年 62 篇,2025 年 107 篇),亟需系统梳理。已有的扩散+推荐综述(Lin et al.)以**扩散模型的角色**(数据工程/编码、推荐模型、内容呈现)为分类视角。本文作者认为,采用扩散模型的根本目的是**提升推荐性能**,而非把推荐任务改造去迁就扩散模型,因此应当以**推荐任务**为本组织文献,提供一个与既有综述互补的相反视角。

## 方法

作者通过 Google Scholar 检索("diffusion models in recommender systems"等查询)并人工核查每篇论文中 diffusion 的定义,仅保留与 [[ncsn]] 或 DDPM 同源的扩散方法(排除 graph diffusion、information diffusion),并通过递归追溯相关工作章节补全,最终收录 188 篇。

**基础铺垫**:综述系统回顾了扩散模型基础——NCSN(score-matching + Langevin dynamics)、DDPM([[ddpm]],x-prediction/ε-prediction 训练目标),以及改进与效率方向:[[ddim]](非马尔可夫加速采样)、ODE solver(SDE 视角下 NCSN 对应 VE-SDE、DDPM 对应 VP-SDE)、[[latent-diffusion-model]],和条件生成的 classifier guidance 与 [[classifier-free-guidance]]。

**三正交轴 taxonomy**:
1. **Core Recommendation Tasks(What)**:[[collaborative-filtering]] 与 [[sequential-recommendation]]。其下又区分两种通用范式——**data augmentation**(扩散模型作为生成模块,合成交互/负样本以稠密化稀疏数据、辅助对比学习)与 **direct generative recommendation**(扩散模型作为核心推荐器,去噪交互向量/嵌入,再按概率排序或相似度排序)。CF 按辅助信息细分为 implicit feedback、explicit ratings、item graph、user graph、knowledge graph;序列推荐按历史序列的角色分为 sequence as target、as guidance、as both,并把 POI 推荐作为特例。
2. **Data Modality and Domain(Where)**:image generation(如用 Stable Diffusion 生成个性化/广告商品图,DPO 微调)、text-to-recommendation(DMSR 用 v-prediction 做 slate/playlist 生成)、multimodal recommendation、cross-domain recommendation。
3. **Trustworthy Objectives and Constraints(Why)**:fairness、accountability(隐私、抗 shilling 攻击、差分隐私、联邦推荐)、transparency(DIEXRS 生成解释)、out-of-distribution(分布鲁棒优化、图增强提升泛化)。

## 结果

本文为综述,核心"结果"是文献组织与跨论文的实证对比(均直接取自各原论文,以各自最强 baseline 计相对增益):

- **CF(Table 1,Recall@20 / NDCG@20)**:在 Amazon-Books、[[movielens-1m]]、Yelp 上,扩散类模型(HDRM、DiffRec、DDRM、BSPM、CF-Diff 等)持续优于各自最强 baseline。例如 DiffRec 在 Amazon-Books Recall@20 较 MultiVAE 提升 +8.02%,NDCG@20 较 MultiVAE 提升 +12.78%;DDRM 在 MovieLens-1M NDCG@20 较 DeCA 提升 +9.81%。
- **序列推荐(Table 2,HR@20 / NDCG@20)**:在 YooChoose、[[kuairec]]、Zhihu 上,扩散类模型(ADIGRec、TDM、TA-Rec、[[dreamrec]]、DiffDiv)显著超越最强对比 baseline。如 ADIGRec 在 Zhihu HR@20 较 DimeRec 提升 +42.18%;某序列模型在 YooChoose NDCG@20 较 DreamRec 提升 +104%。
- **数据集汇编(Section 6)**:按 Fashion/E-commerce、Social/Review、Media/Entertainment、Location、Meal Planning 五域整理常用数据集及规模(如 Amazon 54M 用户 / 5.7 亿评论、Tmall 13.3 亿交互、[[movielens]] 系列、Steam、MIND、Foursquare 等)。

**开放方向(Section 7)**:效率(DDIM/latent diffusion/ODE solver/step reduction 加速,但缺乏标准化延迟 benchmark;Benigni et al. 报告 DiffRec/CF-Diff/GiffCF/DDRM 多次运行方差大、部分弱于简单 baseline);guidance 的有效利用(concatenation vs cross-attention 仍偏架构附加,缺乏 disentangled/task-aware guidance 表征);以及 flow matching(FlowCF)等新方向。

## 在本 wiki 中的位置

本文是连接[[diffusion-model 类生成模型]]与 [[recommender-systems|recommender-system]] 两大主题的综述性 source,可作为扩散+推荐子领域的入口索引。它与 wiki 中已有的 RL-based 推荐([[rl-based-recsys]]、[[easyrl4rec]])、[[llm-for-recommendation]]、以及生成式推荐(如 [[p5]])相互补充,共同覆盖推荐系统的不同建模范式;其涉及的 [[ddpm]]、[[ddim]]、[[latent-diffusion-model]]、[[classifier-free-guidance]] 等基础概念可与生成模型条目交叉引用。
