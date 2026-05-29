---
type: source
subtype: paper
tags: [llm-agents, multi-agent-systems, multimodal, social-simulation, recommender-system, user-simulation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2412.09237
raw: raw/2412.09237.pdf
authors: [Yijun Liu, Wu Liu, Xiaoyan Gu, Xiaodong He, Yong Rui, Yongdong Zhang]
year: 2024
---

# LMAgent: A Large-scale Multimodal Agents Society for Multi-user Simulation

LMAgent 是一个基于多模态 LLM 的超大规模 agents 社会,可在电商场景中模拟一万以上 agent 的自主浏览、购买、评价、聊天与直播等行为,并能复现接近真实用户的 co-purchase 模式与从众等 emergent behavior。

## 问题

可信的多用户行为模拟对理解复杂社会系统至关重要。已有的 [[llm-based-agents]] 与 [[multi-agent-systems]](如 [[generative-agents]]、AgentVerse、[[chatdev]])大多存在两个局限:

1. 只考虑**少量 agent** 之间、且仅限**文本模态**的交互,忽视了真实世界中大量个体参与的多模态互动(图片、商品、直播等)。
2. 用 LLM 驱动大规模用户模拟在**计算上极其昂贵**,难以扩展到上万 agent。

论文以电商为具体场景,试图解决:(1) 如何整合多模态信息、增强 agent 的多模态分析能力以准确模拟用户行为;(2) 如何提升 LLM-based agent 的运行效率以支持大规模模拟。

## 方法

LMAgent 以多模态 LLM(ChatGPT 的 gpt-4-1106-preview 与 gpt-4-vision-preview,即 [[gpt-4]])为中央控制器,基于 [[langchain]] 实现。核心由多模态 agent 架构与 sandbox 环境组成:

- **多模态 agent 架构**:区分 internal 与 external behavior。
  - *Persona*:为每个 agent 赋予 name/gender/age/occupation/personal traits/购买偏好等属性,age 服从截断正态分布,偏好由 LLM 推断。
  - *Fast Memory(快速记忆机制)*:借鉴认知神经科学,设 sensor / short-term / long-term memory。sensor memory 用提示函数 f_c 压缩观测 o_i 为简洁句子;short-term memory 记录格式化记忆并用 LLM 打分重要性 I_i;long-term memory 用 [[clip]] 式 embedding(text-embedding-ada-002)的余弦相似度聚合,并采用基于时间与重要性的**遗忘公式**(对应 [[ebbinghaus-forgetting-curve]] 思想)。
  - *Memory Bank(记忆库)*:由于 agent 60% 以上的观测是"进入社媒/商城"等 basic behavior,记忆库缓存这些基本行为的 (action type, importance, embedding),直接检索而不调用 LLM,从而**减少约 40% 的多模态 LLM 调用**、提升效率。
  - *Planning 与 Reflection*:沿用 [[generative-agents]] 思路,设定高层目标并通过反思提炼洞见存入长期记忆。
- **External behavior**:shopping(browsing/searching/paging/viewing details/purchasing)、social(chatting/posting)、live streaming(少数"superstar" agent 直播带货)。
- **Self-consistency Prompting(自一致性提示)**:受 [[chain-of-thought]] 启发,把决策**拆成两个阶段**——第一阶段基于 persona 与观测生成内部画像总结 P1 = f_s(C_i, o_i);第二阶段结合 P1 与商品图文等多模态环境 E,推断最终动作 a = f_e(P1, E)。解耦使 LLM 每步只关注一部分决策,提升多模态决策的一致性与可信度。
- **Sandbox 环境**:用 **small-world model**(small-world topology network)初始化 agent 关系网络(Algorithm 1),使其具有更高 clustering coefficient 与更短 average path length,符合**六度分隔理论(six-degree-of-separation)**,既贴近真实社交网络又提升通信效率;时间复杂度随 agent 数 N 线性增长(kN)。Multi-user Simulator(Algorithm 2)让 agent 轮流行动并实时更新记忆。

## 结果

数据集为 Amazon Review Dataset(2.331 亿条购买/评论、2000 万+ 用户;见 [[amazon-reviews]])。

- **用户购买行为模拟**(指标 a@(a+b),沿用 [[recagent]] 的设定):在 1@6 / 3@6 / 3@10 / 3@10 等设置下,LMAgent 全面超过 Random、Embedding、Collaborative Filtering、[[recsim]]、[[recagent]]。平均(AVG)分数:LMAgent **73.04**,RecAgent 58.44,RecSim 56.27。相对最优 baseline 平均提升约 **29.34%**;在更难的 1@6 / 1@10 设置提升更显著,平均达 **32.80%**。
- **Agent 行为与人类对比**(Table II,Believability/Knowledge/Personalization/Social Norms/Social Influence,由 Humans 与 GPT-4 各打 1–5 分):LMAgent 各维度均接近人类水平,平均 4.30(人类 4.60),显著高于 Random 基线(3.08),多数维度与人类差异 ≤ 0.3。
- **大规模仿真**:支持 **10,000+ agent** 的社会模拟;从 1000 agent 跑 10 轮、以及 50 名志愿者操控 500 agent 的对照中,分析 behavior chain 与 behavior content,发现 LMAgent 能复现与真实用户数据**高度相似的 co-purchase 模式**,并自发出现 **herd behavior(从众/羊群效应)** 等 emergent behavior(大量 agent 集中购买某商品,即便并不需要)。

## 在本 wiki 中的位置

LMAgent 属于 [[llm-multi-agent]] 与 [[social-simulation]] 方向,是把 [[generative-agents]] 的"可信代理"思路扩展到**多模态 + 超大规模(万级)+ 电商**的代表性工作。它与 [[recagent]]、[[recsim]] 等 [[recommendation-simulator]] / [[user-simulation]] 工作相关,但侧重 agent 社会的群体行为(emergent behavior)而非单纯推荐评测。方法上复用了 [[fast-memory]]、[[memory-stream]]、[[self-consistency]]、[[chain-of-thought]] 与 [[small-world-model]] 等概念,可与 [[agent-memory]]、[[llm-agents|llm-agent]] 相关页面互链。
