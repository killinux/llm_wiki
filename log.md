# Log

Append-only record of operations. Each entry: `## [YYYY-MM-DD] <op> | <title>`
where op ∈ {ingest, query, lint, note}. Newest at the bottom.

Tip: `grep "^## \[" log.md | tail -5` shows the last 5 operations.

## [2026-05-29] note | Wiki initialized

Created the LLM Wiki skeleton for the topic **LLM & AI research**: `CLAUDE.md` schema,
`raw/` (immutable sources), `wiki/{sources,entities,concepts,topics}/`, `wiki/index.md`,
and this log. Ready for first ingest.

## [2026-05-29] ingest | LATS — Language Agent Tree Search (arXiv 2310.04406)

Source: Zhou et al. 2023. Raw PDF saved at `raw/2310.04406v3.pdf`. Pages touched (10 created):
- source: [[2023-lats-language-agent-tree-search]]
- concepts: [[language-agent-tree-search]], [[monte-carlo-tree-search]], [[llm-agents]],
  [[react]], [[reflexion]], [[tree-of-thoughts]]
- entities: [[gpt-4]], [[humaneval]], [[webshop]]
- updated [[index]].
Key recorded results: 92.7% pass@1 on HumanEval (GPT-4); 75.9 avg on WebShop (GPT-3.5).
Stubs to expand on future ingests: ReAct, Reflexion, ToT (originals), GPT-4 model card,
HumanEval/WebShop origin papers.

## [2026-05-29] note | 全库改为简体中文

将全部 11 个 wiki 页面 + `index.md` 的正文改写为简体中文(专有名词/缩写保留原文)。在
`CLAUDE.md` 增加语言约定:今后 ingest 默认用中文撰写。frontmatter 字段保持英文不变。

## [2026-05-29] ingest | Generative Agents (arXiv 2304.03442)

Source: Park 等 2023(UIST 2023)。原文 `raw/2304.03442v2.pdf`。新建/更新页面:
- source: [[2023-generative-agents]]
- 新建概念:[[generative-agents]]、[[memory-stream]]
- 新建人物:[[joon-sung-park]]
- 更新枢纽页 [[llm-agents]](新增"社会模拟"分支)、[[reflexion]](交叉链接"反思同名不同义")、[[index]]
要点:记忆流(完整自然语言存档 + 近因/重要性/相关性检索)+ 反思 + 规划三组件;25 智能体沙盒中
涌现情人节派对等社会行为;消融证明观察/规划/反思各自关键。
过程纠错:本次开始时误以为新资料是 ReAct/ToT 并起草了相关页面 → 发现 raw/ 实为 2304.03442
(Generative Agents),那批草稿均被取消、未落盘,无污染;已按真实文件重做。

## [2026-05-29] lint+fix | 按原文核对 Generative Agents,并修断链

依据用户提供的论文前两页(事实来源)核对 [[2023-generative-agents]] 与 [[generative-agents]]:
- 修正:架构三组件应为 memory stream / reflection / planning;消融维度为 observation /
  planning / reflection(此前混为一谈)。补充基础模型 = ChatGPT,补 repo/demo 链接。
- 修断链:上一条 ingest 写的 [[llm-agents]] 误引用了尚未建页的 chain-of-thought / hotpotqa /
  fever / alfworld / shunyu-yao(属未 ingest 的 ReAct/ToT),已改为纯文本并标注"待 ingest"。
  现全库无断链。

## [2026-05-29] lint+fix | 移除未接地的 ReAct/ToT 页面,恢复 grounding

发现先前"以为被取消"的 ReAct/ToT 草稿其实落盘并被提交,产生了 raw/ 中无对应原文的页面
(违反"内容必须可追溯到 raw/")。raw/ 实际仅 2 篇:LATS、Generative Agents。处理:
- 删除:[[chain-of-thought]]、[[hotpotqa]]、[[fever]]、[[alfworld]]、[[shunyu-yao]]
  (这些只属于未 ingest 的 ReAct/ToT/CoT)。
