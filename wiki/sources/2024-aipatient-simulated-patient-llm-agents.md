---
type: source
subtype: paper
tags: [llm-agent, medical-ai, simulated-patient, retrieval-augmented-generation, knowledge-graph, multi-agent-systems, medical-education]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2409.18924
raw: raw/2409.18924.pdf
authors: [Huizi Yu, Jiayan Zhou, Lingyao Li, Shan Chen, Jack Gallifant, Anye Shi, Jie Sun, Xiang Li, Jingxian He, Wenyue Hua, Mingyu Jin, Guang Chen, Yang Zhou, Zhao Li, Trisha Gupte, Ming-Li Chen, Zahra Azizi, Qi Dou, Bryan P. Yan, Yanqiu Xing, Yongfeng Zhang, Themistocles L. Assimes, Danielle S. Bitterman, Xin Ma, Lin Lu, Lizhou Fan]
year: 2024
---

# AIPatient:基于 LLM 多智能体的模拟病人系统

AIPatient 是一个由六个任务专用 [[llm-based-agents]] 驱动、结合 Reasoning RAG 工作流与基于 MIMIC-III 真实病历构建的知识图谱(AIPatient KG)的模拟病人系统,可用于医学教育中的高保真、可扩展病史采集训练。

## 问题

模拟病人(Simulated Patient, SP)系统是医学教育与研究的核心工具,但传统由真人扮演的 SP 成本高、规模受限,且评估方法主观、依赖评分者间一致性、泛化性差。已有的 [[large-language-models]] 模拟病人尝试面临四个核心问题:(1) 缺乏大规模、全面、多样的病人档案数据库;(2) 需要事实核查机制以减少 [[hallucination]] 并保证一致性;(3) 在扮演不同人格时灵活性不足;(4) 缺乏完善的评估框架。

## 方法

- **数据与知识图谱(AIPatient KG)**:从 MIMIC-III 数据库分层抽样 1,500 条去标识化真实病历(出院小结等非结构化文本 + 结构化表),用基于 LLM 的命名实体识别(NER)抽取症状、病史、生命体征、过敏、家族/社会史等实体,存入 Neo4j(AuraDB v5)图数据库。最终 KG 含 1,500 条住院记录、15,441 个节点、26,882 条边。
- **Reasoning RAG 智能体工作流**:在传统 [[retrieval-augmented-generation]] 基础上插入分步推理,分三阶段六个智能体:检索阶段(Retrieval Agent、KG Query Generation Agent),推理阶段(Abstraction Agent、Checker Agent),生成阶段(Rewrite Agent、Summarization Agent)。三个输入为 AIPatient KG、用户自然语言提问、对话历史。
- **人格建模**:基于 Big Five 框架组合生成 32 种人格类型,注入 Rewrite Agent。
- **模型选型与基准**:NER 与 QA 任务基准测试 11 个模型——5 个 [[claude]] 模型(Claude-3 Haiku、Claude-3-Sonnet、Claude-3.5 Sonnet、Claude-4-Sonnet、Claude-4-Opus)、3 个 GPT 系列([[gpt-4]] Turbo、[[gpt-4o]]、[[gpt-3-5-turbo]])、3 个开源模型(DeepSeek-V3 671B、Qwen3-32B、[[llama-3]] 70B)。因 MIMIC-III 数据使用协议禁止向在线服务传输 PHI,采用 Azure OpenAI、Amazon Bedrock,以及本地 Ollama 部署开源模型。
- **评估**:五个维度——知识库有效性(NER 的 F1)、QA 准确率(对 KG Query Generation Agent 做 8 种配置的消融研究)、可读性(Flesch Reading Ease 与 Flesch-Kincaid Grade Level)、稳健性(对每题改写 3 次,t 检验/ANOVA)、稳定性(32 种人格的数据损失比例 ANOVA)。还包含与真人模拟病人(H-SPs)的配对交叉用户研究、OSCE 式核查表,以及在 CORAL 肿瘤报告数据集上的分布外(OOD)评估。

## 结果

- **知识库有效性**:GPT-4-Turbo 的 NER 整体 F1 最高 = **0.89**;GPT-4o 次之 F1=0.75;Claude Sonnet/Opus 系列平均 F1=0.73。开源模型整体偏低。NER 黄金标准标注集 100 例,标注者间 span 级 F1=0.79。最终用 GPT-4-Turbo 构建 AIPatient KG。
- **QA 准确率(消融)**:全部六个智能体 + few-shot 配置达整体准确率 **94.15%**;去掉 AIPatient KG 与 Reasoning RAG 的基线明显更差(Family and Social History 类别降至 13.33%)。few-shot 平均提升 QA 准确率 11.1%。最佳配置下跨模型对比:GPT-4-Turbo 94.15% > Claude-4-Opus 90.80% > GPT-4o 89.02%;开源模型在 Medical History 有潜力(DeepSeek-v3-671B 79.31%、Qwen-3-32B 77.27%)但多数类别落后。
- **可读性**:Flesch Reading Ease 中位数 **68.77**(范围 10.91–99.23),Flesch-Kincaid Grade Level 中位数 **6.4**(峰值在六年级),阅读复杂度近似小说《Harry Potter》。
- **稳健性**:改写不显著影响整体 QA 准确率(ANOVA F=0.6126, p=0.5420),但 Medical History 类别显著受影响(F=5.3038, p=0.00589)。
- **稳定性**:32 个人格组中位数据损失 2%(范围 0%–5.88%),整体无显著差异。
- **用户研究(对比 H-SPs)**:招募 20 名医学生 + 10 名非医学志愿者。AIPatient 在多数维度匹配或优于 H-SPs:情感真实感 4.37 vs 3.74(t=3.41, p<0.01)、案例脚本一致性 4.32 vs 4.08、交互易用性 4.20 vs 3.79、技术可靠性 4.39 vs 3.79(t=2.68, p<0.01)、诊断准确支持 4.27 vs 3.87、临床推理技能提升 4.41 vs 3.97(t=2.19, p<0.05)。
- **OOD(CORAL 数据集)**:全智能体 + few-shot QA 准确率 81.04%;可读性 Flesch Reading Ease 中位数 70.6、Grade Level 6.8;稳健性与稳定性无显著差异。

## 在本 wiki 中的位置

本文是 [[llm-multi-agent]] 与 [[retrieval-augmented-generation]] 在医疗垂直领域的代表性应用:用结构化 EHR + 基于 LLM 的 NER 构建知识图谱,并以多智能体 Reasoning RAG 流程缓解 [[hallucination]]、提升一致性与可读性。与通用 [[generative-agents]]、社会模拟类 agent 工作不同,它把多智能体协作落在「模拟病人」这一具体教育/临床任务上,并提供了与真人 SP 的对照用户研究。可与 [[rag]]、[[llm-based-agents]]、[[multi-agent-systems]]、[[grounding]] 等条目互参;模型层面涉及 [[gpt-4]]、[[gpt-4o]]、[[gpt-3-5-turbo]]、[[claude]]、[[llama-3]] 的横向基准。
