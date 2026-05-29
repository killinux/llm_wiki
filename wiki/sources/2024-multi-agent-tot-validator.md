---
type: source
subtype: paper
tags:
  - llm-multi-agent
  - reasoning
  - tree-of-thoughts
  - math-benchmark
  - self-verification
created: 2026-05-29
updated: 2026-05-29
arxiv: "2409.11527"
raw: raw/2409.11527.pdf
authors:
  - Fatemeh Haji
  - Mazal Bethany
  - Maryam Tabar
  - Cho-Yu Jason Chiang
  - Anthony Rios
  - Peyman Najafirad
year: 2024
---

# Improving LLM Reasoning with Multi-Agent Tree-of-Thought Validator Agent

将 [[tree-of-thoughts]] 与多智能体推理结合,引入一个 Thought Validator agent 对各 Reasoner 的推理分支做有效性校验,只有逻辑成立的分支才参与共识投票,从而在 [[gsm8k]] 上稳定提升 [[large-language-models]] 的算术推理表现。

## 问题

[[llm-multi-agent]] 策略通过给不同 agent 分配专门角色来增强 [[reasoning]],但其中的 "Reasoner" agent 往往对推理路径探索过浅(shallow exploration),无法充分覆盖问题空间。[[tree-of-thoughts]](ToT)能通过探索多条推理路径缓解这一问题,但也带来新风险:ToT 可能生成存在逻辑缺陷的推理分支(flawed reasoning branches),若不加校验,这些错误路径会进入最终的多数投票,损害答案的可信度(trustworthiness)。现有方法(如 CFMAD、CausalGPT)仍受限于推理路径采样过浅或简单多数投票,容易传播早期推理错误。

## 方法

提出一个结合 ToT 的多智能体框架,核心是新增 **Thought Validator agent**。整体流程见论文 Figure 1:

- **Reasoner Agent**:多个 Reasoner 并行运行,每个使用 [[tree-of-thoughts]] 探索不同推理路径。形式化为对状态树的搜索,状态 $s_t = [Q, z_1, \dots, z_t]$ 包含查询 $Q$ 与中间推理步。分三步:
  - Step 1 思维路径分解与生成:由 Thought Generator $G(p_\theta, s_t, k)$ 从每个状态生成多个后续分支(对比 [[chain-of-thought]] 的单一线性路径)。
  - Step 2 状态评估与路径选择:state evaluation agent 给每步打分 $V(p_\theta, s_{t+1})$,每层选最高分分支展开,$s^*_{t+1} = \arg\max V$。
  - Step 3 推理分支构造:每个 Reasoner 取各层最高分步骤,得到链 $C_i = [z^*_1 \dots z^*_T]$。
- **Thought Validator Agent**:灵感来自老师给学生反馈,对每条分支 $C_i$ 做三项检查——逻辑一致性(logical consistency)、事实准确性(factual accuracy)、完整性(是否完整回答原问题),输出二值校验状态 $V_i \in \{0,1\}$。
- **共识投票(Consensus-Based Voting)**:只有 $V_i=1$ 的分支参与投票,被判无效的弃权,$S^* = \arg\max_S \sum_i V_i \cdot \delta(S=S_i)$。
- **迭代精炼(Iterative Refinement)**:若未达共识,带着 Validator 的反馈开启新一轮推理,直至达成共识或超过最大迭代次数。

实验设置:ToT 树深 2、宽 5(沿用 Yao 等人参数);IO/CoT/ToT 用 temperature=1、top_p=1;Thought Validator 用 temperature=0.5、top_p=0.4 以提高确定性。

## 结果

在 [[gsm8k]](随机抽取 500 个样本作为测试集)上,跨四个 LLM 评测,准确率(%)对比见 Table 1:

| Method | [[gpt-3-5-turbo]] | [[gpt-4o-mini]] | [[llama-3]].1-8B | Llama3.1-70B |
|---|---|---|---|---|
| Standard IO | 60.0 | 91.2 | 75.4 | 93.0 |
| [[chain-of-thought]] | 68.0 | 89.2 | 76.0 | 89.4 |
| [[tree-of-thoughts]] | 75.4 | 91.6 | 80.2 | 92.8 |
| **MA ToT + Thought Validator** | **84.2** | **92.2** | **89.0** | **94.8** |

- 本方法在四个模型上全面领先,**相比标准 ToT 平均提升 5.6 个百分点**。
- 在 GPT-3.5-turbo 上提升最大:相比 ToT 提升 **8.8 个百分点**(75.4% → 84.2%)。
- 当基线模型本就很强时(GPT-4o-mini、Llama3.1-70B),ToT 与其他方法的增益收窄,说明 ToT 的效果取决于任务难度与模型能力,在更具挑战性的推理任务上收益更明显。

局限:ToT 采用固定树宽/深度,缺乏动态探索,简单问题易引入冗余、难题又探索不足;方法计算开销大——500 样本评测中,GPT-3.5-turbo 每题平均 token 从 CoT 的 256 增至 ToT 的 4000,GPT-4o-mini 从 341 增至 10600;每个 Reasoner 每题约 20 次 API 调用,还要乘以 agent 数与校验步骤。评测仅限 GSM8K 算术推理,泛化性待验证。代码:https://github.com/SecureAIAutonomyLab/MA-ToT

## 在本 wiki 中的位置

本文处于 [[llm-multi-agent]] 与 [[reasoning]] 的交叉点,将 [[tree-of-thoughts]] 作为 Reasoner 的探索机制,并叠加一个独立的验证 agent 做 [[self-verification]] 式的分支过滤。其 Thought Validator 思路与 [[self-refine]]、[[reflexion]] 等 [[self-correction]] 工作相关,共识投票则与 [[self-consistency]]、[[multi-agent-debate]] 一脉相承。相关多智能体方法包括 [[multi-agent-collaboration]]、CausalGPT、Counterfactual Multi-Agent Debate(CFMAD)。评测基准为 [[gsm8k]],对比基线含 [[chain-of-thought]] 与标准 IO prompting。
