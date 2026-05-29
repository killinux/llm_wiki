---
type: source
subtype: paper
tags: [agent, benchmark, llm-as-agent, evaluation, reasoning, decision-making]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2308.03688
raw: raw/2308.03688.pdf
authors: [Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen Men, Kejuan Yang, Shudan Zhang, Xiang Deng, Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng Shen, Tianjun Zhang, Yu Su, Huan Sun, Minlie Huang, Yuxiao Dong, Jie Tang]
year: 2023
---

AgentBench 是首个系统性评估 "LLM-as-Agent"(把 LLM 当作智能体)能力的多维基准,横跨 8 个交互式环境,对 29 个 API 与开源(OSS)模型进行了大规模测评,揭示了顶级商业模型与开源模型之间的巨大差距。

## 问题

业界普遍认可 LLM 作为自主智能体的潜力(如 [[autogpt]]、BabyAGI 等应用),但缺乏一个系统、标准的基准来定量评估 LLM 在具有挑战性的交互环境中的推理与决策能力。已有的智能体评估存在三类局限:历史上的文本游戏环境动作空间封闭离散、只关注常识 grounding;近期的具身智能体依赖复杂的多模态模拟器,与 LLM 的纯文本实际用例不符;多数基准只聚焦单一环境,无法全面刻画 LLM 在多样应用场景下的能力。因此需要一个面向纯文本 LLM、覆盖真实任务的综合性 agent 评估基准。

## 方法

作者将 "LLM-as-Agent 的交互式评估" 形式化为一个**部分可观测马尔可夫决策过程(POMDP)** $(\mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \mathcal{U}, \mathcal{O})$,并统一采用最朴素的 [[chain-of-thought]](CoT)提示(单轮内同时输出 "Thought" 与 "Action"),不使用多次采样、ensemble、reflection 或 search,以贴近最常见、最廉价的部署方式;推理时设 temperature=0(贪婪解码)。

AgentBench 包含 **8 个不同环境**,分为三类 grounding(其中 5 个为首次构建):
- **代码类(Code)**:Operating System(Ubuntu Docker 中执行 bash,指标 SR)、Database(真实 SQL 查询,指标 SR)、Knowledge Graph(基于 [[freebase]] 的多跳问答,指标 F1)。
- **游戏类(Game)**:Digital Card Game(基于 2021 THUAC 的 Aquawar,指标 win rate)、Lateral Thinking Puzzles(海龟汤,指标 game progress)、House-Holding(基于 [[alfworld]],指标 SR)。
- **网页类(Web)**:Web Shopping(基于 [[webshop]],指标 reward)、Web Browsing(基于 [[mind2web]],改造为无需微调的 prompt 评估,指标 step SR)。

数据集分 Dev/Test 两个 split,规模分别约 269 与 1,014 条,总推理调用约 3k+11k(与 [[mmlu]] 量级相当)。**总分计算**:先把每个任务在所有模型上的平均分归一化,再用各任务在所有模型上的平均分的倒数作为固定权重(weight$^{-1}$)做加权平均,避免高分任务(如 Web Shopping)主导总分。配套发布了基于 Server-Client、HTTP 协议、Docker 隔离的即插即用评估工具包。

作者还把 agent 的结束原因归为五类:Context Limit Exceeded(CLE)、Invalid Format(IF)、Invalid Action(IA)、Task Limit Exceeded(TLE)、以及正常 Complete。

## 结果

在 29 个模型的测评中,**顶级商业模型与开源模型差距显著**:全部 API 模型的总分(OA)均高于 1.00,而开源模型(均 ≤ 70B)表现远逊。

- [[gpt-4]](0613)总分 **4.01**,在 8 个数据集中的 6 个上夺得最佳;在 House-Holding 上达到 78.0% 的成功率,具备一定实用性。
- [[claude-2]](2.49)与 claude(2.44)整体明显优于 [[gpt-3-5-turbo]](2.32)。claude-3(opus)总分 3.11,glm-4 总分 2.89。
- 开源阵营最强的是 codellama-34b,总分仅 **0.96**,仍明显落后于 gpt-3.5-turbo;开源模型平均总分 **0.51**,而 API 模型平均 **2.32**。
- 主要失败原因分析(Table 4):占比最高的是 **Task Limit Exceeded(TLE)**,反映长程推理与决策能力不足;Database 与 Digital Card Game 多见 Invalid Format(格式不达标),House-Holding 与 Web Browsing 多见 Invalid Action(动作越界)。

关键发现:
- **代码训练是把双刃剑**:用代码微调对遵循静态流程的任务(如 Web Shopping)有帮助,但会损害通用推理(codellama 在 Digital Card Game、Operating System 上不如 llama-2)。
- **高质量对齐数据很关键**:vicuna-13b(用 [[gpt-4]]/gpt-3.5 生成的 ShareGPT 数据对齐)显著优于同底座从零对齐的 llama-2-13b,甚至可比肩 3 倍大的 codellama-34b。
- **llama-2-13b 与 llama-2-70b 表现意外接近**,作者推测 70B 预训练不充分(按 scaling law 应训练更多 token)或指令对齐不足。

## 在本 wiki 中的位置

本文是 [[llm-agent]] 评估领域的奠基性 [[benchmark]],由 [[tsinghua-university]]([[thudm]])联合 Ohio State、UC Berkeley 提出。它将 [[chain-of-thought]] 与多轮交互结合,系统量化了 [[gpt-4]]、[[claude-2]]、[[gpt-3-5-turbo]] 等模型在真实环境中的智能体能力,可与 [[mmlu]] 等静态知识基准、以及 [[webshop]]、[[alfworld]]、[[mind2web]] 等单环境 agent 数据集对照阅读。其揭示的 "长程推理/决策/指令遵循是 usable agent 的主要瓶颈" 与 "代码训练双刃剑" 等结论,为后续 agent 模型(如 [[autogpt]] 类应用)训练方向提供了参考。