- 还原 [[react]]、[[tree-of-thoughts]]、[[webshop]] 为仅依据 [[2023-lats-language-agent-tree-search]]
  的干净 stub(ReAct/ToT 仍作为 LATS 的相关工作以简页保留,标注原文待 ingest)。
现 wiki 仅含 LATS 与 Generative Agents 两篇真正 ingest 的内容;无断链、无对未 ingest 源的引用。
教训:批量写入被中断时,工具结果即便显示 cancelled 也可能已落盘 → 每次 ingest 后必须跑
lint/断链与 grounding 检查。

## [2026-05-29] ingest | ReAct (arXiv 2210.03629)

Source: Yao 等 2022(ICLR 2023,Princeton + Google)。先下载原文到 `raw/2210.03629.pdf`(接地),
内容经 arXiv 摘要核对。新建/更新页面:
- source: [[2022-react-reasoning-and-acting]]
- 把简页升级为完整页:[[react]]
- 合法重建(现有原文接地):[[chain-of-thought]]、[[hotpotqa]]、[[fever]]、[[alfworld]]、[[shunyu-yao]]
- 更新 [[webshop]](加入 ReAct +10% 行,sources:2)、[[llm-agents]](sources:3)、[[index]]
关键结果:HotpotQA/Fever 借 Wikipedia API 抗幻觉;ALFWorld +34%、WebShop +10% 绝对成功率(1–2 示例)。
说明:这些页面正是上一条 lint 删除的那批——区别在于此次 raw/ 中已有 ReAct 原文,内容可追溯,合规。

## [2026-05-29] ingest(batch) | 第1波 40 篇

本波批量 ingest 后,以**磁盘实际文件**为准重写了 `wiki/index.md`,把新增的 source / entity /
concept 页面并入既有索引(保留原有分组结构与候选主题,未丢弃已有内容)。

当前磁盘实际页面统计(以 `ls wiki/{sources,entities,concepts}/*.md` 为准):
- 资料 (sources):**43 篇**(`2020-rag` 至 `2023-voyager`)。本波新增约 40 篇,涵盖两大方向:
  - LLM 推理 / 智能体:RAG、CoT、InstructGPT、Constitutional AI、STaR、Inner Monologue、
    ToT、Reflexion、Self-Refine、Self-Debugging、CRITIC、Plan-and-Solve、RAP、
    Multi-Agent Debate(两篇)、CAMEL、AutoGen、ChatDev、MetaGPT、AgentBench、ExpeL、
    Voyager、MemoryBank、Let's-Verify-Step-by-Step 等。
  - 推荐系统(去偏 / 因果 / 强化学习):KuaiRand、Deep-Deconf、iDCF、CDR、DORL、RLUR、
    TSCAC、RMTL、HAC、GFN4Rec、D²Co、BHE(数据异质性)、Divide-and-Conquer EBR,以及
    因果推断综述与 MTDRS 综述各一篇。
- 实体 (entities):**170 个**(`entities/CLAUDE.md` 为说明文件,非 wiki 实体页,未列入索引)。
  按子节:模型 48、人物 39、机构(labs)20、数据集 19、benchmark 30、产品 15。
- 概念 (concepts):**171 个**,在"概念"下按主题群细分:LLM 智能体与推理、多智能体、记忆、
  自我改进、工具与代码、对齐与安全、训练与推理范式、强化学习、推荐系统、因果推断与去偏、其他。

校验:逐一比对磁盘文件与 index 链接,确保索引行全部对应真实存在的 .md(无虚列、无遗漏);
主题区新增了去偏/短视频 RL/自我改进等候选主题条目。

## [2026-05-29] ingest(batch) | 续批 70 篇

本波继续批量 ingest,并**以磁盘实际文件为准**把新增/更新页面并入既有 `wiki/index.md`,
保留原分组结构(主题 / 实体[模型·人物·机构·数据集·benchmark·产品] / 概念 / 资料)与既有条目,
未丢弃已有内容。`{sources,entities,concepts}/CLAUDE.md` 为说明文件,均不计入索引。

