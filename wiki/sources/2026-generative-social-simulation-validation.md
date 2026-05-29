---
type: source
subtype: paper
tags:
  - llm-agents
  - multi-agent-systems
  - generative-agents
  - agent-based-modeling
  - social-simulation
  - validation
  - systematic-review
created: 2026-05-29
updated: 2026-05-29
arxiv: ""
raw: raw/10.1007_s10462-025-11412-6.pdf
authors:
  - Maik Larooij
  - Petter Törnberg
year: 2026
---

# Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling

一句话:这是一篇系统性文献综述(发表于 *Artificial Intelligence Review* 2026, 59:15),系统梳理了用 [[large-language-models]] 驱动的"生成式 Agent-Based Models(GABMs)"在社会模拟中的应用,核心论点是——引入 LLM 不但没有解决 ABM 长期存在的"验证(validation)"难题,反而因黑箱性、文化偏见与随机性而加剧了它。

## 问题

Agent-Based Models(ABMs,基于主体的建模)长期承诺以"自下而上"的方式刻画社会系统:把个体建模为自主主体,让宏观模式从微观交互中涌现。但它在社会科学中始终难以被主流接受,原因有二:(1)把人简化为"if-then 规则执行者"或优化器,行为现实性不足;(2)经验扎根薄弱——缺乏标准化的校准(calibration)与验证(validation)实践,导致可复现性、可比较性差,曾陷入"复制危机"。

[[large-language-models]] 的兴起带来了所谓"生成式主体([[generative-agents]])":能记忆、推理、用自然语言对话的主体,似乎一举解决了"行为现实性"问题。但作者提出关键疑问:生成式 ABM 是否、以及如何解决了第二个、也是更根本的"验证"难题?作者指出 LLM 反而带来三重新挑战:黑箱性(emergent + 随机输出难以复现)、对社会群体的失真表征(社会偏见 social bias 与选择偏见 selection bias,以及训练语料导致的"数据泄漏 data leakage")、以及[[hallucination]](尤其在分布外/无历史先例场景中)。

## 方法

- **检索与筛选**:遵循 PRISMA 2020 流程,2025 年 3 月 27 日在 Scopus 上用布尔查询(组合 "multi-agent system" AND "generative AI"、"generative agent"、"social simulation" AND "LLM"、"large language model-based agents")检索,得 209 篇;经标题/摘要筛选与全文评估,并用反向滚雪球(backward snowballing)补充,最终纳入 **35 篇**原创研究。明确排除了纯任务完成型、不模拟人类行为、综述类,以及侧重基础设施/框架的工作(如 [[chatdev]] 同源的 CAMEL、[[metagpt]]、CGMI、[[autogen]])。编码由单一编码者完成(作者承认这是局限)。
- **三个研究问题**:RQ1 生成式模拟在模拟哪些社会现象;RQ2 文献中报告了哪些验证策略;RQ3 这些验证策略是否足以相对于模型既定目的达成"操作性有效性(operational validity)"。
- **现象分类(RQ1)**:区分个体行为(profile alignment、emotion、conversation/content、social awareness、decision-making/reasoning、opinion/attitude)与群体行为(network propagation、network structure、social dynamics)。
- **验证类型(RQ2)**:沿用 internal/external 与 subjective/objective 两组维度,归纳出五类验证:基于人类(或类人 [[llm-as-judge]])判断、对照公认社会模式、对照已有模型、对照人类生成数据、基于内部一致性。
- **评判标尺(RQ3)**:用"操作性有效性"为最低标准,要求验证满足三点——目的对齐(purpose alignment)、外部扎根(external grounding,基于人类数据或预注册基准而非仅 face-validity)、稳健性(robustness,多次运行 + 敏感性检查)。

## 结果

- **纳入 35 篇**;最常见主题为"内容生成与对话""社会动态""网络传播";21 篇只聚焦单一类别,整体平均每篇 **1.63 个**类别。现象统计(Table 1):Conversation/Content 10、Social Dynamics 10、Profile Alignment 8、Network Propagation 8、Decisions/Reasoning 7、Social Awareness 5、Network Structure 5、Emotion 2、Opinion/Attitude 2。
- **验证技术统计(Table 2,主技术计数)**:对照公认社会模式 14、基于人类(类人)判断 12、对照人类生成数据 12、对照其他模型 1、内部一致性 1、其他 1。其中 **15/35** 篇仅依赖主观评估,22 篇以主观评估作为主要验证手段。
- **方法学诊断(RQ3/讨论)**:(1)验证目标与模型目的常常错位——验证文本"风格逼真"而非其声称要刻画的行为机制(弱耦合);(2)主观验证(含用 [[gpt-4]] 当评审,存在循环性与自我偏好,引用 [[llm-as-judge]] 的可靠性质疑)仍占主导;(3)客观比较常暴露人/机文本的系统差异(LLM 输出更长、更礼貌、更"得体");(4)几乎所有研究用零样本提示而非微调,"校准"被降格为 prompt engineering,带来误表征社会群体、复制刻板偏见的风险。
- **计算成本论证**:给出量化示例——100 个主体、每步 10 次交互、100 步、每次调用约 100 tokens,共约 1000 万输入 + 1000 万输出 tokens;以 2025 年 6 月 GPT-4.1 nano 定价(\$0.10/M 输入、\$0.40/M 输出)约 **\$5/次**;一次含 10 个取值、各 10 次重复的双参数扫描需 1000 次运行 ≈ **\$5,000**;换用 GPT-4.1(\$2/M 输入、\$8/M 输出)则升至 \$100/次、约 **50 万美元**/同等扫描。交互随群体规模二次增长、随参数指数增长,使大规模模拟在财务上不可行。
- **总体结论**:生成式 ABM 处于"模糊的方法学空间"——既无形式模型的简约与解释清晰,又缺数据驱动方法的经验有效性。作者建议三条出路(更严格的经验验证以建立操作性有效性、聚焦"情境特定的可泛化性"、发展可解释性技术),并提出或许应把生成式 ABM 当作一种"新方法学体裁"(如合成数据生成、快速原型),而非用既有范式硬性评判。论文涉及的代表性系统包括 [[generative-agents]](Park 等的 Smallville/Generative Agents)、SOTOPIA-EVAL 社会智能[[benchmark]]、以及多种合成社交平台(Reddit、Twitter/HiSim、Chirper.ai)。

## 在本 wiki 中的位置

本文是一篇关于 [[llm-multi-agent]] / [[multi-agent-systems]] 在社会科学应用的批判性综述,与本 wiki 中 [[generative-agents]]、[[autonomous-agents]]、[[llm-based-agents]]、[[user-simulation]]、[[role-playing-agent]] 等条目直接相关。它把 [[generative-agents]] 这类工作放回 Agent-Based Modeling 的方法学传统中审视,提供了一个"验证/评估"视角:对比 [[llm-as-judge]] 的可靠性问题、[[hallucination]]、以及 [[selection-bias]] 等概念,可作为评估 LLM 多智能体社会模拟工作的批判性参照。它与本 wiki 中聚焦 agent 能力/架构(如 [[reflexion]]、[[react]]、[[voyager]]、[[chatdev]]、[[metagpt]]、[[autogen]])的源文件互补——后者关注"怎么做得更强",本文关注"做出来的东西能不能被验证、是否对社会科学有贡献"。
