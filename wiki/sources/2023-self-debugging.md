---
type: source
subtype: paper
tags: [code-generation, self-debugging, prompting, llm-agents, text-to-sql, code-translation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2304.05128
raw: raw/2304.05128.pdf
authors: [Xinyun Chen, Maxwell Lin, Nathanael Schärli, Denny Zhou]
year: 2023
---

提出 SELF-DEBUGGING:通过 few-shot prompting 教会 LLM 像程序员做"小黄鸭调试(rubber duck debugging)"一样,执行自己生成的代码、用自然语言解释代码,从而在无人工反馈的情况下自行发现并修复 bug。

## 问题

LLM 在代码生成上表现出色,但面对复杂编程任务时一次性生成正确代码很困难。先前的两类做法各有局限:

- 一类是从多个采样中重排序选优(reranking),通常需要采样几十个候选,采样成本高。
- 另一类是训练专门的 code repair 模型来修复错误代码,需要额外训练,且依赖人工反馈或显式的错误信息(error message)。

近期工作还表明,在缺乏外部反馈(如单元测试或人工指令)时,LLM 往往无法自行纠正代码。本文要回答的是:能否仅靠 prompting、不做额外训练、不依赖人工反馈,就让 LLM 自我调试代码?

## 方法

SELF-DEBUGGING 使用一个未经微调的预训练 LLM,一轮调试包含 3 个步骤(见论文 Figure 1):

- **Generation(生成)**:给定问题描述,模型生成候选程序。
- **Explanation(解释)**:模型用语义上有用的方式处理预测,例如用自然语言逐行解释代码,或生成执行轨迹(execution trace)。
- **Feedback(反馈)**:生成关于代码正确性的反馈信息;可由模型自身判断,也可由外部单元测试给出。当反馈判定代码正确,或达到最大调试轮数(本文设为 10,但成功的调试多在 3 轮内完成)时终止。

论文研究了几种反馈格式:Simple feedback(仅说"对/错")、Unit test feedback(UT,带失败单元测试的执行结果)、Code Explanation feedback(Expl.,逐行代码解释,即小黄鸭调试的核心)、Execution trace feedback(Trace,逐行模拟执行过程)。其中代码解释与执行轨迹都由模型生成、不需要访问真实的中间执行状态。

应用于三个任务:text-to-SQL 生成([[spider]],无单元测试,靠解释判断正确性)、代码翻译([[transcoder]],C++ 转 Python,利用单元测试反馈)、text-to-Python 生成([[mbpp]],仅给出部分单元测试)。当有多个候选时,先用 execution-based selection(在不报错的候选中取最频繁执行结果)选出初始代码,再做 self-debugging。

## 结果

评估模型包括 [[codex]](code-davinci-002)、[[gpt-3-5-turbo]]、[[gpt-4]] 和 [[starcoder]](15.5B)。

- **Spider(无单元测试)**:Codex baseline 81.3,加代码解释(+Expl.)提升到 84.1,在不同初始采样数下稳定提升 2-3%;在最难(extra hard)的 SQL 问题上准确率提升 9%(63.9 → 72.9)。SELF-DEBUGGING 超过了需要训练的 SOTA(LEVER 81.9、T5-3B+N-best 80.6),也超过纯 prompting 的 Coder-Reviewer(74.5)和 MBR-Exec(75.2)。
- **TransCoder(C++→Python,560 题,每题 10 个单元测试)**:Codex baseline 80.4,UT+Expl. 提升到 92.5,提升达 12%。
- **MBPP(500 题 Python)**:Codex 仅用 n=10 候选即达 72.2,加 UT+Trace 达 75.6,匹配/超过采样 100 个候选的 LEVER(68.9)。GPT-4 上 self-debugging 增益约 8%。
- **样本效率**:在 Spider 上,对 greedy 解码结果做 self-debugging 即可匹配 baseline 用 16 个采样的准确率;从 8 个采样做 self-debugging 超过 baseline 用 32 个采样,能匹配或超过采样 10 倍以上候选的 baseline。
- **消融**:代码执行很关键——去掉单元测试执行后(Table 3),Codex 仍提升最多 5%,且 execution trace 反馈持续优于 simple feedback;但 GPT-3.5/GPT-4 在无执行时容易对自身预测过度自信,提升有限。
- **错误类型**:Spider 上修复的错误多为小错(缺 WHERE 条件 25.7%、缺 DISTINCT 17.1%、JOIN 错 14.3% 等);TransCoder/MBPP 上 60-70% 的成功修复属于"输出不匹配"类错误。

## 在本 wiki 中的位置

SELF-DEBUGGING 是 LLM "自我反思/自我修正"思路在代码领域的代表性工作,与 [[self-refine]]、[[reflexion]] 同属用模型自身反馈迭代改进输出的范式,但强调利用**代码执行**和**自然语言解释**(rubber duck debugging)作为反馈来源。其 prompting 思想与 [[chain-of-thought]] 一脉相承(让模型先产生有用的中间输出)。相关概念见 [[self-debugging]]、[[rubber-duck-debugging]]、[[execution-based-selection]]、[[code-generation]]、[[few-shot-prompting]]。
