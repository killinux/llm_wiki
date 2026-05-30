---
type: topic
tags: [reinforcement-learning, recommender-system, offline-rl, long-term-value, user-retention, multi-objective]
created: 2026-05-30
updated: 2026-05-30
sources: 20
---

# 推荐系统中的强化学习 (RL for Recommendation)

> 一句话:把推荐建模为**序贯决策 (MDP)**,用 [[reinforcement-learning|强化学习]]直接优化**长期累计收益**(留存、总时长、生态健康),
> 而非贪心优化单步点击。核心张力是:线上真实试错代价高 → 必须做 **offline RL**,而 offline RL 的命门是
> **分布外 (OOD) 外推误差**与 world model 奖励不准。

这是本 wiki "推荐系统"半边的主干方法线,概念枢纽见 [[reinforcement-learning-for-recommendation]]。与 [[generative-social-simulation]]
那条"社会模拟"线在**用户模拟器 / 离线评估**处交汇(见下"评估"一节)。

---

## 一、为什么用 RL:长期价值 vs 即时指标
监督式 CTR/CVR 排序逐 item 打分、只优化即时反馈,会损害留存与多样性。RL 的价值在于显式优化**跨期回报** Σγᵗrₜ:
- **留存**:[[2023-rlur-user-retention-short-video]](RLUR,WWW'23)把留存建模为**无限时域、以请求为单位的 MDP**,目标=最小化累计回访时间,
  已在 [[kuaishou|快手]] 全量上线;难点是留存奖励的**长延迟、高方差、群体偏差**(高活用户天然留存高,故对高/低活分别学两套策略)。
- **时长 + 多目标**:[[2023-two-stage-constrained-actor-critic]](TSCAC,快手上线)把"最大化 WatchTime + 软约束 Like/Follow/Share"建模为
  **CMDP**,用 multi-critic(每种响应单独价值模型,避免稠密信号淹没稀疏信号)+ 两阶段 actor;离线 NCIS 评估 WatchTime 13.14(+2.23% vs BC)。
  另见 [[2023-multi-task-recommendations-with-rl]]、[[2023-hyper-actor-critic-recommendation]]。

## 二、核心难题:Offline RL 与 OOD 外推
线上试错贵,主流是只用日志学策略的 **offline RL**;其根本风险是函数逼近器对**日志未覆盖的 state-action 外推 Q 值**导致高估发散。
两条技术路线:
- **Model-free + 保守性**:[[bcq]](只取数据内动作)、[[cql]](压低 OOD 动作 Q 值)。
- **Model-based**:先学 [[world-model]](奖励模型,常用 [[deepfm]]),再在其中训策略——更 sample-efficient(稀疏日志上能造更多交互序列)。
  这是推荐 offline RL 的主流,演化出下面一条清晰的谱系。

### Model-based 奖励修正谱系(本线最活跃的脉络)
| 工作 | 关键贡献 | 代表数字 |
|---|---|---|
| MOPO | 不确定性惩罚的保守 MDP | — |
| [[2023-dorl-matthew-effect-offline-rl-recommendation]] | 发现保守性会加剧**马太效应**,加 **熵惩罚**做反事实探索 | KuaiRec 累计奖励 20.49(次优 IPS 12.83) |
| [[2024-roler-reward-shaping-offline-rl-recsys]] | **非参数 (kNN/聚类) reward shaping** 修正不准的奖励 + 解耦不确定性惩罚(摆脱 ensemble) | KuaiRec R_tra≈33.25(GT 上界≈36.75),4 benchmark SOTA |
| [[2025-darlr-dual-agent-offline-rl-recsys]] | **双 agent**(selector+recommender)在训练中**动态精炼** world model 奖励,自适应不确定性 | 缓解 frozen reward |

另见 [[2024-edt4rec-max-entropy-decision-transformer]]、[[2025-maximum-in-support-return-modeling]]、[[2025-energy-guided-diffusion-rl-recommendation]]。

## 三、马太效应与生态健康
保守性/贪心都会让"热门越热、冷门越冷",形成 filter bubble、损害长期满意度。[[2023-dorl-matthew-effect-offline-rl-recommendation]]
用熵惩罚鼓励指向多样状态的动作;[[2025-imitation-enhanced-rl-for-recommendation]]、[[2026-lerl-llm-enhanced-rl-long-term-recommendation]] 等延续。
与 [[item-side-fairness|物品侧公平]]、[[exploration-exploitation|探索-利用]] 直接相关。

## 四、多阶段 / 多智能体
工业推荐是 matching→pre-ranking→ranking→re-ranking 级联。[[2024-unex-rl-multi-stage-recommender]] 把各阶段建模为
[[multi-agent-reinforcement-learning|MARL]] 的多个 agent,指出标准 CTDE 失效(上游动作改变下游候选集→违反 observation 假设),
提出 **单向执行 (unidirectional execution)** + **Cascading Information Chain**(仅用第一阶段 observation 重放全系统)+ 方差缩减(SG、CQR)。

## 五、序列建模视角:Decision Transformer
把 RL 重构为**条件序列生成**([[decision-transformer]]):以 return-to-go 为条件自回归生成动作,规避显式 TD 学习。
推荐变体:[[2024-edt4rec-max-entropy-decision-transformer]]、[[2025-tadt-csa-temporal-advantage-decision-transformer]]、
[[2025-multi-objective-controllable-decision-transformer]](按偏好向量在 Pareto 前沿移动)、[[2026-fairness-begins-with-state-dsrm-hrl]]。

## 六、评估:仿真器与离线评估(与社会模拟线的交汇)
RL 推荐落地的前提是能**离线评估**(见 [[offline-evaluation]]):
- **off-policy 估计**:IPS / doubly robust 校正曝光偏差;采样可靠性见 [[2025-sampling-strategies-offline-recommender-evaluation]],
  偏差严重时离线估计**不可靠**([[2025-debias-can-be-unreliable]])。
- **仿真器**:[[2023-kuaisim-recommender-simulator]]、[[easyrl4rec]] 提供沙盒;LLM 用户模拟器([[2024-lusifer-llm-user-simulation]]、
  [[2025-recoworld-simulated-environments-agentic-recsys]])是新方向,但需验证是否真对齐人类——这正是 [[generative-social-simulation]] 的
  "可信度验证"争议在推荐场景的投影([[2025-can-llm-agents-simulate-human-behavior]])。

## 七、开放问题
- **离线-在线一致性**:离线 cumulative reward 高 ≠ 线上留存涨;world model 偏差与 off-policy 估计偏差叠加。
- **奖励设计**:长期留存稀疏延迟、多目标冲突、生态公平如何编码进单一奖励仍是手艺活。
- **可扩展性**:全链路多阶段 + 十亿用户级的 MARL 训练稳定性与方差。
- **LLM × RL**:用 LLM 当 world model / 奖励 / 规划器([[2024-llm-learnable-planners-long-term-recommendation]]、[[2026-lerl-llm-enhanced-rl-long-term-recommendation]])是否真带来增益。

## 相关概念页
[[reinforcement-learning-for-recommendation]]、[[offline-rl]]、[[offline-evaluation]]、[[exploration-exploitation]]、
[[contextual-bandits]]、[[multi-objective-optimization]]、[[item-side-fairness]]、[[decision-transformer]]、[[world-model]]、[[markov-decision-process]]
