---
type: source
subtype: paper
tags: [llm-agent, social-simulation, agent-based-modeling, generative-agents, llm-multi-agent, computational-social-science]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2502.08691
raw: raw/2502.08691.pdf
authors: [Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li, Junbo Yan, Xiaochong Lan, Zhihong Lu, Zhiheng Zheng, Jing Yi Wang, Di Zhou, Chen Gao, Fengli Xu, Fang Zhang, Ke Rong, Jun Su, Yong Li]
year: 2025
---

AgentSociety 是一个把 LLM 驱动的生成式社会 agent、真实的城市-社会-经济环境与大规模分布式仿真引擎整合在一起的大型社会模拟器,可支持上万 agent、每天约 500 次交互,并复现极化、谣言传播、UBI、飓风冲击、城市可持续性等五类真实社会实验。

## 问题

理解人类行为与社会是社会科学的核心,而 [[agent-based-modeling]](ABM)长期受困于一个根本问题:模拟中的「个体」能否真正像人那样行动。传统 agent 由规则、方程或机器学习模型驱动,行为远离真实(例如把观点建模为标量/向量、把交互建模为方程),难以生成类人行为。LLM 的出现让 agent 具备类人的「心智」、推理与决策能力,但已有工作存在三大缺口:(1) agent 多只覆盖单一行为侧面,缺乏整合 emotion/needs/cognition 与多种社会行为的「完整社会个体」;(2) 缺少能提供物理约束与真实反馈的可信社会环境;(3) 缺少能支撑万级 agent 大规模交互、并服务社会科学方法(实验/访谈/调查/干预)的仿真引擎。论文要在这三个维度上同时突破,迈向「计算社会科学 2.0」。

## 方法

AgentSociety 由三大组件构成,并用一个评测框架沿「social agents / societal environment / simulation engine」三维度刻画(见 Table 1 与同类工作对比):

- **LLM 驱动的生成式社会 agent**:agent 设计植根于心理学(Maslow 需求层次)、经济学(DSGE)与行为科学(Theory of Planned Behavior、Gravity Model)等理论。每个 agent 含 Profile & Status(人口属性、性格、经济与社会关系)、三层 Mental Process(emotion / needs / cognition),并由心智驱动 mobility、social interaction、employment & consumption 等社会行为。mind 与 behavior 通过 **Memory** 耦合,Memory 分为 Profile、Status 与 Stream Memory(Event Flow 客观事件流 + Perception Flow 主观体验流)。mobility 采用「Need-Plan-Behavioral Sequence」与 [[gravity-model]] 做空间选择。
- **真实社会环境**:分 Urban Space(基于 OpenStreetMap/SafeGraph 的路网、AOI、POI,支持驾车/步行/公交/出租多模式出行,IDM+MOBIL 交通模型)、Social Space(社交网络 + supervisor 内容过滤/封禁)、Economic Space(firm/agent/government/bank 四类主体,工资、税收、Taylor Rule 利率、NBS 统计 GDP 等宏观指标)。
- **大规模社会仿真引擎**:把每个 agent 视为独立异步单元,基于 [[ray]] 做分布式多进程并行 + asyncio 协程,引入 agent group 复用连接以避免 TCP 端口耗尽;用 IoT 协议 [[mqtt]](emqx)做 agent 间消息传递,PostgreSQL 存储、MLflow 记录指标;并提供 intervention / interview / survey 的社会实验工具箱。LLM 后端实验使用 [[deepseek-v3]]。

## 结果

- **规模与效率**:支持 >10k agents、每 agent 日均约 500 次交互;并发实验中 individuals 从 1k 增至 1M、qps 从 10^2 到 10^5 时性能退化极小。每步平均耗时:10^3 agents 为 8.578×10⁻³ s,10^6 agents 仅 0.168 s。
- **消息系统**:MQTT(emqx)吞吐 44,702 msg/s,RabbitMQ 23,667 msg/s,Redis Pub/Sub 81,216 msg/s;Kafka 无法在 5 分钟内完成 10 万 agent 初始化。最低需求约 20,000 msg/s,MQTT 因自带 GUI 工具被选为默认实现。
- **极化实验**(gun control,100 agents):control 组 39% 更极化;homophilic(同质)组 52% 更极化;heterogeneous(异质)组 89% 变得更温和、11% 被说服,表明接触对立观点可缓解极化。
- **谣言/煽动性消息传播**(徐州「铁链女」事件):煽动性消息比普通内容传播更广、情绪强度更高;node-level 干预(封号)比 edge-level(断连)更有效。
- **UBI 实验**(Texas,100 agents,每月发 $1,000):引入 UBI 后消费上升、抑郁水平(CES-D 量表)下降,与 Texas 真实 UBI 实验结论一致。
- **飓风冲击**(Hurricane Dorian,Columbia SC,1,000 agents):飓风前活动水平 70%-90%,飓风期骤降至约 30%,过后回升,仿真出行曲线与真实数据趋势吻合。
- **城市可持续性**(Beijing,200 agents,6 个研究团队设计 eco-normative 干预):所有干预都提升环保规范并降低出行 CO₂;强调 personal norms 与 identity norms 的方案(Team 3)效果最佳,印证 personal norm 是亲环境行为最强预测因子。

## 在本 wiki 中的位置

本文是 [[social-simulation]] 与 [[generative-agents]] 方向的大规模工作,沿用并扩展了 [[generative-agents]](Park et al.)的「LLM agent 自驱动日常生活」范式,以及作者团队此前的 [[2023-s3-social-network-simulation]]、[[2023-econagent-macroeconomic-simulation]] 等。它与 [[concordia-generative-agent-based-modeling]]、Sotopia、RecAgent 等 LLM 社会模拟器同属 [[agent-based-modeling]] + [[large-language-models]] 交叉领域,但强调三件事的整合:完整社会个体、真实城市-经济-社会环境、万级 [[llm-multi-agent]] 分布式引擎。其工程栈([[ray]]、[[mqtt]]、[[deepseek-v3]])与 [[llm-agents|llm-agent]] 系统设计相关,应用面向 [[computational-social-science]] 的政策评估、风险防控与未来人-AI 社会研究。作者团队来自 [[tsinghua-university]],[[yong-li]] 等参与。
