---
type: concept
subtype: method
tags: [llm-agent, agent, memory, multi-agent, tool-use, recommendation, planning]
created: 2026-05-29
updated: 2026-05-29
sources: 9
---

# LLM Agent

LLM Agent 指以大语言模型为核心决策器、能够通过记忆、工具调用、规划与多智能体协作等机制自主感知环境并采取行动以完成目标的系统。

## 在本 wiki 中的出现

- [[2026-memory-in-the-age-of-ai-agents-survey]]:一篇关于智能体记忆的综述,提出 forms-functions-dynamics 三维统一分类法,整合碎片化的 agent memory 研究并汇总相关 benchmark 与开源框架。
- [[2025-multi-agent-reflexion-mar]]:把 Reflexion 的单 Agent 自我批评换成多 persona 辩论加 judge 合成反思,在 HotPotQA(EM 44→47)与 HumanEval(pass@1 76.4→82.6)上超过单 Agent Reflexion。
- [[2026-ab-agent-recsys-evaluation]]:A/B Agent:一个多模态 LLM 用户智能体,在带海报的推荐沙盒 UI 中模拟用户多模态感知、多页交互与疲劳退出,用以替代昂贵的在线 A/B testing 评估推荐模型并做数据增强。
- [[2026-trirec-tri-party-agent-recommendation]]:TriRec 是首个用户—物品—平台 tri-party LLM-agent 推荐框架,让物品 agent 主动个性化自我推销,再由平台做曝光感知的多目标重排,在精度、公平与物品效用上同时提升。
- [[2026-entropy-guided-agentic-recommendation]]:提出 IDSS,用 Shannon 熵作为统一信号贯穿对话式推荐的偏好询问、排序与多样化呈现三阶段,在用户意图模糊时兼顾追问效率与残余不确定性驱动的多样化推荐。
- [[2026-tooltree-tool-planning]]:免训练的 MCTS 工具规划框架,用执行前/执行后双反馈引导搜索并双向剪枝,在固定预算下提升 LLM 智能体多工具规划的准确率与效率(GTA 66.95 AVG,ToolBench 69.04 AVG)。
- [[2026-memori-persistent-memory-layer-llm-agents]]:Memori 是 LLM-agnostic 的持久化记忆层,用 Advanced Augmentation 把对话压缩成语义三元组+摘要,在 LoCoMo 上仅用约 5% 上下文 token(1,294/query)达到 81.95% 准确率,优于 Zep/LangMem/Mem0 且成本远低于 full-context。
- [[2026-self-evolving-multi-agent-rts]]:SEMA 用结构熵驱动观测剪枝 + 闭环自演化的 LLM 多智能体框架,在 StarCraft II 上实现高胜率与低延迟的实时策略决策。
- [[2026-llm-agents-competition-cooperation-games]]:研究 LLM agent 在资源分配博弈与 Cournot 竞争中的策略行为:多轮非零和提示下 agent 倾向合作而非收敛到 Nash 均衡,fairness 推理是核心驱动,并提出 θ/γ 合成收益函数框架刻画其信任建立、报复与 endgame 衰减动态。

## 相关

- [[agent-memory]]
- [[multi-agent-system]]
- [[tool-use]]
- [[planning]]
- [[reflexion]]
- [[agentic-recommendation]]
- [[reinforcement-learning]]
- [[game-theory]]
