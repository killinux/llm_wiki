---
type: concept
subtype: method
tags: [in-context-learning, prompting, few-shot, llm]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# In-Context Learning

In-Context Learning (ICL) 指大模型在不更新自身参数的前提下,仅通过提示(prompt)中给出的示例或上下文信息来完成新任务的能力。

## 在本 wiki 中的出现

- [[2022-chain-of-thought]]:ICL 的载体与增强对象。该工作在 few-shot 的 in-context 示例中加入中间推理步骤(chain-of-thought prompting),使大模型在不微调的情况下显著提升多步推理能力,且该增益随模型规模涌现(PaLM 540B 在 GSM8K 上达 57%)。
- [[2023-critic]]:ICL 与外部反馈结合。CRITIC 在 in-context 框架下让 LLM 通过与搜索引擎、代码解释器、PERSPECTIVE API 等外部工具交互来自我验证并迭代修正输出,证明外部反馈对自我改进至关重要。
- [[2023-expel]]:ICL 作为无参数学习的实现路径。ExpeL 让 LLM Agent 不更新参数,从跨任务经验中自主抽取自然语言洞见并召回相似成功轨迹,将历史经验作为上下文注入以提升决策表现。
- [[2023-recommender-ai-agent-interec]]:提出 InteRecAgent,以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思构建交互式对话推荐 agent,并蒸馏出 7B 的 RecLlama。
- [[2024-autoguide-context-aware-guidelines]]:AUTOGUIDE 从离线经验中自动生成并按当前情境检索上下文感知指引,显著提升 LLM 智能体在 ALFWorld、WebShop、WebArena 等序列决策与网页导航任务上的成功率。
- [[2024-stateact-self-prompting-state-tracking]]:StateAct 通过 self-prompting 与 chain-of-states 状态跟踪增强 LLM base agent,纯 in-context learning 即在 Alfworld/Webshop/Textcraft 上比 ReAct 提升 7%-30%。
- [[2024-opencity-urban-llm-agents]]:通过 LLM 请求调度器与 group-and-distill 提示优化,把万级城市 LLM agent 模拟加速约 600 倍,使 10000 agent 的一天活动可在 1 小时内于普通硬件完成。
- [[2026-convapparel-user-simulator-validation]]:Google 提出 ConvApparel(4,146 段人-AI 服装购物对话、双 agent good/bad 协议、逐轮第一人称标注)及 PLSA+HLS+counterfactual validation 三支柱框架,系统量化 LLM user simulator 的 realism gap,发现所有 simulator 平均 HLS 仅 0.004,但 ICL/SFT 在反事实泛化上优于纯 prompting。
- [[2026-experiential-reflective-learning]]:ERL:agent 反思单次任务轨迹与成败信号、提炼可迁移启发式存入持久池,新任务时按相关性检索 top-k 注入上下文,无需更新参数即可自我改进,在 Gaia2 上比 ReAct 基线提升 7.8% 成功率。

## 相关

- [[few-shot-learning]]
- [[chain-of-thought|chain-of-thought-prompting]]
- [[prompting]]
- [[emergent-abilities]]
- [[llm-agents|llm-agent]]
- [[self-correction]]
