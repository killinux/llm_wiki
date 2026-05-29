---
type: source
subtype: paper
tags: [sequential-recommendation, mamba, state-space-model, state-space-duality, time-awareness, recommender-system]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2409.16182
raw: raw/2409.16182.pdf
authors: [Hao Fan, Mengyi Zhu, Yanrong Hu, Hailin Feng, Zhijie He, Hongjiu Liu, Qingyang Liu]
year: 2024
---

# TiM4Rec: An Efficient Sequential Recommendation Model Based on Time-Aware Structured State Space Duality Model

TiM4Rec 把"时间感知增强"首次引入 [[state-space-duality]](SSD/Mamba2)架构,用一个 Time-aware Structured Masked Matrix 在保持线性复杂度的同时,弥补 SSD 在低维序列推荐场景下相对 SSM 的性能下降。

## 问题

序列推荐(Sequential Recommendation)的建模范式正从 [[transformer]] 转向 [[mamba]]。Mamba 有两代:基于 SSM 的 Mamba1(对应 [[recmamba]]/[[mamba]] 系列里的 Mamba4Rec)与基于 [[state-space-duality]](SSD,即 Mamba2)的 SSD4Rec。SSD 相比 SSM 计算效率更高,但在**低维**场景下性能明显退化——而纯 ID 的序列推荐恰恰更适合在低维(论文用 64 维)建模,这就构成核心矛盾。

作者分析其根源:SSM 的掩码矩阵对单个 item 做点对点(point-to-point)掩码($\hat E_i = A_{p:q}^\times \cdot E_i$,系数为矩阵),而 SSD 通过把状态转移矩阵 $A$ 标量化(scalarization)换取高效矩阵乘法,掩码系数退化为标量($A_{p:q}\in\mathbb R^1$),在低维下对 embedding 的精细过滤能力减弱,因此 SSD 行为更接近 [[transformer]] 的全局掩码而非 SSM。

时间感知(time-aware)方法常被用来缓解性能损失,但既有方法(如 [[sasrec]] 路线上的 TiSASRec)有两大障碍:Challenge I 与 SSD 不兼容(SSD 计算核没有显式的 attention score matrix);Challenge II 计算低效(需要扩展时间差矩阵维度,把复杂度推回 $O(T^2N)$)。

## 方法

整体框架(Fig. 2)是多层 Time-aware SSD Layer 堆叠,每层含一个 Time-aware SSD Block + FFN。

- **数据预处理**:ID embedding table $\mathbb E$ + dropout + layer normalization;交互时间戳序列 $\mathcal T$ 通过位移相减得到时间差序列 $\mathcal D=\{d_0,\dots,d_{T-1}\}$($d_0=0$)。
- **Time-aware Structured Masked Matrix(核心贡献)**:把时间差信息直接注入 SSD 的 1-Semi-Separable(1-SS)掩码矩阵 $L$ 的标量项,而不破坏其 1-SS 结构。做法是只取相对时间差矩阵 $\hat{\mathcal D}$ 的次对角线元素构造 $\mathcal D$,再让 $\hat A_i=d_i\cdot a_i$ 进入掩码,通过段累积(segment accumulation)保持 SSD 风格的高效矩阵乘法。这是首个为 Mamba 线性复杂度量身定制的时间感知增强方法。
- **Time-aware SSD Block**:对时间差向量 $\mathcal D$ 先做 time-varying 变换(两层带 sigmoid 的线性变换)再做 causal convolution 增强;离散化采用 $\overline A\approx\Delta A$、$\overline B\approx\Delta B$ 的近似(沿用 Mamba2/SSD 实践)。
- **Prediction Layer**:取特征序列最后一个元素作为兴趣表示 $p$,与全部 item embedding 点积后 Softmax,用 Cross Entropy 训练。

复杂度:SASRec 为 $O(T^2N)$,TiSASRec 在此之上额外 $O(T^2N)$;Mamba4Rec/SSD4Rec 为 $O(TN^2)$;**TiM4Rec 仅在 SSD 基础上增加 $O(T)$**,且时间感知掩码全靠标量计算,不会在高维场景下放大开销。

## 结果

数据集(Table 2):MovieLens-1M(ML-1M,6,040 用户 / 999,611 交互)、Amazon-Beauty(22,363 用户 / 198,502 交互)、KuaiRand(23,951 用户 / 1,134,420 交互)。指标为 HR/Recall@K、[[ndcg]]@K、MRR@K(K=10/20/50),模型维度统一 64。

主结果(Table 3),TiM4Rec 在三个数据集上多数指标取得最优或次优:

- **ML-1M**:R@10 0.3310(对 SSD4Rec* 提升 +3.47%),N@10 0.1932(+4.94%),M@10 0.1512(+6.11%)。
- **Amazon-Beauty**:R@10 0.0854(+5.96% vs SSD4Rec*),N@10 0.0446(+5.44%)。
- **KuaiRand**:R@10 0.1109(+5.12%),N@10 0.0611(+3.91%)。

维度对比(Table 4,ML-1M):64D 下 Mamba4Rec(SSM)优于 SSD4Rec;256D 下 SSD4Rec 反超 Mamba4Rec——印证 SSD 擅长高维、SSM 擅长低维的判断。TiM4Rec 在 64D(R@10 0.3310)和 256D(R@10 0.3270)均优于两者,既补齐了 SSD 的低维短板,又保留了高维优势。

效率(Table 5,单张 RTX 3090,ML-1M):TiM4Rec 训练 83.57s / 推理 0.21s,远快于 SASRec(207.42s/0.81s)与 TiSASRec(1149.57s/1.89s),与 SSD4Rec*(74.43s/0.18s)接近;不同序列长度下保持线性、无退化。

消融(Table 6):去掉 time-aware(w/o Time)和去掉 FFN(w/o FFN)均使指标下降,验证时间感知算法与 FFN 特征映射的有效性;层数对比中 ML-1M 用 3 层最优。代码开源:https://github.com/AlwaysFHao/TiM4Rec。

## 在本 wiki 中的位置

本文属于 [[mamba]]/[[state-space-model]] 在 [[recommender-systems|recommender-system]] 领域的应用分支,具体面向 [[sequential-recommendation]]。它与 [[recmamba]] 同属 Mamba-for-RecSys 谱系,但聚焦 [[state-space-duality]](Mamba2)架构的低维退化问题,并把 [[transformer]] 路线上的时间感知思想(TiSASRec,基于 [[sasrec]])迁移到 SSD。可与基于注意力的 [[sasrec]]、基于 RNN 的 [[gru4rec]]、以及 [[ndcg]] 等评测指标交叉参考。