当前磁盘实际页面统计(`ls wiki/{sources,entities,concepts}/*.md`,排除 CLAUDE.md):
- 资料 (sources):**113 篇**(`2020-rag` 至 `2026-transformers-graph-recommender-survey`)。
  较上一波(43 篇)新增约 **70 篇**,主要方向:
  - LLM 推理 / 自我纠错 / 验证:CoVe、Self-RAG、Shepherd、CriticGPT(LLM critics)、
    TS-LLM、compute-optimal inference(REBASE)、Quiet-STaR、V-STaR、RISE、
    Reflection-on-Search-Trees、Tree-Search-for-LM-Agents、"LLMs cannot self-correct yet"、
    "when can LLMs correct mistakes"、self-reflection-llm-agents。
  - LLM 智能体 / 微调 / 记忆 / 编排:AgentTuning、FireAct、MemGPT、AutoGuide、HiAgent、
    MegaAgent、Eureka(奖励设计)。
  - 社会模拟 / 生成式 ABM:SOTOPIA、SOTOPIA-π、Concordia、swarm-intelligence、
    generative-AI-as-economic-agents、2026 生成式社会模拟验证综述。
  - 自动驾驶:DriveMLM(2023 / 2025 两篇)。
  - 时序基础模型:TimesFM。
  - 推荐系统(LLM agent / 模拟器 / 对话 / 多智能体):AgentCF、RecMind、InteRecAgent、
    Agent4Rec(generative-agents-in-recommendation)、MACRec、LUSIFER、KuaiSim、
    LLM4Rerank、LLM-tags-vs-classical、LLM-learnable-planners。
  - 推荐系统(去偏 / 因果 / RL / 公平 / 架构):HierRec、MQSA-TED、VLDRec、CQE、
    counterfactual-watch-time、CroCoDiL、release-interval-bias、DFEI、feature-level-bias-ctr、
    fairness-with-missing-labels、BankFair、future-impact-decomposition、touch-the-core、
    RoLeR、EDT4Rec、EasyRL4Rec、RecMamba、SIGformer、recommendation-editing、
    robust-recommendation(RGCL)、user-creator-feature-polarization、
    model-based-multi-agent-short-video、UNEX-RL、situation-aware-recommender-enhancer。
  - 数据集:MicroLens、MerRec、EEG-SVRec。
  - 另含一篇非 LLM 主题(运筹/优化):uncertain-random-geometric-programming(已如实标注)。
- 实体 (entities):**258 个**(模型 68 · 人物 71 · 机构 31 · 数据集 27 · benchmark 34 · 产品 27)。本波增量按子节:
  - 模型:CLIP、ViT、Mamba、LLaMA-3、Mistral-7B、Pythia、GRU4Rec、BPR、
    Decision-Transformer、TimesFM、RecMamba、RecLlama、MercaTran、CriticGPT、DriveMLM 等。
  - 人物:SOTOPIA / 社会模拟 / 推荐 / 推理方向新作者若干(如 hao-zhu、maarten-sap、
    graham-neubig、petter-tornberg、maik-larooij、chongming-gao、xiang-wang、jianxun-lian、
    sean-welleck、zhiqing-sun 等)。
  - 机构:CMU、NUS、Mila、阿姆斯特丹大学、密歇根大学、中科大、温莎大学、山东大学、
    西湖大学、腾讯、LG AI Research、Artificial Intelligence Review(期刊)等。
  - 数据集:Ali-CCP、Amazon-Book、EEG-SVRec、MerRec、ShareGPT、Steam-dataset。
  - benchmark:SOTOPIA、SOTOPIA-EVAL、WebArena、Steam。
  - 产品/系统:AgentCF、InteRecAgent、MACRec、MegaAgent、LUSIFER、EasyRL4Rec、
    CARLA、Apollo-AD、Chat-Rec、LinRec、ReplicantLife、Mercari 等。
