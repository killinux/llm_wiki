---
type: source
subtype: paper
tags: [llm-agent, ai-safety, reinforcement-learning, tool-use, alignment, prompt-injection]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2507.08270
raw: raw/2507.08270.pdf
authors: [Zeyang Sha, Hanling Tian, Zhuoer Xu, Shiwen Cui, Changhua Meng, Weiqiang Wang]
year: 2025
---

本文提出首个面向 tool-using agent 的统一**安全对齐**框架,通过 structured reasoning + sandbox [[reinforcement-learning]] 让 [[llm-agent]] 同时抵御 user-initiated 与 tool-initiated 两类威胁。

## 问题

随着 [[large-language-models]] 从被动对话接口演化为能调用外部工具、自主执行多步任务的 [[autonomous-agents]](如 [[autogpt]]、BabyAGI、[[gpt-engineer]] 等),出现了超越传统对话误用的新型安全风险。作者将威胁分为两类:

- **User-Initiated Threats(用户侧)**:对手精心构造输入(prompt injection、对抗指令、社会工程),诱导 agent 调用 sensitive 工具造成伤害。
- **Tool-Initiated Threats(工具侧)**:即使用户意图完全善意,被攻陷的工具返回的输出中可能嵌入隐藏指令、poisoned data,操纵 agent 发起有害调用。文中以 2025 年 5 月披露的 CVE-2025-31491(AutoGPT 的 GitHub OAuth token 泄露漏洞)为真实案例。

已有 agent 安全研究多停留在**度量与分类**风险(如 [[agentbench]] 类 benchmark),少数主动防御工作要么不能让 agent 本身变安全、引入额外推理开销,要么只是把传统 LLM 的安全对齐直接迁移到 agent 域。

## 方法

核心是一个统一的「execute-refuse-verify」策略,贯穿 ingress(user prompt)与 egress(tool response)两个通道。

- **三模态分类(tri-modal taxonomy)**:对 user prompt 与 tool output 都分为 benign / malicious / sensitive 三类。
  - Benign:直接执行。
  - Malicious:类别化拒绝(refuse),不调用任何工具。
  - Sensitive:本身无害但有风险,必须触发 `<tool_check>` 与用户进行 "double-check" 确认对话,获得授权后才执行。
- **多模态数据构造**:用 [[deepseek-r1]](DeepSeek-671B)在 few-shot 模式下生成 N_U = 20000 条 user prompt 和 N_T = 5000 条 tool utterance,经静态过滤(去除已知 prompt-injection 模式、policy-violating 关键词、低多样性重复)+ 人工抽检 + 类别平衡。
- **训练环境**:基于 [[react-reasoning-and-acting]] 思路的 ReCall framework 构建 sandbox,把环境规范解析成可调用函数嵌入 system prompt;agent 调用工具时生成暂停,sandbox 模拟执行并返回结果;需确认时 sandbox 随机回 "yes"/"no" 模拟用户回复。
- **奖励函数(reward function)**:R = R_gen × R_ℓ,结构检查不通过则归零。
  - 通用奖励:EOS Compliance(以 EOS token 结尾)与 `<think>` Integrity(think 标签正确配对)。
  - 场景奖励按 threat label 设计:benign 要求 Tool-Invocation Soundness(合法 JSON 含 name/arguments)且无 double-check;malicious 要求 No Tool-Invocation + 明确拒绝,并额外训练一个 **rejection classifier** REF(a_t) 判断文本是否表示拒绝;sensitive 要求先发 `<tool_check>` 请求确认,再依 `<tool_check_result>` 的 0/1 决定是否调用。
- **优化策略**:on-policy 循环——Rollout、Reward Assignment、Policy/Value Update(clipped policy-gradient + batch-normalized returns)。

实验在 Qwen-2.5-7B-Instruct 与 Qwen-2.5-14B-Instruct 上进行,对比四种设置:No Defense、Prompt Guarded、User Aligned、User-Tool Aligned。

## 结果

在公开与自建 benchmark 上评估:用户侧用 [[agentbench]] 风格的 Agent SafetyBench (ASB)、自建 Malicious/Sensitive Test;工具侧用 InjecAgent;通用能力用 Berkeley Function-Calling Leaderboard (BFCL)。

- **用户侧威胁(Table 1)**:7B No Defense 仅 ASB 15.3 / Malicious 0.9 / Sensitive 0;User Aligned 7B 提升到 ASB 69.9 / Malicious 99.2 / Sensitive 98.9。14B User Aligned 达 ASB 88.8 / Malicious 97.3 / Sensitive 99.7,匹配或超过 Prompt Guarded 的安全性而不牺牲 utility。
- **工具侧威胁(Table 3,越低越安全)**:7B No Defense 的 InjecAgent 36.8、自建 Malicious Test 0.0;User-Tool Aligned 7B 把自建 Malicious Test 提升到 92.5、14B 提升到 94.6,显著优于只做 user alignment 的版本——说明须**联合对齐**两侧。
- **Utility(Table 4)**:aligned 模型在 BFCL/BFCL-Live 上几乎不掉分(User-Tool Aligned 7B 在 BFCL 91.3,对比 No Defense 95.3),在自建 utility test 上反而更高(User-Tool Aligned 14B 达 94.6,远高于原 14B 的 75 和 Prompt Guarded 的 4.3)。值得注意的是 Prompt Guarded 虽能防御恶意工具,但 utility 大幅下降。

结论:safety 与 effectiveness 可联合优化,为可信部署 autonomous LLM agent 奠定基础;未来工作指向 multi-agent 环境、动态工具注册与 long-horizon planning。

## 在本 wiki 中的位置

本文属于 [[llm-agent]] 安全方向,把 [[ai-safety]] / [[alignment]] 从传统对话 LLM 扩展到 tool-using agent 场景。与本 wiki 中以能力评测为主的 [[agentbench]] 等 benchmark 工作不同,它是首个从安全视角提出 agent **训练**框架的工作,通过 [[reinforcement-learning]](RLHF 风格的 on-policy 优化)而非纯 prompt 防护来内化安全行为。其 sandbox + reward shaping 思路与 [[react-reasoning-and-acting]]、tool-use 训练范式相关;统一处理 user-side 与 tool-side(prompt injection)威胁的设计补充了 [[hallucination]]、prompt injection 等已有安全议题。作者来自 [[ant-group]]。
