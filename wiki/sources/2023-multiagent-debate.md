---
type: source
subtype: paper
tags: [multi-agent, debate, reasoning, factuality, llm, prompting]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2305.14325
raw: raw/2305.14325.pdf
authors: [Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, Igor Mordatch]
year: 2023
---

让多个 LLM 实例针对同一问题各自给出答案,再经过多轮"辩论"互相参考与批评对方的回答,从而显著提升推理质量与事实准确性。

## 问题

单个 LLM 在推理与事实性任务上容易产生不一致、错误甚至"幻觉"的输出。已有方法如 [[chain-of-thought]]、[[self-consistency]] 以及自我反思(self-reflection)主要依赖单一模型实例的内部链路改进,难以纠正模型自身坚信的错误。作者提出一个互补的思路:利用多个语言模型实例之间的交互来逼近更可靠的答案。

## 方法

灵感来自 Minsky 的《Society of Mind》。提出 **multiagent debate(多智能体辩论)** 框架:

- 同一问题交给多个 LLM 实例(agent),每个先独立生成一个初始回答与推理过程。
- 进入多轮辩论:每一轮,把其他 agent 上一轮的回答拼接(或先 summarize)进 prompt,要求每个 agent 参考其他人的回答并更新/批判自己的答案。这一过程被视为一个 multi-agent game,经验上多轮后会收敛到单一共识答案。
- 该方法与具体模型无关,只需黑盒访问语言生成(不需要 likelihood / 梯度),可直接套用在现成 LLM 上,无需额外训练或微调;并与 [[chain-of-thought]]、retrieval 等单模型方法正交,可叠加。
- 作者用不同 prompt(short/long debate prompt)控制 agent 对自身答案的"坚持程度",发现鼓励更长辩论的 prompt 收敛更慢但最终共识更准确。
- 主实验全部用 gpt-3.5-turbo-0301(chatGPT),典型配置为 3 个 agent、2 轮辩论;并探讨了 [[chatgpt]] 与 [[bard]] 跨模型辩论。

## 结果

主实验用 3 个 agent、2 轮辩论(zero-shot)。

推理任务(Table 1,Single Agent vs Multi-Agent Debate):
- Arithmetic(六个两位数算术表达式):67.0% → 81.8%
- Grade School Math(GSM8K):77.0% → 85.0%
- Chess(走子优劣,Stockfish 估的相对 pawn score ΔPS):91.4 → 122.9
- 其中 reflection(自我反思)基线只带来小幅提升;debate 提升远大于 reflection 与 majority voting。

事实性任务(Table 2):
- Biographies(作者新构建的 524 位计算机科学家传记 ground-truth 数据集):66.0% → 73.8%
- MMLU:63.9% → 71.1%(用不同 persona 初始化可进一步到 74.2%)
- Chess Move Validity(BIG-Bench Chess-State Tracking 的 synthetic_short 任务):29.3% → 45.2%
- 在事实性设定下 reflection 反而表现较差,debate 在所有三项上都显著优于各基线。

其他发现:
- 增加 agent 数量(图 10a,1→7 个)与辩论轮数(图 10b,约到 3-4 轮)都单调提升准确率;summarize 其他 agent 回答可在 agent 数较多时进一步提升性能。
- 跨模型辩论:在 20 道 GSM8K 题上,Bard 单独解出 11、chatGPT 解出 14,两者联合辩论解出 17。
- 辩论不只是"放大"已有正确答案——存在所有 agent 初始都答错、但经辩论收敛到正确答案的案例。
- 局限:辩论计算成本更高(多次生成 + 多轮);LLM 不善于表达不确定性,有时会自信地收敛到错误答案。作者提出可将辩论结果蒸馏回基模型形成自我提升循环。

## 在本 wiki 中的位置

本文是 LLM **推理增强**与**测试时计算(test-time scaling)**方向的重要工作,与 [[chain-of-thought]]、[[self-consistency]] 同属"无需训练、靠 prompting/采样提升推理"的家族,并开辟了 [[multi-agent-debate]] 与 [[llm-agents]] 这一交互式协作子方向。可与后续多智能体协作、self-reflection、以及 [[llm-as-judge]] 等概念相互参照。