- 概念 (concepts):**270 个**。新增概念覆盖:自我纠错/验证(chain-of-verification、
  intrinsic-self-correction、reflection、self-inspiring、self-instruct)、搜索与推理算力
  (compute-optimal-inference、rebase、reflection-on-search-trees、test-time-scaling)、
  社会模拟(social-simulation、social-intelligence、agent-based-modeling、metacognition)、
  架构(transformer、state-space-model、adversarial-robustness)、对齐(DPO)、
  RL(sac、behavior-cloning、multi-agent-rl、cross-entropy-method、lagrangian-relaxation、
  constrained-optimization)、推荐(llm-for-recommendation、long-term-recommendation、
  situation-aware-* 系列、interactive/context-aware-recommendation、ctr、ndcg、cold-start、
  data-sparsity、recommendation-editing/simulator/diversity、rl-based-recsys、
  affective-engagement、eeg-signal、conditional-quantile-estimation、quantile-regression)、
  因果(backdoor-adjustment、performative-prediction、feature-level-bias-ctr、
  disentangled-representation-learning)、公平与社会经济(provider-fairness、
  two-sided-fairness-reranking、minimum-exposure-guarantee、content-creator-incentive、
  dual-influence、polarization、dimensional-collapse、bankruptcy-problem、talmud-rule、
  billp、margin-maximization、graph-contrastive-learning、rgcl、lightgcn)、其他
  (evaluation、model-validation、systematic-literature-review、model-editing、
  differential-entropy、multi-embedding、cirs)。概念区因此新增"公平性与社会经济"分节。

校验:逐行比对磁盘 .md 与 index 链接(脚本核对),确保 113 source / 258 entity / 270 concept 全部
对应真实文件——index 共 615 个唯一 slug,与磁盘完全一致(无虚列、无遗漏;部分 slug 同时作为实体与
概念存在如 reflexion/recagent/sasrec 故唯一数小于三类之和)。既有正确条目均保留;主题候选区补充了
社会模拟/LLM 推荐/公平性等候选。

## [2026-05-29] ingest(batch) | 续批 39 篇

本波继续批量 ingest,并**以磁盘实际文件为准**重写 `wiki/index.md`,把新增/更新页面**并入**既有
索引(保留主题 / 实体[模型·人物·机构·数据集·benchmark·产品] / 概念 / 资料 的分组结构与既有正确条目,
未丢弃已有内容)。`{sources,entities,concepts}/CLAUDE.md` 为说明文件,均不计入索引。

当前磁盘实际页面统计(`ls wiki/{sources,entities,concepts}/*.md`,排除 CLAUDE.md):
- 资料 (sources):**269 篇**(`2020-rag` 至 `2601-dsmoe-scenario-adaptive-moe-matching`)。
- 实体 (entities):**474 个**(模型 119 · 人物 128 · 机构/labs 76 · 数据集 45 · benchmark 64 · 产品 42)。
- 概念 (concepts):**428 个**。

本波新增 source 概况(约 39 篇,沿用既有两大方向):
- 推荐系统(LLM 世界知识 / 生成式序列 / 多任务 / 召回 / 公平 / 长期价值):
  GRASP(LLM 世界知识注入序列推荐,线上 GMV +1.71%)、FuXi-γ(decoder-only 生成式序列推荐,
  受 Ebbinghaus 启发的时间编码+对角稀疏剪枝,训练加速 4.74×/推理 6.18×)、FuXi-Linear
  (线性复杂度时间感知序列推荐,最高 21× 推理加速)、KAML(非对称多标签 CVR,RPM +12.11%)、
  DSMOE(多场景召回 MMOE+低秩 SAP+蒸馏)、SMES(Kuaishou 可扩展稀疏 MoE 多任务)、
  LERL(LLM 高层语义规划 + RL 低层选品的长期推荐)、HRL4PFG(分层 RL 主动引导 item-side 公平)、
  DSRM-HRL(扩散提纯用户状态 + 分层 RL 公平/参与 Pareto)、Where-to-Explore
  (低成本无偏探索 UI 行,Gini 0.203 vs 0.494)、IDSS(Shannon 熵贯穿对话推荐三阶段)、
  TriRec(用户-物品-平台 tri-party LLM-agent 推荐)。
