---
type: source
subtype: paper
tags: [generative-recommendation, semantic-id, recommender-system, codebook, mixture-of-experts, long-tail, cold-start]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2511.20673
raw: raw/2511.20673.pdf
authors: [Zheng Hui, Xiaokai Wei, Reza Shirkavand, Chen Wang, Weizhi Zhang, Alejandro Peláez, Michelle Gong]
year: 2025
---

FlexCode 是一个面向生成式推荐(generative recommendation)的双 codebook 表示学习框架,把 item 表示拆成协同(CF)codebook 与语义 codebook,并用 popularity-aware 的 MoE 路由在固定 token 预算内自适应分配容量,从而兼顾 head item 的记忆精度与 tail item 的语义泛化。

## 问题

现有 [[generative-recommendation]] 方法(基于 [[semantic-id]],如 [[tiger]]、VQ-Rec)普遍用**单一共享 codebook** 对所有 item 编码,作者指出这带来两个结构性缺陷:

1. **表示纠缠(representation entanglement)**:同一套 codeword 既要表达文本/视觉等模态语义,又要编码高阶共现结构,二者相互干扰,导致 token 既不语义纯净也不协同精确,引发表示坍缩([[dimensional-collapse]] 类问题)。
2. **静态容量分配(static capacity allocation)**:所有 item 分到相同数量、相同类型的 token,忽略了推荐数据的长尾特性。head item 有充足交互数据、受益于高容量协同表示;tail item 缺交互、更依赖语义证据(文本、属性、metadata)。统一处理会在 head 上过拟合、在 tail 上欠表达。

作者将其抽象为**自适应容量分配(adaptive capacity allocation)**问题:在固定 token 预算下,如何决定每个 item 把多少容量分给协同特异性、多少分给语义泛化。

## 方法

FlexCode(论文中也称 Dynamic Dual-Codebook Learning)由以下部分组成:

- **双 codebook 构造**:协同 codebook C_CF 用类 [[sasrec]] 架构得到上下文感知的协同 embedding;语义 codebook C_SEM 把 item 的 brand/price/category/title 等属性拼成文本,送入预训练文本 embedding 模型。两者各自用 [[rq-vae]](Residual Quantization VAE)离散化为 token 序列,损失为重构 + [[vector-quantization]] 损失。
- **Cross-Codebook Alignment (CCA)**:在两套 codebook 的**重构** embedding 上用 [[infonce]] 风格的 [[contrastive-learning]] 对齐到共享潜空间,既保证跨 codebook 一致性,又作为正则缓解 VQ codebook 坍缩。
- **Popularity-Aware Token Allocation (PATA)**:用轻量 [[mixture-of-experts]] 路由器(一个浅层 MLP)对每个 item 构造特征向量 x_i = [log(1+f_i), age, sparsity, uncertainty],输出协同/语义两路 logits,经温度 softmax 得分配比例 α_i。固定总预算 L_total 下软分配 token 数 L_CF = α_i·L_total,训练用 sigmoid 软 mask 保持可微,推理时四舍五入离散化。head item 路由向 CF、tail item 路由向语义。还引入分层 load-balancing 与局部平滑正则保证路由稳定。
- **自回归生成 (ARG)**:把用户历史 item 的组合 codebook 序列喂给自回归 Transformer,用标准 cross-entropy 预测下一 item 的 token。
- **总目标**:L_total = L_SCL + L_CCL + λ_CCA·L_CCA + λ_ARG·L_ARG + λ_lb·L_lb + λ_smooth·L_smooth,端到端联合训练。

直觉上 g(i)=1 退化为纯 CF tokenization,g(i)=0 退化为纯语义 tokenization,FlexCode 在两端之间平滑插值。

## 结果

数据集:[[amazon-reviews]] 的 Beauty(22,363 用户 / 12,101 item)、Sports and Outdoors(35,598 / 18,357),[[kuairand]]-1K(1,000 用户 / 3.6M item / 11M 交互),以及一个 tens-of-millions 用户、tens-of-thousands item 的工业自有数据集(约 1.5M+ 用户 / 1M+ item / 45M+ 交互)。评测用 leave-last-out、5-core 过滤,指标 Recall@K 与 [[ndcg]]@K(K∈{5,10})。

主结果(Table 1,全部 p<0.01 显著):

- FlexCode 在三个公开 benchmark 全部指标上超过 [[sasrec]]、S³-Rec、[[bert4rec]] 等 Item-ID 模型,以及 VQ-Rec、TIGER、[[lc-rec]]、COBRA、URL 等 Semantic-ID 模型。
- Beauty:R@10 0.0769 / N@10 0.0483(最强基线 URL 为 0.0736 / 0.0471)。
- Sports:R@10 0.0471,相对最强语义基线 URL 提升 **5.3%**。
- KuaiRand:N@10 **0.0632**,较 URL 提升 **8.0%**;R@10 0.0825。
- 工业数据集:相对 SASRec 基线,NDCG@10 提升 **13.2%**、HR@10 提升 **16.5%**;纯 CF 生成模型反而退化 5% 以上,统一模型 URL 仅提升约 4.9%。

消融与分析:

- **PATA 的贡献**:KuaiRand 上动态分配把 N@10 从固定 50/50 split 的 0.0562 提升到 0.0632(相对 +12.5%)。
- **head vs tail**(工业集,Figure 2b):baseline 存在权衡——CF-only 提升 head 但 tail 退化 5.5%,SID-only 提升 tail 5.7% 但 head 变差;FlexCode 同时取得 head +3.0%、tail **+11.3%** 的 N@10 提升。
- **结构消融**(Table 3,KuaiRand):仅用 CID(N@10 0.0372)或仅用 SID(0.0401)都显著下降;去掉 MoE gating 用固定 split 降到 0.0598;去掉 alignment loss 降到 0.0615;完整模型 0.0632。
- **token 预算敏感性**(Table 4):L∈{3,4,5,6} 下 FlexCode N@10 由 0.0632 升至 0.0693,始终领先 SID-only / Fix 变体,显示低预算下仍稳健。
- **超参敏感性**(Table 5):对 codebook 大小 K、维度 d、正则权重 λ_align/λ_smooth 在较宽范围内稳定,K 与 d 增大有轻微增益直至饱和。

## 在本 wiki 中的位置

本文属于 [[recommender-system]] 中 [[generative-recommendation]] / [[semantic-id]] 路线,直接对话 [[tiger]]、[[lc-rec]]、[[vq-rec]] 等单 codebook 方法,核心贡献是把 [[rq-vae]] 量化、[[mixture-of-experts]] 路由与 [[contrastive-learning]] 对齐组合成"双 codebook + popularity-aware 分配",针对 [[cold-start]] 与 [[popularity-bias]] / 长尾问题。与 [[cobra]] 等"协同+语义融合"工作思路相邻,可与 [[sasrec]]、[[bert4rec]]、[[sequential-recommendation]] 等序列推荐基线对照阅读。
