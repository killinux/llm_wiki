---
type: source
subtype: paper
tags: [recommender-system, reinforcement-learning, large-language-models, imitation-learning, inverse-reinforcement-learning, offline-rl, llm-for-recommendation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.13229
raw: raw/2510.13229.pdf
authors: [Yi Zhang, Lili Xie, Ruihong Qiu, Jiajun Liu, Sen Wang]
year: 2025
---

# Beyond Static LLM Policies: Imitation-Enhanced Reinforcement Learning for Recommendation

提出 IL-Rec:一个离线 [[reinforcement-learning]] 框架,通过对 LLM 生成的轨迹做模仿学习并用 [[inverse-reinforcement-learning]] 抽取奖励模型,从而把 LLM 的语义知识迁移给 RL 推荐策略,既消除在线频繁调用 LLM 的开销,又超越静态 LLM 策略的表现。

## 问题

LLM 凭借强泛化与上下文理解能力为 [[recommender-systems|recommender-system]] 带来潜力,但把 LLM 直接当作推荐策略部署面临几大挑战:

- **高计算成本与高延迟**:在线推荐需要低延迟响应,而每步都调用 LLM API 会带来持续的高延迟与算力开销。
- **幻觉与偏差**:LLM 输出易出现 [[hallucination]] 与 [[popularity-bias]],倾向重复表面关联、强化高频项,降低推荐多样性(图 1 中 "Godfather" 子串匹配的例子)。
- **静态策略难以适配动态偏好**:LLM 通过 prompting 生成的策略是静态的,难以随用户兴趣动态演化而调整。
- 传统 [[rl-based-recsys]] 虽能优化长期参与度,但只能依赖粗粒度反馈信号,无法捕捉用户历史中细腻的语义依赖。LLM 微调路线([[fine-tuning]])则代价高昂。

## 方法

IL-Rec 把推荐建模为 [[markov-decision-process]],用离线 LLM 演示训练 RL 策略,**无需在线调用 LLM、也无需微调 LLM**。整体流水线分三阶段:

- **World Model 学习**:沿用 model-based 离线 RL 思路,用离线日志以监督方式(如 [[deepfm]])学习奖励函数 r̂;转移函数由序列模型(state tracker)实现,构成 [[world-model]]。
- **LLM 演示采集(Demonstrations)**:由四个模块协作生成专家轨迹——Reflector(对完整 episode 生成文本反思 m_k)、Planner(基于状态检索历史反思、生成高层文本规划 g_t)、LLM Actor(两阶段动作生成 + 候选选择,生成动作后取与候选 item embedding 余弦相似度最高者)、LLM Critic(估计状态价值,结合 [[actor-critic]] A2C 计算优势函数)。各模块通过 [[memory-module]] 检索([[faiss]] 相似度搜索)共享信息,状态-动作对用 [[llama]] 编码为文本嵌入。
- **Adversarial Inverse RL + 加权模仿**:用判别器 D_ψ 区分当前策略 π_θ 在 world model 中 rollout 的轨迹与专家演示([[adversarial-imitation-learning]] / GAIL 思路),奖励定义为 r_IRL = −log D_ψ(s,a)。由于 LLM 演示是 suboptimal 的,引入双重加权:基于环境优势的权重 w_env = exp(A_demo/β) 与基于判别器置信度的 IRL 权重 w_IRL,二者用系数 α 融合为 w(s,a),对高质量演示加权、弱化低质量演示。策略损失为加权模仿损失 L_imit 与 [[reinforcement-learning]] actor-critic 损失之和(L_policy = λ_imit·L_imit + L_RL),通过 [[off-policy-evaluation]] 式的混合 replay buffer 迭代优化,直至学到的策略超越原始 LLM 演示。

## 结果

- **数据集**:[[steam-dataset]](6012 用户 / 190365 item)与 [[amazon]] book(3109 用户 / 13864 item),沿用 [[billp]] 协议。指标含 R_traj(累积奖励,主指标)、R_each(单步奖励)、Len(平均交互长度)。
- **整体表现(RQ1)**:IL-Rec 在两个数据集上累积奖励均最高。Steam 上 R_traj=78.478,超过此前 SOTA [[billp]];Amazon 上 R_traj=48.219,相对 BiLLP 提升 **13.4%**。交互长度 Len:Steam 17.533(较 BiLLP +14.1%),Amazon 11.136(较次优 +18.3%)。单步奖励 R_each 有竞争力(Steam 4.476 / Amazon 4.330),但不一定居首,因为基于直接 LLM 推理的 ReAct/ActOnly 偏好短期参与。
- **效率**:IL-Rec 单次训练约 12 GPU-hours(NVIDIA Tesla A100 40GB:world model 模拟 3h + LLM 演示生成 3h + adversarial inverse RL 6h),约为 BiLLP(6 GPU-hours)的两倍;但 world model 模拟与演示生成是一次性成本。
- **消融(RQ2)**:去掉整体加权(w/o w),Steam R_traj −14.1%、Amazon −18.4%;去掉 w_env,Steam −19.3%、Amazon −16.5%(Len 也分别降 24.7% / 22.3%);去掉 w_IRL,Steam −9.1%、Amazon −8.7%。表明环境权重主要支撑长期回报,IRL 权重也主要影响长期表现。
- **LLM 泛化(RQ3)**:LLM 能力越强收益越大。用 [[gpt-4]]-32k 时 R_traj 达 Steam 128.346 / Amazon 64.121,显著优于其他变体;即便用 [[llama-2]]-7b、Deepseek-R1-Distill-Qwen-14b 等较小模型,IL-Rec 仍可媲美甚至超过 BiLLP(如 Llama2-7b 在 Steam R_traj=71.75)。
- **超参敏感性(RQ4)**:β(w_env 温度)Steam 在 β=10 最优、Amazon 在 β=1 最优;权重融合系数 α 在 Steam 0.5、Amazon 0.25 最优;熵温度 α_ent 两个数据集均在 0.1 最优;模仿损失系数 λ_imit 在 Steam 0.25、Amazon 0.5 最优。

## 在本 wiki 中的位置

本文处于 [[rl-based-recsys]] 与 [[llm-for-recommendation]] 的交叉点,核心贡献是用 [[imitation-learning]] + [[inverse-reinforcement-learning]]([[adversarial-imitation-learning]] / GAIL)把 LLM 的语义知识蒸馏进低延迟的 RL 推荐策略。可与 [[billp]]、[[dorl]]、[[cirs]]、[[roler]] 等 model-based 离线 RL4RS 工作对照,也与 [[react]]、[[reflexion]] 等 LLM agent 推理范式相关。其离线 RL 组件涉及 [[offline-rl]]、[[markov-decision-process]]、[[actor-critic]]、[[world-model]] 等概念。
