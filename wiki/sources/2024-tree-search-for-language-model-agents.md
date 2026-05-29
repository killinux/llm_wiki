---
type: source
subtype: paper
tags: [llm-agent, tree-search, web-agent, test-time-compute, monte-carlo-tree-search, gpt-4, planning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2407.01476
raw: raw/2407.01476.pdf
authors: [Jing Yu Koh, Stephen McAleer, Daniel Fried, Ruslan Salakhutdinov]
year: 2024
---

# Tree Search for Language Model Agents

为基于 LLM 的 web agent 提出一种 inference-time 的 best-first tree search 算法,在真实交互式 web 环境中显式进行 exploration 与 multi-step planning,把 GPT-4o agent 在 VisualWebArena 上的成功率相对提升 39.7%(达到 SOTA 26.4%),并展示了 [[test-time-compute]] scaling 的收益。

## 问题

由 language model 驱动的 [[autonomous-agents]] 在 web 自动化等决策任务上展现潜力,但 LM 主要为自然语言理解与生成而优化,在解决真实计算机任务时面临 multi-step reasoning、planning 以及利用环境反馈的困难。当前最好的 LM agent 在真实 web benchmark 上远不及人类:在 [[webarena]] 与 VisualWebArena 上人类成功率分别为 78% 和 89%,而即便最强的 frontier 模型成功率通常低于 20%。

一个核心瓶颈在于现有 agent 无法利用 test-time computation 做 exploration 与 multi-step planning。大多数方法把任务当作 partially observable MDP,只依据当前 observation $o_t$ 预测下一动作 $a_t$,导致误差逐步累积——若在某步走错且进入坏状态,无法轻易纠正。web 环境的动作空间(一个网页上所有可能动作)远大于多数视频游戏或文本模拟器,因此高效 exploration 与 pruning 尤为关键。

## 方法

作者提出一种 **best-first tree search**,在实际环境空间内运行(grounded in the actual environment space),并与多数 SOTA agent 互补。这是据作者所知首个在真实 web 任务上展现有效性的 LM agent 树搜索算法。

- **Agent backbone**:任意 prompt-based 的(multimodal)LM agent $f_\phi$,以当前 observation 预测下一动作,可结合 [[react-reasoning-and-acting]]、RCI、[[chain-of-thought]] 等 prompting 技术。本方法无需重训或微调 $f_\phi$。
- **Value function**:用 best-first 启发式,value function $f_v$ 估计当前状态 $s_t$ 的期望 reward $\mathbb{E}[R(s_t)] \in [0,1]$,以 task instruction $I$ 与历史 observation 为条件:$v_t = f_v(I, \{o_1,...,o_t\})$。实现上用一个 multimodal LM(GPT-4o)接收 task instruction 与 observation 截图,被指示输出当前状态是 success/failure/在通往成功的轨迹上,分别赋值 1/0/0.5。借鉴 [[self-consistency]],用 CoT 采样 20 条 reasoning path 并取平均,得到细粒度可靠分数。
- **Search algorithm**:loosely 受 A* search 启发的 best-first search。超参为 depth $d$、branching factor $b$、search budget $c$。维护一个 frontier $\mathcal{F}$(max priority queue)。每次迭代从 frontier 弹出得分最高的状态 $s_p$,用 value function 算分 $v_p$;若 $v_p$ 超过当前最佳则更新最佳状态 $\hat{s}_t$。若 $v_p \geq \theta$(可能找到 goal)或 $s \geq c$(预算耗尽)则终止并导航到 $\hat{s}_t$;否则在深度允许下用 $f_\phi$ 生成 $b$ 个候选动作,执行后把结果状态加入 frontier,并通过 backtracking 重复。动作通过 nucleus sampling(温度 1.0,top-p 0.95)采样,每步生成 20 个 CoT 输出并取计数最高的 top-$b$ 动作分支。

实验搜索参数:$d=5$、$b=5$、$c=20$,最多执行 5 步动作。

## 结果

在完整的 910 个 VisualWebArena (VWA) 与 812 个 [[webarena]] (WA) 任务上评测:

- **VWA**:GPT-4o + SoM 加搜索后成功率从 18.9% 提升到 **26.4%**(相对 +39.7%),刷新 SOTA。弱基座 Llama-3-70B-Instruct + captions 从 7.6% 提升到 16.7%(相对 +119.7%)。
- **WA**:GPT-4o 加搜索从 15.0% 提升到 **19.2%**(相对 +28.0%);Llama-3-70B-Instruct 从 7.6% 提升到 10.1%(相对 +32.2%/+32.3%)。
- **Search budget scaling**(200 VWA 子集,$d=5,b=5$):成功率随 budget $c$ 增大而上升。$c=5$ 即把成功率从 24.5% 提升到 32.0%(相对 +30.6%);$c=20$ 提升到 37.0%(相对 +51.0%),凸显 [[test-time-compute]] scaling 的价值。
- **Depth 与 breadth ablation**:同时增大 $b$ 与 $d$ 才能取得强性能;$d=5,b=5$ 时 SR 37.0%(相对 +51%)。
- **Value function ablation**(Tab.4):无搜索 24.5%;LLaVA-1.6-34B(w/ SC, n=20)30.0%;GPT-4o(no SC)28.5%;GPT-4o(w/ SC, n=5)32.5%;GPT-4o(w/ SC, n=20)37.0%;groundtruth value 上界 43.5%。GPT-4o value function 显著优于 LLaVA,self-consistency 采样数增加有益。

代码与模型发布于 jykoh.com/search-agents。

## 在本 wiki 中的位置

本文把经典 [[tree-search]] / best-first search(及 A*、[[monte-carlo-tree-search]] 思想)引入 [[llm-agent]] 的 web 自动化场景,是 [[test-time-scaling]] / [[test-time-compute]] 在 agent 领域的代表性工作。它与 [[tree-of-thoughts]]、[[reasoning-via-planning-rap]]、[[language-agent-tree-search]] 等"LLM + 搜索"路线相关,但区别在于直接在真实环境空间(而非纯文本推理空间)中搜索并利用环境反馈。方法与 [[react-reasoning-and-acting]]、[[reflexion]] 等基座 agent 互补,在 [[webarena]] / VisualWebArena 等 benchmark 上评测,基座用 [[gpt-4]](GPT-4o)与 [[llama]] (Llama-3-70B)。出自 Carnegie Mellon University。
