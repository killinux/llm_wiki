---
type: source
subtype: paper
tags: [social-simulation, llm-agent, world-model, user-simulation, agent-based-modeling, social-intelligence]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2504.10157
raw: raw/2504.10157.pdf
authors: [Xinnong Zhang, Jiayu Lin, Xinyi Mou, Shiyue Yang, Xiawei Liu, Libo Sun, Hanjia Lyu, Yihang Yang, Weihong Qi, Yue Chen, Guanying Li, Ling Yan, Yao Hu, Yu Wang, Xuanjing Huang, Jiebo Luo, Shiping Tang, Libo Wu, Baohua Zhou, Zhongyu Wei]
year: 2025
---

# SocioVerse: A World Model for Social Simulation Powered by LLM Agents and A Pool of 10 Million Real-World Users

SocioVerse 是一个由 [[llm-agents|llm-agent]] 驱动的社会模拟 world model,借助 1000 万真实用户池和四个对齐模块,在政治、新闻、经济三大领域复现大规模人群行为。

## 问题

[[social-simulation]] 正在用虚拟个体与环境的交互来重塑社会科学研究,但现有方法在多个维度面临 **alignment(对齐)** 难题。论文将其归纳为四个核心问题:

- **Q1 环境对齐**:LLM 的静态知识无法跟上真实世界不断产生的新事件与新内容。
- **Q2 用户对齐**:真实用户群体复杂多样,难以枚举,需精确识别目标用户分布并赋予 agent 高保真的人口学/情境/行为画像。
- **Q3 交互机制对齐**:社会交互形式各异(人数、社会结构、信息传播方式),导致独立构建的任务专用 pipeline 重复劳动、缺乏通用性与可扩展性。
- **Q4 行为模式对齐**:即便环境与用户对齐,当前 LLM 仍存在固有偏差,难以推断不同类型用户的行为。

## 方法

SocioVerse 框架由四个对齐模块组成(见论文 Figure 2):

- **Social Environment(社会环境)**:注入实时事件与情境知识,分为 social structure(人口分布、文化规范等知识库)、social dynamics(持续抓取带时间戳与事件标签的新闻)、personalized context(借鉴 [[recommender-systems|recommender-system]] 思路为 agent 推送个性化内容)。
- **User Engine(用户引擎)**:核心是 **1000 万真实用户池**,从 X 与小红书(Rednote)收集真实社媒数字足迹,过滤广告与 bot 数据。用户池规模为 X 1,006,517 用户/30,195,510 帖,Rednote 9,158,404 用户/40,963,735 帖,合计约 1000 万人(媲美匈牙利或希腊全国人口)。配套 **demographic annotation 系统**:多个 LLM 作初始标注、人工评估精炼、再训练专用分类器实现低成本大规模标注,覆盖 15 个人口学维度(age、gender、vocation、race、income、education、settlement type、region、employment、marital status、religious、party、ideology、BigFive personality、hobbies)。
- **Scenario Engine(场景引擎)**:将真实社会情境抽象为四类模板——questionnaire(1-to-N)、in-depth interview(1-to-1)、behavior experiment(1-to-N 或 N-to-N)、social media interaction(N-to-N),并按用户池人口分布采样以放大单次模拟。
- **Behavior Engine(行为引擎)**:整合用户历史、交互机制与社会情境来预测个体行为,可由 traditional [[agent-based-modeling]](规则/数学模型,适合海量边缘用户)与 LLM agent(general/expert/domain LLM,通过非参 prompting 或参数化训练激活角色扮演能力)共同驱动。

论文实现了三个代表性场景:(a) 美国总统大选预测、(b) 突发新闻反馈分析(以 ChatGPT 发布为目标新闻)、(c) 中国全国经济调查。采样上分别用 IPF(iterative proportional fitting)与 IDS(identical distribution sampling)合成与抽取目标人群。

## 结果

实验对比 Llama-3-70b-Instruct、Qwen2.5-72b-Instruct、DeepSeek-R1-671b、[[deepseek-v3]]、GPT-4o、[[gpt-4o-mini]];开源模型部署于 8 张 NVIDIA RTX4090,经 vLLM,max tokens 2048,temperature 0.7。三场景规模:总统大选 331,836 agents / 12 demographics、突发新闻 20,000 agents / 7 demographics、经济调查 16,000 agents / 9 demographics。

- **总统大选预测**:GPT-4o-mini 与 Qwen2.5-72b 表现最优,Acc 均达 0.922(RMSE 0.046 / 0.037)。按 winner-takes-all 计,**超过 90% 的州投票结果被正确预测**,实现高精度宏观还原。DeepSeek-R1-671b 有时会"过度思考"导致精度下降。Battleground(摇摆州)子集更难:GPT-4o-mini Acc 0.800、Qwen2.5-72b Acc 0.800、DeepSeek-V3 Acc 0.867。
- **突发新闻反馈**:用 ABC attitude model(Affect-Behavior-Cognition)+5 点 Likert 设计 6 维问卷(PC、PR、PB、TR、FA、PA)。GPT-4o 在 KL-Div(0.196)、Qwen2.5-72b 在 NRMSE 上最贴近真实人群;potential audience set 驱动的模型行为与 ground truth 用户一致;Llama3-70b 表现较差。
- **全国经济调查**:覆盖 8 类支出。整体 Llama3-70b 最佳(KL-Div 0.016 / RMSE 0.026);各模型在 developed-region(GDP 前 10)子集表现更好。逐类 NRMSE(Table 5)显示**所有模型在 daily necessities 支出上预测最好、在 housing 支出上最差**。
- **消融实验(Table 4,总统大选)**:去掉 real-world user knowledge 或改用随机人口分布都会显著降低 Acc 与 RMSE。例如 Llama3-70b 完整为 Acc 0.733/RMSE 0.045,去知识降到 Acc 0.533,去知识且随机分布 RMSE 升至 0.386。说明 prior distribution 与 real-world knowledge 对模拟均很关键。

总体证明 SocioVerse 能以标准化 pipeline、最小人工干预支撑多样且准确的大规模社会模拟,但底层 LLM 选择会影响不同场景的精度。

## 在本 wiki 中的位置

本文属于 [[social-simulation]] / [[llm-agents|llm-agent]] 方向,把社会模拟封装为 [[world-model]],强调真实用户池驱动的 [[user-simulation]]。与 [[generative-agents]]、[[recagent]]、[[social-simulation]] 类工作相比,SocioVerse 的差异点在于 1000 万真实社媒用户池 + 人口学分类器对齐,以及统一的四模块框架。它结合了 [[agent-based-modeling]] 与 LLM agent 两种行为引擎,并触及 [[recommender-systems|recommender-system]] 的个性化内容机制。评测中使用的 [[deepseek-v3]]、[[gpt-4o-mini]] 等模型可作为模拟 backbone 的参照。研究由 [[fudan-university]] 等机构完成,可与 [[role-playing]]、[[social-intelligence]] 等概念互链。
