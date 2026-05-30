---
type: topic
tags: [llm-agents, self-correction, self-improvement, reflection, tool-feedback, debate, reasoning]
created: 2026-05-30
updated: 2026-05-30
sources: 20
---

# LLM 自我改进与自我纠错 (Self-Improvement & Self-Correction)

> 一句话:让 LLM 在**推理时**(无权重更新)或**训练时**用自身/外部产生的反馈迭代改进输出。
> 核心张力——一批工作声称"自我反思→自我修正"能大幅提升;随后一批批判性工作证明:**没有外部反馈的"内在自我纠错"
> 其实无效甚至变差**,先前的"提升"多源于 oracle 标签泄露。瓶颈不在"改",而在"**能否可靠地生成反馈/发现错误**"。

这是 [[llm-agents|LLM 智能体]] "任务求解"分支的方法核心,与 [[generative-social-simulation]] 的"可信度验证"争议同构:
**都经历了"热捧→证伪→厘清边界条件"的演化**。

---

## 一、按反馈来源的分类(关键变量就是"反馈从哪来")

### 1) 内在自反馈(intrinsic):同一模型自评自改
- [[2023-self-refine]] —— 同一 LLM 充当 生成器 / 反馈器 / 修正器,要求反馈 *actionable + specific*,≤4 轮迭代;在 7 个任务上**平均 ~20% 绝对提升**(无需训练)。
- [[2024-recursive-introspection-rise]]、[[2024-self-reflection-llm-agents]]、[[2024-positive-experience-reflection]](不仅从失败、也从**成功经验**反思)。

### 2) 外部反馈(extrinsic):工具 / 环境 / 单元测试
公认更可靠——把"发现错误"外包给可验证信号。
- [[2023-critic]] —— 与搜索引擎、代码解释器、[[perspective-api]] 交互做 verify-then-correct;明确指出**纯自我修正收益有限、需外部反馈**。
- [[2023-self-debugging]] —— "小黄鸭调试":让模型解释/执行自己的代码,用单元测试反馈,≤10 轮(多在 3 轮内成功)。
- [[2023-reflexion]] —— **verbal RL**:把环境的成功/失败反馈转成反思文字存入 [[memory-stream|记忆]],下次试验作上下文,无梯度更新(Actor/Evaluator/Self-Reflection 三件套)。
- [[2023-self-rag]]、[[2023-chain-of-verification]] —— 用检索 / 自生成核查问题降低幻觉。

### 3) 多智能体辩论(debate):用"分歧"打破思维定势
- [[2023-multi-agent-debate]] —— 多个 debater 针锋相对 + judge 裁决,针对单 agent 反思的 **Degeneration-of-Thought (DoT)**(对错误答案过度自信、无法产生新想法);跨模型 judge 更优。
- 相关:[[2023-camel-communicative-agents]]、[[2025-multi-agent-reflexion-mar]]。

### 4) 训练时自我改进:把推理时收益蒸馏进权重
- [[2022-star-self-taught-reasoner]](STaR)—— 用自洽/正确的推理轨迹做拒绝采样微调,自举推理能力;[[2024-v-star-verifiers-for-self-taught-reasoners]] 加验证器。
- [[2024-quiet-star]](为每个 token 生成内部 rationale)、[[2024-score-self-correct-via-rl]](用 RL 训练自我纠错)、[[2024-recursive-introspection-rise]]。
- **批评者模型**:[[criticgpt]]、[[2024-llm-critics-help-catch-llm-bugs]]、[[2023-shepherd-critic-for-lm-generation]] 训练专门的批评/奖励模型给反馈。

---

## 二、核心争议:内在自我纠错"其实不行"
这是本线最重要的厘清,直接对前述 ① 类工作"祛魅":
- [[2023-llms-cannot-self-correct-reasoning-yet]](Huang et al.)—— 定义 **intrinsic self-correction**(无外部反馈/标签/工具)。实验显示在推理任务上 LLM 内在纠错后
  **性能反而下降**;先前正面结果多依赖 **oracle 标签**(用真值决定何时停/是否改)。并论证 [[2023-multi-agent-debate|多智能体辩论]]的增益**本质更接近 [[self-consistency]] 自洽投票**,而非真正"自我纠错"。
- [[2024-when-can-llms-correct-mistakes]](批判性综述)—— 把框架拆成 初始响应 / **反馈生成** / refinement 三阶段,提出 RQ1/2/3 与实验检查清单;结论:
  **瓶颈在反馈生成**——仅凭自身能力在一般任务上无法可靠纠错,但**有外部信息时可以**。
- [[2025-mirror-loop-recursive-non-reasoning]] 等延续"递归自指未必带来真推理"的反思。

## 三、边界条件:什么时候自我改进"真有效"
综合正反两方,共识正收敛为——自我改进有效当且仅当存在**可靠的误差信号**:
1. **可验证任务**:代码(单元测试)、数学(可执行/可检验)、事实(检索核查)——外部反馈把"发现错误"变得可靠。
2. **外部工具/环境**:CRITIC、Reflexion 式的环境反馈;[[2024-autoguide-context-aware-guidelines]]、[[expel]] 从经验抽取指导。
3. **训练时蒸馏**:STaR 家族把"采样-筛选-微调"循环固化进权重,绕开"推理时能否自评"的难题。
4. **多样性来源**:辩论/多采样的增益更多来自**集成/投票多样性**,而非单体反思——用对了仍有效,但要正确归因。

## 四、开放问题
- **反馈生成的可靠性**:如何让模型在**无 oracle** 时可靠判断自己错没错(这是整条线的真正瓶颈)。
- **正确归因**:区分"真自我纠错" vs "自洽投票 / 集成"带来的提升,避免高估。
- **训练时 vs 推理时**:STaR 式自举与推理时 refine 的最优配比;与 [[test-time-scaling|推理时扩展]]、[[best-of-n]] 的关系。
- **过度优化**:用自生成反馈/奖励训练易 reward hacking([[2024-v-star-verifiers-for-self-taught-reasoners]] 式验证器缓解)。

## 相关概念页
[[self-correction]]、[[self-reflection]]、[[reflexion]]、[[self-refine]]、[[chain-of-thought]]、[[self-consistency]]、
[[test-time-scaling]]、[[best-of-n]]、[[reward-model]]、[[tool-use]]
