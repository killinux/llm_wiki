---
type: concept
subtype: method
tags: [alignment, reinforcement-learning, human-feedback, fine-tuning]
created: 2026-05-29
updated: 2026-05-29
sources: 18
---

# RLHF

RLHF(Reinforcement Learning from Human Feedback)是一种用人类偏好信号训练奖励模型、再以强化学习优化语言模型的对齐方法,使模型输出更符合人类期望。

## 在本 wiki 中的出现

- [[2022-instructgpt]]:RLHF 的标志性应用。InstructGPT 采用 SFT → 奖励模型 → PPO 的三阶段流程对齐 GPT-3,使 1.3B 模型在人类偏好评估上胜过 175B 的 GPT-3,且更真实、毒性更低。
- [[2022-constitutional-ai]]:对 RLHF 的扩展。Anthropic 提出 Constitutional AI,用一套人类书写的原则替代人类的有害性标注,通过模型自我批评修改与 AI 反馈(RLAIF),训练既无害又非回避的助手。
- [[2023-lets-verify-step-by-step]]:与 RLHF 中奖励建模相关。OpenAI 比较过程监督(PRM)与结果监督(ORM),证明过程监督在 MATH 多步数学推理上显著更优(best-of-N 达 78.2%),并开源步骤级标注数据集 PRM800K。
- [[2023-self-refine]]:无需训练的反馈替代方案。用同一个 LLM 在测试时迭代"自我反馈 → 自我修正",不依赖 RLHF 式的训练流程,即在 7 个任务上平均提升约 20%。
- [[2023-dorl-matthew-effect-offline-rl-recommendation]]:RL 优化在推荐场景的应用。提出 DORL,在 model-based offline RL 的悲观惩罚上加入熵惩罚,以缓解推荐中的马太效应,提升交互式推荐的用户长期满意度。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM 用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升生成质量、事实性与引用准确率。
- [[2024-eureka-reward-design-via-coding-llms]]:Eureka 用编码 LLM(GPT-4)零样本生成可执行奖励函数代码,结合进化搜索与奖励反思迭代改进,在 29 个 RL 环境上达到人类专家级奖励设计并首次让模拟 Shadow Hand 学会转笔。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-sotopia-pi-social-agents]]:通过 behavior cloning 与 self-reinforcement 在 GPT-4 评分过滤的社交对话数据上训练,使 7B LLM 的社交目标完成能力逼近 GPT-4,同时提升安全并保持 MMLU。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述,细分自我纠错的三类研究问题并提出实验检查清单,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督方式帮助人类更准确评估模型生成的代码。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。
- [[2024-mitigating-false-refusal-single-vector-ablation]]:提出 training-free、零推理开销的方法,通过正交化并消融单个 false refusal vector 来缓解 LLM 的过度拒绝,同时保持安全性与通用能力。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。
- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。
- [[2025-llm-collaboration-marl-magrpo]]:把多 LLM 协作建模为合作式 MARL(Dec-POMDP)并提出 Multi-Agent GRPO(MAGRPO),在写作与编码协作上微调多个 LLM;TLDR/arXiv return 达 94.5%/93.1%,HumanEval/CoopHumanEval return 达 86.7%/88.5%。

## 相关

- [[ppo]]
- [[reward-model]]
- [[supervised-fine-tuning|sft]]
- [[rlaif]]
- [[constitutional-ai]]
- [[process-supervision]]
- [[alignment]]
- [[human-preference]]
- [[grpo]]
- [[refusal-vector]]
- [[abliteration]]
- [[multi-agent-reinforcement-learning]]
