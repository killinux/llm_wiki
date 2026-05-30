---
type: source
subtype: paper
tags: [llm-agents, social-simulation, agent-based-modeling, macroeconomics, computational-social-science]
created: 2026-05-30
updated: 2026-05-30
arxiv: 2310.10436
raw: raw/2310.10436.pdf
authors: [Nian Li, Chen Gao, Mingyu Li, Yong Li, Qingmin Liao]
affiliations: [Tsinghua University]
venue: "ACL 2024"
year: 2023
---

# EconAgent: Large Language Model-Empowered Agents for Simulating Macroeconomic Activities

用 [[large-language-models]] 驱动的、具备类人特征的 agent 做**宏观经济**仿真:每个 agent(家庭)逐月决定
**是否工作**与**消费倾向**,在含劳动 / 消费 / 金融市场与政府税收的环境中交互,自下而上涌现出经典宏观经济现象。
清华 [[yong-li]] 团队,ACL 2024(arXiv 2310.10436v4)。

## 问题
传统 [[agent-based-modeling]] 在宏观经济仿真中有两条路线:早期 **rule-based**(预设规则,对 agent 行为做过度简化假设)
与后来的 **learning-based**(用大规模行为数据训练神经网络)。两者都难以刻画 **agent 异质性**——定制规则需大量专家知识与
校准,定制网络则参数暴涨、训练困难;且通常只看当期、单一因素,忽视**多期市场动态**与多维宏观因素对决策的影响。

## 方法
仿真环境含四部分:劳动市场、消费市场、金融市场、政府税收;每步 = 一个月。
- **Agent 决策**:工作 `l_i ∼ Bernoulli(p^w_i)`(时薪按 Pareto 分布初始化,月薪 = 时薪 × 168 小时)+ 消费倾向 `p^c_i`(花掉财富的比例)。
- **感知模块 (perception)**:针对 agent profile 与真实经济情境生成提示,使 agent **自动呈现异质决策机制**。
- **记忆模块 (memory) + 反思 (reflection)**:让 agent 回顾过往个人经历与市场动态,从而把**多期宏观趋势**纳入决策——这是相对
  rule/learning-based agent 的核心增量。
- **政府**:按 **2018 美国联邦累进税率**征收个人所得税并均等再分配;**银行**按通胀/通缩用 Taylor Rule 式逻辑调整利率。

## 结果
设置:**N=100** agent,backbone **GPT-3.5-turbo-0613**,模拟 **20 年**;baseline 为 LEN、CATS、Composite(随机混用两规则)、
**AI-Economist**(RL,理性人假设)。
- **指标合理性**:EconAgent 的通胀第 3 年后稳定在 **−5%~+5%**、失业率在 **2%~12%**(贴近真实);而 rule/RL baseline 剧烈震荡
  (通胀时常 >20%),AI-Economist 失业率高达约 **46%**(异常,论文未报告)。
- **经济规律(核心卖点)**:**仅 EconAgent** 正确涌现 **Phillips 曲线**(失业↔工资通胀负相关,Pearson **r=−0.619, p<0.01**)与
  **Okun 定律**(失业增长↔实际 GDP 增长负相关,**r=−0.918, p<0.001**);rule-based baseline 甚至给出**错误的正相关** Phillips。
- **消融**:去 perception → 指标"过度平稳"(对经济变化不敏感);去 reflection → 前 3 年通胀异常逼近 **15%**——印证长期(季度级)环境感知的重要性。
- **机制**:回归(100 agent×240 月决策)显示税收/再分配/预期收入显著影响**工作倾向**,物价对两类决策都显著;消费倾向**随年龄递增**(合 Carroll 1997)。
- **外部干预(RQ4)**:在 2020-03 起的 prompt 注入 COVID-19 事件,成功复现 **2020 Q1 失业率骤升**。
- **局限**:仅建模家庭(无厂商定价/雇佣);只复现 stylized facts,未做政策优化与预测。代码开源(tsinghua-fib-lab/ACL24-EconAgent)。

## 在本 wiki 中的位置
属于 [[generative-social-simulation]] 的**经济模拟**子分支,与 [[2024-generative-ai-as-economic-agents]]、
[[2025-mmoagent-economic-simulation-mmo]] 相邻。是清华 [[yong-li]] 团队 [[2025-agentsociety-large-scale-social-simulation]]
的前身工作之一(AgentSociety 的经济空间设计沿用其思路)。连接 [[computational-social-science]]、[[agent-based-modeling]]、
[[memory-stream]](记忆-反思机制同源于 [[2023-generative-agents]])。
