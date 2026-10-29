# 头发描线修复复盘（v1.0.1）

[English](OUTLINE-REPAIR.md) · **简体中文** · [文档目录](README.zh-CN.md)

> **状态：已在 v1.0.1 彻底修复，并由单元测试与 `validate.py` 永久守卫。**
>
> 在 `v1.0.0` 首次导出时，一条旨在清理透明边缘杂色的后处理规则，误把部分**半透明深色外轮廓像素**当成“颜色溢出（Color Spill）”，用邻近的浅金发色或白帽填色替换了它们的 RGB 值，导致菲比啾比的头发外描线在特定背景下出现断续的浅色斑段。

---

## 1. 故障机理：为什么深色描线会变浅，且自动校验没报错？

在 2D 透明精灵图中，角色外轮廓与透明背景交界处有一圈 `0 < Alpha < 255` 的半透明抗锯齿像素。`v1.0.0` 导出管线在生成 PNG 与 WebP 之前运行了一步边缘清理，其失误链路如下：

```text
[清理前认可原图 (source-before-cleanup.png)]
  外轮廓抗锯齿像素：RGB = (0, 0, 0) 纯黑描线, Alpha = 140（半透明）
         │
         ▼  ❌ v1.0.0 边缘清理规则误判：
            把“半透明深色外描线”当成边缘杂色，取邻近不透明浅金发像素做平均
         │
[受污染的导出图 (v1.0.0 PNG & WebP)]
  同一坐标像素变为：RGB = (100, 95, 74) 浅灰黄, Alpha = 140（透明度未变！）
         │
         ├─► 结构校验（检查尺寸/边距/Alpha 非零边界） ──► 通过（因为 Alpha 没变）
         └─► 编码一致性校验（比对 PNG 与 WebP 像素）  ──► 通过（因为两者带有同一个错误！）
```

- **精确复现验证**：在保存完好的清理前原图（[`art/repair/v1.0.1/source-before-cleanup.png`](../art/repair/v1.0.1/source-before-cleanup.png)）上重放当时的清理规则，可以逐字节 100% 复现 `v1.0.0` 发布包中的受损像素。
- **影响范围**：当时的本地安装、云端导入副本和公开 `v1.0.0` 压缩包使用的是同一份受影响图片。

---

## 2. 无损修复方案与像素级取证

因为问题只出在导出前的最后一步边缘色彩平均，而清理前的认可原画完好无损，所以 `v1.0.1` 的修复不需要重新让 AI 画图或做任何模糊涂抹：

1. **找回清理前原像素**：直接读取冻结的 [`art/repair/v1.0.1/source-before-cleanup.png`](../art/repair/v1.0.1/source-before-cleanup.png)。
2. **保持 Alpha 与几何位置 100% 不变**：73 个有效格的 Alpha 通道、角色位置、待机眨眼、9 类动作比例和 Dot 16 向布局与 `v1.0.0` 完全一致，**只恢复被冲淡的 RGB 颜色**。
3. **保护内部金棕发丝线**：头发内部的金棕色发丝线属于原本的角色设计，原样保留，仅恢复外侧深色轮廓。

<p align="center">
  <img src="../art/repair/v1.0.1/before-after.png" width="760" alt="v1.0.0 受损描线像素与 v1.0.1 恢复后像素的最近邻放大对比" />
</p>

上图局部采用**最近邻无插值放大（Nearest-Neighbor Zoom）**，以便直接观察真实像素颗粒。以下三处典型坐标（格内左上角从 `(0, 0)` 开始计数）已被写入 `tests/` 作为永久回归测试用例：

| 所在帧 | 格内像素坐标 `(x, y)` | v1.0.0 受损 RGB（被浅金发冲淡） | v1.0.1 恢复后 RGB（原画深色墨线） |
| --- | :---: | :---: | :---: |
| `idle/00` | `(37, 180)` | `(100, 95, 74)` | `(0, 0, 0)` |
| `running-right/03` | `(155, 73)` | `(141, 135, 108)` | `(7, 0, 0)` |
| `running-left/07` | `(138, 108)` | `(148, 140, 113)` | `(8, 1, 0)` |

