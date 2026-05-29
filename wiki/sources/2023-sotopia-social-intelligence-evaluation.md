---
type: source
subtype: paper
tags:
  - benchmark
  - llm-agents
  - social-intelligence
  - role-playing
  - llm-as-judge
  - interactive-evaluation
created: 2026-05-29
updated: 2026-05-29
arxiv: "2310.11667"
raw: raw/2310.11667.pdf
authors:
  - Xuhui Zhou
  - Hao Zhu
  - Leena Mathur
  - Ruohong Zhang
  - Zhengyang Qi
  - Haofei Yu
  - Louis-Philippe Morency
  - Yonatan Bisk
  - Daniel Fried
  - Graham Neubig
  - Maarten Sap
year: 2023
---

# SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents

SOTOPIA 是一个开放式的社交互动模拟环境与多维评测框架(SOTOPIA-EVAL),用于交互式地评估 [[large-language-models]] 驱动的 [[llm-agents]] 在目标导向社交场景中的社会智能(social intelligence)。

## 问题

人类在日常互动中追求并平衡复杂、多面的社交目标,这是社会智能的核心,但 AI 系统在这方面的能力仍不明确。作者指出现有评测存在两类缺陷:
- 大量社会智能 [[benchmark]](如 SocialIQA、ToMi、FauxPas)是**静态、非交互**的,无法刻画社交互动的动态性与丰富社会语境;
- 现有的交互式评测要么缺乏多样的目标驱动行为,要么只聚焦特定任务(如谈判、具身任务)。

因此需要一个**真实(realistic)、混合效用(mixed utilities)、开放式(open-ended)**的环境,既能程序化生成多样任务,又能从多维度评估 [[role-playing]] 智能体的社交表现。

## 方法

**SOTOPIA 环境**:任务由「场景情境 + 角色 + 各自的社交目标」组合而成。论文构建了 40 个角色(含性格、职业、价值观、决策风格、秘密与公开信息)、90 个关系、90 个社交场景,覆盖合作、竞争、混合(谈判、交换、竞争、协作、迁就、说服)等互动类型。角色、关系、场景均通过 prompt [[gpt-4]] 自动生成并经人工校验(其中借鉴 Social Chemistry 101、SocialIQA、Deal or No Deal 等数据集来"启发"生成)。每个 episode 中两个智能体轮流(round-robin)行动,可选择 speak、非语言交流、物理动作、none(沉默)或 leave(结束),上限 20 轮。智能体只能观察自己的目标与角色档案,对方目标不可见、对方档案按关系部分可见。

**SOTOPIA-EVAL 评测框架**:借鉴社会学、心理学、经济学,设 7 个维度,各有取值范围:
- Goal Completion (GOAL) [0–10]、Believability (BEL) [0–10]、Knowledge (KNO) [0–10];
- Secret (SEC) [-10–0]、Social Rules (SOC) [-10–0]、Relationship (REL) [-5–5]、Financial and Material Benefits (FIN) [-5–5]。

评测既用人类标注(Amazon Mechanical Turk,11 点 Likert 量表 + 自由文本理由),也用 [[gpt-4]] 作为 [[llm-as-judge]]。每场景采样 5 对角色,共 450 个任务,枚举模型对进行模拟。对比模型:[[gpt-3-5]](gpt-3.5-turbo-16k-0613)、[[gpt-4]](gpt-4-0613)、[[llama-2]]-70b-chat、MPT-30b-chat;智能体 temperature=1、评测器 temperature=0。

## 结果

**GPT-4 可作为部分维度的人类代理**:超过 74% 的 GPT-4 评分落在人类评分 ±1 标准差(σ=2.15)内,且 GPT-4 倾向于打分偏高。人类标注者一致性 Randolph κ=0.503。在模型扮演角色时,GPT-4 评分与人类在 GOAL(r=0.71)、FIN(0.62)、REL(0.56)上有显著强相关;但评估人类扮演者时,除 GOAL 外相关性大幅下降。GPT-4 在 SOC、SEC 维度常比人类打分偏高。

**模型间差异(跨 partner 模型平均,Table 2)**:GPT-4 在多数维度最佳:GOAL 7.62、BEL 9.28、KNO 3.73、REL 1.94、FIN 0.81;GPT-3.5 次之(GOAL 6.45、BEL 9.15);Llama-2-70b-chat(GOAL 5.38);MPT-30b-chat(GOAL 4.10)。

**与静态 benchmark 趋势不同**:Llama-2-70b-chat 在交互中各维度普遍低于 GPT-3.5,与其在静态语言理解 benchmark 上与 GPT-3.5 相当甚至更优的表现相悖;作者推测因其接受的人类反馈/用户交互训练较少。说明静态 benchmark 表现好不代表交互场景成功。

**其它发现**:较弱的对话伙伴会拖累对方表现;所有模型在 SOC、SEC 维度均为负分,存在泄露秘密、违反社会规范的风险;模型(尤其 GPT-4)偶尔给出富有创意的"跳出框架"解法。

**SOTOPIA-hard 子集(模型 vs 人类)**:基于奖励上下界差距选出对 GPT-4 最难的 20 个任务。在该子集上,人类的 GOAL 分(human-with-human 6.15、human-with-GPT-4 5.95)显著高于 GPT-4(4.85,p<0.05);人类平均每轮 16.8 词,GPT-4 平均 45.5 词(GPT-4 因大量人类反馈训练而过度"积极倾听"、显得啰嗦);人类在谈判中更具策略性与目标坚持性。

发表于 ICLR 2024。

## 在本 wiki 中的位置

SOTOPIA 把 [[llm-agents]] 的评测从静态任务推进到**开放式、目标导向的交互式社交评测**,与 [[agentbench]]、[[webshop]]、[[mind2web]] 等智能体 benchmark 属同一谱系,但聚焦"社会智能"这一维度。其用 [[gpt-4]] 充当 [[llm-as-judge]] 的做法,与 [[constitutional-ai]]、[[multi-agent-debate]] 等评测/对齐方法相关,也呼应了 [[generative-agents]]([[joon-sung-park]] 等)对可信人类行为模拟的研究。所考察的 [[role-playing]] 与多智能体协作能力,与 [[camel]] 风格的 [[multi-agent-collaboration]]、[[chatdev]]([[chen-qian]])等工作互补。作者团队来自 [[stanford-university]] 圈外的 Carnegie Mellon University(CMU),作者包括 [[graham-neubig]] 等。
