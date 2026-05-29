---
type: source
subtype: paper
tags: [llm-agent, social-simulation, agent-based-modeling, efficiency, generative-agents, urban-simulation, benchmark]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.21286
raw: raw/2410.21286.pdf
authors: [Yuwei Yan, Qingbin Zeng, Zhiheng Zheng, Jingzhe Yuan, Jie Feng, Jun Zhang, Fengli Xu, Yong Li]
year: 2024
---

# OpenCity: A Scalable Platform to Simulate Urban Activities with Massive LLM Agents

OpenCity 通过「LLM 请求调度器」+「group-and-distill 提示优化」两层系统级与提示级优化,把大规模城市 [[llm-agent]] 模拟的单 agent 耗时加速约 600 倍,使得 10,000 个 agent 的一天活动可在 1 小时内于普通硬件上完成。

## 问题

[[agent-based-modeling]](ABM)长期用于研究个体行为如何聚合成城市层面的复杂社会现象,而 [[large-language-models]] 驱动的 [[generative-agents]] 能以前所未有的真实度模拟人类行为。但 LLM agent 的模拟存在严重的扩展瓶颈:

- LLM 本身推理慢,商用 LLM 还要通过 API 访问,网络传输与等待响应占用了单次请求的绝大部分时间。
- 城市 LLM agent 的 prompt 含动态元素(不断变化的 memory 与感知到的环境),无法像静态 agent 那样简单复用单次 LLM 响应——复用会破坏 agent 独立性、降低模拟保真度。
- Park 等人的开创性 [[generative-agents]] 工作仅模拟了 15 个 agent;现有 LLM 推理加速系统(FlashAttention、vLLM、SGLang 等)针对通用推理,未利用城市 generative agent 的特性。

## 方法

OpenCity 从系统级与提示级两方面加速,并提供易用的 Web 门户:

- **LLM Request Scheduler(系统级):** 关键观察是单次请求的核心耗时在「等待响应」。利用操作系统的 IO 多路复用(Linux 的 epoll)并行化多个 agent 的相互独立的 LLM 请求,实现对数据传输的「零感知」(Time saving#1);维护可复用连接池避免反复建立/销毁 TCP 连接(Time saving#2);把 agent 的本地 CPU 任务(如更新 memory、检索附近地点)当作 "local IO" 卸载到多核并行(Time saving#3)。
- **Group-and-Distill Meta-Prompt Optimizer(提示级):** 用「群组信息」替代逐个 agent 的静态属性来共享 prompt,同时保留 agent 的动态属性。包含两部分:**In-context Prototype Learning(IPL)** 利用 [[in-context-learning]] 对前 M 个 agent 聚类并生成群组描述,再用阈值 T 把其余 agent 分入已有群组或新建群组;**Distill Meta-Prompt** 借助 [[chain-of-thought]],把原始 prompt 按 summarization / context extraction / information sharing / rewriting 四步改写为蒸馏后的元提示,运行时把同组 agent 的请求聚合为单个 Distill 请求,降低请求数与 token 消耗。
- **Web Portal:** 提供拖拽式 agent blueprint(基于 [[langchain]]、[[autogpt]] 等框架)、免代码配置、实时监控与可视化(如 OD 地图)。

agent 主体采用 [[generative-agents]] 的 perception–planning–reflection 框架(带 [[memory-stream]]),并以经典规则模型 EPR(Explore and Preferential-Return)作为对比。

## 结果

在 6 座城市(Beijing、New York、San Francisco、London、Paris、Sydney)上、10,000 个 agent 的实验(华为 ECS,64 核 Xeon、256GB RAM):

- **加速:** 平均单 agent 0.058s、平均加速 635.3x;LLM 请求数平均减少 73.7%、token 消耗平均减少 45.5%。可扩展性随 agent 规模(10→10,000)提升,单 agent 耗时从 36.25s 降到约 0.06s。
- **保真度(location choice,JSD / top-1 hit rate):** 与 batch prompting 相当但波动更小、token 更省,远优于复用式的 archetype prompting(后者 T1 仅个位数百分比)。用强模型时 top-1 命中率最高达 96%([[gpt-4o-mini]] 跨城 T1 多为 71–86%;用 GPT-4o 在 NY/Pa 达 96–97%)。
- **复现城市动态(1,000 agent,RMSE/ODMSE/SMSE 三层指标):** Generative Agent 与 EPR 均能低误差复现;LLM agent 在多数城市表现持平或优于规则式 EPR(如 London RMSE 6.24 vs 25.7、Sydney 15.1 vs 54.2)。
- **反事实案例(实测城市隔离):** 把不同收入 agent 均匀分布以消除居住隔离后,NY 平均隔离指数从 0.845 降到 0.172、SF 从 0.665 降到 0.232,提示区域差异是隔离的主因;还能用自然语言与 agent 对话以提升可解释性。

## 在本 wiki 中的位置

OpenCity 属于 [[social-simulation]] / [[multi-agent-systems]] 方向,是把 [[generative-agents]]、[[recagent]] 这类 [[llm-agent]] 模拟从十几个 agent 扩展到万级规模的关键基础设施工作。它的贡献偏「系统与提示效率」,与面向推理任务的 [[autogpt]]、[[metagpt]]、[[chatdev]] 等任务型 agent 形成互补;其首次为城市 generative agent 建立的对比 benchmark 也使 [[agent-based-modeling]] 的反事实政策分析成为可能。作者来自 [[tsinghua-university]] 与香港科技大学(广州)。
