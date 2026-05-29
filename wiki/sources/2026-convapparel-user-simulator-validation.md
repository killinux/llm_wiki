---
type: source
subtype: paper
tags:
  - user-simulation
  - conversational-recommender
  - benchmark
  - dataset
  - evaluation
  - counterfactual-validation
  - llm-as-judge
created: 2026-05-29
updated: 2026-05-29
arxiv: "2602.16938"
raw: raw/2602.16938.pdf
authors:
  - Ofer Meshi
  - Krisztian Balog
  - Sally Goldman
  - Avi Caciularu
  - Guy Tennenholtz
  - Jihwan Jeong
  - Amir Globerson
  - Craig Boutilier
year: 2026
---

# ConvApparel: A Benchmark Dataset and Validation Framework for User Simulators in Conversational Recommenders

ConvApparel 是 Google 提出的人-AI 服装购物对话数据集与一套三支柱验证框架,用来衡量基于 [[large-language-models]] 的 user simulator 在 conversational recommender system 中的"realism gap"(真实性差距),核心创新是用 counterfactual validation 检验 simulator 能否泛化到未见过的 agent 行为。

## 问题

基于 LLM 的 user simulator 被寄望于规模化训练和评估 conversational AI,但存在严重的 realism gap:它们系统性偏离真实人类行为(过度啰嗦、缺乏稳定 persona、无法表达连贯偏好、不合理的耐心等)。这会让自动评估失真,并可能把 agent 训练引向不真实的用户行为。

作者强调要区分两个目标:**缩小** realism gap(造更好的 simulator)与**测量** realism gap(建立可靠的衡量工具)。本文聚焦后者——如何严谨、全面地验证 simulator 的 fidelity,而不只是看任务成功率或单一统计指标。已有评估常依赖单一手段(如 statistical alignment),不足以判断 simulator 是真正学到了用户行为模型,还是只在模仿表层模式。

## 方法

**ConvApparel 数据集**:服装购物领域的人-AI 标注对话。

- 付费参与者用多模态(文本+图片)对话界面完成 4 个高层购物任务;每轮 agent 返回文本回复 + 推荐商品 carousel。
- 关键设计:dual-agent protocol。商品目录扩展自 Amazon Reviews Dataset,构造"good agent"(乐于助人、用稳健 semantic retrieval)与"bad agent"(故意无用、跑题、混淆,且检索被刻意降级为只用部分信息编码)。任务按 80/20 随机分给 good/bad agent。这种对照为 counterfactual validation 提供了两种受控交互条件。
- 完成任务后进入 rater mode,参与者回顾性地逐轮标注第一人称内部状态(满意、沮丧、困惑)与购买意愿,再做 session 级总体反馈。
- 规模:4,146 段对话、897 名参与者、14,736 轮。数据已发布于 Kaggle 与 HuggingFace。

**三支柱验证框架**:

1. **Population-Level Statistical Alignment (PLSA)**:比较 simulator 与人类群体在三类指标上的分布——基础对话统计(轮数、每轮词数)、behavioral dialog acts(inform-preference、ask-clarification、accept/reject-recommendation 等)、user experience(满意/沮丧/困惑等潜在状态)。dialog act 与 user experience 用 [[llm-as-judge]] 标注。
2. **Human-Likeness Score (HLS)**:受 Turing test 启发,训练一个 LLM-based 判别器 D(Gemini 2.5 Flash-Lite)做"人类 vs 合成"的二分类,D(c) ∈ [0,1] 即该对话由人类生成的概率,作为整体真实性评分。
3. **Counterfactual Validation**(主要方法贡献):问"如果用户面对一个(行为上)不同于训练分布的系统会怎样反应?"。做法是只用 good-agent 数据训练 simulator,再让它与未见过的 bad agent 交互,看它能否像真实用户那样表现出更多沮丧、更低满意、更高 critique 率(以及反方向 bad→good 实验)。这检验 simulator 是否学到稳健、可泛化的用户行为模型,而非过拟合特定系统的表层模式。

