# 检查记录索引

[English](README.md) · **简体中文** · [审查指南](../REVIEW.zh-CN.md)

这些报告对应恢复后的 **v1.0.1** WebP，整图哈希用于标识实际审查的文件，报告中的路径相对于仓库根目录。

## 文件与动作测量

| 报告 | 内容 |
| --- | --- |
| [atlas.json](atlas.json) | 图片标识、网格、格子占用、透明度和杂色边缘。 |
| [frames.json](frames.json) | 标准动作帧的几何信息和最终裁剪图。 |
| [continuity.json](continuity.json) | 相邻转头姿态、轮廓连续性和保留的局部提醒。 |
| [chroma-preservation.json](chroma-preservation.json) | 保留原生透明度，不混合邻近颜色。 |
| [pet-quality.json](pet-quality.json) | 最终文件标识、小跳抬升与落地、转头位置。 |

## 画面与方向审查

| 记录 | 内容 |
| --- | --- |
| [direction-semantics.json](direction-semantics.json) | 16 个姿态的预期方向和可见判断依据。 |
| [审查者 A](blind-reviewer-a.json) · [B](blind-reviewer-b.json) · [C](blind-reviewer-c.json) | 揭晓答案前保存的独立 A/B 判断。 |
| [blind-majority.json](blind-majority.json) | 按每张图的严格多数汇总。 |
| [blind-answer-key.json](blind-answer-key.json) | 预期方向和配对关系。 |
| [blind-validation.json](blind-validation.json) | 多数判断与答案的比对结果。 |
| [independent-all-frames.json](independent-all-frames.json) | 全部 73 帧浅深背景的独立画面复查。 |

审查者为 AI。主审查还看过顺序逐帧图、完整循环和原生尺寸的浏览器播放。通过标准和保留问题见[画面检查与限制](../REVIEW.zh-CN.md)。

## 查看图片

[无标签配对图](../../art/repair/v1.0.1) · [浅深背景逐帧图](../../art/repair/v1.0.1/review-boards) · [方向总览](../../previews/directions.png) · [逐帧恢复报告](../outline-restoration.json)
