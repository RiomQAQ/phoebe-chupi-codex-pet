# 头发描线修复

[English](OUTLINE-REPAIR.md) · **简体中文** · [文档目录](README.zh-CN.md)

**已在 v1.0.1 修复。** v1.0.0 导出时的边缘清理把部分深色轮廓改成了附近的金发或白色填色，导致头发描线出现浅色斑段。

## 原因

清理规则把部分半透明描线像素当成杂色，用邻近颜色替换。在保存的清理前单帧上重放这条规则，可以精确复现发布图中的错误像素。本地安装、云端图片和公开 v1.0.0 安装包使用的是同一份受影响图片。

结构校验没有发现颜色丢失。PNG 和 WebP 也能通过一致性检查，因为两者都已经包含了这个错误。

## 修复方式

找回清理前的认可原像素，对齐到已有整图后直接导出无损 WebP。73 格的透明度和位置均与旧版相同，只恢复颜色，眨眼、动作、比例和 Dot 方向布局保持原样。

![v1.0.0 原像素与 v1.0.1 恢复后的像素](../art/repair/v1.0.1/before-after.png)

局部使用最近邻放大，便于观察真实像素。以下三处作为明确的回归用例，格内坐标从 0 开始：

| 帧 | 像素 `(x, y)` | v1.0.0 RGB | 恢复后的 RGB |
| --- | --- | --- | --- |
| `idle/00` | `(37, 180)` | `(100, 95, 74)` | `(0, 0, 0)` |
| `running-right/03` | `(155, 73)` | `(141, 135, 108)` | `(7, 0, 0)` |
| `running-left/07` | `(138, 108)` | `(148, 140, 113)` | `(8, 1, 0)` |

头发内部的金棕色发丝线属于造型的一部分，继续保留原色。

## 检查结果

| 检查 | 结果 |
| --- | --- |
| 原图比对 | 73 格的可见像素均与认可原图一致，无差异。 |
| 颜色恢复 | 恢复 88,948 个可见像素的 RGB。 |
| 深色描线 | 检查 263,885 个源像素，无差异。 |
| 几何位置 | 透明度和帧位置与 v1.0.0 一致。 |
| 画面检查 | 全帧浅深背景、九类循环、小跳衔接和十六方向均已复查，另完成一轮独立全帧审查。 |
| 方向审查 | 3 名独立 AI 审查者，14 组多数判定全部通过。 |
| 回归检查 | 有问题的 v1.0.0 图片不通过，恢复后的图片通过。 |

详细资料包括[逐帧恢复报告](outline-restoration.json)、[检查记录](repair-qa/README.zh-CN.md)、[浅深背景对照](../art/repair/v1.0.1/review-boards)和[当前审查结果](REVIEW.zh-CN.md)。修复对应 [Issue #1](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues/1)。

## 复现修复

```sh
python3 -m pip install -r requirements.txt
python3 scripts/restore_outlines.py --build --report docs/outline-restoration.json
python3 scripts/render_previews.py
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
python3 scripts/package.py
```

`--build` 从固定的[清理前原图](../art/repair/v1.0.1/source-before-cleanup.png)直接导出，不重画、不缩放，也不混合邻近颜色。[v1.0.0 快照](../art/releases/v1.0.0)保留用于对照。

后续导出应保留干净的原生透明度，并对照认可原图检查轮廓颜色。PNG/WebP 一致性用于检查编码，还需要同时通过原图颜色比对和画面审查。
