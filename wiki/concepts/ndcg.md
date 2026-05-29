---
type: concept
subtype: method
tags: [ranking, evaluation, recommendation, information-retrieval]
created: 2026-05-29
updated: 2026-05-29
sources: 12
---

# NDCG

NDCG(Normalized Discounted Cumulative Gain,归一化折损累计增益)是一种衡量排序列表质量的指标,通过对靠前位置赋予更高权重来累计相关性收益,并以理想排序进行归一化,常用于推荐系统与信息检索的排序效果评估。

## 在本 wiki 中的出现

- [[2024-bankfair-fluctuating-traffic-reranking]]:BankFair 借鉴破产问题的 Talmud rule,把两侧推荐的曝光分配建模为序列化破产问题并用在线学习求解,在波动用户流量下同时保证短期用户准确性与长期提供方公平性。
- [[2024-tim4rec-time-aware-mamba]]:TiM4Rec 用 Time-aware Structured Masked Matrix 把时间感知增强首次引入 SSD/Mamba2 架构,在线性复杂度下弥补 SSD 在低维序列推荐场景相对 SSM 的性能退化。
- [[2026-pdqubo-quantum-feature-selection]]:PDQUBO 用反事实分析量化单特征与特征对的推荐性能影响,构造性能驱动的 QUBO 系数矩阵,在量子退火器上做模型无关、指标无关的推荐系统特征选择。
- [[2024-recflow-full-flow-recommendation-dataset]]:首个包含工业推荐系统多级漏斗各阶段未曝光样本的大规模全流程数据集,用于研究分布偏移、选择偏差与多阶段联合优化。
- [[2024-online-item-cold-start-popularity-aware-meta-learning]]:提出 PAM,一种按物品热度固定切分 meta-learning 任务的 model-agnostic 框架,在流式在线推荐中解决新物品冷启动并缓解马太效应。
- [[2024-large-recommendation-models-scaling]]:华为诺亚与 USTC 的工作,系统评估 large recommendation models 的 scaling law,以生成式推荐模型 HSTU 为代表,在多 backbone、复杂用户行为与 ranking 任务上验证可扩展性及其来源组件。
- [[2025-llm-agents-for-recommender-systems-survey]]:系统综述 LLM 驱动 agent 在推荐系统中的应用,提出"面向推荐/交互/模拟"三范式,并用 Profile-Memory-Planning-Action 四模块统一架构对比 23 个方法、汇总数据集与评测。
- [[2025-agentcf-plus-plus]]:通过双层记忆架构、两步融合机制与兴趣组共享记忆增强 AgentCF 用户模拟器,在跨域推荐中减少无关信息并显式建模流行度因素。
- [[2025-bankfair-plus-regret-aware-reranking]]:BankFair+(BankFair 的扩展期刊版)把 regret theory 的非线性满意度函数与 fuzzy programming 引入推荐重排,在保证供给侧最低曝光公平与用户平均精度的同时,显著提升被忽视的用户个体公平(KuaiRand-1K 上 MMR 0.741 vs BankFair 0.493)。
- [[2025-autocdsr-self-attention]]:AutoCDSR 把跨域序列推荐建模为偏好感知的 Pareto 最优多目标问题,通过动态最小化 cross-domain attention scores,仅优化 transformer 内在 self-attention 即可自动迁移有益跨域知识并抑制 negative transfer。
- [[2025-pub-personality-user-behaviour-simulator]]:PUB 是一个基于 LLM 的用户行为模拟器,把 Big Five 人格特质嵌入用户建模,从行为日志推断人格并生成高保真合成交互,用于推荐系统的离线评估。
- [[2025-tadt-csa-temporal-advantage-decision-transformer]]:面向工业生成式推荐的 Decision Transformer 改进框架,用 Temporal Advantage 信号和对比式状态抽象解决 DT 的轨迹拼接弱与状态空间过大问题。

## 相关

- [[recommendation-system]]
- [[information-retrieval]]
- [[ranking-metric]]
- [[two-sided-fairness]]
