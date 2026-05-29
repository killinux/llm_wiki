---
title: "You Don't Bring Me Flowers: Mitigating Unwanted Recommendations Through Conformal Risk Control"
type: source
subtype: paper
tags: [recommender-system, conformal-risk-control, content-moderation, recommendation-diversity, kuairand, ai-safety]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2507.16829
raw: raw/2507.16829.pdf
authors: [Giovanni De Toni, Erasmo Purificato, Emilia Gómez, Bruno Lepri, Andrea Passerini, Cristian Consonni]
year: 2025
---

一个 post-hoc、模型无关、distribution-free 的方法,用 [[conformal-risk-control]] 给推荐结果中"不想要内容"(unwanted content)的比例提供可证明上界,并通过把潜在有害项替换为用户曾看过且未举报的"安全"重复内容,在控制风险的同时尽量保住推荐质量。

## 问题

[[recommender-systems|recommender-system]] 在个性化的同时会传播 irrelevant、unwanted 乃至 harmful 的内容,助长 misinformation、radicalization 与 [[filter-bubble]],侵蚀用户信任。平台虽提供 YouTube 的 "Not Interested"、Kuaishou 的 "Don't recommend"/"Report" 等反馈机制,但这些机制效果有限、对用户反馈反应迟缓,且缺乏对系统"风险"的精确、透明、用户可控的保证。

作者先在 [[kuaishou]] 短视频平台的 [[kuairand]] 数据集上做实证分析,得到三点关键洞见:

- engagement 与 perceived harmfulness 并不完全相关——被举报视频与未举报视频的观看比例 W% 分布相同,因此最大化 engagement 并不意味着减少有害内容。
- negative feedback 极其稀疏:60.1% 用户每看 1000 个视频最多举报 1 个,超过 95% 用户举报的视频占其观看量不到 1%。
- 重复消费(repeated consumption)普遍存在:平均 2.6% 的观看是重看过的视频;在重复视频中,首次未举报、再看仍未举报的占 99.79%,而"首次未举报、二次才举报"的极罕见(0.11%),这为"用旧的安全内容替换"提供了依据。

现有把 conformal prediction 用于推荐的工作只做简单过滤,会丢失对推荐集大小的控制(作者用 Proposition 2 证明:纯阈值过滤在 α<1 时往往无法返回 k 个项),且只提供 group-level 保证或需要从反馈中学策略。

## 方法

把推荐看作:ranker f(U,I) 给出相关性分数,post-processing 用阈值 λ 构造候选集 T_λ(U)={i: s(U,I=i)≥λ},再取 top-k 得 S_λ(U,k)。风险 R_H 定义为推荐集中被用户标记 unwanted(H=1)项的比例(Eq.5)。