- LLM 智能体(推荐评估 / 模拟器验证 / 社会模拟 / 多智能体编排 / 工具规划 / 记忆 / 自我改进):
  A/B Agent(多模态 LLM 用户智能体替代在线 A/B)、ConvApparel(Google 服装购物对话数据集 +
  realism-gap 验证三支柱,平均 HLS 0.004)、PolicySim(LLM 智能体社会模拟沙盒 + contextual bandit
  主动优化平台策略)、Orchestration-MAS / Skan AI 编排式多 agent 统一架构、ToolTree
  (免训练 MCTS 工具规划,GTA 66.95 / ToolBench 69.04)、SEMA(结构熵剪枝 + 闭环自演化 RTS 多智能体)、
  MAR(多 persona 辩论 Reflexion,HotPotQA EM 44→47、HumanEval 76.4→82.6)、ERL(经验式反思学习,
  Gaia2 +7.8%)、生成式 MMO 仿真(SFT+GRPO 微调玩家 agent)、多智能体价值多样性社会模拟
  (Schwartz 价值观)、Yerkes-Dodson 倒 U 形合作曲线(中等压力 upkeep=5 合作峰值 29 次)。
- 记忆方向综述/系统:Memory-in-the-Age-of-AI-Agents 综述(forms-functions-dynamics 三维分类法)、
  Memory-for-Autonomous-LLM-Agents 综述(POMDP 写-管-读循环)、StructMemEval
  (评测 agent 组织记忆而非仅回忆)、Memori(LLM-agnostic 持久记忆层,LoCoMo 81.95%、约 5% token)。
- 数据集:VK-LSVD(VK 迄今最大公开短视频工业数据集,400 亿交互 / 1000 万用户 / 近 2000 万视频)。

实体 / 概念增量(随本波 source 落盘):
- 实体新增以推荐模型与 LLM-agent 系统/数据集为主,如 grasp-world-knowledge-sequential-recommendation、
  fuxi-* 、dsmoe(及相关)、convapparel、policysim、tooltree、skan-ai、vk-lsvd、structmemeval、
  memori 等;人物与机构按各论文作者/单位补全(模型 119 · 人物 128 · 机构 76 · 数据集 45 · benchmark 64 · 产品 42)。
- 概念新增覆盖记忆(memory-augmentation/evolution、long-context、context-engineering)、自我改进/自演化
  (self-evolving-agents、self-play、self-verification)、工具与编排(tool-planning、agent-orchestration、
  function-calling)、多智能体与社会模拟(value-diversity、collective-intelligence、structural-information-theory、
  schwartz-theory-of-basic-values 等)、推荐(generative-recommendation、multi-scenario-* 、proactive-recommendation、
  preference-elicitation、conformal-risk-control、popularity-bias 等)。本波及历批尚未归入既有子群的概念
  统一暂列于概念区"其他(后续批次新增,待归类)"分节,待后续 lint 细分。

校验:脚本逐一比对磁盘 .md 与 index 链接 —— sources 269 / entities 474 / concepts 428 **全部**对应真实文件,
无虚列、无遗漏、无类内重复;跨类同名 slug(如 reflexion/recsim/mmoe/transformer 等既为实体又为概念)按既有惯例
两类各列一次。既有正确条目与主题候选区均保留。

## [2026-05-29] lint(大规模) | 全库去重 + 枢纽页 + 链接重写

269 篇 source 全部 ingest 完成后执行大 lint：
- 合并 83 组跨目录重复页(同 slug 在 concepts/ 与 entities/ 各一份 → 保留一份,按实体/概念类型归入合适目录)
- 合并单复数变体页(diffusion-model(s)、recommender-system(s)、llm-agent(s) 等)
- 新建 19 个高频枢纽概念页(generative-recommendation、offline-reinforcement-learning、GRPO、CTR-prediction、long-term-memory、multimodal-llm 等)
- 重写 ~650 个文件的变体链接到 canonical slug(recommendation-system→recommender-systems、mcts→monte-carlo-tree-search、chain-of-thought-prompting→chain-of-thought 等)
- 重建 index.md（基于磁盘实际文件）
最终：269 source · 429 concept · 475 entity = 1173+ 页；跨目录重复 0；接地 269/269 ✓。
长尾悬空链接(引用 <8 次)保留为"待写"标记,符合 Karpathy 模式设计。

