---
type: source
subtype: paper
tags:
  - recommender-system
  - causal-inference
  - debiasing
  - instrumental-variable
  - latent-confounder
created: 2026-05-29
updated: 2026-05-29
arxiv: 2410.12451
raw: raw/2410.12451.pdf
authors:
  - Jianfeng Deng
  - Qingfeng Chen
  - Debo Cheng
  - Jiuyong Li
  - Lin Liu
  - Xiaojing Du
year: 2024
---

IViDR 是一种推荐系统去偏方法,联合使用 [[inverse-propensity-score|工具变量(IV)]] 与 [[ivae|identifiable VAE(iVAE)]],同时缓解推荐数据中两类潜在混淆偏差(dual latent confounding biases):item 与 user feedback 之间、以及 item exposure 与 user feedback 之间的潜在混淆。

## 问题

[[recommender-system]] 普遍受到 [[confounding-bias]] 的困扰,尤其是当存在影响 item 与 user feedback 两侧的 [[deconfounder|潜在混淆变量(latent confounder)]] 时。已有的 [[debiasing]] 方法大多只处理单一类型的潜在混淆:

- [[deconfounder|Deconfounder]]、HCR、[[iDCF]] 等方法依赖历史数据近似潜在混淆,或借助 [[proximal-causal-inference|proximal causal inference]] 进行 [[identifiability|可识别]] 估计;但当某些潜在混淆缺乏可靠的 proxy variable(代理变量)时,这类方法难以直接从交互数据推断它们。iDCF 主要聚焦于**有 proxy variable 的潜在混淆(论文记为 C)**。
- [[inverse-propensity-score|IV4Rec / IV4Rec+]] 利用预定义工具变量分解输入向量,处理 item 与 user feedback 之间的潜在混淆;但它们直接修改输入向量、缺乏 [[identifiability|identification guarantee]],且忽视了 item exposure 与 user feedback 之间的潜在混淆(论文记为 **B**)。

把 IV4Rec 与 iDCF 简单组合仍无法在学到的表示上获得可识别性。作者指出:目前缺少一个同时处理两类潜在混淆(dual latent confounding biases)的实用方案。

## 方法

作者提出 **IViDR**(Instrumental Variables-based identifiable Disentangled Debiased learning in Recommendation),核心思想是用 [[inverse-propensity-score|IV]] 解决一类潜在混淆,再用 [[ivae|iVAE]] 解决另一类。

设定上采用 [[potential-outcome-framework|potential outcomes framework]] 与因果 DAG:Z=用户特征 embedding(作为 IV)、T=treatment(target item 及已交互 item 的 embedding)、A=exposure 向量、R=user feedback、W=proxy variable、C=有 proxy 的潜在混淆、B=无 proxy 的潜在混淆。

1. **Treatment reconstruction(基于 IV 的 2SLS)**:把用户特征 embedding **Z 作为有效 IV**(论文给出 Theorem 1 论证其满足 IV 的三个条件),用 [[inverse-propensity-score|two-stage least squares(2SLS)]] 重构 treatment。先做 treatment decomposition,用最小二乘的闭式解把 T 回归到拟合部分 T̂(解释用户偏好)与残差部分 T̃(其他交互因素),再用两个 MLP 估计权重 α¹、α² 把二者组合成重构后的 T^re,使其不受 exposure 与 feedback 间潜在混淆 **B** 的影响。

2. **Interaction data reconstruction**:用 X^re = X + T^re 得到去偏交互数据,作为 iVAE 的输入。

3. **Learning latent confounder C via iVAE**:借助 proxy variable W(如消费商品的平均价格)、交互数据与去偏交互数据,用 [[ivae|iVAE]] 推断可识别的潜在混淆表示 C(分别采样 C1、C2 并融合 C = ρ·C1 + τ·C2)。作者证明了所学表示 C 的 [[identifiability|可识别性]](Theorem 2),并给出使用 IV 的合理性证明(Theorem 1)。

4. **推荐模型**:IViDR 是通用框架,可接任意推荐模型;实验以 [[matrix-factorization|Matrix Factorisation(MF)]] 为骨干。最终损失结合 iVAE 损失与 MF 的 point-wise 损失,使用 [[binary cross-entropy|BCE]] loss。

## 结果

在三个真实数据集 [[coat|Coat]](290 用户 / 300 item)、[[yahoo-r3|Yahoo!R3]](5,400 / 1,000)、[[kuairand|KuaiRand]](23,533 / 6,712)上评估,指标为 RECALL@5 与 NDCG@5,各跑 10 次取均值±方差;骨干为 PyTorch + Adam,treatment/feature embedding 维度在 Coat/Yahoo!R3/KuaiRand 上分别为 32/96/128。

- **整体性能(Table 3)**:IViDR 在全部数据集与全部指标上均为最佳。NDCG@5:Coat 0.5903、Yahoo!R3 0.6602、KuaiRand 0.4161;RECALL@5:Coat 0.5783、Yahoo!R3 0.7901、KuaiRand 0.3549。第二名普遍是 [[iDCF]](如 KuaiRand NDCG@5 0.4080、RECALL@5 0.3481)。t-test p 值显示提升具统计显著性(如 KuaiRand NDCG@5 的 p=5e-20)。对比 baseline 包括 [[matrix-factorization|MF]]/MF-WF、[[inverse-propensity-score|IPS]]/RD-IPS、InvPref、DDCF-MF、[[inverse-propensity-score|IV4R-MF]]、[[iDCF]]。
- **消融(Table 4)**:完整 IViDR 优于只加原始 treatment 的 IViDR-T、只加拟合部分的 IViDR-F、只加残差部分的 IViDR-R,验证 treatment reconstruction 各组件的作用。
- **潜在混淆可识别性(Table 5)**:在合成数据上用 mean correlation coefficient(MCC)评估估计的潜在混淆与真值的吻合度。随 exposure 噪声权重 γ 增大,IViDR 始终优于 iDCF(例如 γ=0.0 时 0.8405 vs 0.8162;γ=20.0 时 0.6262 vs 0.4264),且 t-SNE 可视化显示 IViDR 估计的混淆聚类结构更接近 ground truth。

**局限**:依赖 IV 假设与 proxy variable 的存在;用户偏好、特征、推荐机制间关系复杂,难以验证假设、确保合适的 IV 与 proxy 可得,效果也取决于这些变量的质量与相关性。

## 在本 wiki 中的位置

本文属于**因果推荐 / 推荐去偏**方向,把 [[causal-inference]] 中的 [[inverse-propensity-score|工具变量]] 与 [[ivae|可识别 VAE]] 结合用于 [[recommender-system]] 去偏。它直接延续并对比 [[iDCF]](proxy-based [[proximal-causal-inference]])与 IV4Rec 系列([[inverse-propensity-score]] 分解),其创新点是**同时**处理两类 [[deconfounder|潜在混淆]]。相关概念可参见 [[confounding-bias]]、[[selection-bias]]、[[debiasing]]、[[identifiability]]、[[potential-outcome-framework]]、[[matrix-factorization]]。
