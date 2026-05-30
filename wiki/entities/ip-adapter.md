---
type: entity
subtype: method
tags: [diffusion-models, image-generation, adapter, image-prompt, controllable-generation]
created: 2026-05-30
updated: 2026-05-30
arxiv: 2308.06721
raw: raw/2308.06721.pdf
authors: [Hu Ye, Jun Zhang, Sibo Liu, Xiao Han, Wei Yang]
affiliations: [Tencent AI Lab]
---

# IP-Adapter

IP-Adapter(Text Compatible **I**mage **P**rompt Adapter)是一个轻量适配器,让预训练的文生图 [[diffusion-models|扩散模型]]
能接受**图像作为 prompt**(image prompt),无需微调基础模型即可实现"以图生图"风格/主体控制。腾讯 AI Lab,arXiv 2308.06721。

## 核心思想:解耦交叉注意力
关键设计是 **decoupled cross-attention(解耦交叉注意力)**:为图像特征**单独**增加一套 cross-attention 层,与原有的文本 cross-attention
**并行**而非共享,从而把图像 prompt 信息注入扩散过程,又不破坏模型原有的文本对齐能力。适配器参数量很小(约 22M),即插即用。

## 特点
- **不动基模**:冻结原扩散模型,只训练适配器 → 可复用、可迁移到同基座的衍生模型与社区微调权重。
- **文本兼容**:图像 prompt 与文本 prompt 可**同时**使用,实现多条件可控生成。
- **可组合**:与 [[controlnet]]、[[lora]]、[[dreambooth]] 等结构兼容;变体见 [[regional-ip-adapter]](区域化控制)。

## 在本 wiki 中的位置
属于扩散模型的**可控生成 / 适配器**方向,与 [[lora]]、[[dreambooth]]、[[controlnet]]、[[latent-consistency-model]] 等个性化/加速/控制技术相邻。
是本 wiki 图像生成簇(相对 LLM/推荐主线较边缘)的一个常被引用的枢纽方法。
