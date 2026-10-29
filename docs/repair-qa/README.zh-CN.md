# v1.0.1 描线修复检查记录索引（Outline Repair QA）

[English](README.md) · **简体中文** · [审查指南](../REVIEW.zh-CN.md)

本目录保存了 **v1.0.1** 头发深色外描线无损恢复版本的全套自动化测量、浅深双背景复查与三方无标签盲审证据。所有报告均通过整图 SHA-256（`e1971a5c89d073739c4956e04292249385eb47298dd8ce873deb1be6aaf3bdf2`）绑定到实际审查的 [`art/releases/v1.0.1/spritesheet.webp`](../../art/releases/v1.0.1/spritesheet.webp)，报告内的文件路径均相对于仓库根目录。

> **与当前 v1.0.2 的关系**：当前发布的 `v1.0.2` 在前 9 行（共 **57 张标准动作帧**）上 100% 沿用了本目录所验证的 `v1.0.1` RGBA 像素；关于第 9、10 行 Dot 转头姿态的最新修订证据，请一并查阅 [`docs/look-repair-qa/`](../look-repair-qa/README.zh-CN.md)。

---

## 视觉复查图板预览

### 1. 像素级描线恢复对比（v1.0.0 受损浅斑 vs v1.0.1 恢复墨线）

<p align="center">
  <img src="../../art/repair/v1.0.1/before-after.png" width="760" alt="v1.0.0 与 v1.0.1 头发描线像素最近邻放大对比" />
</p>

### 2. v1.0.1 全帧浅深背景与动作总览

<table>
  <tr>
    <td align="center" width="50%">
      <img src="../../art/repair/v1.0.1/contact.png" width="370" alt="v1.0.1 标准动作全帧总览" /><br />
      <sub><b>9 行标准动作（57 帧）</b>：恢复描线后的整图总览</sub>
    </td>
    <td align="center" width="50%">
      <img src="../../art/repair/v1.0.1/directions.png" width="370" alt="v1.0.1 16 向转头总览" /><br />
      <sub><b>v1.0.1 16 向转头历史快照</b>（后于 v1.0.2 进一步重绘优化）</sub>
    </td>
  </tr>
</table>

---

## 文件与动作测量报告

| 报告文件 | 核查内容与关键指标 |
| --- | --- |
| [`atlas.json`](atlas.json) | 整图 SHA-256 标识、`1536 × 2288`（8×11）网格、73 个有效格与 15 个全透明格、透明度边距以及边缘杂色检查。 |
| [`frames.json`](frames.json) | 57 张标准动作帧的几何边界框、中心对齐数据以及与最终裁剪帧的逐像素比对。 |
| [`continuity.json`](continuity.json) | 相邻转头姿态的轮廓连续性测量及当时记录的局部过渡提醒。 |
| [`chroma-preservation.json`](chroma-preservation.json) | 验证直接保留清理前原图的原生透明度与深色描线（恢复 **88,948** 个可见像素 RGB，核对 **263,885** 个深色墨线像素 0 差异）。 |
| [`pet-quality.json`](pet-quality.json) | 最终发布文件校验、坐姿小跳抬升高度（`21 px`）与落地零偏移（`0 px`）、转头中心注册稳定性。 |

---

## 画面与方向盲审记录

<p align="center">
  <img src="../../art/repair/v1.0.1/blind-part-1.png" width="700" alt="v1.0.1 无标签 A/B 方向盲审配对图（第一部分）" />
</p>

| 记录文件 | 内容说明 |
| --- | --- |
| [`direction-semantics.json`](direction-semantics.json) | 全部 16 个转头姿态的预期屏幕朝向与可见解剖/配饰判断依据。 |
| [审查者 A (`blind-reviewer-a.json`)](blind-reviewer-a.json) · [B (`blind-reviewer-b.json`)](blind-reviewer-b.json) · [C (`blind-reviewer-c.json`)](blind-reviewer-c.json) | 在揭晓答案表之前保存的三份独立无标签 `A / B` 视线方向判断。 |
| [`blind-majority.json`](blind-majority.json) | 按每张图的严格多数（至少 2/3 一致）汇总的盲审结果。 |
| [`blind-answer-key.json`](blind-answer-key.json) | 14 组盲测配对图的真实角度与预期方向映射表。 |
| [`blind-validation.json`](blind-validation.json) | 严格多数判断与标准答案表的自动比对结果（**14 / 14 全部通过**）。 |
| [`independent-all-frames.json`](independent-all-frames.json) | 针对全部 73 个有效格在浅色与深色双背景下的独立全帧画面复查报告。 |

三名盲审审查者均为相互隔离的 AI Agent；主审查同时核对了顺序逐帧图板、完整 GIF 循环以及原生 `192 × 208` 尺寸下的浏览器播放。完整的通过标准与已知特性见[审查与校验指南](../REVIEW.zh-CN.md)。

---

## 快速访问归档图板

- **无标签盲测配对图**：[`art/repair/v1.0.1/`](../../art/repair/v1.0.1)（含 `blind-part-1.png`、`blind-part-2.png`、`blind-part-3.png`）
- **11 行浅/深双背景逐帧复查图板**：[`art/repair/v1.0.1/review-boards/`](../../art/repair/v1.0.1/review-boards)（`row-00.png` 至 `row-10.png`）
- **当前方向总览图**：[`previews/directions.png`](../../previews/directions.png)
- **逐帧像素恢复统计 JSON**：[`docs/outline-restoration.json`](../outline-restoration.json)
- **技术复盘文档**：[头发描线修复复盘（v1.0.1）](../OUTLINE-REPAIR.zh-CN.md)