## [2026-05-30] note | 建综述页:生成式社会模拟(斯坦福小镇线)
新建 `wiki/topics/generative-social-simulation.md`,首个 topics 页。综述串联约 28 篇 source:范式起点(Smallville 三组件:记忆流/反思/规划)、演化时间线、六个子分支(大规模平台/scale-agency 权衡/经济博弈游戏/社交智能评测与 persona/记忆机制/用户模拟接口),并专设"验证与涌现真伪"核心争议章节(can-llm-simulate 的 11.86% 过程级准确率、emergent-behaviors-data-leakage、generative-social-simulation-validation 综述)。更新 index.md 主题区。

## [2026-05-30] note | 补建 6 篇库外社会模拟代表作占位页(stub-unverified)
为 generative-social-simulation 综述补全"待 ingest"代表作,新建 6 个 source 占位页(均标 status: stub-unverified,内容源自外部知识,raw/ 暂无原文,数字待核实):2024-generative-agent-simulations-1000-people(Park 1000 真人 agent)、2023-out-of-one-many-llm-simulate-human-samples(Argyle 奠基作)、2023-econagent-macroeconomic-simulation、2023-s3-social-network-simulation、2023-waragent-world-war-simulation、2024-project-sid-minecraft-civilization。已回链入 topics 综述页与 index.md(单列"待 ingest 占位"区,与已核实 source 分开)。

## [2026-05-30] ingest(batch) | 社会模拟线补全:下载并 ingest 5 篇 + 去重 1 篇
从 arXiv 下载 6 篇原文入 raw/(2411.10109/2310.10436/2307.14984/2311.17227/2411.00114/2209.06899)。
**去重事故纠正**:上一轮建的占位页 2024-generative-agent-simulations-1000-people 经核实即 arXiv 2411.10109,
与库中既有 2024-generative-agents-self-reports 同一篇(只是 v1 旧标题 "1000 People"),已删除重复页,
并在 self-reports 页加旧标题注释、回链综述。
正式 ingest(核实原文,去 stub 横幅)5 篇:2023-out-of-one-many-llm-simulate-human-samples(Argyle/BYU,
algorithmic fidelity/silicon sampling)、2023-econagent-macroeconomic-simulation(清华,ACL24,Phillips/Okun)、
2023-s3-social-network-simulation(清华,AgentSociety 前身)、2023-waragent-world-war-simulation(Rutgers)、
2024-project-sid-minecraft-civilization(Altera,PIANO)。修正 AgentSociety 内两处悬空链接指向新页;
综述页时间线/子分支接入 6 篇;index.md 更新。环境:装 pip(ensurepip)+pypdf 抽取 PDF 文本。

## [2026-05-30] ingest(deepen) | 5 篇社会模拟页升级为定量深度页
读 raw/ 原文结果章节,把 EconAgent / Out-of-One-Many / S³ / WarAgent / Project Sid 的"结果"补成带数字版本:
EconAgent(Phillips r=-0.619/Okun r=-0.918,通胀-5~5%/失业2-12%,COVID 干预);Out of One Many(图灵测试 61.7% vs 61.2% 不可区分,ANES 投票 0.43 vs 0.48 等,四判据);S³(传播 Cor 0.858/0.892,gender Acc 0.71,Markov 情绪);WarAgent(四基石+秘书agent+六维档案,100% 史实同盟,匿名化测试,战争必然性反事实);Project Sid(单agent需GPT-4o,角色专业化需social awareness,25选民民主投票修税法,宗教/meme传播)。

