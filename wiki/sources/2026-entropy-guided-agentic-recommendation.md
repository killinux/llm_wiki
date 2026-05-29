---
type: source
subtype: paper
tags:
  - recommender-system
  - llm-agent
  - conversational-recommendation
  - preference-elicitation
  - recommendation-diversity
  - uncertainty
created: 2026-05-29
updated: 2026-05-29
arxiv: "2603.11399"
raw: raw/2603.11399.pdf
authors:
  - Dat Tran
  - Yongce Li
  - Hannah Clay
  - Negin Golrezaei
  - Sajjad Beygi
  - Amin Saberi
year: 2026
---

# Entropy Guided Diversification and Preference Elicitation in Agentic Recommendation Systems

提出 IDSS(Interactive Decision Support System),用 Shannon 熵作为统一信号,贯穿对话式推荐中的偏好询问(elicitation)、排序(ranking)与结果呈现(presentation)三个阶段,从而在用户意图模糊/不完整时既能高效追问、又能用残余不确定性驱动多样化推荐。

## 问题

电商用户在搜索初期对自身偏好往往不确定,初始 query 经常模糊、不完整或弱约束(如只给出预算、模糊的品质/风格描述)。[[agentic-ai]] 式 [[recommender-system]] 被期待主动追问澄清问题并代用户行动,但现有系统存在两个失败模式:(1) 过度追问导致 question fatigue / 交互负担过大;(2) 过早把模糊意图收敛到狭窄解释,提前坍缩搜索空间、排除可行选项。同时,现有系统多把 preference elicitation、ranking、result presentation 当作独立模块,无法一致地推理不确定性在整条推荐管线中的传播。

## 方法

IDSS 是一个对话式推荐框架,采用 information-theoretic 视角,用熵量化候选集上对用户偏好的不确定性,并由三个模块实现三条设计原则:

- **Semantic Parsing(语义解析)**:用 GPT-5 + JSON schema 强制约束,把自由文本 query 解析为结构化状态 `(F, P, s)`:`F` 为硬过滤约束(如 body_style、price 区间),`P = (P+, P-)` 为喜欢/不喜欢的软偏好特征,`s ∈ {patient, impatient}` 为用户耐心/参与度;跨轮次合并 filter(新值覆盖旧值),并检测 impatience 信号以提前结束追问。
- **Entropy-Guided Question Selection(熵引导追问)**:在当前候选集 `C` 上,对每个属性维度 `d` 计算 Shannon 熵 `H(d) = -Σ p(v) log2 p(v)`(连续属性如 price/mileage/year 先做 quantile-based 等频分箱,再用归一化熵 `H_norm` 保证跨维度可比)。选取熵最大的可询问维度 `d* = argmax H(d)`;设最小熵阈值 `τ_H = 0.3`,若 `H(d*) < τ_H` 则直接进入推荐(Algorithm 1)。选定维度后由 LLM 结合分布统计与对话历史生成自然问题。
- **Candidate Ranking(候选排序,两种互补策略)**:(i) **Embedding Similarity with MMR**——用 sentence transformer(all-mpnet-base-v2)计算 query 文本与候选描述的余弦相似度,再用 [[maximal-marginal-relevance|MMR]] 去冗余,`λ = 0.85`;(ii) **Coverage-Risk Optimization**——用 phrase-level 语义匹配对齐 item review 的 pros/cons,对喜欢特征算 coverage、对不喜欢特征算 risk,贪心最大化 `Σ Pos - λ Σ Neg`(`λ = 0.5`,`τ = 0.6` 阈值过滤弱匹配),覆盖项的 submodularity 给出 `(1 - 1/e)` 近似保证。
- **Entropy-Based Result Diversification(熵驱动多样化呈现)**:在已排序候选上,从未约束维度 `D_unspec` 中选归一化熵最大的维度 `d_div` 作为展示维度,按其取值分区后从每个分区取 top-n,组成 `r × n` 网格(Grid Bucketing,Algorithm 2),让 trade-off(如 hybrid vs electric)可视、支持通过对比进行偏好发现。
- **边界处理**:零结果时按重要性(cosmetic 先松、fundamental 后松)做 progressive filter relaxation;检测到不耐烦则提前结束 interview。

