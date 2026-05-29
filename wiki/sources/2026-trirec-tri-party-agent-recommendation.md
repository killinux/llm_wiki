---
type: source
subtype: paper
tags:
  - llm-agent
  - recommender-system
  - multi-stakeholder-recommendation
  - provider-fairness
  - cold-start
  - re-ranking
created: 2026-05-29
updated: 2026-05-29
arxiv: "2603.10673"
raw: raw/2603.10673.pdf
authors:
  - Yaxin Gong
  - Chongming Gao
  - Chenxiao Fan
  - Haoyan Liu
  - Wenjie Wang
  - Jianshan Sun
  - Yangyang Li
  - Fuli Feng
  - Xiangnan He
year: 2026
---

TriRec 是首个 tri-party(用户—物品—平台)LLM-agent 推荐框架,通过赋予物品 agent 主动"自我推销"能力并由平台进行曝光感知的多目标重排,打破传统以用户为中心、把物品当作被动实体的范式。

## 问题

现有 agent-based 推荐方法(见 [[llm-for-recommendation]]、[[agentcf]]、[[macrec]])大多沿袭以用户为中心的决策范式,只优化用户效用,把物品当作被动的信息载体或属性描述符,忽视了内容创作者、平台运营方等其他关键利益相关者的利益。这种单边优化加剧了 [[matthew-effect]](马太效应)与 [[popularity-bias]]:曝光集中在已经流行的物品上,长尾创作者可见度低([[cold-start]] / [[long-tail-creators]]),导致创作者流失、内容池同质化,损害平台长期生态健康。即使部分工作引入物品 agent 或内容 agent([[rec4agentverse]]、[[dualrec]]),它们仍主要充当信息载体,缺乏对物品自身利益的主动追求。

## 方法

作者提出 TriRec(**Tri**-party Re**c**ommendation),核心是显式协调用户、物品、平台三方效用的两阶段解耦架构。整体在固定参数(frozen)的 LLM 上推理,基于 [[agentcf]] 式的 agent 记忆(用户偏好记忆 + 物品语义记忆)进行 [[agent-based-preference-interaction]]。

- **多方效用建模**:用户效用为预测相关性 r(u,i);物品效用用 Expected Item Utility(EIU)= 位置依赖曝光 v(rank)·CTR;平台效用聚合 Distributional Group Unfairness(DGU)与 Maximal Group Unfairness(MGU)两个 group-level [[provider-fairness]] 指标。
- **Stage 1 — Generative Personalized Self-Promotion(生成式个性化自我推销)**:物品 agent 针对目标用户兴趣表征生成个性化推销文案 S(i→u),仅基于静态元数据(标题、类别、描述)且 prompt 强制 grounding,杜绝测试期信息泄露与虚构属性。用户 agent 通过多轮语义偏好推理(argsort)对候选物品的自我推销进行相关性导向重排,缓解 [[cold-start]] 障碍。此阶段不注入任何曝光/公平约束,只产出高质量相关性 backbone。
- **Stage 2 — Platform-Led Multi-Objective Re-Ranking(平台主导多目标重排)**:把曝光建模为动态系统状态(historical exposure vector),平台作为 [[markov-decision-process]] / 序列控制过程,通过 Greedy Sequential Re-ranking 逐位贪心选择,最大化 position-aware joint utility = g(相关性-公平凸权重)× 曝光感知物品效用调制器。设计 Position-Aware Participation Policy(α_k 随排名位置单调变化)在头部位置保护用户相关性、向低位逐步注入平台公平正则,实现可控的 relevance–fairness trade-off。曝光状态用对数衰减 v(k)=1/log₂(k+2) 跨轮累积。

## 结果

在 4 个真实数据集(Amazon CDs & Vinyl、Amazon Movies & TV、Goodreads YA、Steam Games,均用 Sentence-BERT 编码语义嵌入,leave-one-out + SASRec 硬负采样,默认候选集 n=9 即大小 10)上,以 GPT-4o-mini 为默认 backbone:

- **整体性能(Table 2)**:TriRec 在全部 4 个数据集上取得最高 NDCG@5;CDs & Vinyl 上 NDCG 0.4951、MRR 0.4702、EIU 0.5925,均优于 [[macrec]]、[[agentcf]]、[[rec4agentverse]]、[[dualrec]]、[[scruf-d]]、[[ltp-mmf]]。EIU(物品效用)在 4 个数据集上全部最高。
- **公平性**:在 Movies & TV、Goodreads YA、Steam Games 上取得最佳 DGU 与 MGU;CDs & Vinyl 上 SCRUF-D 的 DGU/MGU 最低但其 NDCG 仅 0.258(约为 TriRec 0.495 的一半),说明其以牺牲相关性换公平;TriRec 在 DGU 0.160 / MGU 0.147 下仍保持最高精度。
- **消融(Table 3)**:去掉 Stage 1 使 NDCG 下降 31.7%;引入 item self-promotion 带来 +10.4 个 NDCG 点的同时把 DGU 从 0.170 改善到 0.166,挑战"公平与相关性必然冲突"的假设。去掉 U_user 使 NDCG 降至 0.263(平台重排过度偏向公平)。
- **超参(RQ3)**:λ_item 从 0 升到 5–20 时三方指标同时改善(NDCG +6.6% 到 0.499),默认 λ_item=10。Log 衰减在四数据集上提供最一致的公平优势(Table 4)。
- **backbone(Table 5)**:GPT-3.5-Turbo / GPT-4o-mini / GPT-4o / DeepSeek-V3 / Qwen-plus 结果接近,增益来自 tri-party 设计而非特定 LLM。
- **效率**:CDs & Vinyl 上 TriRec 每用户请求 98.4 tokens,与 MACRec(114.3)相当,远低于 Rec4AgentVerse(143.7),且因 Stage 1 并发生成、Stage 2 为闭式算术,wall-clock 延迟基本独立于候选集大小。
- **冷启动案例(RQ4)**:训练中零曝光、初始排名第 10 的目标物品(Digital Music "The Book of Mormon"),物品 agent 锚定用户对 "original cast recording / Broadway / rich audio quality" 的偏好生成推销,用户 agent 给出 9.5/10 最高分,成功重排到第 1 位,打破 "无曝光→无反馈→无推荐" 循环且无需协同过滤信号。

局限:offline 协议未必完全反映长期动态;生成的自我推销缺乏事实性量化审计,未来需多轮模拟、在线 A/B、retrieval-grounded 事实约束及对抗性自我推销/provider gaming 的防护。

## 在本 wiki 中的位置

本文属于 [[llm-agent]] 驱动的 [[recommender-system]] 方向,可与 [[agentcf]]、[[rec4agentverse]]、[[dualrec]]、[[macrec]] 等 agent-based 推荐工作对照,代表从"以用户为中心"转向 multi-stakeholder / [[provider-fairness]] 的 tri-party 路线。其 Stage 2 把 re-ranking 建模为 [[markov-decision-process]] 序列控制,与 [[ltp-mmf]]、[[scruf-d]] 等平台公平重排方法相关;对 [[cold-start]]、[[matthew-effect]]、[[popularity-bias]] 的处理可与 [[content-creator-incentive]]、[[two-sided-fairness-reranking]] 等创作者侧/双边公平研究联系。作者团队来自 [[university-of-science-and-technology-of-china]]([[chongming-gao]]、[[fuli-feng]]、[[xiangnan-he]] 等)。
