---
type: source
subtype: paper
tags:
  - time-series-forecasting
  - foundation-models
  - zero-shot
  - decoder-only
  - patching
created: 2026-05-29
updated: 2026-05-29
arxiv: "2310.10688"
raw: raw/2310.10688.pdf
authors:
  - Abhimanyu Das
  - Weihao Kong
  - Rajat Sen
  - Yichen Zhou
year: 2023
---

TimesFM 是 Google Research 提出的一个 decoder-only 时序预测基础模型,在大规模真实+合成时序语料上预训练后,无需微调即可在多个未见数据集上做出接近全监督 SOTA 的 zero-shot 预测。

## 问题

时序数据在零售、金融、制造、医疗等领域无处不在,预测是其核心用例。受 NLP 中 [[large-language-models]] 进展启发,作者提出疑问:能否像训练 LLM 一样,在海量时序数据上训练一个时序基础模型,使其对**之前未见过的**数据集具备良好的 out-of-the-box zero-shot 预测能力?这样可以免去下游用户的额外训练负担并大幅降低算力需求。难点在于:时序没有像 NLP 那样定义良好的词表/语法;模型需支持不同 history 长度(context)、prediction 长度(horizon)与时间粒度(granularity);且可用的公开时序数据远少于文本数据。

与近期推荐用 [[gpt-3]]、[[llama-2]] 等 LLM 直接做 zero-shot 预测的工作(llmtime / GFQW23)不同,作者主张:专门从零在时序数据上训练的基础模型,能以极小的成本获得远更好的 zero-shot 表现。

## 方法

模型名为 **TimesFM**(Time-series Foundation Model),核心设计原则:

- **Patching(输入分块)**:借鉴 PatchTST,把时序切成连续不重叠的 patch,每个 patch 经一个带残差连接的 MLP(Residual Block)映射为 model_dim 维 token,加上位置编码后送入 transformer。patch 是 NLP token 的自然类比,可提升性能并把 token 数减少为 patch 长度的因子,加快推理。
- **Decoder-only 模型**:与 PatchTST 的关键区别是采用 decoder-only 训练,使用 causal self-attention,给定一串输入 patch 预测下一个 patch,可在整个上下文窗口上并行训练,自动支持任意长度历史的预测(类似 LLM 的自回归)。
- **更长的 output patch**:允许 output_patch_len 大于 input_patch_len(论文示例 input=32、output=128)。一次预测更长的 horizon 可减少自回归步数、提升长 horizon 精度;但 output patch 过长会难以处理短时序(如月度/年度)。
- **Patch Masking(掩码训练)**:为了让模型见到从 1 到最大上下文长度的所有 context 长度,训练时对每个 batch 采样随机数 r,把第一个 input patch 的前 r 个时间点掩掉,从而避免只学到 input_patch_len 整数倍的上下文长度。
- **Input/Output Layers**:输入层把每个 patch 配一个二进制 padding mask 经 Residual Block 编码;输出层用另一个 Residual Block 把输出 token 映射为预测值,使输入与输出 patch 长度可不同。损失函数为点预测的 MSE。

**预训练语料**(Table 1,合计约 O(100B) 时间点):
- **Google Trends**:约 22k 头部查询、2007-2022 共 15 年的搜索兴趣,含小时/天/周/月粒度,约 0.5B 时间点。
- **Wiki Pageviews**:2012-2023 全维基页面浏览量,清洗聚合后约 300B 时间点(最大来源)。
- **合成数据**:为 ARMA 过程、季节性(正余弦)、趋势、step function 等设计生成器,共 3M 条长 2048 的合成时序。
- 其他公开数据:M4、Electricity、Traffic、Weather 等。

训练混合 80% 真实 + 20% 合成数据,最大 context 长度 512(月度等长粒度用 256/64),采用 reversible instance normalization 的标准归一化部分。模型规模仅 200M 参数,预训练数据 O(100B) 时间点,远小于 LLM。

## 结果

在三组完全 held-out 的公开数据集上做 zero-shot 评测,与各组最佳基线对比(其中只有 TimesFM 与 llmtime 是 zero-shot):

- **Monash Archive**(18 个数据集,GM of scaled MAE):TimesFM 是表现最好的模型,略优于全监督的 N-BEATS,比 llmtime(基于 GPT-3)好 **25% 以上**。
- **Darts**(8 个单变量数据集):TimesFM 与最佳方法(llmtime、seasonal ARIMA)在统计显著性范围内相当(每个数据集只有一条时序,误差线较宽)。
- **Informer / ETT**(ETTm1、ETTm2、ETTh1、ETTh2,horizon 96 与 192 共 8 个任务,Average MAE):TimesFM 表现最佳,与全监督 SOTA 深度模型 PatchTST 在统计显著性内相当;其余长 horizon 方法明显更差,llmtime 优于 FEDFormer 但弱于 PatchTST。

**消融**:Scaling 实验用 17M/70M/200M 三种规模,Monash 上 Scaled MAE 随 FLOPS(对数尺度)单调下降;output_patch_len 从 8 增到 128,ETT 上 Average MAE 单调下降;input_patch_len 在 p=16、32 时最优(p=32 训练比 p=16 快近一倍,作为稳妥选择);去掉合成数据会在 Monash 与 15min ETTm 上掉点(粒度欠表示问题)。微调实验中 TimesFM 在所有数据集上优于基线。200M 模型在 16 核 TPUv5e 上 2 天完成 1.5M 次迭代。

## 在本 wiki 中的位置

本文把 [[foundation-models]] 与 zero-shot 预训练范式从 NLP 迁移到时序预测领域,验证了"专用时序基础模型 > 直接复用 LLM 做预测"的论点,可与把 [[large-language-models]]([[gpt-3]]、[[llama-2]])用作 zero-shot 预测器的工作对照阅读。其架构借鉴了 [[large-language-models]] 的 decoder-only 自回归思路与 patching 技术(PatchTST),属于把 LLM 设计原则推广到非语言模态的代表性工作。作者来自 [[google-deepmind]] 关联的 Google Research 团队;Scaling 行为引用了 [[jared-kaplan]] 等的 scaling laws。