---

## 3. 修复验证结果

<p align="center">
  <img src="../art/repair/v1.0.1/review-boards/row-00.png" width="760" alt="v1.0.1 第 0 行（idle）浅色与深色双背景逐帧复查图板" />
</p>

| 检查维度 | v1.0.1 验证结果 |
| --- | --- |
| **原图逐像素比对** | 全部 **73 个有效格**的可见像素均与清理前认可原图 100% 一致，**0 差异**。 |
| **可见色彩恢复** | 共精确恢复 **88,948 个可见像素**的 RGB 值。 |
| **深色描线保护** | 核查全部 **263,885 个深色描线源像素**，**0 差异**。 |
| **几何与透明度** | Alpha 通道与姿态坐标与 `v1.0.0` 完全一致，无任何位移或缩放。 |
| **浅深背景全帧复查** | 73 帧浅/深双背景、9 类动作循环、小跳衔接和 16 向转头全部复查通过，并完成一轮独立全帧审查。 |
| **三方方向盲审** | 3 名独立 AI 审查员完成无标签 A/B 盲测，14 组多数判定全部通过。 |
| **负向与正向回归测试** | 单元测试确保受损的 `v1.0.0` 整图必定被拦截报错，而恢复后的整图顺利通过。 |

相关证据链文件：
- 机器可读逐帧恢复统计：[`docs/outline-restoration.json`](outline-restoration.json)
- `v1.0.1` 完整审查报告目录：[描线修复检查记录](repair-qa/README.zh-CN.md)
- 11 行浅/深背景逐帧复查板：[`art/repair/v1.0.1/review-boards/`](../art/repair/v1.0.1/review-boards)
- 当前 `v1.0.2` 综合审查结果：[审查与校验指南](REVIEW.zh-CN.md)（注：`v1.0.2` 的前 9 行标准动作原封不动继承了 `v1.0.1` 修复后的 RGBA 像素）
- 问题追踪记录：[Issue #1](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues/1)

---

## 4. 在本地一键复现历史修复

你可以随时运行仓库内的修复脚本，从冻结的清理前原图重新导出 `v1.0.1` 历史修复产物，并运行回归测试（含 `v1.0.1` 描线恢复校验）与当前工作区校验：

```sh
python3 -m pip install -r requirements.txt

# 1. 从冻结的清理前原图重现 v1.0.1 修复结果（写入独立目录，不覆盖当前 v1.0.2 运行包）
python3 scripts/restore_outlines.py --build --output-dir output/outline-restore-v1.0.1

# 2. 运行包含 v1.0.1 描线回归校验的单元测试与当前工作区全量校验/预览/打包
python3 -m unittest discover -s tests
python3 scripts/validate.py --report docs/validation.json
python3 scripts/render_previews.py
python3 scripts/package.py
```

- `--build` 参数会直接读取固定的清理前原图 [`art/repair/v1.0.1/source-before-cleanup.png`](../art/repair/v1.0.1/source-before-cleanup.png)，将历史 `v1.0.1` 修复结果导出到你指定的 `output/outline-restore-v1.0.1` 新目录中，不会重画、不会缩放、也不会混合邻近颜色；随后的 `validate.py`、`render_previews.py` 与 `package.py` 则针对仓库当前的 `v1.0.2` 运行包执行（其中 `validate.py` 和 `unittest` 都会自动审计冻结的 `v1.0.1` 快照）。
- 受损的 [`v1.0.0` 历史快照](../art/releases/v1.0.0)与修复后的 [`v1.0.1` 历史快照](../art/releases/v1.0.1)均完整保留在仓库中供对比与回归测试使用。
- **长期工程铁律**：后续任何导出都必须保留干净的原生透明度，直接对照认可原图核查外轮廓色彩；`PNG == WebP` 只用作编码器无损校验，绝不能替代原画色彩比对与肉眼双背景审查。
