---
type: source
subtype: paper
tags: [recommender-system, feature-interaction, ranking-model, multi-task-learning, scaling-law, cross-attention, ctr]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.11565
raw: raw/2508.11565.pdf
authors: [Kaiyuan Li, Yongxiang Tang, Wenzheng Shu, Yanxiang Zeng, Chao Wang, Yanhua Cheng, Xialong Liu, Peng Jiang]
year: 2026
---

INFNet (Information Flow Network) 用一组 hub tokens 中介的 "aggregate-and-broadcast"(聚合-广播)机制,把推荐排序模型中的特征交互从二次复杂度降到关于输入 token 数的线性复杂度,同时保持 width-preserving 的堆叠结构,实现可扩展、task-aware 的特征交互。

## 问题

大规模 [[recommender-system]] 的排序模型中,[[feature-interaction]] 既要表达力强又要可扩展,二者难以兼得。Exhaustive 的 all-to-all 成对交互(如 AutoInt、HSTU)信息连通性强但代价是关于 token/feature 数量的二次复杂度,在线服务延迟约束(常 <30ms)下难以承受数百特征字段与多条行为序列。轻量化方案虽高效,却存在两个常见瓶颈:

- Early aggregation(早期聚合):对行为序列做 Sum-Pooling 或 target-attention 提前压缩,损失细粒度 item-level 信号,深层难以复用 item 级细节;
- Late fusion(晚期融合):task 信号只在最后输出阶段注入(late task fusion),交互过程 task-agnostic,限制了多目标场景下的专业化能力。

## 方法

INFNet 把所有输入显式组织为三组 token:Categorical Features、Behavior Sequences、Task Identifiers。每个 categorical 特征当作一个 token,行为历史中每个 item 当作一个 sequence token(保留 item 粒度,避免预压缩),每个优化目标当作一个 task token。为协调计算代价,为每组分配少量 **hub tokens** 作为通信枢纽。

Group-wise Tokenization & Hub 初始化(三种策略):
- Categorical:对 dense 特征做 logarithmic/quantile binning 离散化后嵌入;通过 MLP 投影(Flatten 后)生成 n_c 个虚拟 hub(压缩策略),语义锚定全局共现模式;
- Sequence:每个 behavior item 嵌入加入可学习绝对位置 p_t 与相对时间间隔 r_t;对每种 behavior type 用 type-specific MLP 投影后平均,得到 "Interest Prototype" hub(每类一个);
- Task:采用 shared-specific augmentation,将 specific task tokens 与额外可学习的 shared hubs 拼接,兼顾任务特定需求与通用知识。

核心 INFNet Block 通过对称的两阶段 aggregate-and-broadcast 机制:
- Phase 1 Multi-View Global Aggregation:hub tokens 作为 query,通过 [[cross-attention]] 从 self-view(本组)、temporal-view(序列)、goal-view(task)三个来源各自检索上下文(Z_C, Z_S, Z_T),concat 后经线性投影融合并加残差、LN 更新 hub。由于 query 数限定为紧凑的 hub 集合(N_hub << N_in),复杂度从 O(N_in^2 d) 降为 O(N_hub N_in d),即关于输入线性。
- Phase 2 Global-to-Local Affine Broadcast:提出 Broadcast Gated Unit (BGU),借鉴 FiLM 思想,将更新后的 hub flatten 投影生成 scaling 向量 α 与 shifting 向量 β,对组内每个原始 token 做 token-wise 仿射调制 BGU(x) = x ⊙ σ(α) + β,把全局上下文广播回细粒度局部特征;再经残差+LN 更新原始 token,保持 width-preserving,可直接堆叠 L 层。

多任务优化:堆叠 L 个 block 后,task-specific 表示经 MLP + sigmoid 输出各任务预测,端到端用加权 binary cross-entropy 损失训练(λ_i 平衡各目标)。

## 结果

数据集:公开 [[kuairand]](27K users / 32M items / 322M interactions / 89 categorical fields / 28 sequence fields / 3 tasks: Click/Like/Long-view)与一个工业短视频广告数据集(>10M users / >1B interactions / >100 fields / 5 tasks: Click/Play3s/Play5s/PlayEnd/Follow)。指标为 AUC 与 GAUC。基线 11 个,分四类:Foundations([[deepfm]]/[[dcn-v2]]/[[autoint]])、Sequence([[din]]/BST/[[hstu]])、Efficient(WuKong/[[rankmixer]]/[[onetrans]])、Composite(RM+PLE / OT+PLE)。

- Table 3 主结果:INFNet 在两数据集所有任务上 AUC/GAUC 均为 SOTA,且 Params/FLOPs 显著更低。KuaiRand 上 INFNet 仅 1.6M params / 3.24G FLOPs;相比最强基线 AUC 提升 Click +0.66%、Like +0.79%、Long-View +0.55%。工业数据集上(100M params / 202G FLOPs)Click AUC 提升 +0.52%,五目标一致正向(Play3s +0.92%、Play5s +1.06%、PlayEnd +0.70%、Follow +0.31%);Click AUC 绝对提升约 0.005,在已高度优化的工业系统中 five-mille 级提升被视为重大突破。
- 消融(RQ2,工业数据集 Avg AUC):w/o Hubs(改为 all-to-all attention)显著退化;w/o Task(task-blind Shared-Bottom)证明显式 task 引导是迁移的前提;w/o Agg(禁用 Phase 1,退化为 Late Fusion)下降最明显;w/o B'cast(禁用 Phase 2,Latent-Only)亦劣于完整模型。微观:MLP 投影 hub 初始化(0.9134)优于 Random(0.9115)/Mean Pooling(0.9124);Concat-Linear fusion、Hybrid task hub、Affine BGU(0.9134)分别优于各自简化变体。
- 超参敏感性:categorical hubs n_c 在 32 达峰(默认取 16);shared task hubs n_s 在 4 达峰。
- 可扩展性(RQ3):INFNet 的 scaling 斜率显著陡于 WuKong/OT+PLE 等高效基线,FLOPs 转化为预测力的效率更高;选 embedding 维度 64、4 层堆叠(100M params)作为容量与延迟的平衡。w/o Task 变体随 FLOPs 增大与全模型差距扩大,w/o Hubs 几乎平坦,印证 hub 中介机制是信号保真与参数效率的根本驱动。
- 在线 A/B(RQ4):某服务十亿级请求/天的广告平台,相对生产基线(约 OneTrans+PLE)一个月 A/B,营收 +1.587%(REV +1.59%)、CTR +1.155%(+1.16%),留存信号 P3s +0.11%、P5s +0.32%、PEnd +0.35% 均正向,延迟反而从 18.28ms 降至 18.17ms。

## 在本 wiki 中的位置

本文属于工业级 [[recommender-system]] 的 [[feature-interaction]] 与排序模型方向,来自 [[kuaishou]]。它与高效交互架构 [[rankmixer]]、[[onetrans]]、序列建模 [[hstu]]/[[din]] 以及 [[multi-task-learning]] 路线(PLE/[[mmoe]])构成同一谱系,并延续推荐 [[scaling-law]] 的讨论。核心技术上用 [[cross-attention]] 实现 hub 聚合、用类 FiLM 仿射门控(BGU)做广播,数据上使用公开基准 [[kuairand]]。
