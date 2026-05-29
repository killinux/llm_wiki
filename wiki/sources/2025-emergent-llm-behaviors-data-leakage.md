---
type: source
subtype: paper
tags:
  - social-simulation
  - data-contamination
  - agent-based-modeling
  - emergent-behavior
  - llm-agents
  - critique
created: 2026-05-29
updated: 2026-05-29
arxiv: "2505.23796"
raw: raw/2505.23796.pdf
authors:
  - Christopher Barrie
  - Petter Törnberg
year: 2025
---

一篇批判性短文(commentary):作者论证 LLM 多智能体模拟中所谓"自发涌现的社会规范"在观测上等价于 data leakage / 数据污染——模型只是把预训练中已知的协调博弈知识"反射"回研究者,而非真正自组织。

## 问题

Ashery 等人(*Science Advances*, 2025)用 zero-shot LLM 扮演 agent 玩经典的 "naming game"(命名游戏):两个 agent 随机配对,从词表中选词;选同词得 +100 奖励,选不同词得 -50 惩罚。他们声称去中心化的 LLM agent 群体能像人类一样**自发涌现**出共享的语言约定(social convention),无需中央协调。

[[Christopher Barrie]] 与 [[Petter Törnberg]] 指出这一结论存在两个根本问题:

1. **机械人工痕迹(mechanical artifact)**:Ashery 等人模拟代码中的 "inventory pruning rule"(词表裁剪规则)是硬编码的——agent 匹配后会把词表裁到最后匹配的词,这在统计上机械地偏向后续配对继续命中同一约定。"涌现"因此是 trivial 的。
2. **data leakage / contamination**:更深层的问题是,已有科学文献(包括 naming game 本身)很可能已在 LLM 的训练数据中。模型不是给出新发现,而是在 regurgitate(复述)既有研究结论。这对整个 generative ABM([[agent-based-modeling]])文献都是隐患。

## 方法

作者用一个简单而直接的检验:**直接问模型**(we can ask it)。他们复用 Ashery 等人的原始 prompt,但追加 User Prompt 询问:

- 这个设置让你想起社会科学中哪个已有模型或理论?请命名并解释类比;
- 成功(双方选同动作)后的 optimal move 是什么;
- 你认为这个博弈全局上会如何收敛。

被测的 LLM 包括(共约 14 个):llama3.2:3b、llama3:instruct、llama3:70b-instruct、deepseek-r1:8b、mistral:7b、gemma3:4b、claude-3-5-sonnet-20241022、claude-3-5-haiku-20241022、claude-3-haiku-20241022、claude-3-opus-20240229、claude-3-haiku-20240307、[[gpt-4o-mini]]、gpt-4o、gpt-4.1、gpt-3.5-turbo。每个模型查询 10 次。

随后用 gpt-4.1 作为 [[llm-as-judge]] 标注每个回答的三个维度(并附原文摘录佐证),再人工核验:
- **coordination**:是否识别为 coordination game(协调博弈);
- **optimal move**:是否指出成功后最优动作是重复同一动作;
- **convergence**:是否预测会收敛到唯一全局均衡。

## 结果

实验清楚表明模型"知道"这是什么类型的博弈、成功后的最优动作、以及最终收敛形态。以 gpt-4.1 为例,它明确把场景识别为 game theory 中的 Coordination Game / Social Convention Formation,并指出成功后应重复同一动作、全局会 "lock in" 到第一个成功的协调点。

Figure 1(各模型正确识别各维度的 run 占比):

- **coordination 维度**:多数较强模型接近或达到 100%(如 claude-3-5-sonnet、gpt-4o、gpt-4.1、claude-3-5-haiku 均约 100%);llama3:70b-instruct 约 100%。
- **optimal move 维度**:大模型普遍 90–100%;较弱模型偏低(如 gemma3:4b 约 20%、mistral:7b 约 40%)。
- **convergence 维度**:整体最难预测,但许多模型仍能做到(强模型约 90–100%)。
- 最弱的小模型(mistral:7b、gemma3:4b、llama3.2:3b)在三个维度上得分都明显更低。

**核心结论**:Ashery 等人观测到的"涌现社会约定",在观测上等价于一连串 LLM agent 把 payoff 描述映射到其预训练中已有的协调博弈知识。这一隐患波及所有依赖 LLM 复现人类系统"涌现"属性的模拟。作者认为靠 obfuscation(如用 unicode 字符当 token)不足以阻止识别;真正的解法是发明一个 LLM 确定没见过的全新博弈,但这本身就需要一个有研究价值的新人类行为模型。文章还讨论了应对 data contamination 的方向:sparse autoencoder 可解释性探测、基于 prompt 的 next-token perplexity 测量、动态/时间敏感测试构造,但能否迁移到 generative ABM 仍是 open question。

## 在本 wiki 中的位置

本文是对 LLM-based [[social-simulation]] 与 [[agent-based-modeling]] 的方法论批判,与 [[generative-agents]] 路线(用 LLM 充当人类 agent 模拟社会现象)直接相关,可视为对该范式 [[evaluation]] 有效性的警示。它把 [[emergent-abilities]] / 涌现行为重新诠释为 data leakage(数据污染)的观测等价物,与 LLM 的 [[hallucination]]、记忆/复述训练数据等问题同源。提出的可解释性探测方向与 sparse autoencoder、perplexity 检测相关联,被测主体涵盖 [[claude]]、[[gpt-4o-mini]] 等本 wiki 常见模型。
