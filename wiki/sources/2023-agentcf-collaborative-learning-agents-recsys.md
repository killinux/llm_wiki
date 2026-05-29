---
type: source
subtype: paper
tags: [llm-agent, recommender-system, collaborative-filtering, user-simulation, agent-memory]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2310.09233
raw: raw/2310.09233.pdf
authors: [Junjie Zhang, Yupeng Hou, Ruobing Xie, Wenqi Sun, Julian McAuley, Wayne Xin Zhao, Leyu Lin, Ji-Rong Wen]
year: 2023
---

# AgentCF: Collaborative Learning with Autonomous Language Agents for Recommender Systems

AgentCF 把推荐系统里的**用户和物品都建模成 LLM agent**,通过二者的自主交互与协同反思来模拟用户-物品交互,从而把传统协同过滤的思想迁移到 [[large-language-models]] 驱动的 agent 上。

## 问题

现有 [[llm-agent]] 工作大多聚焦于模拟人类的**对话**(如 [[generative-agents]] 中的 Smallville),而对推荐系统中的**非语言行为**——比如用户点击/购买物品——探索不足。这类行为隐含用户偏好,但 LLM 难以理解 user-item 关系:经典协同过滤能捕捉"周五买尿布的人也倾向买啤酒"这种模式,而 LLM 会因为两件商品语义不相关而困惑。

同时,既有研究(如 [[recagent]])主要刻画**用户侧**行为,用通用 LLM 模拟用户,忽略了交互过程中的**物品侧建模**。作者认为这是单纯的 self-learning,而非真正建模二者关系的 collaborative learning。

## 方法

AgentCF 提出**基于 agent 的协同过滤**,核心是同时优化 user agent 和 item agent。

- **Memory Design(记忆设计)**:user agent 配有短期记忆 $M^s_u$(自然语言描述近期偏好,如"I enjoy listening to CDs")与长期记忆 $M^l_u$(历史偏好文本池);item agent 配统一记忆 $M_i$,记录自身特征及其采纳者(adopter)的偏好,由标题、类目等身份信息初始化。
- **Autonomous Interactions for Contrastive Item Selection(自主交互做对比选择)**:把真实用户行为序列当作"训练数据"。每步给 user agent 一对候选——正样本 $i^+$ 和负样本 $i^-$,并刻意引入流行度偏置和位置偏置(把高热度负样本排在正样本前)增加区分难度。user agent 据记忆选出 $i^o$ 并给出解释 $y_{exp}$。
- **Collaborative Reflection and Memory Update(协同反思与记忆更新)**:对比 agent 决策 $i^o$ 与真实交互记录得到反馈信号,在没有梯度的情况下,提示 user agent、正样本 item agent、负样本 item agent 一起反思并调整各自记忆。作者把这一过程类比为传统推荐模型的反向传播,称之为"semantic gradient"。
- **Preference Propagation(偏好传播)**:由于每条交互记录都会更新 user 和 item 双方记忆,物品记忆会聚合历史采纳者的偏好,并在后续交互中传播给新用户/新物品,从而隐式实现协同过滤的"like alike"。

推理阶段提供三种 prompting:基础版直接用短期记忆 $M^s_u$ 排序候选(AgentCF$_B$);AgentCF$_{B+R}$ 额外从长期记忆检索专门化偏好;AgentCF$_{B+H}$ 引入历史交互,让 LLM 充当序列推荐器。

## 结果

数据集为 Amazon Review 的 "CDs and Vinyl" 与 "Office Products" 两个文本密集子集;因 API 开销,从每个数据集各采样 dense/sparse 两个子集(各 100 用户)。评测用 leave-one-out + NDCG@{1,5,10},负样本随机采样,三次重复取平均。

- **总体性能**(Table 2):在多数场景下 AgentCF 优于 tuning-free 基线(Pop、BM25、[[chatgpt]] 零样本排序器 LLMRank)。例如 CDs$_{dense}$ 上 AgentCF$_{B+R}$ 取得 N@1=0.2333、N@5=0.4142、N@10=0.5405;Office$_{sparse}$ 上 AgentCF$_{B+H}$ N@10=0.5076。
- AgentCF 仅用约 0.07% 的全量数据训练,却能逼近甚至在部分场景超过同规模采样数据上训练的传统模型 [[bpr]]/[[sasrec]](sampled 版本),体现泛化能力。
- **消融**(Table 3):去掉 Autonomous Interaction、User Agent 或 Item Agent 性能均下降,验证三个组件均有效;尤其去掉 item agent 后变差,说明物品侧建模对捕捉二者关系关键。
- **偏置鲁棒性**(Figure 2):相比 LLMRank,AgentCF 对位置偏置和流行度偏置更稳定,说明它确实在按个性化偏好而非常识排序。
- **协同反思有效性**(Figure 3):优化后约 **95%** 的 user agent 能做出正确的对比选择。
- 还展示了 user-user 交互(读评论后决策)、item-item 交互缓解冷启动、偏好传播随 hop 数衰减(Figure 7,1-hop 比例 0.8125/0.6415)、以及多 agent 辩论协作生成广告等扩展实验。

## 在本 wiki 中的位置

本文属于"LLM agent 用于 [[recommender-system]] / [[user-simulation]]"方向,与 [[recagent]]、[[generative-agents]] 是同类用 agent 模拟用户行为的工作,但其创新在于**把物品也建模为 agent** 并做双向协同优化,把 [[collaborative-filtering]] 思想引入 [[llm-based-agents]]。方法上依赖 [[agent-memory]]/[[memory-module]] 与 [[self-reflection]] 机制(对比 [[reflexion]]、[[react]] 的 task-focused reflection,本文强调 collaborative reflection)。其无梯度的"语义梯度"优化思路可与 [[bpr]]、[[sasrec]] 等传统模型的梯度优化对照阅读。作者来自 [[renmin-university-of-china]]、UC San Diego 与 [[tencent-ai-lab]](WeChat),通讯作者 [[ji-rong-wen]] 团队。
