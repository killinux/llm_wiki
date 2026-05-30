---
type: concept
subtype: method
tags: [recommender-system, ranking, reranking, multi-objective]
created: 2026-05-30
updated: 2026-05-30
sources: 7
---

# 重排 (Re-ranking)

重排是推荐 / 信息检索流水线的**最后一个阶段**:在召回(retrieval)与精排(ranking)给出候选及其单点分数之后,
重排考虑**整个列表的上下文**(item 间的相互影响、多样性、多目标权衡、公平性、业务约束)对最终展示顺序做调整。

## 为什么需要单独一阶段
精排通常**逐 item 独立打分**(point-wise),忽略了:
- **列表内互影响**:相邻 item 的互补 / 竞争(list-wise context),用户对整页的感知不是单点分之和;
- **多目标权衡**:点击、时长、转化、留存等目标常冲突,需在列表层面平衡([[multi-objective-optimization]]);
- **多样性与去冗余**:避免同质化(如 MMR、DPP);
- **多边公平**:用户 / 创作者 / 提供方利益,见 [[2024-bankfair-fluctuating-traffic-reranking]]、[[2025-lhrl-lifecycle-fairness-recommendation]];
- **业务/平台约束**:广告插入、品类配额、流量调控。

## 方法谱系
- **启发式**:MMR(最大边际相关)、DPP(行列式点过程)做多样性。
- **学习式列表重排**:把列表生成建模为序列决策——[[2024-llm4rerank-auto-reranking-recommendation]] 用 LLM 自动重排;
  生成式列表推荐如 [[2023-gflownet-listwise-recommendation]](GFlowNet)、[[gfn4rec]] 兼顾质量与多样性。
- **RL 重排**:把重排看作 MDP,用强化学习优化长期 / 列表级收益。

## 相关页
[[recommender-systems]]、[[ranking]]、[[multi-objective-optimization]]、[[item-side-fairness]]、[[reinforcement-learning-for-recommendation]]
