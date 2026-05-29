---
type: source
subtype: paper
tags: [offline-rl, recommendation, model-based-rl, matthew-effect, interactive-recommendation]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2307.04571
raw: raw/2307.04571.pdf
authors: [Chongming Gao, Kexin Huang, Jiawei Chen, Yuan Zhang, Biao Li, Peng Jiang, Shiqi Wang, Zhong Zhang, Xiangnan He]
year: 2023
---

本文提出 [[dorl]](Debiased model-based Offline RL),通过在 model-based [[offline-rl]] 的悲观惩罚项上增加一个熵惩罚(entropy penalty),缓解离线 RL 推荐中保守性导致的"马太效应"(Matthew effect),从而提升交互式推荐的用户长期满意度。

## 问题

离线强化学习(offline RL)从历史日志中学习策略而无需与线上环境交互,是交互式推荐(interactive recommendation)等决策场景的理想选择。但 offline RL 面临 value overestimation 问题:函数逼近器对 logged data 未充分覆盖的 state-action pair 外推 Q 值,导致不稳定与发散。现有方法(model-free 如 [[bcq]]/[[cql]],model-based 如 [[mopo]])通过引入保守性(conservatism)缓解,即约束学到的策略贴近 behavior policy 或惩罚 out-of-distribution(OOD)动作。

然而,作者发现把这种保守性直接用到推荐中会引发严重的[[matthew-effect]]——"the rich get richer and the poor get poorer":历史中流行的物品/类别被进一步放大推荐,冷门物品被压制,造成 filter bubble,损害用户满意度。作者在 [[kuairand]] 和 [[lfm-1b]] 数据集上做了实证研究(Empirical Study):随着 repeat rate(重复曝光率)升高,用户的 Day-1 Retention(次日留存)下降;并在 [[kuairec]] 上展示保守性系数 λ 越大,majority category domination(MCD,头部类别占比)越高,即保守性越强,马太效应越强。

## 方法

作者沿用 model-based offline RL 框架 [[mopo]]:学习 user model / world model(reward model)$\widehat{R}$ 模拟用户偏好,并在估计奖励上加惩罚 $\bar r(s,a)=\hat r(s,a)-\lambda p(s,a)$ 得到保守 MDP。核心贡献是重新设计惩罚项 $p(s,a)$:

- **理论分析**:提出 mismatch function $G^\pi_{\widehat M}(s,a)$,将其分解为不确定性项 $d_1(\widehat R,R)$ 与长期满意度偏差项 $d_V(\widehat R,R)$。指出 MOPO 只惩罚不确定性会让模型偏向高频物品、忽略冷门物品,从而加剧马太效应。
- **Entropy Penalizer(熵惩罚)**:对 behavior policy $\pi_\beta(\cdot|s)$ 在状态 $s$ 上的熵进行惩罚 $P_E=-D_{KL}(\pi_\beta(\cdot|s)\|\pi_u(\cdot|s))=\mathcal H(\pi_\beta(\cdot|s))-\log(|\mathcal A|)$,其中 $\pi_u$ 为均匀分布。当某状态下 behavior policy 只推荐少数物品(熵低)时给予大惩罚,间接鼓励指向更多样状态的动作,实现离线数据上的反事实探索(counterfactual exploration)。熵通过 k-order entropy 在所有用户日志的连续子序列上统计估计。
- **最终奖励**:$\bar r(s,a)=\hat r(s,a)-\lambda_1 P_U+\lambda_2 P_E$,其中 $P_U$ 为不确定性惩罚(用 K 个 ensemble reward model 的方差捕获 epistemic uncertainty,用 Gaussian Probabilistic Model 捕获 aleatoric uncertainty)。
- **DORL 框架**:以 [[deepfm]] 为 user model 骨干,用 actor-critic 学习 RL 策略;state tracker $f_\omega(s,a,r)$ 建模状态转移(采用 naive average layer 作为 state encoder)。

## 结果

在两个支持离线 RL 评估的数据集 [[kuairec]] 和 [[kuairand]] 上做交互式推荐实验,以累积奖励 $\sum_t r_t$ 衡量长期满意度,quit 机制为同类别连续 N=4 轮即终止、M=0、最大轮数 30,结果取 100 条交互轨迹平均(Table 2):

- **KuaiRec**:DORL 累积奖励 $R_{tra}=20.494\pm2.671$,显著优于次优 IPS 的 $12.833$、MOPO 的 $11.427$、MBPO 的 $12.043$;交互长度 Length $=26.712$,远超其他方法(MOPO 12.809,IPS 16.727)。
- **KuaiRand**:DORL $R_{tra}=11.850\pm1.036$,优于 MOPO 10.934、MBPO 10.933;Length $=27.609$ 为最高。
- 整体上 model-based 方法(MBPO/IPS/MOPO/DORL)的轨迹长度与累积奖励显著优于 model-free 方法(SQN/CRR/CQL/BCQ),因 model-based RL 更 sample efficient,能在稀疏日志上构造更多交互序列。
- DORL 牺牲了少量 single-round reward($R_{each}$,KuaiRec 0.767)但大幅提升多样性与交互长度,从而最大化长期累积奖励,验证缓解马太效应能提升用户长期体验。

## 在本 wiki 中的位置

本文是 [[offline-rl]] 应用于推荐系统的代表性工作,把 [[mopo]] 的 model-based offline RL 框架与对 [[matthew-effect]] / filter bubble 的处理结合。其 entropy penalty 体现了在无线上反馈下做反事实探索的思路,可与 [[rlhf]]、bandit、其他 offline RL 方法([[bcq]]/[[cql]])对照阅读。代码开源(DORL-codes)。
