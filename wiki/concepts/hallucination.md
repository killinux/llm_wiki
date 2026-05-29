---
type: concept
subtype: method
tags: [hallucination, factuality, reliability, self-correction, retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 26
---

# Hallucination

Hallucination 指 LLM 生成看似合理但与事实不符、缺乏依据或无法被来源支撑的内容,是影响模型可靠性与事实性(factuality)的核心问题。

## 在本 wiki 中的出现

- [[2020-rag]]:通过将预训练 seq2seq 生成器与可检索的 Wikipedia 稠密索引结合,RAG 让生成基于外部知识进行接地(grounding),从而在知识密集型 NLP 任务中减少凭空生成、缓解 hallucination。
- [[2023-critic]]:CRITIC 让 LLM 借助搜索引擎、代码解释器、PERSPECTIVE API 等外部工具自我验证并迭代修正输出,利用外部反馈纠正事实错误,是针对 hallucination 的事后检测与修正方法。
- [[2023-multi-agent-debate|2023-multiagent-debate]]:让多个 LLM 实例多轮辩论、互相批评彼此答案,以多智能体交叉检验抑制 hallucination,在事实性任务(MMLU 63.9%→71.1%)上显著提升。
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
- [[2024-aipatient-simulated-patient-llm-agents]]:AIPatient 用六个任务专用 LLM 智能体 + Reasoning RAG + 基于 MIMIC-III 真实病历的知识图谱驱动模拟病人系统,以真实病历约束生成、抑制 hallucination,EHR-QA 准确率达 94.15%、NER 知识库 F1=0.89。
- [[2024-optima-optimizing-llm-multi-agent]]:OPTIMA 通过生成-排序-选择-训练的迭代范式联合优化多智能体系统的通信效率与任务有效性,在重信息交换任务上达成 2.8x 性能提升且 token 用量不到 10%,减少冗余交流带来的错误累积。
- [[2024-llm-powered-user-simulator-for-recommender-system]]:用 LLM 离线蒸馏用户偏好关键词与情感,在线用逻辑+统计集成模型显式推断 like/dislike,构建可解释、低幻觉、低成本的推荐系统用户模拟器。
- [[2025-multi-agent-collaboration-mechanisms-survey]]:系统综述沿 actors、types、structures、strategies、coordination protocols 五个维度刻画 LLM 多 agent 协作机制,并将 hallucination 等列为跨领域应用中的关键挑战。
- [[2025-extended-refusal-defense-against-abliteration]]:通过 extended-refusal 微调把安全信号从单一潜在方向分散到多 token 位置与多维度,使模型在 abliteration 攻击后仍保持 >90% 拒绝率,同时通用性能几乎不变。
- [[2025-emergent-llm-behaviors-data-leakage]]:批判性短文指出 LLM 多智能体模拟中"自发涌现的社会约定"在观测上等价于 data leakage——模型只是复述预训练中已知的协调博弈知识,而非真正自组织。
- [[2025-grasp-world-knowledge-sequential-recommendation]]:GRASP 用"生成增强检索 + Sigmoid 整体注意力增强"把 LLM 世界知识作为辅助输入(而非监督信号)注入序列推荐,抵抗 LLM 幻觉噪声,在 Beauty/Fashion/Industry-100K 上叠加多种 backbone 均达 SOTA,并通过线上 A/B 验证 GMV +1.71%。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent 是一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强,其模拟可信度依赖于抑制 LLM 输出失真。
- [[2026-orchestration-multi-agent-systems]]:Skan AI 提出编排式多 agent 系统统一架构(专门化 agent + 四单元编排层 + MCP/A2A 双通信协议 + 治理与可观测性),作为企业落地工程蓝图,其治理与可观测性层用于约束多智能体协作中的 hallucination 风险。
- [[2026-evaluating-memory-structure-llm-agents]]:提出 StructMemEval 基准,测试 LLM agent 组织(而非仅回忆)长期记忆的能力——纯检索系统在任务规模超出检索窗口后崩溃,memory agents 在被提示如何组织记忆时可靠求解但常不主动识别所需记忆结构,关乎记忆失配导致的失真输出。
- [[2026-policysim-proactive-policy-optimization]]:PolicySim 是基于 LLM 智能体的社会模拟沙盒,用 SFT+DPO 训练用户智能体、用带消息传递的 contextual bandit 自适应优化推荐与曝光控制等平台干预策略,实现部署前的主动评估与优化,其可信度取决于智能体行为模拟不失真。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,以持久记忆接地减少跨会话的事实遗忘与失真。

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
