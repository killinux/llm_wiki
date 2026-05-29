---
type: source
subtype: paper
tags: [social-simulation, llm-multi-agent, intervention-policy, contextual-bandit, recommender-system, sft, dpo, polarization, misinformation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2603.19649
raw: raw/2603.19649.pdf
authors: [Renhong Huang, Ning Tang, Jiarong Xu, Yuxuan Cao, Qingqian Tu, Sheng Guo, Bo Zheng, Huiyuan Liu, Yang Yang]
year: 2026
---

# PolicySim: An LLM-Based Agent Social Simulation Sandbox for Proactive Policy Optimization

PolicySim 是一个基于 [[large-language-models]] 智能体的社会模拟沙盒,通过 [[supervised-fine-tuning]]+[[direct-preference-optimization]] 训练用户智能体、并用带消息传递的 [[contextual-bandit]] 自适应优化平台干预策略,从而在部署前(proactive)评估与优化推荐、曝光控制等平台干预政策。

## 问题

社交平台的干预政策(如 [[recommender-system]]、内容过滤、[[exposure-bias|曝光控制]])会无意中放大 [[echo-chamber|回音室]]、[[filter-bubble|过滤气泡]] 与 [[polarization|极化]],带来社会风险。现有评估主要依赖在线 A/B 测试,属于"反应式"(reactive):风险只能在部署后才暴露,反馈循环延迟且代价高昂,甚至可能造成不可逆的危害。已有的 [[llm-based-agents|LLM 社会模拟]] 提供了部署前替代方案,但当前方法存在三点不足:(1) 多数模拟未显式建模平台干预政策,难以刻画其效果;(2) 智能体设计严重依赖 [[prompt-engineering]] 而非对真实社交行为的真实建模,模拟可信度受限;(3) 缺乏利用模拟反馈来优化真实世界干预政策的原则化机制。

## 方法

PolicySim 沿用 [[human-behavior-simulation|HiSim]] 架构,由两大模块构成:

- **User Agent Module(用户智能体模块)**:每个智能体是带真实档案(profile)的 LLM 用户,跨轮累积记忆。
  - **User Profile**:从内容与元数据抽取四个高层属性——likely identity、interested areas、posting style、interaction behavior,用 φ(u_i) 表示。
  - **User Behavior**:在 conventional 社交动作(tweet/retweet/reply/like/dislike/do nothing)之外增加 follow / unfollow 两个关系动作,使网络拓扑动态演化;并采用 **Multiple Behavior Selection**(单轮多动作)。
  - **User Stance**:用 LLM 把用户立场离散分类为 {-1,0,1},并用指数移动平均(系数 α)平滑以降低 [[hallucination]] 噪声。
  - **Memory**:短期记忆 + 长期记忆(按语义相关性与时间衰减 e^{-λΔt} 检索),短帖低于阈值直接入池以省算力。
  - **Agent Training**:不靠 prompt 工程,而用两阶段 **SFT→DPO**。SFT 作为冷启动,在 (event, user, action) 元组上最小化响应序列的负对数似然;DPO 以 SFT 模型为参考策略 π_ref,用偏好对 (y⁺, y⁻)(负样本通过 base model 采样出低相似/动作不一致的 J 个样本)进一步对齐真实社交行为。还用 [[chain-of-thought|CoT]] 增强行为可解释性。
- **Intervention Policy Module(干预策略模块)**:实例化两类典型干预——[[recommender-system|推荐系统]](relational / personalized / headline 三种推荐源)与 **exposure control**(曝光控制,用 exp(u_i)∈[0,1] 调节帖子可见性,模拟审核、内容优先级或公平干预)。
- **Adaptive Intervention Policy(自适应干预)**:把干预建模为 [[contextual-bandit]],每个 arm 是 user-post 对(推荐)或 user-probability 对(曝光控制)。Context 由用户 profile+近期记忆 embedding,并通过 label propagation 在社交图上做 k 跳邻居聚合(X_user^k = γX^{k-1} + (1-γ)D⁻¹AX^{k-1})。优化采用 exploitation(神经网络 g 学 context→reward)+ exploration(神经网络估计 potential gain,即观测 reward 与预测 reward 的差),按 g+ĝ(∇g) 排序选 arm。Reward 对应两个目标:目标1 促进 cross-viewpoint 交互(reward 平衡立场分歧、用 [[perspective-api|Perspective API]] 惩罚 toxicity、按 engagement 加权),目标2 抑制 [[hallucination|misinformation]] 传播。

## 结果

- **数据集与设置**:主实验用 [[twibot-20|TwiBot-20]](229K 用户、33.5M 推文、456K 关注边),另在 [[weibo|Weibo]] 上补充。用户智能体 backbone 为 [[qwen2-5-instruct|Qwen2.5-3B-Instruct]](上下文 32,768),LoRA rank 64,SFT 学习率 1e-6 / batch 256,DPO β=0.1 / 学习率 5e-7 / J=2,均训练至多 10 epoch,12 张 A100-40GB。EMA α=0.8,bandit λ=1, k=4, β=0.5。
- **微观评测(Table 2,TwiBot-20)**:PolicySim 取得最佳 BERTScore F1 = 58.05、BertSim = 88.06;behaviour alignment Accuracy = 65.56(较 random 与 backbone baseline 提升 **8.26%**);self-consistency Accuracy = 56.00(提升 **10.15%**);social capability(LLM-as-Judge,1-4 分)Engagement = 3.20、Robustness = 2.73 均为最佳;Suitability(0-100)= 59.44。消融显示去掉 user profile 的 PolicySim-φ 显著下降;仅 SFT 或仅 DPO 均弱于完整 SFT+DPO,说明 SFT 是 DPO 的必要基础。Qwen 系列随规模增大稳定提升,印证 [[scaling-law]]。
- **宏观评测**:按时间注入触发新闻(以 Anti-abortion Legislation / Roe v. Wade 为主题,GPT-4o 总结 10 条),平均立场呈"快速下降后逐步回升"的真实舆论轨迹;立场标准差随轮次上升,表明出现极化;施加推荐系统干预后极化加剧(用户更多暴露于同质内容)。
- **干预策略效果(Table 3)**:目标1,PolicySim 把 cross-stance 交互比例提到 **0.56**(origin 0.04、ε-greedy 0.14、UCB 0.50),同时把 toxicity 降到最低 **0.0386**;目标2,把 misinformation ratio 从 origin 40% 降到 **24%**(优于 ε-greedy 26%、UCB 30%),初始 20% 用户发布错误信息。
- **可扩展性(Figure 4)**:运行时间随智能体数量近似线性增长(R²=0.9905,r=0.9904),最多测到 1000 个智能体。

## 在本 wiki 中的位置

PolicySim 属于 [[llm-based-agents|LLM 社会模拟]] 与 [[social-simulation]] 方向,定位与 [[oasis|OASIS]]、[[agent4rec|Agent4Rec]]、[[human-behavior-simulation|HiSim]]、[[s3-social-network-simulation|S³]]、[[generative-agents]] 同属社交平台多智能体模拟系统(见论文 Table 1 的对比),其差异在于**显式建模平台干预政策 + 用反馈自适应优化策略**。方法层面把 [[supervised-fine-tuning]]→[[direct-preference-optimization]] 的训练范式从对齐场景迁移到社会智能体训练,并用 [[contextual-bandit]]+消息传递做 [[recommender-system]] 与曝光控制的策略学习,衔接 [[reinforcement-learning]] 在 [[recommender-system]] 的应用。研究主题(去 [[echo-chamber]]、抑制 [[polarization]] 与 misinformation、促进 cross-viewpoint 交互)对应 [[computational-social-science]] 与 [[ai-agent-behavioral-science]]。作者来自 [[zhejiang-university]]、[[fudan-university]]、[[hkust]] 与 MyBank/[[ant-group]]。