**被评测的 simulator**:三种代表性 LLM simulator,均基于 Gemini 模型家族——Prompted(纯 prompt engineering)、[[in-context-learning]](RAG 检索 k=3 个最相似对话作 few-shot)、[[supervised-fine-tuning]](在 ConvApparel 上微调 [[gemini-2-5-flash]])。

## 结果

数据集有效性:good-agent 交互被评为更自然(0.59 vs 0.49)、更满意(0.38 vs 0.23);bad-agent 显著更高沮丧(0.16 vs 0.06)与困惑(0.10 vs 0.06);χ² 检验显示 good/bad 在沮丧、满意上差异极显著(p<0.001),整体接受率下降 10.8%——证明 dual-agent 在功能上确实造出两类很不同的体验。

LLM-as-judge 可靠性:LLM 判断与第一人称人类评分相关性中等(Kendall τ≈0.165 满意、0.168 沮丧),但人类第三方评分者与第一人称的相关性同样不高(τ≈0.155、0.12),说明差距主要来自内部状态本身的不可观测性,而非模型无能;LLM judge 与人类第三方评分者高度一致(τ≈0.579 满意、0.485 沮丧;推荐接受这类客观指标 accuracy 达 0.813),因此 LLM judge 是第三方观察者的可靠代理。

HLS 判别器:zero-shot prompted 判别器只有 0.57 accuracy;在全数据上微调后达 **0.99** test accuracy。一个仅用 unigram/bigram 词表的简单基线就有 0.92 accuracy,说明 simulator 用词与人类显著不同,realism gap 真实且可学习。

PLSA:data-driven simulator(ICL、SFT)在分布上比 Prompted 更贴近人类基线;Mann-Whitney U 与 KS 检验显示 realism gap 仍持续存在,但 ICL/SFT 的 KS 距离在多数指标上明显小于 Prompted。Human-vs-Human 基线确认不相交的人类群体在统计上无法区分,坐实 gap 的真实性。

HLS 评测:判别器 D 几乎把所有 simulator 对话都判为合成,所有 simulator 平均 HLS 仅 **0.004**(对比 D 对真实留出对话约 0.99 accuracy),说明虽然聚合统计可对齐,更细粒度的真实性测试下 gap 依然巨大。判别器泛化表存在非对称:SFT 训练的判别器能抓出 Prompted 对话(0.978),反之 Prompted 判别器难以识别 SFT 对话(0.041 specificity),说明 SFT 对话"simulator 痕迹"更少。

Counterfactual Validation:只用 good-agent 数据训练的 ICL、SFT 在面对未见 bad agent 时,比 Prompted 基线泛化更好——更真实地表现出更多沮丧、更多 clarification、更少接受推荐,贴合真实用户的行为转移;反方向 bad→good 实验结论一致(bad 数据较少故只用 ICL)。结论:data-driven 方法学到的用户模型比纯 prompting 更稳健、可泛化。

局限:counterfactual 当前只覆盖单一类型的 good→bad 转移;局限于服装购物域;输入只用文本(单模态,无点击);依赖 LLM-as-judge,其与个体人类评分相关性偏低需谨慎解读;论文聚焦 realism 而牺牲了 controllability(steerable behavior),二者权衡留作未来工作。

## 在本 wiki 中的位置

ConvApparel 把"user simulator fidelity 如何评估"这一问题系统化,与 [[recagent-user-behavior-simulation]]、[[kuaisim-recommender-simulator]] 等 LLM/RL 驱动的 [[recommendation-simulator]] 工作互补:后者偏向"造 simulator",本文偏向"严谨地量化 simulator 真实性"。其 counterfactual validation 思路与 [[causal-inference]]/[[counterfactual-reasoning]] 在评估中的应用相通;HLS 判别器是 [[evaluation]] 中 Turing-test 式判别法的实例;PLSA 与 [[llm-as-judge]] 的可靠性分析对所有用 LLM 做评测的工作都有参考价值。可与 [[interec]]、[[lusifer]] 等 user simulation 研究,以及 [[redial]]、[[microlens-micro-video-recommendation-dataset]] 等 CRS/推荐数据集对照阅读。
