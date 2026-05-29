---
type: source
subtype: paper
tags:
  - llm-agent
  - game-theory
  - multi-agent-systems
  - ai-agent-behavioral-science
  - cooperation
  - machine-behavior
created: 2026-05-29
updated: 2026-05-29
arxiv: 2512.07462
raw: raw/2512.07462.pdf
authors:
  - Trung-Kiet Huynh
  - Duy-Minh Dao-Sy
  - Thanh-Bang Cao
  - Phong-Hao Le
  - Hong-Dan Nguyen
  - Phu-Quy Nguyen-Lam
  - Minh-Luan Nguyen-Vo
  - Hong-Phat Pham
  - Phu-Hoa Pham
  - Thien-Kim Than
  - Chi-Nguyen Tran
  - Huy Tran
  - Gia-Thoai Tran-Le
  - Alessio Buscemi
  - Le Hong Trang
  - The Anh Han
year: 2025
---

# Understanding LLM Agent Behaviours via Game Theory: Strategy Recognition, Biases and Multi-Agent Dynamics

通过博弈论框架(扩展 [[fairgame]])系统审计 LLM agent 在重复社会困境中的策略行为,发现稳定的、与模型和语言相关的合作偏差,并用监督分类模型把 LLM 的行为轨迹映射到经典博弈策略以识别其潜在意图。

## 问题

LLM 越来越多地作为自主决策者部署在交互式与多智能体系统中(推荐、协商、多任务助手),在这些场景中会反复面对**合作困境**(cooperation dilemma):贡献共同目标、搭便车(free-riding)或执行社会规范。评估这类系统不能只看事实正确性或对话质量,而需要分析 agent 随时间表现出的**涌现策略**(emergent strategy)及其背后的**行为意图**(behavioural intention,定义为把历史交互映射到当前行动的决策规则)。

已有的 [[fairgame]] 框架主要聚焦于对称的两人矩阵博弈、同质玩家与简单的结果度量(如平均合作率),留下两个未解问题:(i) 即使博弈结构固定,LLM agent 对**收益绝对量级(stakes)**的敏感性如何;(ii) 在多玩家共享公共物品、可能出现联盟与协调的群体环境中,它们如何行为。

## 方法

工作沿两个互补方向扩展 [[fairgame]],并叠加一个机器学习意图识别流水线:

- **收益缩放的 Prisoner's Dilemma**:固定 PD 收益矩阵的策略结构(T>R>P>S,基线 (6,6)/(0,10)/(10,0)/(2,2)),引入标量 λ∈{0.1, 1.0, 10.0} 整体缩放所有收益,对应衰减、基线、放大三种 stakes。博弈进行固定 T=10 轮,agent 在每轮看到完整公开历史。中性框架下 Option A=defection、Option B=cooperation,prompt 不含道德语言。每个设置评估 40 局、400 次决策,跨 [[gpt-4o]]、[[claude-3-5-haiku]]、Mistral Large 三个 backend,并用英语与越南语两种语言实例化。

- **三人 Public Goods Game(PGG)**:群体规模 N=3(产生非两人效应的最小群体),贡献成本 c=10,协同因子(multiplication factor)r∈{1.1, 2.0, 2.9},每轮 agent 选择 Contribute 或 Keep,收益按公式 π_i = r·Σs_j·c/N − s_i·c 计算。把 [[fairgame]] 的 2×2 静态矩阵替换为动态公共物品收益模块,历史泛化为向量值记录,prompt 适配多智能体群体激励(见 Algorithm 1)。固定 T=10 轮,每个(语言, 模型, r)组合重复 10 次。

- **行为意图识别流水线**:遵循 Di Stefano 等人的协议,基于四种经典策略 ALLC(Always Cooperate)、ALLD(Always Defect)、[[tit-for-tat]](TFT)、WSLS(Win-Stay-Lose-Shift)合成带执行噪声(ε∈{0, 0.05})的 [[iterated-prisoners-dilemma]] 轨迹,训练 [[logistic-regression]]、[[random-forest]]、Neural Network、[[lstm]] 四类分类器。把 [[fairgame]] 日志的中性标签(OptionA/OptionB)编码为基于上一轮联合行动的 state-action 格式(R/P/T/S),用最佳模型在概率 >0.9 的高置信预测上推断 LLM 采用的策略。对单标签 LSTM 的局限,叠加规则化标注以覆盖多策略模式。

## 结果

- **收益量级敏感性(PD)**:λ=0.1(very low stakes)在所有模型/语言/人格配对下产生**最高的总惩罚**(即合作最少、defection 最频繁),与演化博弈论预测一致;ordinary 与 high 设置模式相近。不同模型对 λ 的反应方向不同:[[gpt-4o]] 随收益缩小越来越自私;Mistral Large 趋势相反;[[claude-3-5-haiku]] 关系较弱且不一致。
- **跨语言差异**:越南语语境强烈偏向 defection;从英语切到越南语时多个模型行为反转。PGG 中合作率随 r 增加而上升(符合博弈论预测);英语合作开始约 40-60% 并平滑下降,越南语在早期就更陡峭地崩塌至更低水平。合作型情境下英越跨语言差距最高达 **29 个百分点**。
- **末期效应与协调**:后期 strategy mismatch 大幅下降,agent 收敛到共同(多为非合作)行为模式,Mistral Large 收敛最强(round 10 mismatch 接近 0)。selfish 人格下三模型在首轮后迅速一致;cooperative 人格维持更高的行为异质性。
- **模型特定偏差**:[[claude-3-5-haiku]] 即便在 selfish 框架下仍维持约 **2%** 残余合作(prosocial bias);[[gpt-4o]] selfish 场景下两语言均零合作(最强人格遵从)但 cooperative 场景跨语言分歧最大;Mistral Large 语言不变性最强、跨语言不一致性最低。
- **分类器与策略分布**:在 5% 噪声下 [[lstm]] 准确率最高(约 **94%**,Accuracy/F1≈0.984),优于 [[logistic-regression]](约 0.756)与 [[random-forest]](约 0.980 但对噪声更敏感);LSTM 的循环结构对执行噪声更鲁棒。高置信策略分布显示 Claude 3.5 Sonnet 偏合作(ALLC 31.7%、WSLS 29.6%);Llama 3.1 405B Instruct 强烈偏 WSLS(46.5%);Mistral Large 分布最均衡(TFT 29.9%);[[gpt-4o]] 偏 WSLS(34.1%)且 ALLD 最低(10.2%)。聚合分析提出 "Linguistic-Cultural Priming":语言作为潜变量影响策略,Arabic/Vietnamese 偏 defect-heavy,English/Chinese 偏自适应 WSLS,French 最合作(AC+TFT)。

## 在本 wiki 中的位置

本文属于 [[ai-agent-behavioral-science]] / [[machine-behavior]] 方向,把 [[game-theory]] 与 [[social-simulation]] 用作审计 [[llm-agent]] 策略行为的统一方法论。它直接扩展 [[fairgame]] 基准,使用 [[iterated-prisoners-dilemma]] 与 Public Goods Game 这两个经典 [[cooperation]] 困境,与同样研究 LLM 多智能体合作/博弈行为的工作(如 [[cogbench]]、[[sotopia]]、[[oasis]])相关。其用监督分类器(含 [[lstm]])从行为轨迹反推 [[tit-for-tat]] 等经典策略的做法,是把 [[multi-agent-systems]] 安全审计与 [[ai-alignment]]、AI governance 联系起来的一条路径,呼应 [[generative-agents]] 与 [[human-behavior-simulation]] 中关于模型对齐如何塑造策略的讨论。
