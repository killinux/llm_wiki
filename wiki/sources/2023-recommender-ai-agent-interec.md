---
type: source
subtype: paper
tags: [llm-agent, recommender-system, tool-use, llm-planning, agent-memory, conversational-recommendation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.16505
raw: raw/2308.16505.pdf
authors: [Xu Huang, Jianxun Lian, Yuxuan Lei, Jing Yao, Defu Lian, Xing Xie]
year: 2023
---

# Recommender AI Agent: Integrating Large Language Models for Interactive Recommendations

提出 **InteRecAgent**(Interactive Recommender Agent),用 [[large-language-models]] 作为"大脑"、传统推荐模型作为"工具",把基于 ID 的矩阵分解类推荐模型改造为带自然语言交互界面的交互式推荐系统。

## 问题

推荐模型擅长在特定领域提供精准的 item 推荐(充当轻量级领域专家),但难以胜任解释、对话等多样化、交互式任务;而 LLM 具备强大的语言理解、常识推理与人机交互能力,却缺乏领域内 item 目录与用户行为模式的知识,尤其在偏离通用世界知识的私有领域(如 e-commerce)。为每个领域单独 [[fine-tuning]] 一个 LLM 既不经济也不高效。如何结合二者优势,用一个框架把传统推荐模型接入 LLM,是本文要解决的问题。

## 方法

InteRecAgent 以 LLM 为大脑、推荐模型为工具,核心由三部分组成。

**工具集(最小工具集)**:
- Information Query(信息查询):用 SQL 从后端数据库检索 item 细节(如发行日期、价格)。
- Item Retrieval(召回):分 hard condition(显式离散属性,用 SQL 工具)与 soft condition(语义匹配,用 item-to-item 的 ItemCF 工具)两类需求,从全量 item 池给出候选。
- Item Ranking(排序):用类似传统推荐的 one-tower 排序工具(实现为去掉位置编码的 [[sasrec]]),结合用户画像对候选打分。

**记忆机制(Memory)**:
- Candidate Bus(候选总线):一个独立内存,存放当前候选 item,避免把大量 item 拼进 prompt;包含 data bus(候选数据)与 tracker(记录每个工具调用的三元组 (工具名, 输入, 输出),供反思使用)。候选 item 在工具间以漏斗式流动。
- 长期 + 短期用户画像(user profile):以 like / dislike / expect 三个维度结构化表示用户偏好,支持长对话与终身对话场景(超出上下文窗口时从历史段检索并合并入长期记忆)。

**Plan-first Execution + 动态示范(Section 3.3)**:采用"先规划后执行"的两阶段策略替代 [[react]] 式 step-by-step。Plan 阶段 LLM 根据用户当前输入、对话上下文、工具描述与动态示范一次性生成完整工具调用计划;Execution 阶段严格按计划逐步调用工具,通过 Candidate Bus 通信。相比 ReAct(N 步需 N+1 次 API 调用),plan-first 仅需 2 次 API 调用,降低延迟与成本。动态示范(dynamic demonstration)用 sentence-transformers 编码、ChromaDB 做 ANN 检索,选出与当前意图最相似的若干示范注入 prompt 做 [[in-context-learning]];示范本身受 [[self-instruct]] 启发用 input-first / output-first 两种策略由 GPT-4 生成。

**Reflection(反思,Section 3.4)**:采用 [[actor-critic]] 式反思机制。Actor 是带工具的 LLM,生成计划 p^t、得到工具输出 o^t 与回复 y^t;Critic 评估其行为决策,若判断为负则把反馈作为信号让 actor 重新规划(rechain),提升鲁棒性与纠错能力。

**小模型作大脑(Tool Learning with SLM,Section 3.5)**:默认大脑是 [[gpt-4]]。为降本与"民主化"框架,作者用 GPT-4 构造模仿数据集(instruction → tool execution plan),微调 [[llama-2]]-7B 得到 **RecLlama**。数据来自两种方式:user simulator 与 recommender agent(均由 GPT-4 驱动)对话采样,以及人工设计的 30 个多样对话再由 GPT-4 扩展;最终数据集 16,183 条(13,525 来自第一种方法,2,658 来自第二种),仅用 Steam 与 MovieLens 数据生成、排除 Beauty 以检验领域泛化。

## 结果

**评估设置**:三个数据集 Steam、[[movielens]]、Amazon Beauty([[amazon-reviews]]);用 GPT-4 扮演的 user simulator(role-playing)做多轮对话评测,以及 one-turn recommendation 评测。指标:user simulator 用 Hit@k 与 AT@k(average turns,失败记为 k+1);one-turn 用 Recall@k 与 NDCG@k。Baselines 包括 Random、Popularity、LLaMA-2-7B/13B-chat、[[vicuna]]-v1.5-7B/13B、Chat-Rec(3.5/4)、[[gpt-3-5]]、GPT-4。实现细节:SQL 经 pandasql/SQLite,框架用 Python + [[langchain]],动态示范数 3,hard condition 召回上限 1000,soft condition 取 top 5%。

**Session-wise(Table 2)**:InteRecAgent(Ours)在三数据集上 Hit@5 与 AT@5 均超过所有对比 LLM。Hit@5:Steam 0.87、MovieLens 0.85、Beauty 0.54;AT@5:Steam 2.86、MovieLens 3.15、Beauty 3.99。对比 GPT-4 的 Hit@5 仅 0.78 / 0.79 / 0.15。在更私有的 Beauty 领域改进最显著(GPT-4 因专业、冗长的 item 名而严重 [[hallucination]])。Chat-Rec 是单工具的简化版,逊于 InteRecAgent。

**Lifelong 设置**:两种长对话配置 Long-Chat(交替 sharing history / target / casual chat,success 即终止)与 Long-Context(最多 50 轮)。
- Long-Chat(Table 3,Hit@50 / AT@50):Ours+LT Mem. 在 Steam 0.86 / 17.58、MovieLens 0.77 / 20.06、Beauty 0.74 / 25.88,均优于 GPT-4(0.70 / 20.56、0.71 / 24.06、0.06 / 49.42);激活长期记忆模块(+LT Mem.)进一步提升性能。
- Long-Context(Table 4,Hit@5 / AT@5):Ours+LT Mem. 在 Steam 0.79 / 2.70、MovieLens 0.83 / 2.84、Beauty 0.51 / 3.99,优于 GPT-4(0.74 / 3.05、0.82 / 3.03、0.09 / 5.71)。

结论:工具增强的推荐 agent 框架稳健,长期记忆模块对终身交互中捕捉用户偏好有效且必要。

## 在本 wiki 中的位置

本文是 [[llm-agents|llm-agent]] 与 [[recommender-systems|recommender-system]] 交叉方向的代表工作,把 [[tool-use]]、[[agent-memory]]、[[llm-planning]] 等 agent 技术落地到交互式推荐。其 plan-first execution 与 [[react]] 形成对比(降低 API 调用与延迟),反思机制承接 [[reflexion]] / [[self-refine]] / [[actor-critic]] 思路。与同样名为 RecAgent 的 [[recagent]](用户模拟)、[[p5]] 等 LLM4Rec 工作可对照阅读;RecLlama 展示了用 [[gpt-4]] 蒸馏数据微调 [[llama-2]] 小模型充当 agent 大脑的路径。作者来自 [[university-of-science-and-technology-of-china]] 与 [[microsoft-research-asia]]。
