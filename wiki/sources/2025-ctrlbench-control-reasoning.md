---
type: source
subtype: paper
tags: [benchmark, foundation-models, control, cyber-physical-systems, reasoning, code-generation, robotics]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2512.13655
raw: raw/2512.13655.pdf
authors: [Anonymous Authors]
year: 2025
---

CtrlBench 是首个面向**控制导向推理(control-oriented reasoning)**的基准,评估 [[foundation-models]] 能否从动力学系统的形式化描述出发,合成出在闭环仿真中稳定、达标的低层控制器。

## 问题

[[foundation-models]] 与 [[large-language-models]] 在自然语言、视觉、代码上表现亮眼,促使人们尝试将其用于网络物理系统(CPS, cyber-physical systems)的控制。但已有面向 [[llm-agents]] 的基准(如 web 导航、具身任务规划)主要考察高层任务分解、[[tool-use]] 和语言/符号推理,把底层连续动力学交给手工设计或学习得到的控制器。因此它们无法回答一个核心问题:FM 自身是否具备**控制导向推理**能力——即把动力学系统($\dot{x}=f(x,u)$)和控制目标翻译为能实现稳定、高性能闭环行为的控制器。这种推理需要对系统动力学、稳定性、反馈的定量理解,传统上属于控制论而非语言推理范畴。

## 方法

CtrlBench 把控制综合(control synthesis)建模为一个推理任务:给定系统动力学、状态/输入空间与约束、精确的控制目标,模型须产出一个控制器(优先用可执行 Python 代码,也可为带具体参数的显式控制律),随后在统一协议下进行**闭环仿真**评估。

- **任务分类(共 37 个问题,难度递增三档)**:
  - 线性系统:double integrator、DC motor、mass-spring-damper、cart-pole(线性化区间),可用 LQR、极点配置求解,作为基本推理的 sanity check。
  - 非线性系统:pendulum swing-up、cart-pole swing-up、quadrotor 稳定与跟踪、车辆(bicycle model)控制,需对非线性、线性化或预测控制推理。
  - 高维机器人平台:legged locomotion(hopper、half-cheetah、ant)与 manipulation,考验对多耦合自由度与接触富集动力学的推理。
- **评估指标**:settling time、steady-state error、overshoot、tracking error、约束违反率、control effort;并定义每任务归一化成功判据(在容差内到达并维持目标一段时间),以 success rate 作为主聚合指标。
- **两种设定**:zero-shot(仅凭规格产出控制器)与 iterative feedback(模型观察闭环仿真结果——轨迹、指标、失败指示——在固定轮数内修正控制器)。
- **被测模型**:涵盖通用 LLM、推理增强模型与代码生成模型,包括 [[gpt-4o]]、GPT-4.1、o1、[[claude-3-5-haiku|Claude 3.5 Sonnet]],以及开源的 [[llama-3]]、[[qwen2-5-instruct|Qwen2.5]] 等,统一 prompt 与协议。

## 结果

- 存在清晰的难度梯度:线性系统上最强模型成功率高,常能正确产出 LQR / 极点配置控制器并合理调参;非线性系统成功率大幅下降,swing-up、quadrotor 任务常无法稳定;高维机器人系统上所有模型成功率都很低,说明当前 FM 无法可靠地为复杂接触富集动力学合成控制器。
- 推理增强模型普遍优于通用模型,说明显式推理有助于定量控制综合;代码生成能力也与成功率正相关(控制器最终须表达为可执行代码)。
- **反馈效应**:迭代反馈在许多任务(尤其线性与弱非线性)上提升性能,模型能用仿真结果重新调参;但在最难的非线性与高维任务上,反馈仅带来边际增益,许多模型多轮后仍无法收敛到稳定控制器。
- **失败模式**:(1) 选对控制器类型但参数误调,导致不稳定;(2) 用线性控制思路处理强非线性系统,补偿不足;(3) 高维系统中难以协调多自由度;(4) 违反约束或产生超出执行器限幅的控制输入。结论是 FM 编码了大量定性控制论知识,但缺乏稳健控制综合所需的精确定量推理与系统级标定。

## 在本 wiki 中的位置

CtrlBench 把 [[benchmark]] 的关注点从 [[llm-agents]] 的高层 [[llm-planning]] / [[tool-use]] 下沉到连续动力学的低层控制综合,与 [[webarena]]、[[alfworld]] 等具身/规划基准互补,也与用 LLM 生成奖励函数或机器人策略代码的工作形成对照。它揭示了 FM 的语言能力与定量 [[reasoning]] 之间的鸿沟,对其在安全关键的 CPS / 机器人场景的部署具有警示意义,是评估 [[foundation-models]] 物理推理与 [[code-generation]] 能力的一个新测试床。
