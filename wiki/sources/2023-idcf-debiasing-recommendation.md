---
type: source
subtype: paper
tags: [recommendation, causal-inference, debiasing, confounder, identifiability, proximal-causal-inference, ivae]
created: 2026-05-29
updated: 2026-05-29
arxiv: "2302.05052"
raw: raw/2302.05052.pdf
authors: [Qing Zhang, Xiaoying Zhang, Yang Liu, Hongning Wang, Min Gao, Jiheng Zhang, Ruocheng Guo]
year: 2023
---

# Debiasing Recommendation by Learning Identifiable Latent Confounders (iDCF)

提出 iDCF(identifiable deconfounder),借助代理变量(用户特征)与[[proximal-causal-inference|近端因果推断]],在存在未观测混杂变量时为推荐系统的反事实反馈提供可识别性的理论保证,并在真实与合成数据上优于现有去混杂方法。

## 问题

推荐系统的目标是预测用户对尚未曝光物品的反馈,即把曝光看作 treatment、把反馈看作 potential outcome 的因果问题。难点在于**混杂偏差(confounding bias)**:存在同时影响"用户曝光"和"用户反馈"的未观测变量(如用户的社会经济地位)。例如电商中高社会经济地位用户更易被曝光于高价商品,又因标准更高而倾向给出负反馈,模型会学到"贵的商品更易得到负反馈"这一虚假关联。

已有方法分两类:(1) 对未观测混杂做强假设(如 RD-IPS 假设有界混杂影响、InvPref 假设若干抽象环境),但缺乏对潜在结果的可识别性理论保证;(2) 依赖工具变量/中介变量做经典因果推断,但在推荐数据中难以收集满足条件的此类变量。代表性的 [[deconfounder|Deconfounder]](DCF)无需额外辅助变量,从曝光向量学一个替代混杂变量并套用 g-formula,但存在固有的**非可识别(non-identification)**问题:即便替代混杂变量可唯一确定,$p(r^a_{ui})$ 仍可能落在一个区间内取不同值,导致预测不一致。论文用一个二值例子给出:当 $\pi_{\hat z=1}=0.5,\ \pi_{\hat z=1|a}=0.2,\ \pi_{r=1|a}=0.6$ 时,$p(r^a_{ui})$ 的可行区间为 $[0.33, 0.78]$,在阈值 0.5 下会给出自相矛盾的偏好预测。

## 方法

把去偏推荐建模为**多 treatment** 的因果推断问题,引入一个**代理变量(proxy variable)** $w_u$(用户特征,如最近购买物品的平均价格代表消费水平),它由未观测混杂 $z_u$ 决定且在给定 $z_u, a_u$ 时与反馈独立。引入代理变量后,约束方程从 3 个增至 4 个,从而使 $p(r^a_{ui})$ 唯一可解(Lemma 4.2)。

iDCF 是一个 feedback-model-agnostic 的两阶段框架:
- **学习潜在混杂变量**:用 [[ivae|iVAE]](identifiable VAE)从代理变量 $w_u$ 重构曝光向量 $a_u$,学到后验 $q_\phi(\hat z_u|a_u, w_u)$。先验取 $p_\theta(\hat z_u|w_u)=N(\mu_w, v_w)$,后验取 $N(\mu_{aw}, v_{aw})$,由 4 个 MLP 建模;通过最大化 ELBO(其中 KL 项是两高斯之间的散度,重构项用 factorized logistic / 负二元交叉熵)训练。iVAE 的可识别性保证学到的 $\hat z_u$ 与真实 $z_u$ 在某种变换下等价。
- **给定潜在混杂预测反馈**:用点式推荐模型 $f(u,i,\hat z_u;\eta)=f_1(u,i)+f_2(\hat z_u,i)$ 拟合观测反馈,分离用户内在偏好与混杂效应。
- **推理阶段**:由于用户特征 $w_u$ 在训练/测试集不变,对学到的混杂后验取期望(adjustment),得到去混杂的反馈 $p(r^a_{ui}|w_u)=E_{\hat z_u|w_u}[p(r_{ui}|a,\hat z_u)]$。

Theorem 4.3 在 consistency、ignorability、positivity、exclusion restriction、equivalence、completeness 假设下,给出潜在结果分布的可识别性保证。

## 结果

**基线**:MF、MF-WF、IPS、RD-IPS、InvPref、[[deconfounder|DCF]]、DeepDCF-MF、iDCF-W(不使用代理变量的消融版)。
**数据集**(均含偏差训练集 + 随机试验得到的无偏测试集):Coat(290 用户/300 物品)、Yahoo!R3(5,400/1,000)、KuaiRand(23,533/6,712);指标 NDCG@5、Recall@5。

- **真实数据(Table 2)**:iDCF 在三个数据集所有指标上一致超过最佳基线,且 t 检验 p 值很低。NDCG@5:Coat 0.5744、Yahoo!R3 0.6455、KuaiRand 0.4093;Recall@5:Coat 0.5504、Yahoo!R3 0.7837、KuaiRand 0.3513。对应 p 值如 Coat 7e-4 / 2e-2、Yahoo!R3 2e-3 / 1e-4、KuaiRand 5e-3 / 1e-4。
- 在 Coat 上,DeepDCF-MF、iDCF-W、DCF 表现较差,凸显可识别性的重要——它们与 iDCF 用相同输入和相近的 MF 反馈模型,但 iDCF 全面胜出。
- **合成数据(Table 3,RQ2/RQ3)**:在已知真实混杂的合成数据上,iDCF 在所有设置中优于基线且标准差小;随混杂强度 $\beta$ 增大,iDCF 与最佳基线的差距更显著。在曝光高度稀疏(小 $\alpha$)时 iDCF 更鲁棒,而 iDCF-W、DeepDCF-MF 退化严重。可视化(Figure 5)显示 iDCF 学到的潜在混杂比 iDCF-W 更接近真实混杂,验证了可识别性带来的收益。

代码开源:https://github.com/BgmLover/iDCF

## 在本 wiki 中的位置

本文属于 [[causal-inference|因果推断]] 在 [[recommender-systems|推荐系统]] [[debiasing|去偏]] 方向的工作,核心贡献是把 [[proximal-causal-inference|近端因果推断]] 引入多 treatment 推荐场景以解决 [[deconfounder|Deconfounder]] 的非可识别问题,并用 [[ivae|iVAE]] 实现潜在混杂的可识别学习。它与基于倾向得分([[inverse-propensity-scoring|IPS]])和不变学习([[invariant-learning|invariant learning]])的去偏路线互补,关键差异在于提供了对反事实反馈的**可识别性理论保证**。出自 [[bytedance-research|ByteDance Research]] 等机构,发表于 KDD '23。本文与 LLM 的直接关联较弱,主要价值在于因果去偏与隐变量可识别性方法论。