- **Conformal Risk Control(核心)**:基于 Angelopoulos 等的 [[conformal-risk-control]],在 held-out 校准集上,对给定风险上界 α∈[0,1] 选阈值 λ̂ = inf{λ : (n/(n+1))·R̂(λ) + 1/(n+1) ≤ α}(Theorem 1),即可保证 E[R(S_λ̂(U,k))] ≤ α。该保证 model-agnostic、distribution-free,可直接套到任意已训练 recommender,无需 retraining。
- **Item Replacement(实践创新)**:为避免纯过滤导致推荐项不足,提出用"安全的重复内容"替换被过滤项。定义 safe 池 T^(safe)(U)={i': H(U,I=i')=0 ∧ C(I=i')>β}——用户曾看过、未举报、且代理变量 C(取 watch-time W%)超过阈值 β 的项。新候选集 T_λ^(replace)(U)=T_λ(U)∪T^(safe)(U)(Eq.8)。Property 1 形式化"满足条件的重复项二次被举报概率为 0"的假设,Proposition 3 保证替换后仍满足 conformal risk control 所需的单调性。
- **整体 pipeline(Algorithm 1)**:先用 RiskControl 算 λ̂,过滤低分项,识别 safe 替换项,合并后取 top-k。整体复杂度由排序主导,为 O(|I|log|I|);λ̂ 可预计算缓存。Remove 策略为去掉替换(经典纯过滤),Replace 为本文方法。

## 结果

数据集:[[kuairand]],聚焦被至少两个用户看过两次的视频,得 5657 用户、117695 unique items、>300 万 interactions;10-core 设定,train/val/test = 70/15/15,验证集兼作校准集。指标:Recall@k、nDCG@k(k=20),以及经验风险 R_H。Ranker 用四个图/transformer 模型:[[lightgcn]] 系的 LightGCL、GFormer(unsigned),以及 SiReN、SIGFormer(sign-aware);re-ranking 用 NCF。

- **RQ1 & RQ2 风险被可靠控制**:对任意目标削减比例 α,测试集经验削减≥目标(所有点落在对角线上或下方,Fig.3c),确认 Algorithm 1 可靠 enforce 风险控制;Remove 策略往往超额削减(移除项多于必要)。
- **性能-安全权衡**:Remove 随削减目标增大使 nDCG 急剧下降(候选池收缩);Replace 因重新引入旧项保留更高 nDCG(因不对重复项重新打分、复用原 watch-time,仍有部分下降)。两策略的 Recall 都下降。当 α=0(完全移除 unwanted)时唯一选择是替换/移除全部项,印证 Proposition 2。
- **RQ3 打分函数影响替换量**:sign-aware 模型(SiReN、SIGFormer)在同等风险削减下需替换更多项(在 75% 削减时 previously-seen 占比接近 75-100%),因 Kuaishou 负反馈稀疏使其嵌入学习困难、不确定性更高;unsigned 的 LightGCL、GFormer 改动更少、推荐集更大,故后续实验选 LightGCL。
- **RQ4 β 的权衡**:不过滤(None)时风险控制失效(部分旧项二次被举报,呈现 calibration/test 间的 distribution shift);按 watch-time 阈值 β 过滤可恢复风险控制,但 β 越严格候选池越小,行为趋近 Remove——揭示"替换项安全性 vs 推荐集大小"的权衡。
- **RQ5 高/低举报用户偏置**:按 H_X 把用户分为 low-reporting(<0.1)与 high-reporting(≥0.1);low-reporting 用户在较低 α 下削减更多,说明 high-reporting 用户不成比例地主导全局阈值 λ 的校准,可能导致对所有人都过度保守。
- **局限**:全局阈值对不同用户组影响不均(可考虑 group-balanced 或单用户校准);Eq.5 的风险函数不考虑排序位置、对每项等权;Theorem 1 仅为 in-expectation 保证;实验仅依赖 KuaiRand 单一数据集(目前唯一含真实 disaggregated 反馈 + watch-time target 的公开集),外部效度受限。作者指出 EU Digital Services Act 第 40 条对 vetted researcher 的数据访问或有助于未来验证。

被 RecSys 2025(第 19 届 ACM Conference on Recommender Systems)接收,代码开源(github.com/geektoni/mitigating-harm-recsys)。

## 在本 wiki 中的位置

本文把 [[conformal-risk-control]] 这一 distribution-free 的统计工具引入 [[recommender-systems|recommender-system]] 的内容安全治理,与 wiki 中关注 [[debiasing]]、[[filter-bubble]]、[[recommendation-diversity]] 等推荐负面外部性的工作相承接;它使用的 [[kuairand]]/[[kuaishou]] 数据与 [[watch-time]]、negative feedback 信号,与本 wiki 多篇 RL/causal recsys 论文共享同一实证基础。与那些靠重训练 ranker 或学策略来缓解不良内容的方法不同,本文走 post-hoc、model-agnostic、带可证明保证的路线,属于推荐系统 [[ai-safety]] 与 trustworthy recommendation 方向。
