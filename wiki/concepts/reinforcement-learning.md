---
type: concept
subtype: method
tags: [reinforcement-learning, rl, actor-critic, mdp, recommendation, agent]
created: 2026-05-29
updated: 2026-05-29
sources: 19
---

# Reinforcement Learning

Reinforcement Learning(强化学习)是一类通过智能体(agent)与环境交互、以最大化累计奖励(reward)为目标来学习决策策略的机器学习方法。

## 在本 wiki 中的出现

- [[2023-two-stage-constrained-actor-critic]]:作为核心方法,提出两阶段约束式 actor-critic(TSCAC),在最大化短视频 WatchTime 主目标的同时软约束平衡 Like/Share 等稀疏交互,已在快手生产系统全量上线。
- [[2023-rlur-user-retention-short-video]]:把短视频用户留存建模为无限时域请求级 MDP,用 RL 直接最小化累计回访时间(RLUR),在 KuaiRand 上优于 TD3/CEM,并在 Kuaishou 全量上线提升留存与 DAU。
- [[2023-hyper-actor-critic-recommendation]]:提出 Hyper-Actor Critic(HAC)框架,把推荐列表生成解耦为 hyper-action 推断与 effect-action 选择两步,并用对齐与监督模块稳定大动作空间下的 RL 推荐策略学习。
- [[2023-voyager]]:作为终身学习具身智能体的决策范式,首个由 GPT-4 驱动、在 Minecraft 中通过自动课程、可执行代码技能库与自我验证实现持续探索与学习。
- [[2023-gflownet-listwise-recommendation]]:GFN4Rec 用 GFlowNet 流匹配让推荐列表的生成概率正比于其 list-wise 奖励,作为 RL 推荐的替代/补充思路,在保持质量的同时提升列表多样性与在线探索。
- [[2023-kuaisim-recommender-simulator]]:面向推荐系统的综合性用户模拟器,提供 multi-behavior 与 cross-session 反馈,统一支持 request 级 list-wise、whole-session 级 sequential 与 cross-session 级 retention 三类 RL 推荐任务并配套 benchmark。
- [[2023-ts-llm-tree-search-decoding-training]]:TS-LLM:用学习的 value function 的 AlphaZero 风格树搜索,同时指导 LLM 的推理解码与迭代训练,适配任意规模 LLM 并将搜索深度扩展到 64。
- [[2024-eureka-reward-design-via-coding-llms]]:Eureka 用编码 LLM(GPT-4)零样本生成可执行奖励函数代码,结合进化搜索与奖励反思迭代改进,在 29 个 RL 环境上达到人类专家级奖励设计并首次让模拟 Shadow Hand 学会转笔。
- [[2024-unex-rl-multi-stage-recommender]]:UNEX-RL 用多智能体 RL 对多阶段推荐系统的各阶段联合建模,以单向执行与 cascading information chain (CIC) 优化长期回报,Kwai 在线提升日观看时长 0.953%。
- [[2024-future-impact-decomposition-request-level-recommendation]]:提出 ItemA2C 框架,在 request-level MDP 下将 list-wise reward 分解为 item-wise 信用并用 actor-critic 优化每个 item 的长期未来影响,提升推荐长期效果。
- [[2024-easyrl4rec]]:面向 RL-based 推荐系统的易用代码库,基于五个公开数据集构建轻量 RL 环境,提供四个核心模块与面向长期收益的统一训练/评测流程,并给出经典与近期 RL 方法的对照实验。
- [[2024-llm-learnable-planners-long-term-recommendation]]:提出 BiLLP 双层可学习 LLM 规划框架(Planner/Reflector 宏观 + Actor/Critic 微观),在稀疏推荐数据上以 LLM 规划能力做长期推荐,Len 与累积奖励超越从零训练的 RL 与现有 LLM agent 基线。
- [[2024-quiet-star]]:Quiet-STaR 让语言模型在每个 token 前生成隐式 rationale 来更好预测后续文本,以自监督方式从任意文本学会推理,zero-shot 提升 GSM8K(5.9%→10.9%)与 CommonsenseQA(36.3%→47.2%)。
- [[2024-model-based-multi-agent-short-video-recommender]]:MMRF:协作式多智能体 RL 最大化短视频会话累计 WatchTime,并用 model-based 反馈模拟缓解样本选择偏差,离线 +7.3% GAUC、在线 +0.55% WatchTime,已部署服务数亿用户。
- [[2024-lusifer-llm-user-simulation]]:提出 Lusifer:基于 LLM 的用户模拟环境,在每次交互后增量更新可解释的用户画像,为 RL-based 推荐系统生成动态真实的用户反馈,并在 cold-start 场景超越传统协同过滤基线。
- [[2024-edt4rec-max-entropy-decision-transformer]]:EDT4Rec 给 Decision Transformer 加入最大熵探索与基于 CQL Q-function 的 reward relabeling,解决 offline RL 推荐中缺乏 stitching 能力和在线探索不足的问题。
- [[2024-conditional-quantile-estimation-watch-time]]:提出 CQE,用 quantile regression 与 pinball loss 建模短视频观看时长的完整条件分布,并设计保守/动态组合/条件期望三种推断策略,在 Kuaishou 数亿日活平台上线获显著收益。
- [[2024-roler-reward-shaping-offline-rl-recsys]]:ROLeR 用非参数(kNN/聚类)reward shaping 与解耦的不确定性惩罚修正 model-based offline RL 推荐中 world model 的 reward 估计误差,在 KuaiRand/KuaiRec/Coat/Yahoo 四个 benchmark 上达到 SOTA。
- [[2024-recursive-introspection-rise]]:RISE 将单轮问题建模为多轮 MDP 并用 reward-weighted regression 迭代微调,让 7B 级 LLM 在无外部反馈下学会跨多轮递归反思并修正答案。

## 相关

- [[actor-critic]]
- [[markov-decision-process]]
- [[gflownet]]
- [[recommendation-system]]
- [[llm-agent]]
- [[reward-modeling]]
- [[exploration-exploitation]]
- [[offline-reinforcement-learning]]
- [[multi-agent-reinforcement-learning]]
- [[reward-shaping]]
- [[decision-transformer]]
- [[user-simulation]]
- [[tree-search]]
- [[llm-reasoning]]
