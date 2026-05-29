---
type: concept
subtype: method
tags: [retrieval, embedding, recommendation, ranking]
created: 2026-05-29
updated: 2026-05-29
sources: 1
---

# two-tower

双塔模型是一种检索/推荐架构,用两个独立的编码器(塔)分别把用户/查询和物品映射到同一嵌入空间,通过向量相似度(如最近邻搜索)进行高效匹配。

## 在本 wiki 中的出现

- [[2025-gnolr-progressive-implicit-preference]]:提出 GNOLR,用有序标签映射加嵌套优化把多种隐式反馈编码进统一 embedding 空间,既建模用户参与度递进又把多路检索简化为单次最近邻搜索。

## 相关

- [[embedding]]
- [[nearest-neighbor-search]]
- [[implicit-feedback]]
- [[retrieval]]
