---
type: source
subtype: paper
tags: [social-simulation, llm-multi-agent, social-intelligence, role-playing, llm-as-judge, negotiation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2504.16122
raw: raw/2504.16122.pdf
authors: Xuhui Zhou, Zhe Su, Sophie Feng, Jiaxu Zhou, Jen-tse Huang, Hsien-Te Kao, Spencer Lynch, Svitlana Volkova, Tongshuang Sherry Wu, Anita Woolley, Hao Zhu, Maarten Sap
year: 2025
---

SOTOPIA-S⁴(Simple Social Simulation System)是一个面向非技术用户的快速、灵活、可扩展社会模拟系统,让研究者无需编程即可通过自然语言设计、运行并评估多轮、多方的 LLM 社会交互,并支持自定义评估指标。

## 问题

通过 [[large-language-models]] 进行社会模拟是研究社会科学问题与 LLM agent 行为的有力途径,但现有多智能体框架(如 [[autogen]]、CrewAI、OASIS、S3、[[generative-agents]] 以及前作 [[sotopia]])存在技术门槛:要么需要大量编程专业知识来配置模拟,要么缺少自然语言配置、缺少 Web 界面、缺少内置自动评估或多方交互支持(见论文 Table 1)。本文希望降低门槛,让缺乏编程背景的实践者也能:(1)用自然语言规范设计模拟;(2)通过自动并行高效运行大量交互;(3)通过简单配置自定义评估指标;(4)通过 Web 界面管理模拟与结果。

## 方法

SOTOPIA-S⁴ 把核心模拟逻辑与用户界面分离,由三部分组成:

- **模拟引擎(SOTOPIA Engine)**:高性能引擎,后台处理异步执行、LLM API 管理与数据持久化。引擎以 pip 包形式提供。
- **SOTOPIA-API**:基于 FastAPI 的 RESTful 协议。提供非流式操作(GET/POST/DELETE 管理 scenarios、characters、relationships、episodes、evaluation metrics;刻意省略 PUT 以避免并发修改不一致)与流式操作(WebSocket,发送 "START_SIM" 启动模拟、实时回传结果、结束时发送 "FINISH_SIM")。
- **Web UI**:无需编程的网页应用,用于可视化与编辑 scenarios/characters、运行模拟、查看 episode 评估结果。

模拟配置要素继承自 [[sotopia]]:scenario(场景/上下文)、characters(角色画像,含 big-five 人格、moral foundations 等)、relationships(family/friend/romantic/acquaintance/stranger 五类,控制信息可见性)、episodes(单次交互会话,默认最多 20 轮)。每个 agent 每回合可选 5 种动作:speak、non-verbal communication、physical action、do nothing、leave。

核心技术:

- **异步交互框架**:用 message broker 管理消息传递,实现信息不对称(stranger 看不到他人公开信息,family 可见除 secret 外的大部分信息),支持 dyadic 与 multi-party 交互并行运行。
- **Turn-taking 两种模式**:round-robin(固定顺序,适合 Avalon 这类社会推理游戏)与 simultaneous(异步从消息队列取信息后自行决定是否回应,受阅读速度/认知处理等影响,贴近群聊)。
- **模拟评估**:默认评估套件用 LLM 按维度推理打分(继承自 [[sotopia]]):Goal Completion[0–10]、Believability[0–10]、Knowledge[0–10]、Secret[-10–0]、Relationship[-5–5]、Social Rules[-10–0]、Financial and Material Benefits[-5–5];属于 [[llm-as-judge]] 路线,并支持自定义指标。
- **Multi-LLM 集成**:通过 LiteLLM 网关接入 100+ LLM([[openai]]/[[claude]]/Gemini 等),也可用自有实例或微调模型。
- **持久化**:用 Redis 作为高性能内存数据存储,自动处理序列化、缓存与持久化。

## 结果

论文用两个 use case 与一次压力测试展示系统能力:

- **Dyadic Hiring Negotiation(二元招聘谈判)**:AI 招聘经理与模拟人类候选人就 start date、salary 等条款谈判,采用零和计分(总分固定 8400)。研究人格特质 {Extroversion, Introversion} × {High/Low-Agreeableness} 对结果的影响。Table 2 显示 agreeableness 显著影响成交率:High Agreeableness 的 Deal Made = 0.95、Points = 5227.5;Low Agreeableness 的 Deal Made = 0.00、Points = 4180;Extraversion 0.60 / 4802.5;Introversion 0.60 / 4477.5。即高宜人性 agent 成交率与得分都明显更高,与社会科学发现一致。
- **Multiparty Planning Scenario(多方规划)**:5 个 agent 讨论集体计划,初始偏好分歧(Alex 倾向工作项目、Taylor 主张露营、Sam/Riley/Jamie 中立)。通过群聊与私信交互,观察到少数意见 agent(如 Taylor)在群体多数偏好与 Alex 强势主张影响下逐步调整立场,展示了个体偏好与集体决策的相互作用。
- **大规模模拟**:在 Ubuntu 22.04、16GB RAM、Intel Core i7-14650HX CPU 的单台 Linux 服务器上压力测试,该配置可支持至多 150 个 agent 异步互相通信,系统每秒可处理至多 389 次交互。multi-party 情形下每个 agent 独立进程,可分布到不同服务器/机器,agent 数量仅受算力限制。

## 在本 wiki 中的位置

本文是 [[sotopia]] 系列的工程化与产品化延伸,把 [[social-simulation]] 与 [[llm-multi-agent]] 研究从需要编程的框架变为面向非技术用户的系统(引擎 + API + Web UI),与 [[generative-agents]]、[[autogen]]、[[sotopia-eval]] 等 [[social-intelligence]] / [[role-playing]] 工作并列。其评估默认走 [[llm-as-judge]] 路线。作者来自 [[carnegie-mellon-university]]、Aptima、[[stanford-university]] 与香港中文大学,核心作者 [[xuhui-zhou]]、[[hao-zhu]]、[[maarten-sap]]、[[tongshuang-sherry-wu]] 等。
