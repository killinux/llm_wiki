---
type: source
subtype: paper
tags: [llm-agent, multi-agent-collaboration, recommender-system, role-playing, reflection, sigir]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2402.15235
raw: raw/2402.15235.pdf
authors: [Zhefan Wang, Yuanqing Yu, Wendi Zheng, Weizhi Ma, Min Zhang]
year: 2024
---

# MACRec: a Multi-Agent Collaboration Framework for Recommendation

MACRec 是一个由清华大学提出的、用多个角色各异的 LLM agent 协作直接完成推荐任务的框架(SIGIR'24 demo),区别于以往用 agent 做用户/物品模拟的工作,它让 Manager、User/Item Analyst、Reflector、Searcher、Task Interpreter 等专门化 agent 协同求解推荐问题。

## 问题

[[recommender-system]] 在电商、社交媒体等领域至关重要。[[large-language-models]] 催生的 [[llm-agent]] 具备语义理解、规划与决策能力,为更细粒度、上下文感知的推荐打开了空间。作者指出当前研究存在两条主线及其不足:

- **模拟导向(simulation-oriented)**:如 [[recagent]]、Agent4Rec、[[agentcf]] 等,用 agent 模拟用户行为或用户-物品交互以辅助评估,但难以真正集成进推荐系统本身。
- **推荐导向(recommender-oriented)**:如 InteRecAgent、RecMind,主要用**单个** agent 配合规划、记忆与工具(如搜索引擎)来构建推荐器;但推荐场景中存在多种复杂决策任务,单 agent 表现不佳。已有的多 agent 推荐框架 RAH 又只有有限的 agent 类型且协作模式固定,且无公开代码/demo。

作者认为接近人类工作流的 [[multi-agent-collaboration]] 能借助集体智能更好地完成复杂任务,但此前尚无人在推荐场景中系统探索其潜力。MACRec 自称是首个支持多类型 agent、面向多样推荐场景的开源框架。

## 方法

MACRec 提供可定制的、由 LLM 驱动并配备工具的多类型 agent,通过协作直接构建推荐器(而非做模拟)。核心 agent 角色:

- **Manager**:中枢,为任务分配子任务并执行主流程,交替进行 Thought、Action、Observation 三步(类 [[react]] 范式);在 Action 阶段可直接给答案或向其他 agent 求助,其他 agent 的回复进入 Manager 的 Observation。
- **Reflector**:在 Manager 进行第二次及以上重试时介入,判断上一轮答案是否还有改进空间并给出反思建议(如纠正答案格式、补充被忽略的高分历史物品),体现 [[self-reflection]]/[[reflexion]] 思想。
- **User/Item Analyst**:分析用户偏好与物品属性,可调用 info database(获取用户画像、物品属性)与 interaction retriever(获取当前时刻前的交互历史)两个工具。
- **Searcher**:用搜索工具(如 Wikipedia)按 Manager 要求检索并摘要回传相关信息,体现 [[tool-use]]。
- **Task Interpreter**:把对话历史翻译成可执行的推荐任务描述,可调用文本摘要工具压缩长对话历史。

框架支持按场景选择/定制不同 agent 组合,并提供在线 Web 界面可视化协作过程。Manager 给出排序答案、Reflector 反思、再由 Manager 重试,形成 [[closed-loop-feedback]] 式协作。论文引用了 [[autogen]]、CAMEL 等通信式多 agent 系统作为相关工作。

## 结果

本文是 SIGIR'24 的 demo/资源型论文,**未给出定量 benchmark 数字**,重点在于框架设计与应用演示:

- 在四类推荐场景给出 agent 选择方案(Table 2):评分预测(RP)需 User/Item Analyst、可选 Reflector;序列推荐(SR)需 User Analyst 与 Reflector;解释生成(EG)需双 Analyst 与 Searcher;对话推荐(CR)需 Searcher 与 Task Interpreter。
- 案例研究(Figure 2):用户表达喜欢电影《Schindler's List》并求类似历史片,Task Interpreter 归纳任务,Manager 两轮调用 Searcher 检索"历史题材电影"与"与《Schindler's List》相似的电影",最终推荐《Amistad》。
- 在 Table 1 的对比中,MACRec 同时具备 Multi-type Agents、Diverse Rec. Scenarios 与 Open-source 三项,优于 [[recagent]]、Agent4Rec、[[agentcf]]、RAH、RecMind、InteRecAgent 等先前工作。
- 代码与演示视频开源于 https://github.com/wzf2000/MACRec 。

## 在本 wiki 中的位置

本文把 [[multi-agent-collaboration]] 引入 [[recommender-system]],是 [[llm-agent]] 应用于推荐的代表性框架。其设计复用了 [[react]] 的 Thought-Action-Observation 循环、[[self-reflection]] 的反思机制与 [[tool-use]];在多 agent 系统脉络上与 [[autogen]]、[[chatdev]]、[[metagpt]] 等通信式协作框架相呼应,但聚焦推荐这一垂直场景。与 [[recagent]]、[[agentcf]] 等"用 agent 做 [[user-simulation]]"的路线形成对照——MACRec 直接用 agent 充当推荐器。
