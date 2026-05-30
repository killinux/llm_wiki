---
type: topic
tags: [recommender-system, transformer, graph-neural-network, generative-recommendation, sequential-recommendation]
created: 2026-05-30
updated: 2026-05-30
sources: 22
---

# 推荐系统的架构演进:Transformer、图神经网络与生成式推荐 (RecSys Architectures)

> 一句话:推荐建模的骨架经历了三条主线的交汇——用 **[[attention]]/Transformer** 建模**行为序列**与**特征交互**,
> 用 **图神经网络 (GNN)** 建模**用户-物品交互图**,近年又转向 **decoder-only 生成式推荐**(语义 ID + 自回归生成),
> 并在工业落地中被**效率**(线性注意力、Mamba、历史压缩)反复重塑。综述见 [[2026-transformers-graph-recommender-survey]]。

概念枢纽:[[attention]]、[[embedding]]、[[sequential-recommendation]]、[[representation-learning]]。

---

## 一、序列推荐:从 RNN 到自注意力到生成式
| 阶段 | 代表 | 要点 |
|---|---|---|
| RNN | [[gru4rec]] | 会话序列的循环建模 |
| 自注意力 | [[bert4rec]](双向 Cloze)、SASRec | 用 [[attention]] 建模行为序列,捕捉长程依赖 |
| 生成式 / decoder-only | [[hstu]]、[[fuxi-alpha]] | 把推荐重构为**生成式序列转导**,有 scaling 效应 |
| 效率优化 | [[2025-fuxi-gamma-efficient-sequential-recommendation]] | Ebbinghaus 启发的指数幂时间编码 + 对角稀疏位置注意力,训练加速 **4.74×**、推理 **6.18×** |
| 线性/状态空间 | [[2026-fuxi-linear]]、[[2024-recmamba-lifelong-sequential-recommendation]]、[[2024-tim4rec-time-aware-mamba]] | [[linear-attention]]/[[mamba]] 把复杂度降到 O(N),服务长序列 |
| 终身历史 | [[2026-vista-virtual-sequential-target-attention]](Meta) | 把超长 UIH 压成几百个 summarization embedding 缓存,**百万级**历史而成本固定 |

## 二、特征交互 / CTR 架构
从 [[fm|FM]] → [[deepfm]](FM+DNN 共享 embedding)→ [[autoint]](用**多头自注意力**自动学高阶特征交互)→ [[dcn]] 系列;
[[dssm]] 双塔做召回。这条线把 [[attention]] 引入"特征"维度而非"序列"维度。

## 三、图神经网络 (GNN)
把用户-物品交互建成图,用消息传递学协同信号:
- [[lightgcn]](简化 GCN 的轻量协同过滤)是基线;
- [[2024-sigformer-sign-aware-graph-transformer]](SIGformer)—— **sign-aware 图 Transformer**,同时建模正/负反馈;
- 图 + 检索:[[2026-graphrag-irl]];图建模综述见 [[2026-transformers-graph-recommender-survey]]。

## 四、融合与生成式转向
- **Transformer × GNN 融合**:[[2026-transformers-graph-recommender-survey]] 系统梳理二者在推荐中的结合(序列依赖 × 图结构)。
- **生成式推荐 + 语义 ID**:用 [[rq-vae]] 把物品量化为 **semantic ID**,再 decoder-only 自回归生成——[[tiger]]、[[lc-rec]]、[[vq-rec]]、
  [[2025-hid-vae-interpretable-generative-recommendation]]、[[2025-flexcode-dual-codebook-generative-recommendation]];时长/回归也被重构为 token 生成([[2024-generative-regression-watch-time-prediction]])。
- **扩散模型**:[[2026-diffusion-models-in-recommendation-survey]]、[[2025-t2diff-two-tower-diffusion-matching]]、[[2025-energy-guided-diffusion-rl-recommendation]]。

## 五、工业落地的主旋律:效率与规模
- **长序列成本**:生成式架构([[hstu]])质量高但贵 → 线性注意力/Mamba/历史压缩(FuXi-γ、FuXi-Linear、VISTA)是必答题。
- **多任务/多场景融合**:架构需承载多目标([[multi-objective-optimization]])与多域([[multi-domain-recommendation]]),如 MoE 路线 [[2601-dsmoe-scenario-adaptive-moe-matching]]、[[2026-smes-scalable-multi-task-expert-sparsity]]。

## 六、开放问题
- **质量-效率前沿**:生成式/全注意力的质量 vs 线性/稀疏的成本,如何在工业 QPS 下取最优。
- **语义 ID 的质量与可识别性**:量化冲突、可解释性([[2025-hid-vae-interpretable-generative-recommendation]])。
- **图 × 序列 × 生成的统一**:三条线是否会收敛到单一生成式骨架。
- **scaling law 是否成立**:生成式推荐的 scaling 效应能否持续([[2024-large-recommendation-models-scaling]])。

## 相关概念页
[[attention]]、[[sequential-recommendation]]、[[graph-neural-network]]、[[generative-recommendation]]、[[semantic-id]]、
[[linear-attention]]、[[embedding]]、[[representation-learning]]、[[recommender-systems]]
