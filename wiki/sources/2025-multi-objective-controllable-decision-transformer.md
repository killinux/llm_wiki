---
type: source
subtype: paper
tags: [recommender-system, offline-rl, decision-transformer, multi-objective, controllable-recommendation, data-augmentation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2501.07212
raw: raw/2501.07212.pdf
authors: [Chongming Gao, Kexin Huang, Ziang Fei, Jiaju Chen, Jiawei Chen, Jianshan Sun, Shuchang Liu, Qingpeng Cai, Peng Jiang]
year: 2025
---

# Future-Conditioned Recommendations with Multi-Objective Controllable Decision Transformer

提出 MocDT,一种基于 [[decision-transformer]] 的离线 RL 推荐方法,通过把"未来多目标"作为控制信号(类似 prompt),在推理阶段自回归生成对齐指定目标(如累积评分与多样性)的物品序列,无需为目标变化重新训练。

## 问题

[[recommender-systems|recommender-system]] 的终极目标是长期收益,但现有策略面临两大难题:(1) 推荐决策的**未来影响难以观测**,导致只能用即时指标(点击、购买、评分)作代理来优化,难以直接评估长期满意度;(2) 多个目标(如准确性 vs. 多样性)常相互**冲突**,而"训练-评估-重训"循环随目标演化越来越费时费力。过度强化即时表现(反复推荐已偏好物品)会引发用户疲劳,造成参与度下降。现有 [[decision-transformer]] 推荐工作(DT4Rec、CDT4Rec)多面向**单目标**,且只预测"基于交互上下文与指定奖励的下一物品",评估集中于即时指标(NDCG、Recall),忽视规划能力与多样性等长期目标。

## 方法

将多目标交互推荐建模为 [[markov-decision-process]],并提出 **Multi-Objective Controllable Decision Transformer (MocDT)**,核心思想是"面向未来轨迹做条件推荐":

- **Future-conditioned 范式**:借鉴 upside-down RL / [[offline-rl]],模型接收一组优先化的未来目标作为输入(prompt),自回归生成与之对齐的物品序列。用滑动窗口取时刻 t 后的 H 步未来子序列 τ^H,在其上计算多个目标。
- **两个示例目标**:累积评分 O_rate(H 步奖励之和)与多样性 O_div(基于类别 Jaccard 相似度的平均多样性),均归一化到 [0,1]。
- **控制信号 c_t**:由模型 g_φ 从当前状态 s_t 与一组期望未来目标值构造,替代传统 DT 中的 RTG。训练用负对数似然损失 L_MocDT = -E[Σ log π_θ(a_t | τ_{1:t-1}, s_t, c_t)]。论文用 Bayes 法则说明学到的策略相当于按未来条件 c_t 对行为策略重加权。
- **模型架构**:Step Transformer(含 User Encoder / Objective Encoder / History Encoder(GRU))→ Control Signal Encoder(MLP)与 State Initializer → Sequence Transformer(L 层,生成 t..t+H 步)→ Decoder 输出具体物品。
- **三种数据增强**(对应 [[data-sparsity]]):为每个状态从用户已交互物品中构造长度 2H 的合成 to-go 序列。**cumulative rating** 策略每步选未出现过的最高评分物品;**diversity** 策略贪心选与已推荐类别重叠最少的物品;**random** 策略随机选。直接利用已有交互而非额外训练生成模型。

## 结果

在三个公开数据集 [[movielens-1m]](6,040 用户)、[[kuairand-pure]](7,176 用户)、Zhihu-1M(27,285 用户)上评测,生成 H=10 的序列,用 listwise 累积评分(Rating)与多样性(Diversity)两个冲突指标衡量。基线涵盖五类:序列推荐 [[bert4rec]];多任务([[esmm]]、[[mmoe]]、[[ple]]、Shared Bottom、Single Task);多目标 RL(RMTL);可控算法 [[pareto]]-HN(PHN_LS、PHN_EPO);DT 类(DT4Rec、CDT4Rec)。

- **总体表现 (RQ1, Table 2)**:MocDT 在 Diversity 维度三个数据集均排名第 1(MovieLens Diversity 0.87、KuaiRand 0.95、Zhihu 1.00),Rating 维度在 MovieLens、Zhihu 排名第 2(40.57、5.10),KuaiRand 排名第 3(5.42)。优势在于同时具备多目标兼顾与对多目标的**显式控制**能力,而 Bert4Rec/DT4Rec/CDT4Rec 等只优化单目标。
- **可控性 (RQ2, Fig. 3)**:用九个目标点((O_rate, O_div) 组合,如 (1.0,0.0) 表示只重评分不重多样性)测试,MovieLens 上九点形成清晰聚类、相对位置在多个 epoch 间保持稳定,显示可靠的多目标控制;KuaiRand 上观察到 Diversity 与 Rating 的反向关系。
- **数据增强 (RQ3, Fig. 4/5)**:KuaiRand 上增强显著提升性能;MovieLens/Zhihu 因本身已多样,提升有限。增强率提高在 KuaiRand 上稳步提升指标,Zhihu 上反而下降。
- **消融 (RQ4)**:Transformer 层数(Table 3)对 Rating 影响小,但更多层显著提升 Diversity(1→5 层:0.543→0.730);对称配对一层 Step 与一层 Sequence Transformer 效果最佳。未来序列长度 H(Table 4)越小越易预测、单步 Rating/H 越高(H=3 时 4.154,H=15 时 3.736),但太小不实用,实验取 H=10。
- **案例研究 (Table 5)**:对 MovieLens 用户 ID=6040,目标 (1.0,0.0) 生成的 10 部电影累积评分 42.812、Diversity=0(全同类);目标 (0.0,1.0) 生成的列表 Rating 21.607、Diversity 0.902,直观展示推理阶段的目标可控性。

## 在本 wiki 中的位置

本文属于 [[llm-for-recommendation]] / [[rl-based-recsys]] 交叉方向,把 [[decision-transformer]] 从单目标(如 [[user-retention]] 导向的 DT4Rec、捕捉因果的 CDT4Rec)推广到**多目标可控**场景,与 [[long-term-recommendation]]、[[recommendation-diversity]]、[[interactive-recommendation]] 主题直接相关。它体现了 [[offline-rl]] 中 upside-down RL / RTG 条件建模与 [[prompt-engineering]] 思想的结合,可与多目标基线 [[mmoe]]、[[ple]]、[[esmm]]、[[pareto]] 前沿方法对比阅读。作者来自 [[university-of-science-and-technology-of-china]]、[[zhejiang-university]] 与 [[kuaishou]],核心数据集为 [[movielens-1m]] 与 [[kuairand-pure]]。
