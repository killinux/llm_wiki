---
type: source
subtype: paper
tags:
  - recommender-system
  - two-tower
  - online-learning
  - knowledge-distillation
  - kuaishou
created: 2026-05-29
updated: 2026-05-29
arxiv: "2604.22761"
raw: raw/2604.22761.pdf
authors:
  - Lixiang Wang
  - Shaoyun Shi
  - Peng Wang
  - Wenjin Wu
  - Peng Jiang
year: 2026
---

# CS3:面向 two-tower 推荐的高效在线能力协同框架

CS3(Capability Synergy)是 [[kuaishou]] 提出的通用框架,通过 Cycle-Adaptive Structure、Cross-Tower Synchronization、Cascade-Model Sharing 三个模块,让轻量 [[two-tower]] 召回模型在线学习场景下感知自身、对侧塔与下游 cascade 模型的输出,从而提升模型容量、表征对齐和跨阶段一致性,线上广告收入最高提升 8.36%。

## 问题

在多阶段 [[recommender-system]] 中,早期 [[candidate-generation]] 阶段普遍采用轻量级 [[two-tower]] 模型(如 [[dssm]])以平衡效果与效率:用户塔、物品塔分别编码,用点积/余弦相似度计算相关性,物品向量可预计算缓存并用 [[faiss]] 高效检索。但这种解耦的双塔结构带来三类固有局限:

1. **Model Capacity(模型容量)**:每塔独立的简单结构限制表征能力,约束了对复杂用户-物品关系的建模。
2. **Representation Alignment(表征对齐)**:双塔在相似度计算前缺乏跨塔交互,仅靠最终 loss 难以对齐用户与物品的表征空间,在海量用户/物品和在线学习不断产生新数据的场景下尤为困难。
3. **Cross-Stage Consistency(跨阶段一致性)**:双塔在结构和容量上显著弱于下游 cascade [[learning-to-rank]] 模型(后者用 user-item cross features 和 target-aware attention),缺乏建模 user-item 交叉特征和用户行为的机制,削弱了检索与排序阶段的协同。

已有工作通过隐式跨塔交互或 [[knowledge-distillation]](从更强教师模型迁移知识)缓解这些问题,但往往未显式利用对侧塔/cascade 模型,且增加训练/推理开销,难以适配在线学习的高时效要求。

## 方法

CS3 兼容多种双塔结构,核心是让每塔"感知"三类信息源。包含三个模块(对应论文 Figure 2):

- **Cycle-Adaptive Structure(CAS)**:受 RecycleNet 与 [[diffusion-models]] 去噪思想启发,用循环结构替换单塔内的全连接层,实现塔内自修正与特征去噪。每个 cycle 含三步:pre-forward(标准 FC,得到 z_i)、adaptive reweighting(经 Sigmoid 得到重要度权重 e_i,缩放到 (0,2) 期望为 1,再逐元素相乘做去噪 x̃_i = x_i ⊙ 2e_i)、cycle-forward(用 x̃_i 重做前向)。多层堆叠 CAS 增强单塔表征鲁棒性与表达力。

- **Cross-Tower Synchronization(CTS)**:在塔间显式交换信息。引入 cross vectors c_u、c_v 存储所有用户/物品的正向表征;当交互 y=1 时,用对侧塔当前输出经 [[temporal-difference]] 式 EMA(exponential moving average)更新(α 平滑系数),把"对侧塔特征"注入本塔输入,显式对齐用户与物品表征空间,实时捕捉分布漂移。

- **Cascade-Model Sharing(CMS)**:把更强的下游 cascade rank 模型的中间输出(penultimate FC 层,记 h_uv)经 EMA(β 平滑系数)注入双塔,得到 cascade vectors s_u、s_v。与 CTS 只用正样本不同,CMS 同时利用正负样本表征,使双塔继承更强 cascade 模型的部分能力,增强跨阶段一致性。

**在线实现**:在大规模广告系统部署。用 Parameter Server(ParSvr)缓存 CTS 的 cross vectors(自定义梯度更新),用独立的 Embedding Server(EmbSvr,类似 Redis 但优化向量 QPS)缓存 CMS 的 cascade vectors(以 user_id/item_id 为 key,EMA 更新,p99 延迟 < 5ms)。CTS/CMS 仅引入两个额外输入特征,开销极小;CAS 增加单塔计算但因检索成本主要在向量相似度,CAS 仅应用于用户塔除输入层外的 FC 层,QPS 下降 < 1%。在线学习管线约 30 分钟完成一次模型同步。

## 结果

**离线实验**(三个公开数据集 [[taobaoad]]、[[kuairand]]、RecSys2017,5 个随机种子,指标 AUC↑/LogLoss↓):

- CS3 在 4 种双塔架构(DSSM、IntTower、IHM-DAT、transformer-based RCG)上均一致提升,且单独的 CAS/CTS/CMS 各自也有增益。
- 以 DSSM 为例:TaobaoAd AUC 0.6194→0.6855、KuaiRand AUC 0.6646→0.7484、RecSys2017 AUC 0.6855→0.8380,均带统计显著标记(p<0.05)。
- CS3 增强的双塔可媲美 DNN、BST、EulerNet 等排序模型(Table 4),同时保持双塔的效率。
- 鲁棒性:对输入注入 std=0.1 高斯噪声,DSSM+CAS 的 AUC 下降仅 0.051%(4.3%)而 DSSM 下降更大,体现 CAS 去噪能力。
- 冷启动:在交互 ≤3 的冷用户/冷物品上,DSSM+CS3 相对 DSSM,Cold-Users AUC 0.5333→0.6037(+13.2%)、Cold-Items AUC 0.5964→0.6408(+7.4%)。
- 参数研究:α、β(EMA 平滑系数)在一定范围内稳定,论文统一取 α=β=0.8。

**在线 A/B 实验**(广告系统,数亿用户,>7 天,10% 流量):

- Scenario A 逐步叠加:+CAS 收入 +1.677%、+CAS&CMS +7.880%、+CAS&CMS&CTS(完整 CS3) 收入 +8.356%、DAC +0.468%。
- 跨三场景:Revenue +8.356% / +1.366% / +2.177%,DAC(Daily Active Customers)+0.468% / +0.143% / +0.228%,QPS 仅下降约 -0.589% / -0.388% / -0.456%。
- Model Insights(RQ4):CS3 的 24 小时平均 recall loss 更低、与 cascade 模型的 Kendall Tau 一致性更高,t-SNE 可视化显示 CS3 增强的 DSSM 用户嵌入与正样本物品聚集更紧、负样本更远。模型最终全量上线替换 base。

## 在本 wiki 中的位置

本文属于工业级 [[recommender-system]] 中 [[candidate-generation]] / 召回阶段的 [[two-tower]] 模型优化脉络,与 [[dssm]]、[[learning-to-rank]]、[[matthew-effect]] 等召回排序议题相关。其用 [[knowledge-distillation]] 思路从 cascade 排序模型迁移能力的做法,以及借鉴 [[diffusion-models]] 去噪与 EMA([[temporal-difference]] 式更新)的技巧,可与 [[kuaishou]] 的其他推荐工作([[kuairand]]、[[recflow]] 等)以及 [[faiss]] 检索基础设施对照阅读。
