---
type: source
subtype: paper
tags: [recommender-system, user-simulation, implicit-feedback, llm-multi-agent, reinforcement-learning, multimodal, benchmark]
created: 2026-05-29
updated: 2026-05-29
arxiv: 2508.05709
raw: raw/2508.05709.pdf
authors: Boyu Chen, Siran Chen, Zhengrong Yue, Kainan Yan, Chenyun Yu, Beibei Kong, Cheng Lei, Chengxiang Zhuo, Zang Li, Yali Wang
year: 2025
---

G-UBS(Group-aware User Behavior Simulation)提出一个"用户群组管理器 + 用户反馈建模器"双 agent 范式,借助相关用户群组的上下文引导,从含噪的隐式反馈(如快速划走视频)中稳健、深入地推断单个用户偏好,并配套发布了首个多模态隐式反馈视频推荐 benchmark IF-VR。

## 问题

推荐系统依赖用户反馈来优化,但显式反馈(点赞/点踩/评分及其原因)在实践中极其稀缺。更可得的是隐式反馈(快速划走、不点击、低完播率)。然而隐式反馈往往含有大量噪声:用户快速划走某视频可能源于误触、单手操作、环境干扰或个人习惯,而非真正不感兴趣。这种噪声容易误判用户兴趣,损害推荐效果乃至导致用户流失。核心挑战是:在含噪信号下,如何稳健地辨别用户隐式反馈背后的真实成因?现有方法分两类——embedding-based 方法把隐式反馈直接映射为特征,可解释性差、无法揭示不满的原因;LLM-based 方法多局限于纯文本模态,既缺乏跨模态联合感知能力,也未处理个体隐式反馈中的噪声。

## 方法

G-UBS 由两个协作的 LLM-based agent 组成,把群组画像注入到基于 RL 的[[user-simulation]]微调中,用群组级先验来过滤个体隐式反馈中的噪声。属于[[llm-multi-agent]]与[[recommender-system]]结合的[[human-behavior-simulation]]方向。

- **User Group Manager(UGM)**:负责把大规模用户聚成群组并生成群组画像,采用"summarize-cluster-reflect"工作流,支持 1000+ 用户并生成最多 50 个群组画像。
  - Phase 1 Summarize:把含 1000+ 用户的画像集(ID、职业、年龄、性别、视频偏好标签)输入分组 LLM(用 [[deepseek-r1]]),按指定模式(视频偏好或人口属性)输出 k 个群组及各群组的典型用户。
  - Phase 2 Cluster:用相似度把每个用户匹配到典型用户,取与典型用户最相似的 top-60 用户构成初始群组(动态阈值按相似度降序取前 60),再由 profile generator([[gpt-4o]])生成初始群组画像。
  - Phase 3 Reflect:把群组内每个用户的历史观看记录(播放率、标题、时长、点击)输入匹配 LLM(GPT-4o),判定用户兴趣与历史行为是否与初始画像一致,剔除不匹配者(若匹配数 < 10 则不生成该群组画像),最终汇总成精炼的群组画像。
- **User Feedback Modeler(UFM)**:在群组画像引导下解读个体隐式反馈,用 RL 训练。先以 50K 显式不喜欢反馈 + GPT-4o 生成的归因 [[chain-of-thought]] 做 [[supervised-fine-tuning]] 热启动(沿用 DeepSeek-R1 思路),再用 **GA-GRPO(Group-Aware GRPO)** 进行 RL 训练。
  - Profile Sampling:每步采样三类画像——训练用户画像 u_T、其所属的群组画像 P_G(若不属于任何群组则用 u_T 代替)、同群组的相似用户画像 u_S(无相似用户则用 u_T)。UFM 接收采样视频帧 V、标题与观看历史,分别为这三类画像生成响应 o_T、o_S、o_G。
  - Reward 机制:把隐式反馈归因为三类多选题——内容驱动快划(content-driven)、算法驱动快划(algorithm-driven)、用户驱动快划(user-driven)。奖励 R(o)=r_format(格式)+ r_skip(是否正确判断快划)+ r_choice(归因选项是否正确)。
  - GA-GRPO:对来自不同画像的奖励 {R_T, R_S, R_G} 按权重 {W_T, W_S, W_G} 加权,用组内相对优势 A_R=(R−mean)/std 优化策略,并加 KL 散度项约束策略不偏离参考策略(系数 β)。

