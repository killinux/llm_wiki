---
type: source
subtype: paper
tags:
  - watch-time-prediction
  - short-video-recommendation
  - generative-regression
  - sequence-generation
  - ordinal-regression
  - kuaishou
created: 2026-05-29
updated: 2026-05-29
arxiv: "2412.20211"
raw: raw/2412.20211.pdf
authors:
  - Hongxu Ma
  - Kai Tian
  - Tao Zhang
  - Xuefeng Zhang
  - Han Zhou
  - Chunjie Chen
  - Han Li
  - Jihong Guan
  - Shuigeng Zhou
year: 2024
---

# Generative Regression Based Watch Time Prediction for Short-Video Recommendation

提出 Generative Regression (GR) 框架,把短视频 [[watch-time|观看时长]]预测从 ordinal regression 重构为序列生成任务:用结构化离散化(structural discretization)构建词表并把每个 watch time 双射编码为 token 序列,由 encoder-decoder 自回归生成,辅以 curriculum learning + embedding mixup (CLEM) 缓解 teacher-forcing 的 exposure bias,在两个公开数据集和一个工业数据集及 [[kuaishou]] 线上 A/B 上均超过 SOTA。

## 问题

[[watch-time|Watch Time Prediction (WTP)]] 是短视频推荐中衡量用户参与度的核心任务。短视频以滚动模式自动播放,使 [[ctr|click-through rate]] 等传统指标失效,而 watch time 取值范围宽、呈长尾分布,本质上是回归问题。直接回归会有较大估计偏差;近期工作(如 [[cread|CREAD]]、TPM)把连续 watch time 转为 ordinal regression(一系列跨预定义时间区间 bucket 的二分类),但存在两个突出局限:

1. **离散化依赖 bucket 划分**:固定时间区间的强离散化使模型表现高度依赖区间切分方式,损失预测灵活性与精度;尾部 bucket span 过大,会在短 watch time 样本上放大误差。
2. **区间间依赖被低估**:不同区间的预测相互独立产生,未充分利用区间间的条件依赖,错失有效的 error correction 机会。

## 方法

受 [[large-language-models|LLM]] 语言建模成功的启发,提出通用回归范式 **Generative Regression (GR)**,将整段 watch time 预测分解为序列生成:每一步预测总时长的一部分,前一步输出作为下一步输入,构成条件、序列化的建模过程,目标是预测一串时间槽,其和即连续 watch time。

- **模型架构**:Transformer encoder-decoder。Encoder 用 FFN 抽取 user/item 特征得到固定隐表示 $h_i$;decoder 用标准 Transformer block(Masked MHA + Cross-Attention MHA + FFN)自回归预测 watch time,引入 `<SOS>`/`<EOS>`/`<PAD>` 特殊 token,具备输出 `<EOS>` 以灵活生成不同长度序列的能力(优于固定区间二分类)。
- **Vocabulary Construction(词表构建)**:每个 token 对应一个预定义时间槽。提出三原则——Completeness(几乎无损表示所有 watch time)、Balance(token 频率尽量均匀防类别不均)、Adaptability。用 **dynamic quantile adjustment**(Algorithm 1)动态分位数构建词表:从高起始分位 $q_{start}$ 起,按 decay rate $\alpha$ 自适应衰减到终止分位 $q_{end}$,快速削减尾部值、降低更新值方差,缓解长尾分布。
- **Label Encoding(标签编码)**:把每个 watch time 双射映射为 token 序列,遵循 Correctness(可重构,误差 $\le 0.001 \cdot y_i$)、Minimal Sequence Length、Monotonicity(token 值非增,捕捉用户注意力衰减)三原则,采用贪心分解。
- **优化与推理**:训练用 cross-entropy loss + Huber loss 的复合损失($\mathcal{L} = \mathcal{L}_{ce} + \lambda \mathcal{L}_{huber}$),用 teacher forcing 提效。
- **CLEM(Curriculum Learning with Embedding Mixup)**:针对 teacher forcing 导致的 [[exposure-bias]],用分阶段 curriculum learning,以动态概率 $p$ 在 ground-truth token 与预测 token 间采样($p$ 从约 1 按非线性衰减下降),decoder 用 two forward passes 实现;再用 embedding mixup 把邻近 token 的 embedding 加权融合(利用 token 语义可加性),在更低算力下提升精度并保证训练-推理一致。

## 结果

在公开 **CIKM16**、**[[kuairec|KuaiRec]]** 两个 benchmark 和一个 [[kuaishou|Kuaishou]] 工业数据集(**Indust**,超 4 亿 DAU)上评测,指标为 MAE(越低越好)与 XAUC(越高越好)。

- **离线(Table 1)**:GR 在所有数据集均取得一致提升。CIKM16 上相对最优基线 MAE 降低 4.117%、XAUC 提升 1.917%;KuaiRec watch time 上相对次优方法 MAE 降低 3.356%、XAUC 提升 3.367%;watch ratio 上 MAE 降低 7.756%、XAUC 提升 2.033%;Indust 上相对 [[cread|CREAD]] MAE 相对下降 3.629%、XAUC 提升 1.001%。GR 绝对值如 KuaiRec watch time:MAE 3.196 / XAUC 0.614(CREAD 为 3.307 / 0.594)。
- **线上 A/B(Table 2)**:在 Kuaishou App 部署 6 天、覆盖超 2500 万用户。App Usage Time +0.112%(p=0.01)、Average App Usage Per User +0.087%、Video Consumption Time +0.129%(均显著);线上服务 QPS 仅下降 10.2%,ROI 达到全量部署门槛。
- **消融(RQ2-RQ4)**:GR 预测均值贴近 GT 均值且分布更平展多样;是唯一能准确预测接近 0s 的方法(得益于首步即可输出 `<EOS>`)。Dynamic quantile 词表优于 Manual/Binary(Table 3)。CLEM 中 embedding mixup 贡献更大:去掉它 XAUC 降 4.235%、MAE 升 4.853%(Table 4)。
- **LTV 任务(RQ5,Table 5)**:迁移到 Lifetime Value 预测,在 Criteo-SSC 与 Kaggle 上相对前 SOTA OptDist 取得 MAE 相对提升 17.66%、Spearman's ρ 提升 20.79%,验证 GR 作为通用回归方案的潜力。

## 在本 wiki 中的位置

本文属于[[recommender-system|推荐系统]]中 [[watch-time|watch time 预测]]方向,是把生成式/序列建模思想引入回归任务的代表作。它直接对话并改进既有 ordinal regression 路线 [[cread|CREAD]]、TPM,以及 debiasing 路线 [[duration-bias|duration bias]] 相关工作;方法上借鉴了 [[transformer|Transformer]] 自回归语言建模与 [[curriculum-learning]],并把 [[exposure-bias]] 缓解(teacher forcing / scheduled sampling 思路)迁移到推荐场景。其通用回归范式还连接到 [[ctr|CTR/转化预测]] 与 LTV 预测等任务。