## [2026-05-30] lint(fill) | 补 7 个高频缺失概念页 + 清 5 组别名悬空链接
缺口扫描:916 悬空链接。新建 7 个被引用最多且无别名的概念页:game-theory(12 引)、reranking、contextual-bandits、reinforcement-learning-for-recommendation、best-of-n、seq2seq、linear-attention。
别名重写(34 文件):sft→supervised-fine-tuning、dpo→direct-preference-optimization、two-tower-model→two-tower、emergent-behavior→emergent-abilities、inference-scaling-laws→test-time-scaling(均保留显示词)。index 概念区登记新页。

## [2026-05-30] lint(fill) | 续:再建 3 枢纽概念页 + 清 3 组别名
新建 attention(全库最核心却缺失的枢纽页)、multi-objective-optimization、implicit-feedback。别名重写(22 文件):planning→llm-planning、two-tower-retrieval→two-tower、agent→llm-agents。本轮累计:10 个新概念页 + 56 文件别名重写 + 5 篇社会模拟 source 页深度化。

## [2026-05-30] lint(fill)+note | 第2批概念页(7) + 第2篇 topic 综述
新建 7 概念页:item-side-fairness、offline-evaluation、embedding、dense-retrieval、uplift-modeling、exploration-exploitation、personalization。
新建 topics/rl-for-recommendation(推荐中的强化学习综述),读 6 篇 source 原文摘要核实(DORL/ROLeR/DARLR 谱系、RLUR/TSCAC/UNEX-RL 数字),串联 ~20 篇 source,与社会模拟线在"用户模拟器/离线评估"处交汇。index Topics/Concepts 区登记。

## [2026-05-30] lint(fill)+note | 第3批概念页(3) + 第3篇 topic 综述
新建 3 概念页:representation-learning、multi-domain-recommendation、hyperparameter-tuning。别名重写(11 文件):safety-alignment→alignment、a2c→actor-critic。
新建 topics/llm-self-improvement(LLM 自我改进/自我纠错综述),读 7 篇 source 原文核实(Reflexion/Self-Refine/Self-Debugging/CRITIC/MAD + 批判线 llms-cannot-self-correct / when-can-llms-correct),按反馈来源四分 + "内在自我纠错无效"核心争议,串联 ~20 篇 source。index 同步。

## [2026-05-30] lint(fill)+note | 第4批概念页(4) + 第4篇 topic 综述
新建 4 概念页:retrieval、agent-evaluation、embodied-agent、recommendation-fairness。
新建 topics/llm-agent-memory(LLM 智能体记忆机制综述),读 9 篇记忆线 source 原文核实(MemGPT/MemoryBank/A-Mem/Mem0/MemoryOS/RMM/HiAgent + StructMemEval/survey),五技术谱系 + "简单检索打败复杂记忆架构"核心争议,串联 ~14 篇 source。index 同步。

## [2026-05-30] lint(fill) | policy-gradient 概念页 + 清 5 组别名
新建 policy-gradient。别名重写:vae→variational-autoencoder、multi-agent-simulation→multi-agent-systems、llm-recommendation→llm-for-recommendation、llm-benchmark→benchmark、inner-monologue→2022-inner-monologue。

## [2026-05-30] lint(fill) | self-supervised-learning + synthetic-data 概念页 + 2 别名
新建 self-supervised-learning、synthetic-data。别名:fairness-in-recommendation→recommendation-fairness、multi-agent-llm→llm-multi-agent。

## [2026-05-30] note | 第5篇 topic 综述:推荐去偏与因果推断
新建 topics/debiasing-causal-recommendation,读 8 篇 source 原文核实(deep-deconf/iDCF/CDR/LCDR/IViDR/CaseRec + 评估争议 debias-can-be-unreliable),三大方法族(IPS/DR/Deconfounder 谱系)+ 短视频时长去偏 + "去偏评估不可靠"争议,串联 ~18 篇 source。index 同步。本会话 topics 累计 0→5。

## [2026-05-30] note | 第6篇 topic 综述:推荐中的 LLM 智能体
新建 topics/llm-agents-for-recommendation,读 7 篇 source 核实(RecAgent/Agent4Rec/AgentCF 模拟导向 + RecMind/InteRecAgent/MACRec 推荐导向 + survey),两范式分类 + "模拟保真度/集成/成本"张力,缝合社会模拟与推荐两半边,串联 ~18 篇 source。本会话 topics 累计 0→6。

