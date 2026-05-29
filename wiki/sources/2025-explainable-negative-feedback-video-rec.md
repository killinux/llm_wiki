---
type: source
subtype: paper
tags:
  - recommender-system
  - llm-agent
  - negative-feedback
  - multimodal
  - reinforcement-learning
  - video-recommendation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2511.18700"
raw: raw/2511.18700.pdf
authors:
  - Siran Chen
  - Boyu Chen
  - Chenyun Yu
  - Yi Ouyang
  - Lei Cheng
  - Chengxiang Zhuo
  - Zang Li
  - Yali Wang
year: 2025
---

# When Top-ranked Recommendations Fail: 用多智能体 MLLM 建模多粒度负反馈,做可解释、鲁棒的视频推荐

一句话:面向短视频推荐中"高相似度却被用户反感"的问题,作者构建带真实 dislike 理由标注的多模态数据集 TVNF,提出由 Profile / Video / Reason 三个 [[large-language-models]] 智能体组成的 Agentic ENF 框架,并用渐进式强化学习算法 S-GRPO 训练,在负反馈预测与理由解释上显著超过 [[gpt-4o]],线上部署提升观看时长。

## 问题

传统视频 [[recommender-systems|recommender-system]] 主要依赖 ID embedding 映射与 [[collaborative-filtering]],难以捕捉视频内容的深层语义,且常被有偏的用户行为(误点、快速划走 fast-skip)误导,导致 top 推荐反复触发原因不明的负反馈。作者把核心问题归结为三点:

- 负反馈数据稀缺:显式信号(dislike、评论)信息量大但极稀疏(约占全部交互的 0.3%);隐式信号(watch time、skip)海量却噪声大、信息量低。这是一种典型的 [[selection-bias]] / [[popularity-bias]] 之外的 [[exposure-bias]]、[[noisy-watching]] 难题。
- 负反馈的具体原因被忽视:以往方法仅靠聚类负反馈信号得到 dislike 特征后压制相似推荐,不理解"为什么 dislike",跨场景泛化差(例如用户讨厌某条美食视频,不应压制所有美食推荐)。
- 现有基于 LLM 的负反馈方法在多模态场景缺乏细致评测,且大多忽略 item 的复杂多模态内容,也缺乏对可解释理由的评估。

## 方法

数据集 TVNF:来自腾讯新闻真实多模态视频推荐日志,约 1 万用户、2 万视频、32 万交互、连续 7 天(论文另处称约 20,539 条视频、覆盖 10–30 秒为主、平均约 46 秒)。每条视频附原始 URL 与 16 帧均匀采样图像。隐式负反馈以 play_rate < 0.3 判定;额外收集约 1k 条用户显式陈述的 dislike 理由(极稀缺),据真实评论归纳为四类:负面事件、低俗或冲突价值观、剧情乏味、视觉不适元素。用 [[gpt-4o]] 对隐式负反馈打标后人工复核。Table 1 对比显示 TVNF 是唯一同时具备"多模态视频数据 + 显式反馈 + 隐式反馈 + 真实 dislike 理由"的数据集(对比 [[amazon-reviews]]、[[yelp-dataset]]、MultiFeed、[[kuairand]]、[[movielens]]、[[microlens]])。

Agentic ENF 框架(三个层级化协作的 [[llm-multi-agent]]):
- Profile Agent:基于年龄/性别/职业/兴趣与历史观看序列,聚焦 play_rate < 0.3 的视频,推断用户的心理与人格画像(如对负面/低俗内容的容忍度);标题线索不足时通过 [[function-calling]] 动态调用 Video Agent 获取多模态线索。本质是动态更新的 [[agent-memory]] / [[persona]] 建模。
- Video Agent:基于 MLLM 做单视频级多模态分析,识别潜在争议元素并给出上下文解释,反哺 Profile Agent 做 cross-modal 校验。
- Reason Agent:用更新后的画像,从用户视角沿四个维度(兴趣契合、剧情吸引力、负面/极端内容、视觉容忍度)预测用户态度(Like / Not Like)并生成可解释理由,输出 `<think>...</think><answer>...</answer>` 格式。

