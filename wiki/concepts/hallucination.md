---
type: concept
subtype: method
tags: [hallucination, factuality, reliability, self-correction, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 14
---

# Hallucination

Hallucination 指 LLM 生成看似合理但与事实不符、缺乏依据或无法被来源支撑的内容,是影响模型可靠性与事实性(factuality)的核心问题。

## 在本 wiki 中的出现

- [[2020-rag]]:通过将预训练 seq2seq 生成器与可检索的 Wikipedia 稠密索引结合,RAG 让生成基于外部知识进行接地(grounding),从而在知识密集型 NLP 任务中减少凭空生成、缓解 hallucination。
- [[2023-critic]]:CRITIC 让 LLM 借助搜索引擎、代码解释器、PERSPECTIVE API 等外部工具自我验证并迭代修正输出,利用外部反馈纠正事实错误,是针对 hallucination 的事后检测与修正方法。
- [[2023-multiagent-debate]]:让多个 LLM 实例多轮辩论、互相批评彼此答案,以多智能体交叉检验抑制 hallucination,在事实性任务(MMLU 63.9%→71.1%)上显著提升。
- [[2023-metagpt]]:MetaGPT 将人类 SOP 编码进 prompt,以专业化角色与结构化输出约束多智能体协作,论文指出此类结构化约束有助于减少级联式 hallucination,提升多智能体软件开发的可靠性。
- [[2026-generative-social-simulation-validation]]:系统性文献综述(AI Review 2026, 59:15),论证为社会模拟引入 LLM 因黑箱性、文化偏见与随机性而加剧而非缓解了生成式 ABM 长期的"验证"难题,凸显 LLM 输出失真对模拟可信度的威胁。
- [[2023-shepherd-critic-for-lm-generation]]:Meta AI 用约 8K 高质量社区+人工反馈数据微调出 7B 的 LLaMA critic 模型 Shepherd,能精确批判 LLM 输出并给改进建议,以专门 critic 检测包括事实错误在内的缺陷。
- [[2023-recommender-ai-agent-interec]]:InteRecAgent 以 LLM 为大脑、传统推荐模型为工具,通过候选总线记忆、plan-first 执行与 actor-critic 反思约束 LLM,减少推荐对话中的凭空生成。
- [[2023-chain-of-verification]]:Chain-of-Verification (CoVe) 让 LLM 先生成草稿,再独立回答自我规划的验证问题来核查事实,是针对 hallucination 的自我验证式缓解方法。
- [[2024-generative-agents-in-recommendation]]:Agent4Rec 用 1000 个 LLM 驱动的生成式 agent(含 profile/memory/action 模块)构建用户模拟器,探究其能否忠实模拟真实用户行为而非产生失真的模拟。
- [[2023-self-rag]]:Self-RAG 训练单个 LLM 用 reflection token 实现按需检索与自我反思批判,在推理时可控解码以提升事实性与引用准确率,直接缓解 hallucination。
- [[2024-self-reflection-llm-agents]]:在 9 个 LLM、1000 道多选题上对比 8 种自我反思类型,证明所有 self-reflection 都能显著提升 LLM agent 的解题准确率(p<0.001),减少错误输出。
- [[2024-when-can-llms-correct-mistakes]]:批判性综述,论证 LLM 仅凭 prompting 在一般任务上无法可靠自我纠错,瓶颈在于反馈生成,而外部工具/大规模 fine-tuning 可使其奏效,直接关乎 hallucination 的纠正边界。
- [[2024-llm-critics-help-catch-llm-bugs]]:OpenAI 用 RLHF 训练 GPT-4 级别的 critic 模型 CriticGPT,让 LLM 写自然语言批评指出代码 bug,以可扩展监督辅助人类评估模型生成内容的正确性。
- [[2024-megaagent-large-scale-mas-without-sop]]:借鉴操作系统进程/线程模型、无需预定义 SOP、可自动生成数百 agent 并行协作的大规模 LLM 多智能体系统,大规模协作中的输出一致性与可靠性面临 hallucination 挑战。

## 相关

- [[retrieval-augmented-generation]]
- [[self-correction]]
- [[factuality]]
- [[grounding]]
- [[tool-use]]
- [[multi-agent-debate]]
- [[critic-model]]
- [[chain-of-verification]]
- [[self-reflection]]
- [[user-simulation]]
