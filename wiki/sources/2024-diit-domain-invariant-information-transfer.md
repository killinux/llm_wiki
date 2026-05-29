---
type: source
subtype: paper
tags: [recommender-system, cross-domain-recommendation, knowledge-distillation, adversarial-learning, incremental-learning, ctr]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.10835
raw: raw/2410.10835.pdf
authors: [Heyuan Huang, Xingyu Lou, Chaochao Chen, Pengxiang Cheng, Yue Xin, Chengwei He, Xiang Liu, Jun Wang]
year: 2024
---

# DIIT: A Domain-Invariant Information Transfer Method for Industrial Cross-Domain Recommendation

DIIT 面向**工业级增量训练**场景下的跨域推荐(Cross-Domain Recommendation, CDR),用"双抽取器 + 迁移器"把多个 source domain 模型的 domain-invariant 信息蒸馏进 target domain 模型,并做到**推理阶段只需 target 模型**,在 OPPO 生产数据集与 Taobao、[[kuairand]] 上同时提升效果与效率。

## 问题

大型商业平台通常包含多个域(domain),用户因不同目的被划分到不同域,造成域间数据分布漂移。已有 CDR 方法多建立在"用户兴趣短期内基本不变"的**理想静态假设**上,直接搬到工业 [[recommender-systems|recommender-system]] 环境(各域各自维护模型、以 incremental learning 增量更新)会同时损害效果与效率。作者归纳出两个挑战:

- **CH1(效果)**:域内信息可分为 domain-specific(只利于本域)与 domain-invariant(利于多域)。多数方法依赖域间 overlapped samples 作"桥"来传递不变信息,但工业环境因 source domain 数量大、隐私保护等原因难以获得充分重叠样本,严重伤害效果。
- **CH2(效率)**:各域模型以增量模式训练,既有针对工业环境的方法(如 KEEP、CTNet)要么需要额外计算/存储资源,要么推理时还得保留 source domain 模型作外部信息,导致效率低下。

## 方法

DIIT 是端到端、即插即用(plug-and-play)的框架,含三个模块:

- **Warm Start(热启动)**:模拟工业 RS 环境——每个域独立维护模型并以增量模式训练;target 域用上一周期 $t-1$ 模型 warm-start 初始化当前周期 $t$ 模型,各 source 域结构可不同。
- **Domain-invariant Information Extractors(双抽取器,对应 CH1)**:
  - *域级(domain level)*:用 target 模型表示通过一个两层 MLP + softmax 的 **gating network** 自适应聚合多个 source 模型的表示 $\mathbf{e}^t_s$ 与 logits $\mathbf{Z}^t_s$(式 1-2),训练耗时不随 source 域数量显著增长。
  - *表示级(representation level)*:用 **adversarial network**(mapper + discriminator)对齐 source 与 target 的表示分布。判别器判断样本来自哪个域,mapper 则去混淆它,构成 min-max 博弈($L_{adv1}$ 训练判别器、$L_{adv2}$ 混淆判别器,采用类似梯度反转的交替优化),从而分离 domain-invariant 与 domain-specific 信息。这属于 [[adversarial-robustness]] 思路在迁移学习中的应用。
- **Domain-invariant Information Migrator(迁移器,对应 CH2)**:用 **multi-spot [[knowledge-distillation]]** 把不变信息传给 target 模型——中间层蒸馏用 MSE 对齐表示($L_{MSE}$,式 7),logit 层蒸馏用高温 softmax 软标签 + KL($L_{KL}$,式 8),合成 $L_{KD}$(式 9)。
- **优化与推理**:整体损失 $L_{total}$ 分两步(式 12):先优化判别器 $L_{adv1}$,再同时优化 $L_{CE}$(target 域 CTR 任务)、$L_{adv2}$、$L_{KD}$;$L_{KD}$ 的反传不影响 source 模型参数。借助 KD"推理只需 student 模型"的特性,**推理阶段只保留 target 模型**,显著提速。

## 结果

数据集为三个不同量级:OPPO **Production**(广告 CTR,约 7.4 亿样本,按 domain ID 分 10 域,选 3 域、最小者为 target)、**Taobao**(阿里展示广告 CTR,按 city_level 分域)、**KuaiRand**(快手随机推荐,按 tab 分 14 域)。指标用 **AUC** 与 **LogLoss**,backbone 默认 DNN。

- **总体效果(RQ1,Table 2)**:DIIT 在三数据集多数场景优于单域(DNN、DCN、W&D)与跨域(DANN、HAMUR、CTNet)基线。Production 上 AUC 0.7526(相对 DNN +0.71%)、LogLoss 0.0743;Taobao AUC 0.5994(+0.25%);KuaiRand AUC 0.6826(+1.78%),为该集最佳。注:Taobao 上 HAMUR 的 AUC 0.6060 更高,但其依赖理想静态假设,不适用于工业增量环境。
- **效率(RQ1,Table 3)**:相比 CTNet,DIIT 在生产数据集采样测试上的推理耗时从 191s 降到 159s,**减少约 16.75%**;source 域越多,优势越大。
- **兼容性(RQ2,Table 4)**:作为可插拔组件,DNN/DCN/W&D 三种 backbone 加上 DIIT 均有 AUC 提升(如 DCN+DIIT 在 Production +0.44%)。
- **消融(RQ3,Table 5)**:去掉任一组件(Only A / Only C 单源、w/o Gating、w/o Adversarial、w/o Middle、w/o Logit)AUC 均低于完整 DIIT 的 0.7526,验证 gating 聚合、对抗对齐、multi-spot KD 各自有效。t-SNE(Figure 3)显示抽取器作用后 source 与 target 表示更难区分,即分布被对齐。
- **超参与探索(RQ3/RQ4)**:温度 $\tau$、$\alpha$、$\beta_1$、$\beta_2$ 均存在最优区间;不同周期(period 4 vs 7)插入 DIIT 多数能带来正收益,过早插入不一定更好(可能引入过多旧 source 信息淹没最新 target 的 domain-specific 信息)。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] / cross-domain recommendation 方向,与 wiki 中 [[ctr]] 预估、工业 [[recommender-systems]] 落地相关。其技术栈把 [[knowledge-distillation]]、adversarial 域对齐与 incremental learning 结合,可与 [[kuairand]] 等推荐数据集条目互相参照;作者来自 [[oppo]] 与 [[zhejiang-university]](Chaochao Chen)。
