---
type: source
subtype: paper
tags:
  - multi-agent
  - llm-agent
  - benchmark
  - distributed-systems
  - graph
  - coordination
  - collaboration
created: 2026-05-29
updated: 2026-05-29
arxiv: 2507.08616
raw: raw/2507.08616.pdf
authors:
  - Florian Grötschla
  - Luis Müller
  - Jan Tönshoff
  - Mikhail Galkin
  - Bryan Perozzi
year: 2025
---

# AGENTSNET: Coordination and Collaborative Reasoning in Multi-Agent LLMs

AGENTSNET 是一个面向 [[llm-multi-agent]] 系统的新 [[benchmark]],借鉴分布式计算与图论中的五个经典问题,衡量 agent 网络在给定通信拓扑下的自组织、协调与协作能力,并且规模可任意扩展(实验最多探测 100 个 agent)。

## 问题

[[large-language-models]] 在组成 [[multi-agent-systems]] 时展现出强大的问题求解能力,已有工作(如 [[gptswarm]]、generative agents)表明把 LLM-based agent 组织成结构化拓扑能提升其在 [[mmlu]]、[[humaneval]]、GAIA 等基准上的表现。但现有多 agent 基准并未显式评估多 agent 系统的核心能力——可扩展的协调(scalable coordination)、去中心化通信(decentralized communication)与协作推理(collaborative reasoning),且大多只覆盖 2-5 个 agent。论文要回答:一个复杂的 agent 网络是否真的能有效自组织、并利用其拓扑结构进行协作。

## 方法

- **五个任务,源自分布式计算经典问题**(每个问题映射为一个 agentic 任务,见 Table 1 给出其在 randomized LOCAL 模型下的 round complexity 下界):
  - **Coloring**(((Δ+1))-coloring):每个 agent 选一个分组/颜色,使相邻 agent 颜色不同;复杂度 Ω(log* n)。对应多 agent 系统中的角色/子任务分配以避免冗余。
  - **VertexCover**(minimal vertex cover):选出一组 coordinator,使每条边至少有一端是 coordinator,且满足极小性(去掉任一 coordinator 即破坏覆盖);Ω(log* n)。
  - **Matching**(maximal matching):agent 两两配对,无冲突且无法再加边;Ω(log* n)。
  - **LeaderElection**:全网恰好选出一个 leader,其余都确认非 leader;Ω(D)(D 为网络直径)。
  - **Consensus**:所有 agent 就 {0,1} 中一个值达成一致(无 Byzantine / 故障设定);Ω(D)。
- **基于 message-passing 的 agent 通信(LOCAL 模型)**:每个 agent 是一个 instruction-tuned LLM,只能与图上的直接邻居通信。系统采用同步轮次:每轮先接收邻居上一轮消息,再生成发往各邻居的消息(以 flat JSON 表达,key 为邻居名、value 为消息内容),可选地先输出 [[chain-of-thought]]。固定轮数后要求每个 agent 给出 task-specific 的 final response(字符串格式)。全局任务(LeaderElection、Consensus)用 2D+1 轮;局部任务(Coloring、Matching、VertexCover)按图规模设 4/5/6 轮(对应 4/8/16 节点)。
- **图拓扑**:覆盖 small-world(Watts-Strogatz)、scale-free(preferential attachment / Barabási-Albert)与几何图(Delaunay 三角剖分),以贴近真实网络的结构特性,而非简单 Erdős-Rényi 随机图。
- **评测**:主指标为严格的二元评测——只有整个 agent 网络都满足任务规范才算解出(fraction of solved instances)。附录另给出连续的 soft scores。实现基于 [[langchain]] 与 NetworkX,代码与数据集开源。

## 结果

- **模型对比(Table 2,fraction of solved,4/8/16 节点平均的 AGENTSNET 总分)**:Gemini 2.5 Pro 0.80 最高,Claude 3.7 Sonnet 0.70,Gemini 2.5 Flash 0.69,Gemini 2.5 Flash Thinking 0.68,o4-mini 0.53,Gemini 2.0 Flash 0.48,GPT-4.1 mini 0.45,Llama 4 Maverick 0.38,Llama 4 Scout 0.34,Claude 3.5 Haiku 0.26。
- **任务难度差异**:Consensus 最易被解出(多数模型 0.85-1.00,Claude 3.7 Sonnet 与 Gemini 2.5 Flash 达 1.00);VertexCover 与 Coloring 最难(如 Claude 3.5 Haiku 在 Coloring 仅 0.14、VertexCover 0.08)。
- **性价比**:Gemini 2.5 Flash 与 Claude 3.7 Sonnet 表现接近,但运行成本约低 20 倍(Figure 1 的 Pareto 前沿)。
- **规模化(Figure 5,Gemini 2.0 Flash,20-100 agent)**:性能随网络增大平滑下降,到 100 个 agent 时几乎全任务降至接近 0(如 VertexCover 在 20 节点起就为 0;Consensus 从 85% 降到 15%)。说明 AGENTSNET 难度可随网络规模无限提升,且无需改动基准本身即可与未来更强模型共同 scale。
- **定性发现**:(1)策略协调是核心难点——agent 常太晚才统一策略,或各自在 CoT 中假定策略却不告知邻居;(2)agent 普遍接受邻居发来的信息,但有时不质疑错误信息而导致错解;(3)agent 能帮邻居发现并化解候选解中的冲突(如 Coloring 中的颜色冲突)。

## 在本 wiki 中的位置

本文是评估 [[llm-multi-agent]] 协调与协作能力的 [[benchmark]] 类 source,把分布式计算/图论问题作为多 agent 推理的测试床,可与 [[gptswarm]]、[[agentverse]]、[[agentbench]] 等多 agent 系统与基准工作对照。它与 [[multi-agent-collaboration]]、[[multi-agent-systems]]、[[chain-of-thought]] 等概念相关,并在 [[gpt-4]]、[[claude]]、[[gemini]]、[[llama]] 等前沿模型上给出横向比较。出自 [[google-research]] 与 [[eth-zurich]] 等机构。
