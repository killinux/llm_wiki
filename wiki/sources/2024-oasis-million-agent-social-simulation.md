---
type: source
subtype: paper
tags: [social-simulation, llm-agents, agent-based-modeling, multi-agent-systems, recommender-system, scalability]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2411.11581
raw: raw/2411.11581.pdf
authors: [Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang, Ziyue Gan, Zhiyu Wang, Zijian Ling, Jinsong Chen, Martz Ma, Bowen Dong, Prateek Gupta, Shuyue Hu, Zhenfei Yin, Guohao Li, Xu Jia, Lijun Wang, Bernard Ghanem, Huchuan Lu, Chaochao Lu, Wanli Ouyang, Yu Qiao, Philip Torr, Jing Shao]
year: 2024
---

# OASIS: Open Agent Social Interaction Simulations with One Million Agents

OASIS 是一个通用、可扩展的基于 [[large-language-models]] 的社交媒体模拟器,能在 X 与 Reddit 等平台上模拟最多 100 万个 [[llm-agents]],用以复现信息传播、群体极化、从众效应等社会现象。

## 问题

近一年涌现了多个把规则型 [[agent-based-modeling]](ABM)升级为 LLM agent 的社交媒体模拟器,但存在两个痛点:

1. **专用性强**:每个模拟器只为某一特定场景(某一平台、某一现象)设计,迁移到其他平台或现象既费时又费资源,限制了它们在更广社会科学社区的可用性。
2. **规模太小**:现有工作通常只模拟少量 agent(从 2 个到上千个),而真实社交平台有数百万用户。许多群体行为(如涌现现象)只有在足够规模下才会显现,而 LLM-based ABM 的"规模"问题在文献中基本未被探索。

作者据此提出研究问题:(1) OASIS 能否适配不同平台与场景以复现真实世界现象?(2) agent 数量是否影响群体行为模拟的准确性?

## 方法

OASIS 建立在传统社交媒体平台结构之上,由五个核心组件构成:

- **Environment Server(环境服务器)**:用关系型数据库维护用户、帖子、评论、关系、行为轨迹(trace)、推荐表;支持动态更新(新用户、新帖、新关注关系随时间加入)。
- **RecSys(推荐系统)**:控制 agent 可见的信息流,是 OASIS 通用性的关键。X 平台用 in-network + out-of-network 两路召回,基于 [[clip]] 式的 TWHIN-BERT(在超过 70 亿条推文、100+ 语言上预训练)做兴趣相似度匹配,并结合 recency 与 poster 粉丝数(impact)排序。Reddit 平台复刻官方 hot-score 排序公式 `h = log10(max(|u-d|,1)) + sign(u-d)·(t-t0)/45000`(u 为 upvote,d 为 downvote,t0 = 1134028003)。
- **Agent Module(agent 模块)**:核心特性继承自 [[voyager]] 风格的 CAMEL 框架,含 [[memory-module]] 与 action module;支持 **21 种动作**(sign up、refresh、trend、search posts/users、create post、repost、follow/unfollow、mute/unmute、like/unlike、dislike/undo dislike、create comment、like/unlike/dislike/undo dislike comment、do nothing),并用 [[chain-of-thought]] 推理增强行为可解释性。
- **Time Engine(时间引擎)**:每个 agent 用 24 维向量表示每小时活跃概率,按概率激活而非全体同步;一个 time step = 3 分钟。
- **Scalable Inferencer(可扩展推理器)**:异步、分布式设计,agent/环境/推理服务作为独立模块通过通信通道交换数据;专用 manager 在多 GPU 间均衡请求。配套的大规模用户生成算法结合真实数据与关系网络模型,保留社交网络的 scale-free 特性(以 0.2 概率关注 core user),最多生成 100 万用户。

默认 backbone LLM 为 Llama3-8B-Instruct(ablation 还试了 Qwen1.5-7B-Chat、Internlm2-chat-20b)。

## 结果

**通用性 / 现象复现**:

- **信息传播(X)**:用 Twitter15/Twitter16 谣言检测数据中 198 个真实实例(9 类、每实例 100–700 用户)。OASIS 在 scale 与 max breadth 上能无明显偏移地复现真实传播趋势,normalized RMSE 约 30%;但 depth 趋势低于真实(归因于真实 RecSys 与用户画像更复杂)。
- **群体极化(X)**:用 196 个 core user 围绕一个困境("Halen 是否该冒险写小说")讨论 80 个 time step,每 10 步用 GPT-4o-mini(GPT-4o-mini)+ Safe-RLHF benchmark 判断意见是否更极端。随交互推进,agent 回复越来越保守/极端,且 **uncensored(去安全护栏)模型极化更严重**。
- **从众效应(Reddit)**:用 116,932 条真实评论 + 3,600 用户画像,并造 21,919 条反事实内容、生成 10,000 用户;分 down-treated(初始 dislike)、control、up-treated(初始 like)三组,模拟 40 或 30 步。Agent 在 down-treated 组比人类更易从众(human 的分数显著更高),说明 **agent 比人类更易受从众效应、人类更具批判性**。

**规模效应**:

- agent 数从 196 增到 10,196 时意见多样性显著提升;按 Safe-RLHF 标准评判,10,196 agent 的意见比 196 agent 显著更有帮助(1w vs 196:76.5% 更有帮助),扩到 100,196 时帮助度进一步提升。
- 反事实从众:agent 数从 100 增到 10,000,从众效应才明显显现,down-treated 组 disagree score 显著高于其他组——**大规模群体反而引导 agent 走向 self-correction**。

**百万级错误信息传播(X)**:196 个 core user + 100 万 regular agent,4 对真假新闻,60 步,core/regular 激活概率 0.1/0.01,在 24 张 A100 上一周内完成。基于 TF-IDF 相似度统计 733,824 条生成帖,发现**错误信息相关帖数持续超过官方新闻**,影响更持久。

**Ablation**:去掉 RecSys 会让信息传播过早终止(退化为单一 superuser 广播);TWHIN-BERT 优于 paraphrase-MiniLM-L6-v2;去掉 time engine 的时间特征(活跃概率全设 1.0)后无法复现真实传播节奏。效率:10k 规模每步约 15 分钟(4 张 A100)。

## 在本 wiki 中的位置

OASIS 属于 [[social-simulation]] / [[generative-agents]] 谱系,与 [[recagent]]、[[agentcf]] 等 [[user-simulation]] 工作相邻,但目标不同:OASIS 强调跨平台**通用性**与**百万级可扩展性**,而非单一推荐场景。它把 [[recommender-system]] 显式嵌入 [[multi-agent-systems]] 社会模拟,并用 [[agent-based-modeling]] 视角研究信息传播、群体极化、从众等宏观现象。在评估侧,它复用 [[llm-as-judge]](GPT-4o-mini + Safe-RLHF)判定意见的极端度与帮助度。其"规模带来涌现"的观察呼应了 [[emergent-abilities]] 在社会模拟语境下的体现。由 [[bytedance-research]] 之外的 Shanghai AI Lab、[[kaust]]、Oxford 等机构合作完成,代码以开源形式发布(camel-ai/oasis)。