训练:以 [[qwen]] 系列的 Qwen2.5-VL-7B 为底座,沿 [[deepseek-r1]] 的两阶段范式。Stage 1 SFT 冷启动:用 [[gpt-4o]] 基于真实 dislike 理由生成 [[chain-of-thought]] 作为 SFT 数据。Stage 2 用作者提出的 S-GRPO([[chain-of-thought]] 渐进奖励版的 [[ppo]] 替代——基于 [[reinforcement-learning]] 的 GRPO)在无标注数据上微调。S-GRPO 把单一视频判断拆成三级渐进 [[reward-shaping]]:
- Judge Reward(二元判断对错);仅当判断正确才进入下一步,否则提前终止,正反馈也终止。
- Class Reward(负反馈类型多选分类);
- Reason Reward(解释质量,以 ROUGE-1/2/L 对比 `<think>` 内容与真实理由)。
后一步奖励只在前一步正确时触发,实现 easy-to-hard 的 [[curriculum-learning]]。Video Agent 用 3 步奖励训练(显式数据),Reason Agent 因缺真值用 2 步奖励(隐式数据)。实现上 GPT-4o 作 Profile Agent,Qwen2.5-VL-7B 同时作 Video/Reason Agent;4×A100 80G、bf16、ZeRO-2、FlashAttention、vLLM 加速,group G=8、lr 1e-6。部署用 FP16 量化,异步调用可在 15 分钟内分析 1000 用户(约 1 query/s)。

## 结果

显式负反馈(视频争议内容理解与推理,Table 2):本文 Video Agent(7B)取得 Recall 0.808、F1 0.750、Class_Acc 0.654、Reasoning 0.537,均为最佳;Recall 与 F1 明显超过 [[gpt-4o]](Recall 0.630 / F1 0.739)、[[deepseek-r1]]、[[llama]] 70B、Qwen2.5-VL 7B、Qwen3 32B,以及 Video-R1、VideoChat-R1 等视频推理基线。理由分类与解释分别较 GPT-4o 提升 +8.6% 与 +13.5%(GPT-4o 准确率最高 0.882 但对争议内容不敏感)。

隐式负反馈(模拟用户观看行为,Table 3):本文 ENF(7B)Acc 0.612、Precision 0.404、Recall 0.782、F1 0.533、Class_Acc 0.543,综合最佳;对比 [[sasrec]]、MLLM-MSR、Video-R1、VideoChat-R1 与多个 LLM 基线。隐式预测整体更难,最高 Acc 仅 61.2%。

消融:Table 4(Video Agent)显示去掉 SFT 冷启动 / RL / S-GRPO 各项均下降,完整版 Acc 0.861、F1 0.750;Table 5(Reason Agent)显示 Profile Agent、Video Agent 初始化、S-GRPO 三者缺一不可,完整版 Acc 0.612。

跨域泛化(Table 6,二分类偏好对齐):在 [[movielens]]-1M 上 Acc 0.815 / F1 0.808,在 [[steam-dataset]] 上 Acc 0.803 / F1 0.805,超过 [[gpt-4o]]、[[recagent]]、[[agent4rec]]、SimUSER 等。

线上(Table 7,腾讯新闻 Base RS + ENF):平均观看时长 47.6%→53.8%(+13.0%),fast-skip 率 23.7%→14.3%(−39.7% 相对,即论文摘要所述降低 9.4 个百分点),dislike 率 0.61%→0.35%(−42.6% 相对)。

## 在本 wiki 中的位置

本文连接了两条主线:一是 [[llm-for-recommendation]] / [[user-simulation]](与 [[agent4rec]]、[[recagent]]、[[lusifer]]、[[interecagent]] 等同属用 [[llm-based-agents]] 模拟用户行为的路线),区别在于不用 frozen LLM 而用 [[reinforcement-learning]] 对齐真实偏好以抑制 [[hallucination]];二是负反馈与 [[debiasing]] 研究(DFN、CDR、SINE 等),贡献在于从"压制相似项"转向"解释 dislike 原因"。方法上属 [[llm-multi-agent]] + [[multimodal]] MLLM([[qwen]] / [[gpt-4o]])+ 渐进式 GRPO([[deepseek-r1]] 谱系)的组合,可与 [[chain-of-thought]]、[[curriculum-learning]]、[[reward-shaping]]、[[process-reward-model]] 等条目互参。数据集 TVNF 是本 wiki 中少见的"带真实负反馈理由标注"的多模态视频推荐 [[benchmark]]。
