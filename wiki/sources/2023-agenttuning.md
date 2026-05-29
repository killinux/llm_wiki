---
type: source
subtype: paper
tags: [llm-agent, instruction-tuning, agentbench, llama-2, fine-tuning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2310.12823
raw: raw/2310.12823.pdf
authors: [Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao Liu, Yuxiao Dong, Jie Tang]
year: 2023
---

# AgentTuning: Enabling Generalized Agent Abilities for LLMs

AgentTuning 提出一种轻量 instruction-tuning 方法,通过构建跨任务的 agent 交互轨迹数据集 AgentInstruct 并与通用指令混合微调,使开源 [[llama-2]] 在 agent 任务上获得可泛化的能力,同时不损害其通用 LLM 能力。

## 问题

开源 [[large-language-models]](如 [[llama-2]]、[[vicuna]])在传统 NLP 任务上表现良好,但作为 [[autonomous-agents]] 处理真实复杂任务时,显著落后于 [[gpt-3-5]] 和 [[gpt-4]] 等商业模型(见 [[agentbench]] 评测)。已有研究多聚焦于为单一 agent 任务设计 prompt 或框架(如 [[react]]),或在特定任务上微调,这会牺牲模型的通用能力和泛化性。缺乏一种端到端、能从根本上增强 LLM agent 能力且不损害通用能力的方法。

## 方法

AgentTuning 由两部分组成:

- **AgentInstruct 数据集**:一个轻量级 instruction-tuning 数据集,涵盖 6 个 agent 任务([[alfworld]]、[[webshop]]、[[mind2web]]、Knowledge Graph、Operating System、Database,均来自 [[agentbench]]),最终包含 1,866 条经过筛选的高质量交互轨迹,每条轨迹带有 [[chain-of-thought]] 推理(采用 [[react]] 的 thought-action 框架)。构建分三阶段:
  - **Instruction Construction**:有训练集的任务直接取训练 split;无训练集的 OS 与 Database 任务用 Task Derivation(从 BIRD 数据集派生)和 Self-Instruct 方法生成。
  - **Trajectory Interaction**:用 [[gpt-4]](gpt-4-0613)作为 agent 进行 1-shot 交互采集轨迹,Mind2Web 因预算部分用 [[gpt-3-5-turbo]]。
  - **Trajectory Filtering**:按最终 reward r 筛选,多数任务取 r=1(完全正确),Mind2Web 取 r≥2/3。消融显示筛选后(held-in 1.96 / held-out 0.65)显著优于未筛选(1.34 / 0.47),凸显数据质量重于数量。
- **混合 instruction tuning**:将 AgentInstruct 与来自 [[sharegpt]] 的通用域指令(57,096 条 GPT-3.5 + 3,670 条 GPT-4 对话,采样比 1:4)按比例 η 混合。损失函数 J(θ)=η·E_agent[log π_θ] + (1-η)·E_general[log π_θ]。在 7B 上从 0 到 1 扫描,最终选 η=0.2。基座为 [[llama-2]] chat 版(7B/13B/70B),用 Megatron-LM 微调,得到 AgentLM 系列。

## 结果

(Overall 为同类任务加权平均,各任务跨模型归一化到均值 1)

- **Held-in(6 任务)**:AgentLM-70B Overall 2.55,接近 [[gpt-4]](2.75),远超 Llama-2-70B(0.27)与 [[gpt-3-5]](1.59)。AgentLM 在 ALFWorld(86.0 vs GPT-4 78.0)、Database(37.7 vs 33.7)等任务上超过 GPT-4。
- **Held-out(6 未见任务:SciWorld、MiniWoB++、WebArena、HotpotQA、ReWOO、Digital Card Game)**:AgentLM-70B Overall 1.40(相对 7B +176%),接近 [[gpt-3-5]](1.49);7B 为 0.67(+76%),13B 为 0.78(+57%)。表明更大模型泛化能力更强。
- **General 任务([[mmlu]]、[[humaneval]]、[[gsm8k]]、MT-Bench)**:AgentLM-70B Overall 0.96(+1%),与原 Llama-2 持平(7B -1%、13B -7%),说明 agent 能力增强未损害通用能力。
- **错误分析**:相比 Llama-2,AgentLM 显著减少 invalid action、重复生成、拒绝回答等基础错误,说明 AgentTuning 激活了模型固有的 agent 潜能而非过拟合。
- **消融**:仅用 agent 数据训练在 held-in 上提升明显但泛化差;混合通用数据对 held-out 泛化至关重要;70B 在混合训练下 held-out 出现明显跃升(从 agent-only 0.87 到 1.40)。

## 在本 wiki 中的位置

本文是 [[llm-agents|llm-agent]] 训练方向的代表工作,与侧重 prompt/框架的 [[react]]、[[reflexion]]、[[tree-of-thoughts]] 不同,它通过 [[instruction-tuning]] 从根本上增强开源 LLM 的 agent 能力。评测建立在 [[agentbench]] 之上,基座为 [[llama-2]],数据生成依赖 [[gpt-4]] 与 Self-Instruct。可与 [[toolformer]]、[[fine-tuning]]、[[chain-of-thought]] 等条目互参。作者团队来自 [[tsinghua-university]] 与 Zhipu.AI,与 [[chatglm]]、[[thudm]] 同源。
