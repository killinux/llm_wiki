---
type: concept
subtype: method
tags: [distribution-shift, robustness, debiasing, offline-rl, generalization, recommender-systems]
created: 2026-05-29
updated: 2026-05-29
sources: 4
---

# 分布偏移 (distribution shift)

分布偏移(distribution shift)指模型训练时所依据的数据分布与其部署/服务/测试时实际面对的数据分布不一致的现象,这种不一致会破坏经验风险最小化的前提,导致模型在真实环境下表现退化。

## 概述

分布偏移是机器学习鲁棒性与泛化的核心难题:当 train 分布 ≠ test/serving 分布时,在训练集上学到的相关性可能在新分布下失效甚至有害。在本 wiki 中它以多种具体面貌反复出现——推荐系统中的曝光空间 vs 未曝光候选空间不一致([[selection-bias]])、离线 RL 中策略访问的状态-动作分布偏离行为策略数据、LLM 自我纠错中 SFT 训练轨迹偏离模型自身的测试时输出分布,以及校准集与测试集之间的偏移。各类应对手段(分布鲁棒优化、不变学习、悲观惩罚、on-policy 训练、采集未曝光样本等)本质上都在缩小或对冲这一分布鸿沟。

## 在本 wiki 中的出现

- [[2024-recflow-full-flow-recommendation-dataset]]:把分布偏移作为工业推荐数据集的核心动机——模型在曝光空间(exposure space)上训练,但在线服务时却要对海量未曝光候选打分,训练与服务空间不一致带来 [[selection-bias]] 与次优表现。RecFlow 通过显式采集多级漏斗中各阶段"被过滤(未曝光)样本",把这些阶段样本作为 hard negative 或补充负样本来缓解 retrieval / coarse ranking 的分布偏移。
- [[2024-score-self-correct-via-rl]]:在 LLM [[self-correction]] 场景中把分布偏移诊断为 SFT 类方案失败的根因——在离线/他人生成的纠错轨迹上做监督微调,训练分布与模型自身在测试时产生的回答分布不匹配。SCoRe 改用在线(on-policy)多轮 [[reinforcement-learning]] 在模型自生成轨迹上训练,从根本上消除这一训练-测试分布不一致。
- [[2025-mitigating-unwanted-recommendations-conformal-risk-control]]:在用 [[conformal-risk-control]] 控制推荐内容风险时,观察到校准集(calibration)与测试集(test)之间存在分布偏移——若不按 watch-time 阈值过滤"安全重复内容",部分旧项会二次被举报,使原本的风险保证失效;按阈值过滤可恢复风险控制。该方法本身走 distribution-free 路线,以减少对分布假设的依赖。
- [[2023-causal-inference-for-recommendation]]:在因果**鲁棒性**专题下,把应对 distributional shift(连同攻击、稀疏性)列为将因果推断引入推荐的关键动机之一——纯相关学习易随分布变化而失效,而刻画底层因果机制有助于在分布偏移下保持稳定。

## 相关

- [[distributionally-robust-optimization]]
- [[invariant-learning]]
- [[invariant-risk-minimization]]
- [[offline-rl]]
- [[performative-prediction]]
- [[data-heterogeneity]]
- [[selection-bias]]
- [[debiasing]]
- [[recommender-systems]]
- [[recflow]]
