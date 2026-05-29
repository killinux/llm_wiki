---
type: source
subtype: paper
tags: [geometric-programming, uncertainty-theory, stochastic-programming, optimization, operations-research]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2310.01848
raw: raw/2310.01848.pdf
authors: [Tapas Mondal, Akshay Kumar Ojha, Sabyasachi Pani]
year: 2023
---

# Uncertain random geometric programming problems

本文为系数同时含有不确定性(uncertainty)与随机性(randomness)的几何规划(Geometric Programming, GP)问题提出了一个确定性建模框架,引入 linear-normal uncertain random variable 概念,并通过三种 critical value 准则将其转化为可解的随机 GP 问题。

> 注:本文属运筹学/优化理论范畴(arXiv math.OC),与本 wiki 的 LLM/AI 主题关联较弱;此处按实际内容如实记录。

## 问题

经典几何规划(GP)假设目标函数与约束的系数是确定、精确已知的常数。但现实中 GP 参数往往既不确定又随机。已有研究分别处理过:随机系数的 stochastic GP、区间/模糊系数的 fuzzy GP、以及基于 uncertainty theory(Liu 提出的不确定性理论)的 uncertain GP。然而当不确定分布的参数本身又是随机变量时(即所谓 uncertain random variable,不确定性与随机性的混合),GP 问题尚无人研究。本文要解决的是:当 GP 系数为相互独立的 linear-normal uncertain random variable 时,如何建立等价的确定性表述并求解。

## 方法

核心贡献与流程:

- **新概念:linear-normal uncertain random variable**。在 linear uncertain variable ξ ∼ L(a, b) 中,把参数 a、b 取为相互独立的正态随机变量 A ∼ N(μ_A, σ_A)、B ∼ N(μ_B, σ_B),记作 ξ̄ ∼ LN(A, B)。
- **三种转化准则**:用 critical value(临界值)将 uncertain random variable 转化为普通随机变量:
  - optimistic value criteria(乐观值)ξ̄_sup(α) = αA + (1−α)B;
  - pessimistic value criteria(悲观值)ξ̄_inf(α) = (1−α)A + αB;
  - expected value criteria(期望值)ξ̄_exp = (A+B)/2。
  - 通过特征函数(characteristic function)证明三者均服从正态分布(Theorem 5),并给出对应的概率分布函数。
- **GP 问题转化**:将系数为 LN(A,B) 的 posynomial GP 问题(Problem 4)按三种准则转为随机 GP 问题(Problem 5/6/7);再用容差水平 ε ∈ (0, 0.5] 的概率约束(chance constraint)处理;最后用 Theorem 6 把概率约束化为含 Φ⁻¹(1−ε) 的确定性约束,得到等价确定性 GP(Problem 11/12/13)。
- **求解**:利用 GP 原问题-对偶问题(primal-dual)关系与强对偶定理求解。引入辅助变量降阶,构造对偶问题,按 degree of difficulty D = N − n − 1 判断可解性。

## 结果

通过一个数值算例验证(Problem 14):2 个决策变量项的目标 + 1 个约束,系数为 4 个独立 linear-normal uncertain random variable(如 A₁₀ ∼ N(50,3)、B₁₀ ∼ N(40,2) 等)。

- 取乐观值准则、ε = 0.05,转化后的确定性问题(Problem 16)共 10 项、5 个变量,degree of difficulty D = 10 − 5 − 1 = 4。
- 对 α 从 0.1 到 0.9(步长 0.1)求解,得最优解表(Table 1):目标值从 α=0.1 的 **219.893** 单调下降到 α=0.9 的 **175.417**;相应 x₁* 从 1.454 降到 1.033。
- 乐观值视角下目标值随 α 增大而下降,悲观值视角下随 α 增大而上升,二者在 **α = 0.5 处相交**,该交点恰为期望值准则下的最优目标值(约 193,见 Figure 6)。这与 Remark 5 一致:α=0.5 时乐观、悲观准则均退化为期望值准则。

## 在本 wiki 中的位置

本文属于运筹学中的几何规划与不确定性建模,与本 wiki 主要关注的 LLM/AI 研究主题关联很弱,作为 raw 库中的异类来源如实归档。其方法学(用 [[reinforcement-learning]] 之外的随机/不确定优化处理含噪参数)与 AI 中处理不确定性的思路在概念上有遥远呼应,但无直接技术联系。该来源不应作为 wiki 中 LLM/agent 相关条目的支撑引用。
