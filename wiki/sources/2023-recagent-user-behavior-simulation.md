---
type: source
subtype: paper
tags: [llm-agent, user-simulation, recommender-system, memory, social-simulation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2306.02552
raw: raw/2306.02552.pdf
authors: [Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Hao Sun, Ruihua Song, Wayne Xin Zhao, Jun Xu, Zhicheng Dou, Jun Wang, Ji-Rong Wen]
year: 2023
---

提出 RecAgent:用 [[large-language-models]] 驱动的 agent 框架在沙盒环境中模拟真实用户行为,实现近乎零样本的用户行为仿真,并用它研究信息茧房与从众行为等社会现象。

## 问题

人本 AI 应用(推荐系统、社交网络等)依赖大量真实、可靠的用户行为数据,但获取真实数据成本高、涉及隐私甚至伦理困境。已有的用户行为仿真方法存在三大局限:

1. **决策过程过于简化**:多用内积、MLP 等简单函数模拟用户决策,远离人类真实认知机制。
2. **依赖真实数据**:仿真本意是在缺乏真实数据时生成数据,但传统方法仍需真实数据集训练仿真器,陷入"鸡生蛋"困境,且只能复现已知数据集的行为模式。
3. **仿真环境单一**:通常只局限于单一场景(如推荐系统或社交网络),无法捕捉多环境之间的相互影响。

## 方法

借鉴认知神经科学,为每个用户构建一个 LLM-based agent,包含三个模块:

- **Profile 模块**:确定用户背景,包括 ID、姓名、性别、年龄、职业、性格特质(traits,如"富有同情心")和兴趣(item 类别,如"科幻电影")。
- **Memory 模块**:模仿人类记忆机制设计三类记忆——sensory memory(将环境原始观测压缩为简洁信息并打重要性分)、short-term memory(中间层,反复遇到相似观测时被增强并转入长期记忆)、long-term memory(存储可复用/可泛化信息,并支持 self-reflection 生成高层抽象)。
- **Action 模块**:在推荐系统中支持 4 类行为(搜索、浏览、点击、翻页),并额外支持 2 类社交行为(一对一 chatting、一对多 broadcasting)。

系统以 round-by-round 方式运行;用 **Pareto 分布**建模不同 agent 的活跃度,体现长尾特性(少数用户高度活跃,多数用户低频)。仿真器对推荐算法 agnostic,支持系统干预(编辑 agent profile)和人机协作(真人扮演 agent 或"访谈"agent)。

## 结果

**推荐行为可信度(判别能力)**:在 [[movielens]](Movielens-1M)上采样 20 个用户,留出最后 a 个交互作为 ground truth,混入 b 个负样本组成 (a+b) 推荐列表,用指标 p = Σ |T_u ∩ S_u| / |T_u| 评估。在多组 (a,b) 设置下,RecAgent 显著优于传统基线 [[recsim]] 和 Embedding 方法。平均而言,RecAgent 比最佳基线高约 **68%**,仅比 Real Human 低约 **8%**。

**生成能力(对抗主观评测)**:三位标注者判断哪条行为序列更像真人。N=5 时 RecAgent 的胜率 **45.0%** 显著高于 RecSim 的 **33.3%**;序列变长(N=10)时 RecAgent 仍领先约 **5.0%**。

**Chatting / Broadcasting 行为**:无需领域微调,运行 5/10/15 轮后由标注者按 profile 和 behavior 一致性打分(1-5)。多数得分高于 4;但 15 轮后所有得分低于 4,作者推测记忆累积过多导致 LLM 注意力分散。

**Memory 机制可信度**:在"总结短期记忆"任务中约 **40%** 标注认为 RecAgent 更像真人,仅比 non-expert human 低 1.7%;"生成反思"任务中 RecAgent 略超约 3.3%。消融显示:去掉 short-term memory 会严重降低信息量(informativeness),去掉 long-term memory / reflection 会降低相关性(relevance),完整记忆模块取得最佳相关性与可比的信息量。

**社会现象研究**:用 50 个 agent + 矩阵分解(MF)推荐算法复现了**信息茧房**(熵随轮次下降),并验证了缓解策略——Soc-Strategy(增加不同兴趣的好友)和 Rec-Strategy(向推荐列表注入随机性/替换 item)均能提升熵。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 与 [[user-simulation]] 交叉方向的代表性工作,是 [[generative-agents]]("斯坦福小镇")思路在推荐与社交仿真场景的延伸。其 [[memory-module]](感觉/短期/长期记忆 + self-reflection)设计与 generative agents 一脉相承。可与基于 LLM 的推荐研究、社会模拟类 agent 工作交叉参照。
