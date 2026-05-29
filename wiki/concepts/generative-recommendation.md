---
type: concept
subtype: method
tags: [recommender-system, generative-model, semantic-id, sequential-recommendation, scaling-law]
created: 2026-05-29
updated: 2026-05-29
sources: 7
---

# 生成式推荐 (Generative Recommendation / GR)

生成式推荐是一类把推荐重构为序列生成问题的范式:在用户行为序列上直接自回归生成下一个 item 的 ID(或 [[semantic-id|semantic ID]]、semantic codes),取代传统"召回-排序"判别式打分流水线。

## 概述

传统 [[recommender-systems|recommender-system]] 以判别式建模为主——对候选 item 逐一打分再排序。生成式推荐则借鉴 [[large-language-models|LLM]] 的 next-token 思路,把 item 序列化为 token,用自回归([[transformer|Transformer]] / decoder-only)或扩散等生成模型直接"生成"推荐结果。其效果高度依赖 item tokenization 质量(如基于 [[rq-vae|RQ-VAE]] / [[vector-quantization|VQ]] 的 [[semantic-id|semantic ID]]),并被观察到具有类 LLM 的 [[scaling-law]] 效应,因此成为工业推荐(召回、排序、广告)正在迁移的主流方向之一。

## 在本 wiki 中的出现

- [[2025-hid-vae-interpretable-generative-recommendation]]:把 GR 定义为"端到端自回归 item ID 生成",指出其效果高度依赖 [[semantic-id|semantic ID]];用层次监督 + uniqueness loss 改进 [[rq-vae|RQ-VAE]] 量化,消除 ID 碰撞并赋予可解释的类别路径,提升 GR 的精度与多样性。
- [[2025-flexcode-dual-codebook-generative-recommendation]]:面向 GR 的双 codebook 表示学习,把 item 拆成协同 codebook 与语义 codebook,用 popularity-aware 的 [[mixture-of-experts|MoE]] 路由在固定 token 预算内为 head/tail item 自适应分配容量,缓解单一 codebook 的表示纠缠与长尾问题。
- [[2026-tencent-advertising-algorithm-challenge-2025]]:把"全模态 GR"作为竞赛主题,指出工业推荐正从判别式转向直接在行为序列上运行的 GR;发布 TencentGR-1M/10M 大规模多模态广告数据集与 next-token-prediction 基线,填补工业广告 GR 公共基准的空白。
- [[2024-large-recommendation-models-scaling]]:以 Meta 的生成式推荐模型 [[hstu|HSTU]] 为代表,系统验证 large recommendation model 的 [[scaling-law]] 是否跨 backbone 成立、来自哪些组件,确立 GR 作为推荐侧"可 scale 范式"的实证基础。
- [[2025-fuxi-gamma-efficient-sequential-recommendation]]:把 GR / 自回归 [[sequential-recommendation]]([[hstu|HSTU]]、FuXi 系列)的效率瓶颈作为靶子,用指数幂时间编码器与对角稀疏位置机制,在保持推荐质量的同时大幅加速训练与推理。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:把 [[decision-transformer]] 作为 GR 的一种 return-conditioned 实现引入工业推荐,通过 Temporal Advantage 信号与对比式状态抽象改进其轨迹拼接与高维状态问题,并在 [[kuaishou]] 直播推荐上线。
- [[2026-diffusion-models-in-recommendation-survey]]:在扩散+推荐综述中区分"data augmentation"与"direct generative recommendation"两种范式,把扩散模型作为 GR 的核心推荐器(去噪交互向量/嵌入再排序),代表 GR 的非自回归生成分支。

## 相关

- [[semantic-id]] / [[rq-vae]] / [[vector-quantization]]:GR 的 item tokenization 基础
- [[sequential-recommendation]] / [[recommender-systems]] / [[llm-for-recommendation]]:GR 所属的更大方法谱系
- [[scaling-law]] / [[large-language-models]]:GR 借鉴 LLM 的 next-token 与 scaling 思路
- [[hstu]] / [[tiger]] / [[vq-rec]] / [[sasrec]] / [[decision-transformer]]:GR 的代表性模型与基线
- [[diffusion-models]] / [[dreamrec]]:GR 的扩散生成分支
- [[hierarchical-representation]] / [[disentangled-representation-learning]]:改进 GR token 质量的表示学习方向
- [[benchmark]] / [[tencent]] / [[qwen]]:GR 的工业基准与实现
