---
type: source
subtype: paper
tags: [recommender-system, sequential-recommendation, ctr, linear-attention, user-simulation, scaling-law, industrial-scale, meta]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.22049
raw: raw/2510.22049.pdf
authors: [Zhimin Chen, Chenyu Zhao, Ka Chun Mo, Yunjiang Jiang, Jane H. Lee, Khushhall Chandra Mahajan, Ning Jiang, Kai Ren, Jinhui Li, Wen-Yun Yang]
year: 2026
---

VISTA 是 [[meta]] 提出的一个两阶段建模框架,通过把超长用户交互历史(UIH)压缩成几百个 summarization embedding 并缓存,使下游推荐模型能利用百万级的终身用户历史,同时保持训练与推理成本固定。

## 问题

工业级 [[recommender-system]] 依赖用户交互历史序列来提升性能。把历史扩展到超长(10k 到 100k 甚至百万级 item)通常能提升模型效果,但在工业系统中带来严重的延迟、QPS(每秒查询数)和 GPU 成本问题。

现有两类 [[sequential-recommendation]] 方法各有局限:

- 全序列建模(如 HSTU,见 [[large-language-models]] 风格的序列转导)有 $O(N^2)$ 计算代价,工业系统每天需训练 $O(10B)$ 到 $O(100B)$ 样本并有严格延迟上限,因此难以广泛采用。
- target-specific 序列采样(SIM、TWIN、TWIN V2)存在两个问题:(1)截断子序列与全序列之间的 attention 差距;(2)推理成本随候选数量线性增长,因为每个候选对应独立的 target-specific 序列。

## 方法

VISTA(VIrtual Sequential Target Attention)把传统 target attention 拆成两阶段(见论文 Figure 1):(1)把用户历史摘要成几百个 token;(2)候选 item 只对这些 token 做 attention。

核心组件:

- **UIH 序列摘要(仅训练时)**:用一组随机初始化、跨用户共享的 virtual seed embedding 作为 query,对超长 UIH 序列做 self-attention,输出 summarization embedding,可解释为个性化用户 embedding。PCA 可视化显示不同国家用户的摘要 embedding 自然分离。
- **Quasi-linear Attention(QLA)**:在标准 [[linear-attention]]([[katharopoulos-et-al-2020]] 把 $O(N^2)$ 降到 $O(N)$)的基础上,引入非线性以提升表达力。包含 QLU(Quasi Linear Unit,用 SiLU 非线性建模 Q/K/V 交互)与 SGLU(沿用 TransNormerLLM 的门控)。同时严格保证候选之间不能互相 attention(否则会因推理时 logged candidate 只是候选子集而造成 label leakage)。公式去掉了 RowNormalize(类似 Lightning Attention),并为 target 加入对自身的 attention 项 $\Delta$。论文用 Triton 实现并在 Appendix 推导梯度。
- **生成式序列重建损失(generative reconstruction loss)**:用 causal transformer decoder(去掉 softmax 层)从 seed embedding 和前 $i-1$ 个 UIH item 重建第 $i$ 个 item,损失 $L_{reconstruct}=\sum \|v_i - u_{i+1}\|_2^2$。causal 结构保证无信息泄漏,迫使 seed embedding 最大化保留历史信息。思想源自 VAE([[variational-autoencoder]])。
- **target-aware attention**:第二阶段对紧凑摘要序列用标准 $O(N^2)$ transformer block。

**embedding 交付系统**:摘要 embedding 经量化后导出到 $O(100)$ TB 到 $O(1)$ PB 的 KV 缓存,通过 Kafka 消息队列 + Hive 持久化,跨地域复制为内存 KV store。推理时直接从缓存取回并反量化,绕过昂贵的摘要阶段。摘要 embedding 每 2 小时更新一次,A/B 验证与实时使用摘要模块性能相当。

## 结果

**公开数据集(Table 1/2)**:在 Amazon-Electronics(平均序列 8.93)、KuaiRand-1K(平均 225.20,见 [[kuairand]])、Simplified Prod(1528.18,max 2000)、Industrial-Scale(平均 7000,max 16000)上评测,指标用 normalized entropy(NE)和 AUC,baseline 包括 [[din]]、TTSN、MHA、[[sasrec]]、[[hstu]]。

- Amazon:VISTA-w/-QLA 取得 AUC 0.886、NE 0.621,优于次优模型(p<0.001)。
- KuaiRand:VISTA AUC 0.744、NE 0.863,与 HSTU/MHA 接近,略优。
- Minimal Production(长序列):VISTA 与 HSTU 表现最好,NE 1.038。
- 消融:QLA 显著降低单 epoch 训练/评测时间(Figure 7),AUC/NE 差异很小;增加 seed 数量提升性能(scaling law,Figure 8),但增加存储成本。

**工业级离线(Table 3)**:VISTA 相比 HSTU baseline,在主消费任务 C-Task 上 Training NE -0.47%、Eval NE -0.40%,各 engagement 任务(E1/E2/E3-Task)均有改进。去掉重建损失(VISTA-w/o-Recon)效果变差。Table 4 显示带 QLA 后可扩展到 5 层、16,000 序列长度,QPS +5%,Eval NE -0.13%。

**在线 A/B(15 天,5% 流量,视频推荐系统)**:主消费任务 C-Task +0.5%,在线 onboarding 指标 O1-Task +0.2%、O2-Task +0.04%。**推理 GPU 资源减少 94%**(通过缓存和服务 embedding,而非每次请求重算)。

## 在本 wiki 中的位置

VISTA 属于工业级 [[sequential-recommendation]] 与 [[recommender-system]] 的 long-term 用户行为建模方向,直接对标全序列方法 [[hstu]] 和 target-specific 方法 SIM/TWIN。它把 [[linear-attention]] / [[katharopoulos-et-al-2020]] 的思路与门控非线性结合成 QLA,并借鉴 [[variational-autoencoder]] 的重建思想做摘要 token 的信息保留。与 [[sasrec]]、[[din]] 等经典模型相比,VISTA 的核心创新在于训练/推理解耦的两阶段缓存设计。出自 [[meta]],已部署于服务数十亿用户的工业推荐平台。
