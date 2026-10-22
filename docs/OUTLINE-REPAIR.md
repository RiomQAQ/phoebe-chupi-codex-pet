# v1.0.1 · Restoring the hair outlines

[English README](../README.md) · [中文](#中文) · [Issue #1](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues/1)

The previous release had pale patches in parts of the hair contour. These came from the export cleanup: an edge-pixel rule replaced legitimate dark ink with nearby blonde or white colors. The local, cloud, and GitHub copies contained the same pixels. It was a real artwork-processing mistake, missed by the earlier review.

## What changed

We recovered the approved pixels from before that cleanup and exported them directly to lossless WebP. All **73 occupied cells** now match the recovered source. This restores **88,948 visible RGB pixels**, including faded ink and neighboring edge colors. Alpha is identical to v1.0.0, so placement, silhouettes, proportions, blinking, and motion registration stay the same. Gold/brown lines inside the hair remain part of the design.

![Before and after: hair contour details](../art/repair/v1.0.1/before-after.png)

The enlarged details use nearest-neighbor scaling to expose the actual pixels. `idle/00`, `running-right/03`, and `running-left/07` are zero-based frame names.

## What we checked

| Check | Result |
| --- | --- |
| Approved source comparison | All 73 cells match; zero visible pixel mismatches. |
| Dark ink comparison | 263,885 source ink pixels checked; zero mismatches. |
| Geometry and transparency | Same alpha as v1.0.0; 73 used cells, 15 empty cells. No detected chroma fringe or hidden RGB residue. |
| Format and crops | Lossless WebP equals the final PNG; every published frame crop equals its atlas cell. |
| Visual review | All 73 frames on light and dark backgrounds, including hair, face, proportions, hands, laptop, and accessories. A separate AI reviewer repeated this pass. |
| Motion | Nine loops, idle–hop–idle, and the full head-turn sequence reviewed from the shipped artwork. Native-size browser playback checked on both backgrounds. |
| Direction blind review | Three independent AI reviewers; fourteen majority comparisons passed. |
| Regression tests | The previous release fails the new color-fidelity check; the repaired release passes. Three reported hair pixels are checked explicitly. |

The existing subtleties in `045 / 067.5` and the larger `225 → 247.5` step remain documented in [Review](REVIEW.md). This repair preserves the selected motion; it does not redesign those poses.

Browse the [light/dark frame boards](../art/repair/v1.0.1/review-boards), [all-state motion preview](../previews/all-states.mp4), [light stills](../previews/stills), and [dark loops](../previews/dark). The [per-frame restoration report](outline-restoration.json), [independent reviews](repair-qa), and [production summary](production-review.json) record the checks.

## Reproduce the repair

```sh
python3 -m pip install -r requirements.txt
python3 scripts/restore_outlines.py --build --report docs/outline-restoration.json
python3 scripts/render_previews.py
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
python3 scripts/package.py
```

`--build` uses the frozen [pre-cleanup source](../art/repair/v1.0.1/source-before-cleanup.png). It performs no redrawing, resizing, color averaging, or new image generation. To also export the MP4 preview, run `python3 scripts/render_previews.py --mp4` with FFmpeg available.

The [v1.0.0 snapshots](../art/releases/v1.0.0) remain available for comparison. The current install package is still just `pet.json` and `spritesheet.webp`, with v2 geometry and all sixteen Dot look directions.

## 中文

上一版有些头发外轮廓发灰、发白，是导出时清理透明边缘误伤了原本的黑线。清理规则把附近的金发和帽子颜色混进了描线。本地、云端和 GitHub 的图片一致；之前的审查漏掉了这个问题。

这次从清理前的原图恢复全部 **73 帧**，共还原 **88,948 个可见像素的 RGB 颜色**。没有重画角色，也没有把金棕色的内部发丝线涂黑。透明度、帧位置、比例、眨眼、动作和 Dot 转头都保持原样。

检查包括全部帧的浅深背景、九种动作循环、小跳衔接、16 个转头方向、原图与发布图的像素比对，以及 3 名独立 AI 审查者的方向盲看。另有一轮独立全帧检查。新的回归测试会拒绝有问题的 v1.0.0 图片，避免只看尺寸或 PNG/WebP 一致就算通过。

上方有修复前后的放大对照，完整逐帧图、循环、检查结果和恢复脚本也都保留在仓库里。当前安装包仍然只有两个文件，支持新版 v2 宠物结构和 Dot 随鼠标转头。

更新已有的本地宠物时，先把原文件夹备份到 `pets` 目录外，再只替换 `spritesheet.webp`，保留自己的 `pet.json`。这样名字和身份不会变，也不会多出一个重复条目。回到设置刷新即可；云端导入的宠物应在应用里更新原条目。
