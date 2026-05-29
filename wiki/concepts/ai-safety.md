---
type: concept
subtype: method
tags: [AI safety, alignment, harmlessness, RLHF, RLAIF]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# AI safety

AI safety 是指通过技术与方法手段,让 AI 系统的行为保持无害(harmless)、诚实且与人类意图对齐(aligned),从而降低其造成伤害或被滥用风险的研究领域。

## 在本 wiki 中的出现

- [[2022-constitutional-ai]]:在 Constitutional AI 中,AI safety 是核心目标。Anthropic 用一套人类书写的原则(constitution)替代逐条的人类有害性标注,先通过模型对自身回答的自我批评与修改(self-critique & revision)生成更无害的样本,再以 AI 反馈(RLAIF)进行强化学习训练。其目标是得到一个既无害又非回避(non-evasive)的助手,即在拒绝有害请求的同时仍能解释拒绝理由、保持有用性。
- [[2023-concordia-generative-agent-based-modeling]]:Google DeepMind 提出的库 Concordia,用 LLM 驱动的生成式 agent 在物理/社会/数字空间中扎根交互,通过 Game Master 控制环境,支持 Generative Agent-Based Modeling 的社会仿真与数字服务评估,可用于在受控环境中研究 agent 行为与社会影响。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督(scalable oversight)方式帮助人类更准确评估模型生成的代码。
- [[2024-mitigating-false-refusal-single-vector-ablation]]:提出 training-free、零推理开销的方法,通过正交化并消融单个 false refusal vector 来缓解 LLM 的过度拒绝,同时保持安全性与通用能力。
- [[2025-llm-agents-cooperate-social-dilemma]]:让 ChatGPT-4o 与 Claude 3.5 Sonnet 为 iterated Prisoner's Dilemma 写出完整策略(而非逐步出招),用 evolutionary game theory / Moran process 模拟 LLM agent 群体演化,发现多数场景下侵略策略劣势、系统倾向合作,但博弈论 prompt 与 self-refine 会增强侵略策略并提高收敛到侵略均衡的风险。
- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。
- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]]:一个 post-hoc、模型无关、distribution-free 的方法,用 conformal risk control 给推荐中"不想要内容"的比例提供可证明上界,并以用户曾看过的安全重复内容替换有害项以保住推荐质量。
- [[2025-llm-agent-evaluation-survey]]:SAP Labs 的 LLM agent 评测综述,提出"评测目标 × 评测过程"二维分类法,并强调企业落地中的可靠性、合规与 RBAC 等挑战。
- [[2026-collective-manipulation-risk-controlling-recsys]]:审计基于 conformal risk control 与二元 Not Interested 负反馈的推荐系统,证明仅 1% 协同对抗用户即可让非对抗用户 nDCG 最多降 20%,并提出个体级阈值校准作为缓解。

## 相关

- [[constitutional-ai]]
- [[rlaif]]
- [[rlhf]]
- [[alignment]]
- [[harmlessness]]
- [[self-critique]]
- [[scalable-oversight]]
- [[generative-agent-based-modeling]]
- [[2022-constitutional-ai]]
- [[refusal]]
- [[abliteration]]
- [[conformal-risk-control]]
- [[llm-agents]]
- [[evaluation]]