评估采用 review-driven 模拟用户:以真实车评为锚,改写(rewrite)生成保持情感/评分一致的变体扩大覆盖,再用 LLM 抽取为结构化 persona(显式偏好 + 购物意图 + 聚合偏好信号),生成 initial query 与 latent 行为属性。仿真协议为推荐 agent、模拟用户、自动 LLM judge 三方多轮交互。追问质量由 LLM judge 按 Relevance 与 Newness 两维打二元 pass/fail;推荐质量按 satisfied 标签 + 置信度 `c`,设高置信阈值 `τ = 0.51` 区分 ambiguous 判定,并在均值置信度低时多次重评取多数投票。数据集为 150 personas,分 Short(<10 词,欠规约)与 Long(<120 词,多约束)两种 query verbosity。

## 结果

主要在 car recommendation 域评估(也定性验证了 electronics 域可泛化),报告 Prec@9 / NDCG@9 / Sat@9 / ILD,三次运行均值±标准差(Table 1):

- **MMR 对多样性的影响显著**:去掉 MMR 时 ILD 大幅下降——ES + Short 从 0.779(Full)降到 0.279(−MMR);Long 下 CR 的 ILD 从 0.412 降到 0.241。MMR 是最终推荐列表多样性的主要贡献者。
- **多样性-相关性 trade-off**:去掉 MMR 反而常提升相关性指标——ES + Long 的 Prec@9 从 0.744(Full)升到 0.837(−MMR)。Full 配置在保留多数相关性增益的同时大幅提升多样性。
- **EntropyQ(熵引导追问)持续提升推荐质量**:去掉 EntropyQ 一致使质量下降,Long 设定更明显——ES + Long 的 Prec@9 从 0.744(Full)降到 0.719(−EntropyQ),CR 从 0.801 降到 0.753。
- **排序方法互补**:ES 在 Short(短/欠规约)下整体更稳;CR 在 Long(约束丰富)下 precision 类指标更强。
- **追问质量(Table 2)**:Short 下 EntropyQ 把 Newness 从 0.602(w/o)提升到 0.946(w/);Long 下差距收窄(0.980 vs 0.976),因为用户前置给了大量偏好、高不确定维度变少。Relevance 在所有配置下都接近满分(0.967–1.00),说明 EntropyQ 主要价值在于"问出新信息"而非提升话题相关性。
- **用户调研**:n=12 小规模 pilot,问 0/1/2 个追问的三种策略对比。带更多 elicitation 的 2-追问策略被 9/12 参与者排为最佳,0-追问从未被排第一、被 10/12 排为最差;参与者反映追问帮助补全遗漏约束(如 drivetrain/budget),网格化呈现更便于对比。

整体表明:把不确定性当作贯穿 elicitation、ranking、presentation 的一等信号,优于把三者当独立组件;Long 设定因约束更多更冲突而更具挑战性。

## 在本 wiki 中的位置

这是一篇把 [[large-language-models|LLM]] 驱动的 [[conversational-recommendation|对话式推荐]]/[[interactive-recommendation|交互式推荐]] 与信息论(Shannon 熵)结合的工作,核心贡献在用熵统一 [[preference-elicitation|偏好询问]]、ranking 与 [[recommendation-diversity|推荐多样化]]。与 [[interecagent|InteRecAgent]]、[[recmind|RecMind]] 等 [[llm-agent|LLM agent]] 推荐工作同属"把 LLM 当 agent 做交互推荐"的脉络,但强调可审计的结构化管线(query → SQL filter → embedding 排序 → reranking)。多样化部分扩展了经典 [[maximal-marginal-relevance|MMR]] 与 diversity-aware reranking([[recommendation-diversity]]),把多样化直接绑定到未解析偏好的残余不确定性。评估方法学连接 review-driven [[user-simulation|用户模拟]] 与 LLM judge,可与 [[recsim|RecSim]]、[[kuaisim|KuaiSim]]、SUBER 等 [[recommendation-simulator|推荐模拟器]] 及 LLM-based 用户模拟([[llm-for-recommendation]])对照阅读。
