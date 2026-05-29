---
type: source
subtype: paper
tags:
  - human-behavior-simulation
  - user-simulation
  - benchmark
  - llm-as-judge
  - recommender-system
  - long-context
created: 2026-05-29
updated: 2026-05-29
arxiv: 2604.08362
raw: raw/2604.08362.pdf
authors:
  - Jiawei Chen
  - Ruoxi Xu
  - Boxi Cao
  - Ruotong Pan
  - Yunfei Zhang
  - Yifei Hu
  - Yong Du
  - Tingting Gao
  - Yaojie Lu
  - Yingfei Sun
  - Xianpei Han
  - Le Sun
  - Xiangyu Wu
  - Hongyu Lin
year: 2026
---

# OmniBehavior:面向真实世界的人类行为模拟基准

OmniBehavior 是首个完全基于真实工业日志(Kuaishou)构建的用户模拟基准,刻画长时程、跨场景、异质的行为轨迹,并系统揭示当前 LLM 模拟器存在"积极且趋均值"(positivity-and-average)的结构性偏差。

## 问题

LLM 让"通用用户模拟器"成为可能——用一个模型预测个性化行为,在交互式系统的设计与评估中替代真实用户。但现有 [[human-behavior-simulation]] / [[user-simulation]] 基准大多局限于孤立场景(仅视频浏览、直播或电商对话)和狭窄动作空间(仅 click/watch),无法捕捉真实人类行为的整体性。真实数字足迹是一个跨场景连续体:被动浏览、点击、主动搜索、评论、咨询、购买等异质行为相互交织,例如一次购买决策可能源于几天前某条视频激发的兴趣。这种碎片化评估会系统性误判 LLM 的行为建模能力。

## 方法

作者从快手(日活超 4 亿)收集 2025-09-01 至 2025-11-30 三个月的端到端交互日志,构建 **OmniBehavior** 基准([[benchmark]]):

- **Taxonomy**:涵盖 5 大场景(Video Browsing、Live Streaming、Advertisement、E-commerce、Search Behavior;Customer Service 归入 E-commerce)与 22 种用户动作。
- **构建流水线**:按时间戳聚合多场景日志成统一时序;两级清洗(Behavior-level 按 99.9 分位截断,视频阈值 879s、直播 9,601s,平均剔除每用户 91 条噪声;Text-level 用正则 + [[qwen2-5-instruct]](Qwen2.5-72B-Instruct)清洗 OCR/ASR,OCR 压缩率 85.9%、ASR 5.2%);基于 K-Means 聚类([[clustering]] 思路)的代表性采样,选出 200 名用户;用本地部署的 [[qwen]](Qwen3-235B)做匿名化与有害内容剔除。
- 最终数据:200 用户 × 5 场景,共约 2.12M 交互,平均序列长度 8,143 个动作,部分轨迹超过 100,000 步。
- **任务定义**:user-conditioned 预测——给定用户画像 p_u、历史行为序列 H_u 和当前场景上下文 c_t,模拟器 f_θ 需预测该场景下所有对应行为 y_t,覆盖二元信号(like/follow)、连续信号(watch duration)和文本反馈(客服对话)。

评测用 [[llm-as-judge]](Claude-Sonnet-4.5)对文本行为打分(intent fidelity / persona mimicry / knowledge boundary / semantic alignment 四项);二元行为用 F1,连续行为用归一化的 NMAE。主实验在 6,000 个预测任务上、统一 32K 上下文、用 [[langchain]] 做记忆管理,跑在 NVIDIA A800-SXM4-80GB 上。

## 结果

**真实行为分析(第 3 节)**:
- 整合新场景使兴趣覆盖度提升约 20–30%(单场景存在"隧道视野");累积兴趣覆盖从 Search 的 2.4%/0.4% 增长到 +Video 的 100%/100%。
- 回溯分析显示超过 80% 的转化路径跨多个场景;causal chain 时间跨度上 60% 以上决策依赖 3 天前的线索,81.8% 的链条跨多场景。案例展示一条横跨 12 天、由搜索"Xiaomi"兴趣累积到购买的因果链。
- 与合成数据集 [[locomo]] 对比:真实用户日均兴趣漂移率 0.6311,合成用户仅 0.1698,合成数据呈僵硬的任务驱动尖峰。

**LLM 评测(11 个模型,Table 1)**:
- 最佳模型 [[claude-3-7-sonnet]] 同系列的 Claude-Opus-4.5 总分仅 **44.55**;多数模型聚集在 32–41;多数模型在二元行为(如 like/share)F1 不超过 40%。
- 开源 [[glm-4-7]](GLM-4.7)总分 41.46,超过 Claude-Sonnet-4.5(40.49)和 [[gpt-4o]] 同系列 GPT-5.2(39.07);[[deepseek-v3]] 在 E-commerce 二元任务(33.31)上超过 Claude-Opus-4.5(29.98)。其余基线含 Claude-Haiku-4.5、Claude-Sonnet-4、[[gemini-2-5-flash]] 同系列 Gemini-3-Flash、GPT-4o、Kimi-K2-Instruct、Qwen3-235B。
- **长上下文(第 4.3 节)**:在历史超 128K 的 66 名用户子集上,16K→128K 上下文窗口并不能持续提升性能(与 [[large-language-models]] 长上下文"lost in the middle"现象一致)。记忆管理对比:Summary 总分 24.27(↑14.9%)优于 Truncation(21.13)和 [[retrieval-augmented-generation]](RAG,20.38,↓3.6%),因 RAG 只看语义相似而忽略因果结构。

**结构性偏差(第 5 节)——核心发现 positivity-and-average bias**:
- **Hyper-activity**:真实正向交互率低于 10%,而 Qwen3-235B、Gemini-3-Flash 等高估用户参与度 40–60%,无法建模用于流失预警的负反馈。
- **Persona homogenization**:用 19 维动作率向量分析,真实用户 inter/intra 距离比约 0.29(个体差异明显),而 LLM 模拟用户该比值约 0.7–0.87(分布高度重叠),长尾个性被抹平。
- **Utopian tendency**:E-commerce 客服对话中,真实用户常表达强烈负面情绪(Refund/Fake/Broken/Hurry up),LLM 输出聚集在中性/积极、过度礼貌(受 [[alignment]] 影响),无法模拟不满用户的对抗性交互。

作者据此提出对"在社会科学与行为建模中使用 [[ai-agent-behavioral-science]] / [[social-simulation]]"的告诫框架:不纠正这些内在扭曲,LLM 更像我们理想的镜子,而非现实的地图。

## 在本 wiki 中的位置

- 同属 LLM 作为人类/用户模拟器与 [[social-simulation]] 方向,可与 [[generative-agents]]、[[bases]] 等"LLM 作为模拟器"工作对照——本文强调它们多在受控单任务沙盒中,缺乏真实工业日志支撑。
- 作为 [[benchmark]],它把 [[user-simulation]] 评测从孤立场景推进到跨场景、长时程、异质;与同类基准 [[sotopia]]、[[human-behavior-simulation]] 形成互补,并与 [[locomo]](长时记忆合成数据)做了直接对比。
- 评测协议大量使用 [[llm-as-judge]],并对 [[retrieval-augmented-generation]] 与摘要式记忆管理给出在长时程用户建模中的局限证据,与 [[long-context]] 相关讨论相关。
- 数据源 [[kuaishou]],可与 [[kuairec]]、[[kuairand]]、[[kuaisim]] 等快手系 [[recommender-systems|recommender-system]] 数据集/模拟器并列;揭示的偏差对 [[recommendation-simulator]]、[[user-retention]] 建模有警示意义。
