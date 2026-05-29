---
type: source
subtype: paper
tags: [llm-agent, generative-agents, recommender-system, user-simulation, recommendation-simulator, llm-based-agents]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2310.10108
raw: raw/2310.10108.pdf
authors: [An Zhang, Yuxin Chen, Leheng Sheng, Xiang Wang, Tat-Seng Chua]
year: 2024
---

# On Generative Agents in Recommendation (Agent4Rec)

Agent4Rec 用 1000 个由 LLM 驱动的 [[generative-agents]] 构建电影推荐的用户模拟器,每个 agent 配备 profile / memory / action 三大模块,用于探究 LLM 生成式 agent 在多大程度上能忠实模拟真实自主用户的推荐行为。

## 问题

[[recommender-systems|recommender-system]] 的离线指标与线上表现之间存在显著鸿沟,这阻碍了学术成果落地与算法迭代。理想方案是一个可配置的仿真平台,忠实捕捉用户意图并编码人类认知机制,用于数据收集、推荐评估与算法开发。近期 [[large-language-models]] 与 [[generative-agents]] 的进展为构建这类**推荐模拟器**提供了基础,但要让模拟器忠实反映个性化用户偏好并非易事。核心研究问题(RQ1):LLM 驱动的生成式 agent 能在多大程度上真正模拟推荐系统中真实、独立人类的行为?

## 方法

Agent4Rec 是基于 [[langchain]] 搭建、所有 agent 由 [[chatgpt]] 的 [[gpt-3-5-turbo]] 版本驱动的通用用户模拟器,含两大组成:LLM 生成式 agent + 推荐环境。

**Agent 架构(三模块)**:
- **Profile Module(画像)**:用真实数据集([[movielens-1m]]、[[steam-dataset]]、[[amazon-book]])初始化。两部分:
  - social traits(社会特质):activity(活跃度)、conformity(从众度)、diversity(多样性),按真实统计切分为 high/mid/low 三档;
  - unique tastes(独特口味):从用户观看历史抽 25 条,评分≥3 视为 like、<3 视为 dislike,用 [[chatgpt]] 蒸馏总结口味与评分模式。姓名/性别/年龄/职业等个人标识被刻意隐去以保护隐私。
- **Memory Module(记忆)**:分 factual memory(推荐项与反馈)与 emotional memory(疲劳度 fatigue、满意度等情绪感受)。支持 memory retrieval / writing / reflection 三种操作;引入**情绪驱动的 self-reflection**机制(对比传统的 self-summarization / [[self-correction]] 仅压缩事实知识)。记忆同时以自然语言与向量两种形式存储。
- **Action Module(动作)**:
  - taste-driven actions:浏览、评分、生成观后感;
  - emotion-driven actions:退出系统、给推荐系统打分、参加退出后访谈;用 [[chain-of-thought]] 做情绪推理判断当前满意度与疲劳度,据此决定是否退出。

**推荐环境**:item profile 生成(quality 来自历史评分、genre/summary 由 LLM 生成,并剪除被 LLM 误分类的项以降低 [[hallucination]]);page-by-page(逐页)推荐场景,模拟 Netflix/YouTube/豆瓣;推荐算法作为可插拔模块,内置 random、most popular、[[matrix-factorization]](MF)、LightGCN、MultVAE,并开放接口接入外部算法。

**Task Formulation**:给定用户 u 与物品 i,y_ui=1 表示已交互、r_ui∈{1..5} 为评分;目标是蒸馏出对未见物品的 ŷ_ui 与 r̂_ui。

## 结果

在 [[movielens-1m]]、[[amazon-book]]、[[steam-dataset]] 上做多维评测。

- **口味对齐(Table 1)**:在区分用户喜欢/未交互物品任务上,即使引入干扰项,agent 仍保持约 65% accuracy、约 75% recall。MovieLens 1:1 设置 Accuracy 0.6912、Recall 0.6914、F1 0.6982;Amazon-Book 1:1 Accuracy 0.7190、F1 0.7002;Steam 1:1 Accuracy 0.6892、F1 0.6786。但随喜欢物品比例下降,Precision/F1 急剧下滑(从近 70% 降到约 25%),反映 LLM 倾向稳定挑选固定数量物品的 hallucination 倾向。
- **评分分布对齐(Fig 3)**:agent 模拟评分以 4 分为主、低分(1-2)很少,与真实 MovieLens-1M 分布强一致;但 agent 几乎不给 1-2 分,因 LLM 知识丰富会预先回避低质电影。
- **推荐策略评估(Table 2)**:算法型策略满意度高于 random/popular;LightGCN 在满意度(S̄_sat 3.85*)上优于 MF(2.99)与 MultVAE(3.75),与现实观察一致,显示可作为 A/B testing 的低成本替代。
- **逐页推荐增强(Table 3)**:把 agent 观看过的电影作为正信号回灌再训练,所有算法在离线指标(Recall@20/NDCG@20)与满意度上均提升;若回灌未观看电影则体验下降。
- **洞察(RQ2)**:复现 filter bubble 效应——迭代增加时主类占比 P̄_top1-genre 上升、类型多样性 N̄_genres 下降(Fig 8);用 DirectLiNGAM 做 causal discovery,学得因果图(Fig 9)显示 movie quality 与 popularity 是 movie rating 的成因,并观察到 popularity bias 的放大反馈环。

## 在本 wiki 中的位置

本文属于 [[generative-agents]] 与 [[recommender-systems|recommender-system]] 的交叉,是"基于 LLM agent 的 [[user-simulation]] / 推荐模拟器"代表工作,与 [[recagent]]、[[recsim]] 等模拟器相关。其 agent 设计沿用 Park 等 [[generative-agents]] 的 profile/memory/action 思路,并引入情绪驱动的 [[self-reflection]]。其对 [[matthew-effect]] / popularity bias、filter bubble 与 [[causal-discovery]] 的探讨,可与本 wiki 中推荐去偏、[[causal-inference]] 相关条目互相参照。
