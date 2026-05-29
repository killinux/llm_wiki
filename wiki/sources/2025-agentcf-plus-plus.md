---
type: source
subtype: paper
tags:
  - llm-based-agents
  - user-simulation
  - recommender-system
  - cross-domain-recommendation
  - agent-memory
  - popularity-bias
created: 2026-05-29
updated: 2026-05-29
arxiv: 2502.13843
raw: raw/2502.13843.pdf
authors:
  - Jiahao Liu
  - Shengkang Gu
  - Dongsheng Li
  - Guangping Zhang
  - Mingzhe Han
  - Hansu Gu
  - Peng Zhang
  - Tun Lu
  - Li Shang
  - Ning Gu
year: 2025
---

# AgentCF++: Memory-enhanced LLM-based Agents for Popularity-aware Cross-domain Recommendations

AgentCF++ 通过双层记忆架构 + 两步融合机制 + 兴趣组共享记忆,改进 [[agentcf]] 这类 [[llm-based-agents]] 用户行为模拟器,使其在跨域场景中减少无关信息干扰,并显式建模流行度因素。

## 问题

[[llm-for-recommendation]] 中,[[user-simulation]](用 LLM 模拟用户交互行为)被视为以隐私保护方式理解用户偏好、改进 [[recommender-systems|recommender-system]] 的有前景方向。但现实中用户交互常具有跨域(cross-domain)特征,且个体行为常受他人交互的影响(即流行度因素 / popularity factors)。

作者指出 [[agentcf]] 这一将用户与物品都建模为 agent、用协同过滤式 [[agent-memory]] 传播的方法存在两个局限:

- **单一记忆混合跨域偏好**:用户 agent 把来自多个域的偏好混在同一份记忆里,而决策时只有部分偏好与目标域相关,导致 agent 处理大量无关信息,产生噪声。
- **记忆仅由个体交互构建,无法识别流行度因素**:记忆更新只在用户与物品 agent 直接交互时发生,无法刻画外部因素(如他人交互、天气变化引发的趋势)如何塑造偏好。论文用 Alice/Bob/Carl 购买户外/雨具/露营装备的例子说明:即使 Alice 不再直接交互,其偏好也应随 Bob、Carl 的行为动态演化。

作者特别澄清:与 [[debiasing]] 方法试图剔除流行度因素不同,用户行为模拟的目标是建模真实行为,因此 popularity factor 不是需要消除的干扰项,而是必须显式建模的关键因素(用户行为 Y 同时受用户偏好 X 与流行度因素 P 影响)。

## 方法

AgentCF++ 沿用 AgentCF 的"用户 agent + 物品 agent + 反思更新"范式,主要新增三部分:

- **双层记忆架构(dual-layer memory)**:每个用户 agent 对每个域维护两类记忆——(1) **domain-separated memory** 保留该单一域专属偏好;(2) **domain-fused memory** 整合来自其他域的 domain-separated 记忆。物品 agent 仍用单一记忆。
- **兴趣组与 group-shared memory**:对每个用户 agent,通过 LLM 流程构建兴趣组——(1) 由 domain-fused memory 派生兴趣标签;(2) 用 embedding + K-means 聚类合并同义标签;(3) LLM 综合每簇生成兴趣组名,保留覆盖大部分兴趣的少数兴趣组。同一兴趣组内用户共享一份固定大小的 group-shared memory,存储成员近期交互历史,使流行度效应只在相似兴趣用户间传播,避免污染无关用户。论文强调按兴趣(而非完整交互历史)分组能更精确定位受流行度影响的人群。
- **两步融合机制(two-step fusion)**:在更新阶段(基于 reflection 机制),用户先用最新交互更新 domain-separated memory;再(1)从其他域的 domain-separated 记忆中抽取与目标域相关的偏好,(2)将这些偏好整合进目标域的 domain-fused memory。论文称该机制隐含 attention 思想——第一步类似抽取目标域相关偏好计算注意力分数,第二步类似加权聚合。

**推理阶段**:给定交互 (u, i, d),从域 d 选负样本 j(故意放在正样本之后以缓解 position bias),用户 agent 同时依赖 domain-separated、domain-fused 与 group-shared 记忆识别正样本并解释推理。

## 结果

- **数据集**:基于 [[amazon-reviews]] 数据集构建 5 个跨域数据集 Cross-1 至 Cross-5,组合 Books、CDs、Movies、Games 域(每个数据集 3 或 4 个域),时间跨度 2021-10 至 2022-03,保留评分 ≥ 4、跨多域且总交互 ≥ 10 的用户,随机采样 100 用户,按 8:1:1 划分。
- **评测**:每个 ground truth 物品配 9 个未交互负样本,用户 agent 排序候选,用 [[ndcg]] 与 MRR 评估,5 次运行取平均。
- **baseline**:传统模型 BPR-MF、[[sasrec]];免训练方法 Pop、LLMSeqSim、LLMRank、[[agentcf]]。
- **总体表现(Table 1,MRR)**:AgentCF++ 在全部 5 个数据集上一致优于 AgentCF 及所有 baseline。例如 Cross-1 上 AgentCF++ 达 0.3537,高于 AgentCF 的 0.3284;Cross-4 达 0.3321、Cross-5 达 0.3837。论文也指出 AgentCF 仅与 LLMRank 相当、不及传统模型 SASRec,说明传统模型通过训练机制天然捕获了流行度与跨域协同信息。
- **消融**:设计 AgentCF + dual(仅双层记忆)、AgentCF + shared(仅兴趣组 + 共享记忆)、AgentCF++ w/o group(按完整交互历史而非兴趣分组)。AgentCF++ 一致优于所有消融变体与 baseline;两个消融变体也都优于 AgentCF,验证各模块有效。值得注意的是 AgentCF++ w/o group 不仅差于 AgentCF++,还差于 AgentCF + dual,说明按完整交互历史分组过于粗糙,会让流行度影响波及无关用户、引入噪声。

## 在本 wiki 中的位置

本文是 [[agentcf]] 的直接增强版,属于"用 [[llm-based-agents]] 做 [[user-simulation]] 以服务 [[recommender-systems|recommender-system]]"这一线索,与 [[recagent]]、[[agent4rec]]、[[lusifer]] 等用户行为模拟工作相关。其核心贡献围绕 [[agent-memory]] 设计([[llm-long-term-memory]] 在推荐场景的具体化)与 [[cross-domain-recommendation]]。在对待流行度的立场上,它与 [[debiasing]] / [[popularity-bias]] 方向形成对照:不消除而显式建模流行度因素。作者来自 [[microsoft-research-asia]] 与复旦大学,合作者包括 [[dongsheng-li]]、[[tun-lu]] 等。
