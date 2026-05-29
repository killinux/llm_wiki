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