全流程 LLM 用 Qwen2.5-VL-7B([[qwen2-5-instruct]]系列的视觉版),在 4 张 A100 80G 上对 UFM 做全参数微调,SFT 1 epoch、RFT 200 步,学习率 1e-5,β=0.04。

## 结果

- **IF-VR benchmark**:作者构建的首个面向隐式负反馈归因的多模态视频推荐数据集,源自腾讯视频 App,含 15K 用户画像(性别/年龄/职业等)、25K 视频、933K 交互记录;含 50K 显式"不喜欢"反馈与 72K 由 GPT-4o 标注并经人工核验的隐式反馈归因。涵盖两种模式:序列视频推荐(8000 用户、320K 观看历史)与点击模拟(7000 用户、613K 曝光/点击历史)。Table 1 显示 IF-VR 在 Age/Gender/Job/Interest Tag/Video Data/显式+隐式反馈/负面评论/完播率/点击率/播放率等维度上比 Amazon、Netflix、Yelp、MIND、MovieLens、MicroLens、KuaiRand([[kuairand]])等数据集覆盖更全。
- **SOTA 对比(Table 2)**:G-UBS 在 IF-VR 上 Person Play Rate 52.3%、Total Play Rate 55.3%、Finish Rate 22.1%、Play Rate>30% 为 88.7%、Click Rate 25.7%、Judge F1 54.9%、Judge Acc 72.9%、Reason F1 55.6%、Reason Acc 62.9%,全面超过原始推荐策略、[[sasrec]]、Llama3.3-70b、Qwen-32b、Deepseek-r1、Qwen-2.5VL-7B、Video-R1、Videochat-R1、Doubao-1.5-pro、[[gpt-4o]]。相对最佳 LLM/MLLM 基线:Play Rate>30% 高出约 4.0%、Reasoning Acc 高出约 14.9%;Person Play Rate 从 46.5% 提升到 52.3%,Total Play Rate 从 48.3% 提升到 55.3%。
- **公开数据集用户模拟(Table 3)**:在 [[movielens]] 与 [[amazon-book]] 上,以二分类(喜欢/不喜欢)预测衡量模拟准确率,G-UBS 取得 MovieLens Acc 79.9%/Recall 76.2%/F1 78.2%、Amazon Books Acc 80.1%/Recall 78.9%/F1 80.2%,均优于 [[recagent]]、[[agent4rec]]、GPT-4o 与 SimUser。
- **消融**:群组数 20 最优(Table 4,52.3% Person Play Rate);分组策略上兴趣分组优于人口属性/混合分组(Table 5);聚类方法上 TF-IDF 优于 BERT-Sim 与 K-Means(Table 6);SFT+RL+Group 三者叠加效果最佳(Table 7);多模态视觉信息、reason/skip 奖励、reflection 机制均被证明有效(Tables 8–10);奖励权重 W_T=0.7/W_G=0.15/W_S=0.15 最优(Table 11)。
- **部署效率**:FP16 量化,UGM 8 分钟可分析 1000 用户;UFM 在 4 张 A100 80G 上 QPS 5.3,约每天处理 458K 视频。

## 在本 wiki 中的位置

本文是把 [[llm-multi-agent]] 与 RL 用于[[recommender-system]]中[[user-simulation]]的代表性工作,与 [[recagent]]、[[agent4rec]]、[[agentcf]] 等 LLM 驱动的推荐用户模拟一脉相承,但创新在于:用群组画像作为上下文先验来抑制个体隐式反馈噪声,并把 [[supervised-fine-tuning]] + GRPO([[ppo]]系列的 group-relative 变体)的 RL 训练扩展到多模态视频场景。其归因式建模与 [[chain-of-thought]] 推理相关,benchmark IF-VR 可与 [[kuairand]] 等推荐数据集并置参考。
