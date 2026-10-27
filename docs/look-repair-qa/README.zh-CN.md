# 转头修订检查记录

[English](README.md) · **简体中文** · [检查指南](../REVIEW.zh-CN.md)

v1.0.2 调整了左看、低头和相邻的转头画面。头部转回正面时，脸颊保持紧凑；向上看时，也收回了眼睛下方多出的脸部空间。原来的眨眼和九类动作共 57 帧，与 v1.0.1 的 RGBA 像素完全一致。

本次检查的 WebP，其 SHA-256 为 `c00941ef64ce87b76b60f84da2f5dd0045147ad82017cccf349d2a21330106c6`。[审核源图](../../art/approved/v1.0.2/spritesheet.png)、[源帧映射](../../art/repair/v1.0.2/source-map.json)和[像素保护记录](../../art/approved-runtime.json)将完整画面与发布文件对应起来。

## 检查内容

| 记录 | 用途 |
| --- | --- |
| [方向观察](direction-semantics.json) | 记录十六个方向中，头部、脸颊、眼睛与俯仰的可见线索。 |
| [独立画面复查](independent-final-art-review.json) | 单独检查整套转头，以及浅色、深色背景上的重点衔接。 |
| [浏览器复查](ui-visual-review.json) | 按原生尺寸正反向逐帧查看，并抽样检查运行中的循环。 |
| [脸部对照](face-continuity-before-after.json) | 用相同坐标和阈值，对照最后六处脸型修正。 |
| [动作保护](protected-standard-rows.json) | 核对九行动作的 RGBA 像素完全一致。 |
| [图集校验](atlas-validation.json) · [帧检查](standard-frame-review.json) | 检查网格、有效帧、透明度、连通区域和画面边界。 |
| [连贯性](look-continuity.json) · [质量检查](pet-quality.json) | 检查相邻轮廓变化、头部定位，以及小跳的起落。 |
| [原生透明度](chroma-native-alpha.json) | 确认没有用邻近颜色平均处理描线，也没有改变生成画面的透明度。 |
| [源图归档](archive-verification.json) | 核对源图哈希、像素保留、元数据清理和选定源帧的收录情况。 |

[原生尺寸对照板](../../art/repair/v1.0.2/review-boards)展示了低头和左上方的衔接。可以同时查看[方向循环](../../previews/look-loop.gif)、[深色循环](../../previews/look-dark.gif)和[精确 PNG 帧](../../art/frames/look)。测量用于辅助观察，单看脸部边界框，无法分辨正常转头和不应有的缩放。

## 方向盲审

三位互相隔离的 AI 审查员，在看到答案前，分别判断随机排列、没有方向标签的 A/B 画面。十四组严格多数结果全部通过。

[审查员 A](blind-review-a.json) · [审查员 B](blind-review-b.json) · [审查员 C](blind-review-c.json) · [多数结果](blind-majority.json) · [答案映射](blind-axis-answer-key.json) · [校验](blind-validation.json)

## 仍需了解的表现

宠物使用十六张离散的转头画面。`225 → 247.5` 的侧转和 `270 → 292.5` 的抬头，仍比紧邻的几步更明显。修订后的左上方画面已对照固定的电脑和身体，检查此前反馈的脸部突然放大问题。浏览器播放通过连续截图取样和暂停逐帧查看；本次修订尚未安装到原生 Dot。Windows 的视觉验证也尚未进行。

之前的 [v1.0.1 检查记录](../repair-qa/README.zh-CN.md)和[版本快照](../../art/releases/v1.0.1)继续保留，便于对照。
