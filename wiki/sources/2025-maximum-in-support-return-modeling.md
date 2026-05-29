---
type: source
subtype: paper
tags: [reinforcement-learning, recommender-systems, offline-rl, decision-transformer, large-language-models, lora]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2510.12816
raw: raw/2510.12816.pdf
authors: [Xiaocong Chen, Siyu Wang, Lina Yao]
year: 2025
---

# Maximum In-Support Return Modeling for Dynamic Recommendation with Language Model Prior

MDT4Rec 是一个 offline RLRS 框架,在 [[decision-transformer]] 基础上把 trajectory stitching 移到 action inference 阶段以忽略失败历史,并用预训练 [[large-language-models]] 初始化权重、用 [[mlp]] 替代线性 embedding、用 [[lora]] 高效微调,在五个公开数据集与在线模拟器上超越现有方法。

## 问题

基于 [[reinforcement-learning]] 的推荐系统([[rl-based-recsys]],RLRS)适合处理 [[sequential-recommendation]] 这类序列决策任务,但在真实场景中在线训练成本高,因此转向 [[offline-rl]]。Offline RLRS 仍面临两个核心挑战:

1. **从次优历史中学习**:已有的 trajectory stitching 策略(如 [[decision-transformer]] 方向的 EDT4Rec/CDT4Rec)在训练阶段把次优轨迹与相似的优质轨迹拼接,生成近优序列;但人工拼接的转移可能不符合真实用户意图,导致模型预测与实际行为不一致。
2. **表示复杂的 user-item 交互**:现有 RLRS 工作几乎没有专门处理交互表示的复杂性,而 [[large-language-models]] 在传统推荐中已展现出强大的知识迁移与表示能力,但其在 RLRS 中的潜力尚未充分挖掘。

## 方法

推荐被建模为 [[markov-decision-process]],并用 [[off-policy-evaluation]] 式的 offline RL 在静态交互数据集上训练。MDT4Rec 在 [[decision-transformer]](DT,把 offline RL 重述为以 return-to-go 为条件的序列建模)之上有四点创新:

- **Maximum In-Support Return Modeling**:不在训练阶段拼接轨迹,而是在 action inference 阶段动态选择历史长度。引入最大回报估计器 \(\hat R\),通过 [[iql]] 中常用的 expectile regression(\(\alpha=0.99\),逼近回报分布上尾)来近似 \(\max_{\tau_T\in D} R_t(\tau_T)\),从而在每一步选择能产生最大估计回报的历史长度,既能丢弃低回报的失败子序列,又能在轨迹本身已接近最优时保留更长历史。论文给出定理证明 \(\alpha\to1\) 时该估计收敛到数据集内最大 return。
- **Action Inference 的最优历史长度搜索**:测试时对每个候选历史长度 \(i\) 估计最大可达回报 \(\hat R_i\),用 brute-force 搜索易慢,故引入步长参数 \(\delta\)(实验取 \(\delta=2\))加速,把推理时间降低约 \(\delta\) 倍;再用 Bayes 规则从 expert return 分布采样目标回报(inverse temperature \(\kappa=10\))。
- **LLM as Prior**:用 GPT-2 架构(取 HuggingFace 预训练权重)初始化 DT 的 policy backbone,先在 [[t5]] 类似设定下用 WikiText 数据集做 next-token 预训练。
- **MLP embedding + LoRA**:把线性 embedding 投影换成两层 [[mlp]] 以建模异质信号(离散 ID、数值统计、文本 embedding);用 [[lora]] 仅对注意力权重(Q/K/V)做低秩更新,其余 Transformer 权重冻结。训练目标为 \(\mathcal L = \mathcal L_{dt} + \lambda\cdot\mathcal L_{language} + \mathcal L_{max}\),其中语言建模损失作为辅助任务起正则化作用(\(\lambda=0.1\))。

## 结果

在五个 offline 数据集([[coat]]、[[yahoo-r3]]、[[movielens-1m]]、[[kuairec]]、[[kuairand]])及在线模拟器 [[virtual-taobao]] 上评测,环境经 [[easyrl4rec]] 统一为 OpenAI Gym 格式,state encoder 用 [[sasrec]]、LLM 用 GPT-2。指标为累计回报 \(R_{cumu}\)、每步平均回报 \(R_{avg}\) 与轨迹长度 Length。

- **RQ1 总体对比(Table 1)**:MDT4Rec 在全部数据集上取得最高 \(R_{cumu}\) 与 \(R_{avg}\),优于 [[ddpg]]/[[sac]]/[[td3]] 等 actor-critic 方法以及 DT、DT4Rec、CDT4Rec、EDT4Rec 等 transformer baseline。例如 Coat 上 \(R_{cumu}=89.87\)(DT 为 83.49);MovieLens 上 \(R_{cumu}=38.64\)、\(R_{avg}=4.29\);KuaiRec \(R_{cumu}=33.01\);VirtualTB \(R_{cumu}=81.79\)、\(R_{avg}=5.98\)。轨迹长度与最强 baseline 相近,说明优势来自每步更优决策而非靠拉长交互。
- **RQ2 不同 LLM 初始化(Table 2)**:对比 GPT-2 Large、LLaMA 3.2-3B、[[qwen]] 2.5-7B、[[deepseek-r1]]-7B,整体排名不变;两个 7B 模型(Qwen 2.5、DeepSeek-R1)在多数数据集得分最高,DeepSeek-R1 在 VirtualTB 在线模拟器上尤其出色,但用更轻的 backbone 性能不会崩溃。
- **RQ3 消融与微调策略(Table 3/4,Table 1 变体)**:MDT4Rec-LM(去掉 LM prior)与 MDT4Rec-Max(去掉 maximum in-support return modeling)均明显下降。VirtualTB 上 [[lora]] 优于 frozen 与 full finetuning(\(R_{cumu}=81.79\) vs 80.12 vs 77.89);MLP embedding 优于线性投影(81.79 vs 76.46)。
- **RQ4 超参(Figure 2)**:context length \(T=20\) 取得最高累计回报且序列较短;step size \(\delta=2\) 在回报质量与效率间最优;语言辅助损失能降低训练方差、防止 RL 阶段性能退化。

## 在本 wiki 中的位置

本文处于 [[offline-rl]] 与 [[recommender-systems]] 的交叉点,是 [[decision-transformer]] 系列在推荐场景下的延续(承接 CDT4Rec、EDT4Rec、DT4Rec),并把 [[large-language-models]] 作为权重先验引入 [[rl-based-recsys]]。它与 [[sequential-recommendation]]、[[user-retention]] 导向的推荐方法相关,方法上用到 [[iql]] 的 expectile regression、[[lora]] 微调、[[mlp]] 表示,评测依托 [[easyrl4rec]]、[[virtual-taobao]] 与 [[kuairec]]/[[kuairand]] 等数据集。
