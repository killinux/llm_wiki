---
type: source
subtype: paper
tags:
  - llm-agent
  - tool-use
  - tool-planning
  - monte-carlo-tree-search
  - llm-planning
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.12740
raw: raw/2603.12740.pdf
authors:
  - Shuo Yang
  - Soyeon Caren Han
  - Yihao Ding
  - Shuhe Wang
  - Eduard Hovy
year: 2026
---

# ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning

ToolTree 是一个免训练、即插即用的 [[monte-carlo-tree-search]] 风格 [[tool-planning]] 框架,通过执行前 (pre-evaluation) 与执行后 (post-evaluation) 双重反馈引导搜索,并据此做双向剪枝,在固定计算预算下让 [[llm-agents|llm-agent]] 更高效地规划多工具调用。

## 问题

当前 [[large-language-models]] 智能体的工具规划主要有两条路线,各有缺陷:

- **贪婪式 (greedy-based)**:在每一步独立选择当下看起来最合适的工具(如 [[react|react-reasoning-and-acting]]、[[chain-of-thought]]),缺乏前瞻(lookahead),早期的次优选择会不可逆地传播并放大错误,且只沿单条轨迹推进、不探索备选。
- **搜索式 (search-based)**:扩展多个候选分支(如 [[tree-of-thoughts]]、MCTS)以引入前瞻,但工具引入后分支因子随工具类型/参数/演化状态指数级增长,导致成本高、延迟不可预测。更关键的是,许多变体评估的是假想的"想法"而非真实执行动作,排序与真实工具效用解耦,后续几步才显现的改进难以归功到早期决策上。

因此需要一种既有前瞻、又以真实执行结果为依据 (outcome-grounded),同时在固定预算下保持计算高效的规划方法。

## 方法

ToolTree 把工具规划建模为序贯决策过程:每个状态编码当前对话上下文与中间结果,每个动作对应从工具库 $\mathcal{T}_{lib}$ 中调用一个工具(工具用 JSON 格式的结构化 tool card 描述)。它把工具选择、执行、评估、剪枝直接整合进单个 MCTS 循环中,无需独立 planner、无需任务特定再训练。核心是两个轻量、免训练的信号:

- **Pre-Evaluation(执行前评估)**:对新出现的 $(s,a)$ 对,用 LLM judge 基于上下文、tool card(I/O schema、领域标签、示例)和 schema 合法的参数草稿打分 $r_{pre}(s,a)\in[0,1]$,预测工具在调用前的有用性。该分数进入选择策略,作为先验增强的 UCT 探索项:$\text{UCT}(s,a)=Q(s,a)+\lambda\, r_{pre}(s,a)\sqrt{\ln N(s)/N(s,a)}$。
- **Post-Evaluation(执行后评估)**:执行 $(s,a)$ 得到真实输出 $o_{t+1}$ 后,用同一 LLM judge 评估任务一致性(正确性代理、相关性、约束满足)与鲁棒性,得 $r_{post}(s,a)=J(C_t,a,o_{t+1})\in[0,1]$,作为 rollout reward 通过 backward propagation 更新 $Q(s,a)$。因为基于真实执行的动作,给出忠实的 credit assignment。

**Bidirectional Pruning(双向剪枝)**:
- 执行前剪枝(pre-pruning):若 $r_{pre}(s,a)<\tau_{pre}$ 或不在 top-$K$ 之内,则丢弃该子节点,$\mathcal{A}_{keep}(s_t)=\text{top-}K(\mathcal{A}^+(s_t);r_{pre})$,在调用任何工具前就削减分支因子。
- 执行后剪枝(post-pruning):执行后若 $r_{post}(s,a)<\tau_{post}$,标记该节点不可再扩展,停止在无效续接上消耗预算。

整体流程为 Selection → Pre-Evaluation → Expansion → Execution → Post-Evaluation → Backward Propagation,迭代直至预算耗尽或改进饱和,最后由 Answer Predictor 取最高奖励的工具轨迹生成最终预测。执行时还用确定性缓存复用相同 $(a,\text{args})$ 调用、失败附加错误 token。

## 结果

在 4 个 benchmark 上评测,覆盖闭集 (closed-set) 与开集 (open-set) 两类工具规划:

- **闭集**:[[gta]] 与 m&m(小型固定工具集、带类型 I/O、短多跳链)。在 GTA + [[gpt-4o]] 上,ToolTree 平均得分 66.95,超过 vanilla MCTS 基线 2.2+ 分;step-by-step 的 Tool F1 79.26、Arg F1 50.84,end-to-end 的 Plan F1 85.53、Exec F1 52.17。在 m&m + GPT-4o 上平均 88.61,超 zero-shot 8+ 分。在 [[gpt-4o-mini]] 上也保持一致优势(GTA AVG 55.89、m&m AVG 76.90)。
- **开集**:[[toolbench]] 与 RestBench(16,464 / 143 个真实 API,需检索-再规划)。ToolBench + GPT-4o 上 AVG 69.04(Pass 61.27 / Win 76.81),约比最强基线高 +2.5;RestBench-TMDB 上 AVG 74.50,比次优高 +3.1。
- **效率**:扫描 step limit,ToolTree 在每个预算下性能均领先,最大增益在 16-64 步区间;虽比 ReAct/Best-first 慢、约与 ToT 相当且通常低于 LATS,但在 32-64 步取得最高的 accuracy-per-second(每秒边际增益),甜点约在 32-64 步。
- **消融**:在 GTA + GPT-4o 上,完整 ToolTree 以最低 token 成本 (18.2k) 取得最高 accuracy 76.44。去掉 post-evaluation 掉 7+ 分(76.44→68.94),token 升至 22.9k;去掉 pre-pruning 使节点中位数从约 95 降到约 70 的反向变化(pre-pruning 主要削减扩展节点数),去掉 post-pruning 使 rollout 中位数从约 47 降到约 33。
- **可扩展性**:在 Qwen 与 LLaMA 两个家族上性能随模型尺寸单调提升;在 Contriever / RoBERTa / BM25 三种检索器下均最优,且弱检索下退化最小;工具库从 14 扩到 10014 仍可扩展。
- 与之相比,greedy 控制器(Zero-shot/ReAct/CoT)落后于搜索式方法,ToT、A*、LATS 渐进改进但仍不及 ToolTree。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] 的 [[tool-use]] / [[tool-planning]] 方向,把 [[monte-carlo-tree-search]] 与 [[llm-planning]] 结合,可与 [[react|react-reasoning-and-acting]]、[[tree-of-thoughts]]、[[language-agent-tree-search]] 等推理/搜索范式对照阅读;其双向剪枝由 [[llm-as-judge]] 提供 pre/post 双信号,与 [[toolformer]]、[[toolbench]]、[[gaia]] 等工具使用与评测工作相关。评测在 [[gpt-4o]]、[[gpt-4o-mini]] 及 [[qwen]]、[[llama]] 等模型上完成。
