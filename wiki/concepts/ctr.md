---
type: concept
subtype: method
tags: [推荐系统, 排序, CTR, 点击率预估]
created: 2026-05-29
updated: 2026-05-29
sources: 10
---

# CTR Prediction

点击率预估(Click-Through Rate Prediction)指在给定用户、物品与上下文特征的情况下,预测用户对某次曝光内容发生点击行为的概率,是推荐系统与在线广告排序的核心任务。

## 在本 wiki 中的出现

- [[2024-eeg-svrec-eeg-affective-engagement-dataset]]:首个在真实短视频观看场景下采集 EEG 脑电信号并配以六维情感参与度标注(MAES)与行为日志的推荐数据集,benchmark 显示加入 EEG 特征可提升推荐 AUC。
- [[2024-diit-domain-invariant-information-transfer]]:DIIT 通过 gating 域级聚合 + 对抗表示对齐双抽取器和 multi-spot 知识蒸馏迁移器,把多个 source domain 模型的 domain-invariant 信息注入 target domain 模型,实现推理只需 target 模型的高效工业跨域推荐。
- [[2026-pdqubo-quantum-feature-selection]]:PDQUBO 用反事实分析量化单特征与特征对的推荐性能影响,构造性能驱动的 QUBO 系数矩阵,在量子退火器上做模型无关、指标无关的推荐系统特征选择。
- [[2024-bi-level-user-modeling-deep-recommenders]]:GPRec 提出即插即用的双层用户建模:用可学习分类器与双向(正/负)群体嵌入做群体建模,从 ID 类特征提炼个体偏好并以正交损失解耦,在 ML1M/TenRec/KuaiRand 上稳定提升各类 DRS 主干的 CTR 预测。
- [[2025-self-surrogate-light-feature-selection]]:提出 SELF,用多个 LLM 的世界知识对特征做语义排序、再以轻量 bridge network 融合任务信号,缓解深度推荐系统特征选择对 surrogate model 的依赖。
- [[2026-hesitation-and-tolerance-in-recommender-systems]]:提出并验证推荐系统中介于接受与拒绝之间的 hesitation(犹豫)与 tolerance(容忍)两种中间交互状态,通过问卷、离线日志与线上 A/B 实验论证容忍侵蚀用户留存,并主张将其作为弱正/负信号重新建模。
- [[2024-scenario-wise-rec]]:首个面向多场景推荐(MSR)的开源 benchmark,整合 6 个公开数据集、12 个基线模型与统一的数据处理/训练/评测流水线,并在工业广告数据集上验证。
- [[2025-xmtf-formula-free-multi-task-fusion]]:xMTF 用可学习的单调融合单元(MFC)替代多任务融合中的预定义公式,配合 RL 外层 + 监督内层的两阶段混合训练,离线 Total Watch Time 1279.7s 超越全部基线,线上 Daily Watch Time +0.833%,Kuaishou 全量部署服务超 1 亿用户。
- [[2025-deep-interest-life-cycle-network]]:提出 DILN,显式建模用户兴趣生命周期(emergent/stable/declining)并用 VQ 聚类离散化、注入 MMOE 排序模型,Lofter 线上 CTR +0.38%、CVR +1.04%、时长 +0.25%。
- [[2025-gnolr-progressive-implicit-preference]]:提出 GNOLR,用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进又把多路检索简化为单次最近邻搜索。

## 相关

- [[recommendation-system]]
- [[short-video-recommendation]]
- [[affective-engagement]]
- [[eeg-signal]]
- [[learning-to-rank]]
