---
type: source
subtype: paper
tags:
  - sequential-recommendation
  - llm-for-recommendation
  - hallucination
  - retrieval-augmented-generation
  - recommender-system
created: 2026-05-29
updated: 2026-05-29
arxiv: 2511.20177
raw: raw/2511.20177.pdf
authors:
  - Tianjie Dai
  - Xu Chen
  - Yunmeng Shu
  - Jinsong Lan
  - Xiaoyong Zhu
  - Jiangchao Yao
  - Bo Zheng
year: 2025
---

# Enhancing Sequential Recommendation with World Knowledge from Large Language Models (GRASP)

GRASP 是一个可插拔框架,把 [[large-language-models]] 的世界知识引入 [[sequential-recommendation]],通过"生成增强检索 + 整体注意力增强"把 LLM 语义作为辅助输入(而非监督信号)融合,从而在抵抗 [[hallucination]] 噪声的同时提升推荐效果。

## 问题

传统基于协同过滤(ID embedding)的 [[sequential-recommendation]] 模型信号有限,过度强调高频交互、忽略用户跨品类的多样兴趣(例如买帐篷的用户实际还可能需要睡袋、炉具、照明)。近期工作(如 [[llm-esr]])用 LLM 生成的用户/物品语义特征作为监督信号来增强 SRS,但这些方法默认 LLM 输出正确,易受 [[hallucination]] 噪声影响。作者在工业数据集 Industry-100K 上抽样 500 用户、用 [[qwen2-5-instruct]](Qwen2.5-7B-Instruct)生成语义描述并做人工评估,发现:**用户交互序列越短,幻觉率越高**。直接把这些可能幻觉的语义特征当作监督信号会引入噪声、损害模型性能。核心问题是:如何在引入 LLM 世界知识的同时规避其幻觉带来的错误监督。

## 方法

GRASP 由两个模块组成,与 SRS backbone 正交(可叠加在 [[gru4rec]]、[[bert4rec]]、[[sasrec]] 之上):

- **生成增强检索(Generation Augmented Retrieval)**:用 LLM 根据物品属性 / 用户画像+历史行为生成描述性文本(prompt 模板见附录,Industry-100K 用 [[chain-of-thought]] 增强),再编码为语义 embedding,构建用户库 U 和物品库 I。公开数据集用 OpenAI 的 text-embedding-ada-002(维度 1536);工业数据集因保密用开源编码器 LLM2Vec(维度 4096)。然后对每个用户/物品按 cosine 相似度检索 top-k 近邻、做 average pooling 得到"相似 embedding"。这些 embedding 全部 **freeze 并缓存**。
- **整体注意力增强(Holistic Attention Enhancement, HAE)**:把用户 embedding 作为 query,物品 embedding 作为 key/value,做基于注意力的融合;关键设计是用 **Sigmoid 替代传统 softmax**,避免单峰问题、更好刻画用户多样兴趣。在语义 embedding 与相似 embedding 上做多层 cross attention,得到细粒度(self/similar)与全局(global)增强 embedding,再 concat 后过 MLP 适配 backbone 隐藏维度,最后接入 SRS backbone 做下一物品预测。

理论上(附录 A.3),与 [[llm-esr]] 用正则项 λ‖e_u − e_c‖² 把用户 embedding 硬拉向 LLM 上下文不同,GRASP 把 LLM 上下文当作可学习门控输入(h_u = W_e·e_u + W_c·e_c + b),W_c 的梯度只由主任务损失驱动,当 LLM 上下文是噪声/无信息时模型可自适应把 W_c 压向 0,从而过滤幻觉。在线计算开销主要是 HAE 模块,复杂度 O(l²d);近邻可按品类/分组离线每日预检索,降低部署复杂度。

## 结果

实验在两个公开数据集(Amazon Beauty:52204 用户 / 57289 物品;Fashion:9049 / 4722)和一个工业数据集(Industry-100K:99711 用户 / 1205282 物品,2025-01-17 至 2025-02-23 的电商购买记录)上进行。指标为 [[ndcg]] 和 Hit Rate(k ∈ {1,3,5,10,20}),leave-one-out 划分、负采样 100,单卡 A100,hidden dim 64、seq 长 100,三个随机种子取平均(p<0.05 t-test)。

- **整体性能**:GRASP 叠加在三种 backbone 上均达到 SOTA,优于 RLMRec、LLMInit、[[llm-esr]]。相对此前最优(LLM-ESR)平均提升:Beauty +4.56%、Fashion +1.81%、Industry-100K +6.68%。例如 Beauty+SASRec 上 N@10 从 36.99 提升到 42.76、H@20 从 69.44 到 72.62;Industry-100K+SASRec 上 N@10 从 27.52 到 34.88、H@10 50.60。
- **分组(head/tail,按 Pareto 80/20 划分)**:在易出幻觉的 tail(稀疏交互)场景增益更大——Beauty 上 GRASP 较 LLM-ESR 提升最高达 9.99%,Fashion tail 平均 +5.00%,Industry-100K tail 平均 +8.42%;head 场景也保持优势(Fashion +0.57%、Beauty +4.30%、Industry-100K +6.41%),说明长尾改进未牺牲头部。
- **消融(Beauty+SASRec)**:去掉 HAE 任一部分(attention / i_similar / i_global)都显著掉点;用 softmax 替换 Sigmoid 后 N@10 从 42.76 跌到 30.00,证明 Sigmoid 是关键。超参最优 N=10(相似检索候选池)、d=64。
- **在线 A/B(附录 A.4)**:在 1000 万用户的更大工业集上训练 GRASP(训练 32 张 A100,每日用户表征推理 16 张),把学到的用户表征作为特征接入下游 [[ctr]] 预测模型;2025-08 在 5000 万日活电商平台、5% 流量的线上实验中,CTR 绝对提升 0.14 个点,订单量相对增长 1.69%,GMV 提升 1.71%。

## 在本 wiki 中的位置

本文属于"LLM 增强推荐"方向,直接对标并改进 [[llm-esr]](把 LLM embedding 从监督信号改为可门控的辅助输入,以抵抗 [[hallucination]])。它与 [[tallrec]] 等"LLM 直接当推荐系统"范式不同,走的是把 LLM 语义理解能力注入传统 [[recommender-systems|recommender-system]] 的路线,可叠加 [[gru4rec]]、[[bert4rec]]、[[sasrec]] 等经典 backbone。方法上结合了 [[retrieval-augmented-generation]] 思想(生成描述 + 近邻检索)与 [[self-attention]] 变体(Sigmoid 注意力)。作者来自 [[shanghai-jiao-tong-university]] 与阿里巴巴 Taobao & Tmall Group。
