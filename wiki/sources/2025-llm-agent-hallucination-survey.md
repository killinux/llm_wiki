---
type: source
subtype: paper
tags: [hallucination, llm-agents, agent-safety, survey, taxonomy, multi-agent-systems, tool-use, agent-memory]
created: 2026-05-29
updated: 2026-05-29
arxiv: "2509.18970"
raw: raw/2509.18970.pdf
authors: [Xixun Lin, Yucheng Ning, Jingwen Zhang, Yan Dong, Yilong Liu, Yongxuan Wu, Xiaohua Qi, Nan Sun, Yanmin Shang, Kun Wang, Pengfei Cao, Qingyue Wang, Lixin Zou, Xu Chen, Chuan Zhou, Jia Wu, Peng Zhang, Qingsong Wen, Shirui Pan, Bin Wang, Yanan Cao, Kai Chen, Songlin Hu, Li Guo]
year: 2025
---

# LLM-based Agents Suffer from Hallucinations: A Survey of Taxonomy, Methods, and Directions

这是第一篇系统综述 [[llm-agent]] 中"agent 幻觉"(agent hallucinations)的论文,把 agent 拆成"内部状态(belief state)+ 外部行为"两部分,提出涵盖 reasoning / execution / perception / memorization / communication 五大类的幻觉 taxonomy,梳理其触发原因、缓解与检测方法。

## 问题

以往 [[hallucination]] 研究主要聚焦自然语言生成(NLG)层面,把幻觉划分为 factuality(与事实不符)和 faithfulness(偏离用户输入)两类。但 [[llm-based-agents]] 是更复杂的智能系统,具备目标导向的推理与行动能力,典型由 brain、perception、action 三大模块组成。因此 agent 幻觉不再是"语言错误",而是发生在 agent pipeline 任意阶段的、被过度自信的"类人行为"。作者指出其相比 LLM 幻觉的三个关键差异:

- **类型更多样**:由多模块交互产生的复合行为,而非单模型的单步响应错误。
- **传播链更长**:跨越多步、多状态转移,可在 perception、reasoning 等中间过程中产生并累积放大。
- **后果更严重**:涉及"物理上可执行"的错误,错误的 embodied action 会直接影响任务执行、设备与现实世界用户体验。

现有 LLM agent 综述多关注架构设计与应用,对 agent 幻觉的重视不足,本文填补这一空白。

## 方法

作者先给出 [[llm-based-agents]] 的形式化定义:把 agent 与环境的交互建模为 POMDP(部分可观测马尔可夫决策过程)八元组 E=(S,A,T,G,O,Z,R,γ);agent 维护 belief state b_t,在每个 loop 中执行 Reasoning → Execution → Feedback → Environment Transition → Perception → Memorization → Belief Update;在 [[multi-agent-systems]](MAS)中额外引入 Broadcasting 与 Structure Evolution 两步,通信结构 G_t 随时间演化。

基于"内部状态 / 外部行为"的二分,提出 agent 幻觉 taxonomy,五大类(及九个子类):

1. **Reasoning Hallucinations**:看似合理实则逻辑有缺陷的 plan。分为 Goal Understanding(GUHs)、Intention Decomposition(IDHs)、Planning Generation(PGHs)三类。
2. **Execution Hallucinations**:声称完成实则未执行的子阶段,涉及 [[tool-use]]。分 Tool Selection(TSHs,选用不存在/无关工具)与 Tool Calling(TCHs,参数错填/遗漏/虚构)。
3. **Perception Hallucinations**:接收并转换外部信息时产生偏离事实的内部观测,源于传感器故障或编码能力受限。
4. **Memorization Hallucinations**:未校验 [[agent-memory]] 正确性即使用,分 Memory Retrieval(MRHs)与 Memory Update(MUHs)。
5. **Communication Hallucinations**:MAS 中 agent 间交换的信息不准确/误导/虚构,源于错误消息传播、不协调的通信协议、低效的网络更新。

文中进一步识别了约 **十八个(结论处为 seventeen)触发原因**,并系统梳理 **十类缓解方法**,归为三大分支:

- **Knowledge Utilization**:External Knowledge Guidance(专家知识 + [[world-model]])与 Internal Knowledge Enhancement([[prompt-engineering]] 如 [[chain-of-thought]]/[[tree-of-thoughts]]/constrained prompting,以及 [[model-editing]] 知识编辑与知识遗忘)。
- **Paradigm Improvement**:六种范式——[[contrastive-learning]]、[[curriculum-learning]]、[[reinforcement-learning]]、[[causal-inference]]、graph learning、decoding optimization(测试时范式)。
- **Post-hoc Verification**:Self-verification Mechanism([[self-reflection]]、[[self-consistency]]、self-questioning)与 Validator Assistance(language / retrieval / execution / simulation / ensemble 五类外部验证器)。

并配套梳理各类幻觉的**检测方法**(Fig.4),提及 SelfCheckGPT、ToolBH、MAST、Who&When、MemOS 等代表性工作。

## 结果

- 这是据作者所知**第一篇** LLM agent 幻觉综述;开源整理了 **200+ 篇相关论文**(GitHub:ASCII-LAB/Awesome-Agent-Hallucinations)。
- 提出 **5 类 + 9 子类**的幻觉 taxonomy,识别约 18 个(摘要 eighteen,结论 seventeen)触发原因,总结 **10 类缓解方法**与对应检测方法。
- 在缓解方法 × 幻觉类型的覆盖矩阵(Table I)中发现明显空白:例如 Memory Retrieval Hallucinations(MRHs)几乎只有 EKG、GL、VA 被探索;检测方法整体远少于缓解方法,其中 perception 幻觉检测较多,而 memorization、communication 幻觉检测较少(因后两者属 agent 深层模块,定位更难)。
- 给出 6 个未来方向:幻觉累积研究、精确幻觉定位、幻觉的 mechanistic interpretability、统一 benchmark 构建、持续 self-evolution 能力([[lifelong-learning]])、基础架构升级(linear-complexity 模块、neural-symbolic、AutoML 架构搜索、动态自调度 agentic system)。

注:作为综述,本文不报告自有模型的实验数值,上述均为其分类/统计性结论。

## 在本 wiki 中的位置

本文是 [[ai-safety]] / [[agent-safety-alignment]] 视角下对 [[llm-agent]] 可靠性问题的总览,把单体 LLM 的 [[hallucination]] 概念扩展到完整 agent pipeline 与 [[multi-agent-systems]]。它串联了本 wiki 中大量 agent 模块与方法条目:推理([[chain-of-thought]]、[[tree-of-thoughts]])、工具使用([[tool-use]])、记忆([[agent-memory]])、自我验证([[self-reflection]]、[[self-consistency]])、以及缓解范式([[reinforcement-learning]]、[[contrastive-learning]]、[[curriculum-learning]]、[[causal-inference]]、[[model-editing]]、[[world-model]])。POMDP 形式化与多智能体通信拓扑视角,可与 [[multi-agent-collaboration]]、[[llm-multi-agent]] 等条目互参。

主要来自 [[chinese-academy-of-sciences]] 信息工程研究所等机构,合作单位包括 [[nanyang-technological-university]]、[[renmin-university-of-china]] 等。