## [2026-05-30] ingest+fill | 补具体系统页:lc-rec / ip-adapter / cournot-competition / fairgame
转入"具体系统建页"线。下载 2 篇原文入 raw/ 并核实:lc-rec(2311.09049,RUC+腾讯 ICDE24,RQ-VAE 语义ID+对齐微调)、ip-adapter(2308.06721,腾讯,解耦交叉注意力图像prompt适配器);建 entities/lc-rec、entities/ip-adapter。另建 concepts/cournot-competition(经济博弈概念)、entities/fairgame(据引用工作 2025-llm-agent-game-theory-strategy-recognition 整理,标注原文待 ingest)。index 实体区/概念区登记。

## [2026-05-30] lint(fill) | transfer-learning 概念页 + 4 别名(收尾)
新建 concepts/transfer-learning。别名:user-behavior-simulation→user-simulation、memory→agent-memory、llm-evaluation→agent-evaluation、lifelong-sequential-recommendation→sequential-recommendation。剩余悬空多为 ≤5 引用的"待写标记"(符合 Karpathy 模式设计),停止机械造页。

## [2026-05-30] note | 第7、8篇 topic 综述
新建 topics/solving-agents-search(求解类智能体:推理时搜索与成本-质量权衡;读 ReAct/ToT/RAP/LATS/TS-LLM/tree-search-web/AB-MCTS/compute-optimal-inference 核实,串 ~18 篇)与 topics/recsys-architectures(推荐架构演进:Transformer×GNN×生成式;读 FuXi-γ/SIGformer/VISTA/transformers-graph-survey 核实,串 ~22 篇)。本会话 topics 累计 0→8,覆盖 wiki 两半边全部主干候选。index 同步。

## [2026-05-30] note | 第9篇 topic 综述:公平性与多边福利(原候选清单收齐)
新建 topics/fairness-multistakeholder-welfare,读 7 篇 source 核实(BankFair/LHRL/fairness-missing-labels/user-creator-polarization/conformal-risk-control/collective-manipulation),四节(提供方曝光公平/用户群体公平/动态极化/福利安全抗操控)+ 核心张力,串 ~16 篇。至此 index 原候选 ①–⑨ 全部建成,topics 层 0→9。index 候选注释更新为"已全部上线"。

## [2026-05-30] note | 新建 README.md
新建仓库根 README,说明本库采用 Karpathy "LLM Wiki" 思路(人类策展、LLM 维护;Obsidian=IDE、LLM=程序员、wiki=代码库),介绍三层架构(raw 不可变源 / wiki 生成层 / CLAUDE.md schema)、wiki 四类子目录、9 篇 topic 导航入口、页面约定与三种操作(ingest/query/lint),附当前规模。

## [2026-05-31] lint | 全量 lint + 修复
扫描 1220 页,报告:874 悬挂链接、1 孤立页、1 组近似重复、5 页未入 index、frontmatter 100% 完整。
修复内容:(1) 合并 contextual-bandit → contextual-bandits 并全局替换链接(11 文件);(2) 补录 debiasing-recommendation / policy-gradient / self-supervised-learning / transfer-learning / s3-social-network-simulation 进 index;(3) 为 s3-social-network-simulation 从 social-simulation 加入链;(4) 新建 4 个高频悬挂链接页:bert(entity)、graph-neural-network / q-learning / pretraining(concepts),均入 index。

## [2026-05-31] ingest | 批量补录 13 篇 LLM agent 评估论文
PDF 下载至 ~/work/doc/,创建 12 个 source 页 + 8 个 entity 页,全部入 index。
论文:AgentBench(已有)、GAIA、MINT、WebArena、WebShop、OSWorld、SWE-bench、τ-bench、AgentBoard、ColBench、ToolLLM、MetaTool、ToolEmu。
覆盖方向:综合多环境评估、Web/OS 操控、软件工程、工具使用、安全。
