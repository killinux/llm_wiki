---
type: source
subtype: paper
tags: [recommender-system, debiasing, causal-inference, deconfounding, latent-confounder, variational-autoencoder, identifiability, counterfactual-reasoning]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2505.16708
raw: raw/2505.16708.pdf
authors: [Jianfeng Deng, Qingfeng Chen, Debo Cheng, Jiuyong Li, Lin Liu, Shichao Zhang]
year: 2025
---

# A Novel Generative Model with Causality Constraint for Mitigating Biases in Recommender Systems (LCDR)

提出 LCDR:用一个 identifiable VAE([[ivae]])作为因果约束,去对齐标准 [[variational-autoencoder]] 学到的潜在表征,即使代理变量(proxy variable)质量低/有噪声也能有效恢复潜在混杂因子([[deconfounder]]),从而缓解 [[recommender-systems|recommender-system]] 中的偏差。

## 问题

准确预测反事实的用户反馈([[counterfactual-reasoning]])对构建有效的 [[recommender-systems|recommender-system]] 至关重要。但 latent confounding bias(潜在混杂偏差)会遮蔽用户反馈与物品曝光(item exposure)之间真实的因果关系([[causal-inference]]),最终损害推荐性能。传统相关性方法([[matrix-factorization]]、[[fm]]、[[deepfm]]、DCN、DIN、[[lightgcn]] 等)依赖统计相关性,会引入 popularity bias、[[selection-bias]]、conformity bias 等估计偏差。

已有的因果去偏方法([[debiasing]]/[[deconfounding]])通常依赖很强、现实中难以满足的假设:

- 需要工具变量(instrumental variable,如 [[invariant-learning]] 风格的 IV4Rec)或 [[inverse-propensity-scoring]](IPS)、[[backdoor-adjustment]] 等;
- 或假设 latent confounder 与 proxy variable 之间高度相关(如 [[idcf]]),才能实现可识别建模([[identifiability]])。

而现实中 proxy variable 往往质量低、有噪声,使这些理想假设失效,限制了方法的适用性。论文要解决的核心问题:如何从**低质量** proxy variable 与 item exposure 中,可靠地推断潜在混杂因子 $Z_{lc}$,进而估计 $P(r_{ui} \mid a_{ui}, Z_{lc})$ 并去偏。

## 方法

LCDR(Latent Causality Constraints for Debiasing representation learning in Recommender systems),基于 [[potential-outcome-framework]],核心是**用 iVAE 的可识别潜在因果表征去间接约束标准 VAE 的表征**,分两步:

- **第一步:学习潜在因果约束表征 $Z_{lc}$。** 用 [[ivae]] 从 proxy variable $W$ 与曝光 $A$ 推断可识别的潜在因果表征 $Z$;同时用一个标准 [[variational-autoencoder]](文中称 LCVAE,仅以 $A$ 为输入、不需要 proxy)学习表征 $Z_{lc}$。通过统一的损失函数(ELBO 加一项对齐项 $-\lambda \lVert Z_{lc}-Z\rVert_2$,即 $L_2$ 范数对齐)让 $Z_{lc}$ 向 $Z$ 对齐,从而即使 proxy 噪声大也能把因果信息注入 $Z_{lc}$。iVAE 与 LCVAE 并行训练。论文给出 $\lambda$ 取值:Coat 0.9、Yahoo!R3 0.1、KuaiRand 0.9。
- **第二步:训练推荐模型。** 把 $Z_{lc}$ 输入推荐模型;为便于比较采用 [[matrix-factorization]](MF)作 backbone,用一个简单的加性 point-wise 模型 $f(u,i,Z_{lc};\eta)=L_{LCVAE}+L_{MF}$ 估计 $p(r_{ui}\mid A, Z_{lc})$。

理论上,论文证明了 iVAE 组件学到的潜在因果表征 $Z$ 在指数族条件分布与若干正则条件(噪声特征函数零测集、$f$ 单射、充分统计量线性无关、$\lambda$ 矩阵可逆)下是可识别的([[identifiability]],Theorem 1)。相比 [[idcf]],LCDR 即使没有辅助 proxy 变量也能工作,对 proxy 缺失/低质量更鲁棒,且并行架构使额外开销可控。

## 结果

在三个真实数据集上评测,指标为 NDCG@5 与 RECALL@5(K=5,各方法跑 10 次取均值±标准差):

- 数据集规模([[coat]]:290 用户/300 物品;[[yahoo-r3]]:5,400 用户/1,000 歌曲;[[kuairand]]:23,533 用户/6,712 视频)。沿用 [[idcf]] 设置:全部 biased data 训练,30% unbiased data 验证,其余 unbiased data 测试。
- **LCDR 在所有三个数据集、两个指标上均为最优(boldface)**:
  - Coat:NDCG@5 = 0.5973,RECALL@5 = 0.5878(次优 Mulfact-IPS 0.5646 / 0.5511,iDCF 0.5643 / 0.5498)。
  - Yahoo!R3:NDCG@5 = 0.6631,RECALL@5 = 0.7928(次优 iDCF 0.6421 / 0.7806)。
  - KuaiRand:NDCG@5 = 0.4176,RECALL@5 = 0.3575(次优 VAE-iVAE 0.4092 / iDCF 0.3485)。
- 与各数据集最优基线相比的 t-test p-value 均极小(如 KuaiRand NDCG@5 为 5e-15、RECALL@5 为 1e-12),提升具统计显著性。
- 对比方法包括 MF/MF-WF、IPS、RD-IPS、DR-JL([[doubly-robust]])、RD-DR、InvPref、IV4R-MF、[[idcf]]、DDCF-MF、AKBDR-Gau、Mulfact-IPS,以及消融基线 VAE-iVAE(简单组合 VAE 与 iVAE 表征)。LCDR 优于 VAE-iVAE,说明"对齐约束"优于"简单拼接"(RQ2)。
- 观察:Mulfact-IPS 在小数据集(Coat)尚可但在大数据集(KuaiRand)显著下滑(其无潜在混杂假设难成立);iDCF 因依赖"潜变量与 proxy 高相关"的理想假设在三个数据集上均逊于 LCDR。

## 在本 wiki 中的位置

本文属于 [[recommender-systems|recommender-system]] 的 [[causal-inference]] / [[deconfounding]] 去偏分支,核心贡献是用 [[ivae]] 的 [[identifiability]] 作为因果约束来增强标准 [[variational-autoencoder]] 的表征学习,处理低质量 proxy 下的 latent confounder 恢复。它直接对标并改进 [[idcf]](2023-idcf-debiasing-recommendation),与本 wiki 中 [[debiasing]]、[[selection-bias]]、[[inverse-propensity-scoring]]、[[backdoor-adjustment]]、[[doubly-robust]]、[[counterfactual-reasoning]]、[[potential-outcome-framework]] 等节点紧密相连,数据集层面关联 [[coat]]、[[yahoo-r3]]、[[kuairand]]。作者来自 Guangxi University、University of South Australia 与 Guangxi Normal University。
