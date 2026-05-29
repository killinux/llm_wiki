---
type: source
subtype: paper
tags: [llm-agent, user-simulation, human-behavior-simulation, benchmark, fine-tuning, reasoning, online-shopping, web-agent]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2503.20749
raw: raw/2503.20749.pdf
authors: [Yuxuan Lu, Jing Huang, Yan Han, Bingsheng Yao, Sisong Bei, Jiri Gesi, Yaochen Xie, Yisi Sang, Zheshen Wang, Qi He, Dakuo Wang]
year: 2025
---

# Can LLM Agents Simulate Multi-Turn Human Behavior?

第一项大规模、过程级(process-centric)定量评测,用真实在线购物数据检验 LLM Agent 能否逐步精确模拟人类行为,结论是 prompt-only LLM 行为准确率仅约 11.86%,而在真人点击数据 + 合成 reasoning trace 上微调可显著提升。

## 问题

近年 [[generative-agents]] 等工作表明 [[llm-agents|llm-agent]] 能生成"可信(believable)"的人类行为,并被广泛用作虚拟用户做网站功能测试、自动 A/B 测试、评测 agentic AI 系统等下游应用。但现有评测只关注**主观可信度**(人类评审觉得像不像),或只看任务**最终结果**(是否购买、是否信任),从未在**过程级、动作级**上客观检验:模型逐步生成的动作序列是否真的与某个真实用户在多轮交互中的逐步行为对齐。因此领域缺乏一个回答"LLM 到底能多准地复刻人类行为"的定量基准。

## 方法

以在线购物为案例:一个 session 表示为用户动作序列,以 search 开始,以 purchase 或 terminate(关闭浏览器)结束。任务定义为在第 t 步给定当前 context、历史 context、历史 action 与历史 reasoning,生成下一步的 reasoning 与 action,即 f(c_{1..t}, a_{1..t-1}, r_{1..t-1}) = r_t, a_t。

- **观察空间(context)**:用简化版 HTML 表示网页(去掉 script/CSS/纯视觉元素,保留列表、表格等结构),每个可交互元素赋予自然语言层级名(如 `columbia_shirt.view_product`),既适配未见过的网站,又复用 LLM 对 HTML 的熟悉度。
- **动作空间**:抽象为三种原始浏览器操作 click、type_and_submit、terminate,不绑定任务语义,便于跨环境泛化。
- **合成 reasoning trace**:真实数据没有 groundtruth reasoning,故用 [[claude]] 3.5 Sonnet,结合真人 think-aloud session 作为 [[in-context-learning]] 示例,为每个 ⟨context, action⟩ 合成自由文本 reasoning;借鉴 [[deepseek-r1]] 解决 RL 冷启动的思路。该 reasoning 不追求复刻真实思维,而是提供结构化中间表示以提升预测准确率。
- **数据集 ShopCART**:基于 Amazon.com,31,865 个 session、3,526 个用户、230,965 个动作,最终结果含 4,432 个 purchase、27,433 个 terminate;数据来自显式 opt-in beta 用户,并用 LLM 去除 PII。另在 OPeRA 数据集(51 用户、692 session、28,904 个对齐 pair、604 人工标注 rationale)上复现结论。
- **模型与训练**:在 [[llama]] 3.2、[[qwen]] 2.5、[[mistral-7b]] 等基座上做 [[fine-tuning]],训练时整段 session 拼接为单一输入,仅对 reasoning/action token 算 next-token loss、mask 掉 context token。评测时模型先生成 reasoning 再据此生成 action(两轮对话格式)。训练用 64 张 NVIDIA H200(8 节点×8 卡),约 3700 H200 GPU 小时,40k token 上下文。
- **指标**:Next Action Generation 用 exact-match accuracy(动作类型、目标、属性全对才算对,按 session 先算再平均);Session Outcome 用 buy/terminate 二分类的 F1。Prompt-only baseline 在 ICL 设定下评测 [[claude]]、[[llama]]、[[mistral-7b]] 多个变体及 [[deepseek-r1]]。

## 结果

- **Prompt-only LLM 普遍很弱**:动作生成准确率最高的 [[deepseek-r1]] 仅 **11.86%**,Claude 3.5 Sonnet v2 为 11.69%;Session F1 上 DeepSeek-R1 为 20.01%。reasoning-focused 模型略优于通用 instruction-tuned 模型,大模型一般优于同系小模型。
- **微调显著提升**:微调后的 [[qwen]]2.5-7B 达到 **17.26%** 动作准确率(较 DeepSeek-R1 提升 5.4%,p<10⁻¹⁰,McNemar 检验)、33.86% Session F1(较 baseline 提升 13.85%);Llama-3.2-3B 微调后 Session F1 达 33.99%。所有微调模型都显著超过其自身 ICL 版本(p<10⁻⁵)。
- **合成 reasoning 进一步加分**:加入 reasoning trace 后,动作准确率相对增益 3.54%~69.39%,F1 增益 25.78% 至 600% 以上;如 Qwen2.5-7B 有 reasoning 时 F1 为 33.86%,去掉降到 26.92%。
- **OPeRA 数据集**:pretrained 中 [[gpt-4]].1 最强(21.28% 动作准确率 / 51.17% F1),其次 DeepSeek-R1、Claude-3.7;微调 Qwen2.5-7B + reasoning 达 35.14% / 75.85%,远超所有 pretrained baseline。
- **行为分布与误差**:真人平均每 session 2.82 次 search、极少用 filter;而 prompt-only LLM(Claude、DeepSeek-R1)倾向不改关键词、过度使用 filter、且 purchase 率异常偏高。作者推测这是因为 [[webshop]]、[[webarena]] 等基准以任务完成(购买)为评测目标,诱导模型走"购买导向"轨迹。微调模型的动作分布更贴近真人,且更会改写/纠错 search、更准确地判断何时 terminate。
- **讨论要点**:exact-match 是严格指标;simplified HTML 缺少真人能看到的图片/视觉布局,存在 modality gap;作者建议未来用 partial-match、动作类型加权、分布级指标等更能反映人类"非理性"行为的评测方式。

## 在本 wiki 中的位置

本文属于 [[llm-agents|llm-agent]] / [[user-simulation]] 方向,与 [[generative-agents]]、[[webshop]]、[[webarena]]、[[react]] 等"可信行为 / 任务完成"范式形成对照:它把评测重心从主观 believability 与最终结果转向**过程级动作精确度**,提出 ShopCART [[benchmark]],并用 [[fine-tuning]] + 合成 [[chain-of-thought]] 式 reasoning 给出改进路径。对 [[recommender-systems|recommender-system]]、[[user-retention]] 等领域里用 LLM 做用户/customer 模拟的工作(如 [[recagent]]、[[agentcf]]、[[lusifer]])提供了"是否真实对齐人类逐步行为"的批判性证据与可复用数据集。
