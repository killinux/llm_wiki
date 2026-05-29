---
type: source
subtype: paper
tags:
  - survey
  - llm-agent
  - recommender-system
  - user-simulation
  - conversational-recommendation
  - multi-agent
created: 2026-05-29
updated: 2026-05-29
arxiv: "2502.10050"
raw: raw/2502.10050.pdf
authors:
  - Qiyao Peng
  - Hongtao Liu
  - Hua Huang
  - Qing Yang
  - Minglai Shao
year: 2025
---

# A Survey on LLM-powered Agents for Recommender Systems

一句话:本文系统综述了把 [[llm-agents|llm-agent]] 引入 [[recommender-systems|recommender-system]] 的研究,提出"面向推荐 / 面向交互 / 面向模拟"三大范式,并用 Profile、Memory、Planning、Action 四模块统一架构对现有方法做分解与对比,同时汇总数据集与评测体系。

## 问题

传统 [[recommender-systems|recommender-system]](从 [[matrix-factorization]] 到深度学习方法)虽能基于历史行为做个性化推荐,但有三个固有局限:难以理解超出数值交互的复杂用户意图、缺乏与用户多轮交互探索偏好的能力、推荐结果像"黑盒"缺乏可解释性。[[large-language-models]] 驱动的 [[llm-agents|llm-agent]] 凭借推理、自然语言交互与生成能力,有望同时缓解这三点,并通过预训练知识改善 [[cold-start]]。但该方向尚缺乏统一的分类与架构梳理,本文即为此提供系统综述。

## 方法

这是一篇综述(survey),贡献集中在两套"框架":

**(1) 按方法目标分三大范式:**
- **面向推荐(recommender-oriented)**:让 agent 直接基于用户历史生成推荐决策,强化规划、推理、记忆、工具调用。代表:[[interecagent]] 类、RecMind(统一 LLM agent 直接输出推荐)、[[macrec]](多 agent 协作)。
- **面向交互(interaction-oriented)**:通过对话与解释增强可解释性。代表:AutoConcierge(对话式餐厅推荐)、RAH(ResSys-Assistant-Human 三方 + Learn-Act-Critic 循环)、[[interecagent]]、RecLLM。
- **面向模拟(simulation-oriented)**:用 agent 模拟真实用户行为与物品特征,服务系统评估。代表:[[generative-agents]] 思路的 Agent4Rec(LLM 用户模拟器)、[[agentcf]](用户与物品都建模为 agent 协同学习)、UserSimulator、[[recagent]]。

**(2) 统一 agent 架构四模块:**
- **Profile(画像)**:从历史交互构建用户/物品的动态表示(如 Agent4Rec 的可量化社会特质 + LLM 抽取偏好)。
- **Memory(记忆)**:管理历史交互、情感与上下文;[[recagent]] 用 sensory / short-term / long-term 三级记忆,并支持 [[self-reflection]]。
- **Planning(规划)**:多步策略生成与任务排序,平衡即时满意与长期参与;BiLLP 用 macro(Planner+Reflector)/ micro([[actor-critic]])分层规划。
- **Action(执行)**:把决策转为具体推荐并采集反馈;[[interecagent]] 整合查询/检索/排序三类工具 + Candidate Bus。

文中以 Table 1 给出 23 个代表方法在四模块上的覆盖对比,并用 Table 2 / Table 3 汇总数据集与评测指标。

## 结果

作为综述,本文给出结构化归纳而非单一实验数字:

- **方法对比(Table 1)**:覆盖 RAH、ToolRec、PMS、DRDT、BiLLP、RecMind、[[macrec]]、AutoConcierge、MACRS、RecLLM、[[interecagent]]、KGLA、CSHI、SUBER、FLOW、Agent4Rec、[[agentcf]]、UserSimulator、[[recagent]] 等约 23 个方法,逐一标注是否含 Profile/Memory/Planning/Action 模块。
- **数据集(Table 2)**:汇总传统推荐数据集与会话推荐数据集,如 Amazon Books(10.3M 用户 / 4.4M 物品 / 29.5M 交互)、[[movielens]] 系列(100K 到 20M)、[[steam-dataset]](334.7K 用户 / 3.7M 交互)、[[yelp-dataset]]、Lastfm、Anime;会话类含 ReDial(11348 段对话 / 6925 部电影)、Reddit、OpenDialKG。
- **评测体系(Table 3)**:标准推荐指标 [[ndcg]]@K、Recall@K、Hit Ratio@K;语言生成质量用 BLEU / ROUGE;长期参与用强化学习指标(trajectory length、average/cumulative reward,见 BiLLP、LUSIM);会话效率用 Success Rate、Average Turn 等(MACRS)。
- **挑战与方向**:推理时频繁调用 LLM/API 的成本(部分方法对数据集采样,如 [[agentcf]] 取一稠密一稀疏子集各 100 用户、DRDT 每数据集采 200 用户 + 19 候选项),以及评测标准化、模拟可信度等开放问题。

## 在本 wiki 中的位置

本文是连接 [[llm-agents|llm-agent]] 与 [[recommender-systems|recommender-system]] 两大主线的综述类 source。它把本 wiki 已有的 [[macrec]]、[[interecagent]]、[[agentcf]]、[[recagent]] 等具体系统,纳入"面向推荐/交互/模拟"三范式与 Profile-Memory-Planning-Action 四模块的统一坐标系,可作为浏览这些 LLM 推荐 agent 工作的总索引;其汇总的 [[movielens]]、[[steam-dataset]]、[[yelp-dataset]] 数据集与 [[ndcg]] 等指标,也对应本 wiki 中的推荐评测条目。
