# Review and acceptance / 审查与验收

[English README](../README.md) · [中文说明](../README.zh-CN.md) · [Making of](MAKING-OF.md)

We checked the drawings and the finished files separately: first the character and motion, then the atlas, archive, and install package.

**Correction for v1.0.1:** the earlier review missed dark hair outlines faded by an edge-cleanup pass. PNG/WebP equality passed because both files already contained the mistake. This release compares all 73 cells with the approved pre-cleanup pixels and repeats the visual review on light and dark backgrounds. [Repair evidence](OUTLINE-REPAIR.md).

## Review the source hierarchy

Use the selected community turnaround to judge shape, then the accepted seated/carry images to judge new frames. Use neighboring frames to judge motion, not to redefine the character. A rejected candidate is a comparison artifact, not a new canonical reference.

For third-party references, check the creator attribution and whether the image is official, fan-made, AI-derived, or only a repost. The selected turnaround is community AI-derived. A collection uploader is not automatically the original artist. See [sources](SOURCES.md).

## Per-frame visual review

| Area | Questions to answer |
| --- | --- |
| Identity | Does this still match the canonical face, hat, hair, outfit, and head/body relationship? |
| Asymmetry | Is the clip on viewer-right, with tuft and blue cloth on viewer-left? Was anything accidentally mirrored? |
| Anatomy | Are there exactly the intended two hands/arms? Do gloves and sleeves connect correctly? |
| Face | Any duplicate brow, stray facial line, changed chin, or inconsistent purple eye construction? |
| Laptop | Is it one computer with a plausible lid, hinge, and keyboard? Do the hands hold the intended parts? |
| Motion | Is the requested pose actually readable? Is its change plausible relative to the previous and next frames? |
| Registration | Is the body/laptop anchor stable where the action should be stationary? Does the hop return to its origin? |
| Alpha | Are there light/dark fringes, holes, opaque background remnants, or clipped extremities? |
| Ink color | Does each dark contour retain its source color after export? Keep the reference's gold/brown inner hair lines; do not turn them black. |
| Native size | Does the expression remain legible in a 192 × 208 cell? Does added detail turn into visual noise? |

Inspect on a light checkerboard and a dark solid background. Review at native size first, then enlarge to diagnose a defect. An enlarged screenshot alone is not a fair measure of the native artwork's sharpness.

## Whole-sequence review

For every standard state, inspect a contact sheet, play the loop at the expected runtime speed, and inspect the last-to-first join. Then compare the first/last poses with the common seated or carry anchor.

- Watch `idle → jumping → idle` for takeoff, prop attachment, landing, and recovered baseline.
- Compare waiting, working, review, and help states for a coherent emotional range.
- Check that left/right movement use the same character and closed laptop without mirrored accessories.
- Run the look sequence through its wraparound; check torso/laptop drift separately from head cues.
- Revisit a frame after normalization and encoding. Approval of a large source drawing does not approve a badly fitted small cell.

The public [standard contact sheet](../previews/contact-sheet.png), [direction sheet](../previews/directions.png), [all-state loop](../previews/all-states.gif), and [dark look loop](../previews/look-dark.gif) support these checks. GIF palettes reduce color precision; [final PNG](../art/final/spritesheet.png) and [exact frame crops](../art/frames) retain the pixels.

## Direction blind review

The original production review used unlabeled pairs so reviewers had to report apparent screen direction rather than agree with a filename. Three AI reviewers considered fourteen comparisons: seven horizontal and seven vertical. Cardinal comparisons were treated as strong gates, with intermediate-angle comparisons also reviewed.

The final majority result identified the intended directions for all fourteen pairs. Earlier unsuccessful candidates were repaired before that final result. The sanitized [production-review.json](production-review.json) records the final pairs and summary.

The reviewers were AI agents. The remaining weak angles are listed below.

For v1.0.1, three independent AI reviewers classified a fresh unlabeled set from the repaired WebP. All fourteen majority comparisons passed. A separate all-frame review covered all 73 cells on both backgrounds. Individual answers and the new results are in [repair QA](repair-qa/); the original record remains in [v1.0.0 history](../art/releases/v1.0.0/production-review.json).

For a future change, randomize the pair order again, hide labels and answer keys, ask for apparent direction plus confidence, and compare against the intended answer only afterward. Do not resolve a failed visual test by renaming the expected answer.

## Recorded results

| Check | Result | Scope |
| --- | --- | --- |
| Native grid | 1536 × 2288, 8 × 11 | Rechecked on the shipped WebP. |
| Required cells | 73 populated | 57 standard + 16 look. |
| Unused cells | 15 fully transparent | Rechecked on the shipped WebP. |
| PNG/WebP equality | Same decoded RGBA | Encoding comparison, not a visual-quality rating. |
| Exact final crops | All 73 equal their atlas cells | Rechecked by the public validator. |
| Source color fidelity | All 73 match the approved pre-cleanup pixels | 88,948 visible RGB pixels restored; zero source mismatches. |
| Dark ink preservation | 263,885 protected pixels unchanged | Compared with the approved source, in addition to visual inspection. |
| Source image archive | 742 distinct originals, 1,290 working occurrences | Original hashes and sanitized aliases mapped in the archive index. |
| Hop peak / landing | 21 px / 0 px offset | Remeasured for v1.0.1 with alpha > 16. |
| Gaze horizontal registration | Maximum center drift 3.5 px | Remeasured with the same threshold. |
| Gaze width ratio | Maximum 1.0625 | Remeasured with the same threshold. |
| Direction pairs | 14 final majority passes | Three fresh AI reviews for v1.0.1. |
| Metadata | EXIF removed from one reference; no RGBA pixel change | Remaining published images checked for unreviewed EXIF/XMP/comments. |
| Local runtime | Accepted blinking artwork installed and selected on macOS | Dot cursor-following was confirmed by the project owner; Windows has not been visually tested. |

The raw alpha bounds in [validation.json](validation.json) use any nonzero alpha. The movement measurements use alpha > 16; the two boundary policies should not be mixed.

## Known limits and release decision

1. `045` and `067.5` directions remain visually close.
2. `225 → 247.5` is a larger visual step; the original comparison counted 1,820 differing pixels versus a neighboring average of 1,019 under that check's policy. It was reviewed and accepted, not silently treated as uniform.
3. The blink includes half-closed and closed-eye poses. Runtime timing or reduced-motion behavior can make a pose noticeable as a still.
4. A fully awake experiment reduced this issue but was rejected by the project owner as less expressive. The released runtime remains the earlier blinking version.
5. The native cell is small. Runtime magnification, screenshot scaling, and GIF palettes can soften the appearance without indicating a corrupted source file.
6. App feature rollout, caching, scaling, state selection, and timing are outside the atlas's control. Dot cursor-following is supported and was confirmed in use. Windows was not visually tested here.

Future edits should preserve the expressive range while improving the particular weak frame or transition. Replacing all eye motion merely to avoid a possible freeze-frame is not the current accepted direction.

## Repeatable mechanical validation

```sh
python3 -m pip install -r requirements.txt
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
```

The script validates the portable five-field v2 manifest, atlas dimensions and alpha, static WebP, required/empty cells, cell-edge margins, exact final crop equality, PNG/WebP pixel equality, approved source colors, archive file hashes, image decoding, metadata, common private-data markers, file-size limits, and runtime checksums. The regression tests also reject the real damaged v1.0.0 artifact. Reports use repository-relative paths.

CI runs the same file checks. After changing the artwork, repeat the visual review too.

## Release checklist

- [ ] Confirm the selected artwork version and its accepted baseline.
- [ ] Re-review modified frames, adjacent frames, loops, and state transitions.
- [ ] Repeat blind direction comparisons if a look pose changed.
- [ ] Regenerate previews from the exact WebP being shipped.
- [ ] Run validation and review its limitations, not just its exit code.
- [ ] Preserve rejected candidates in the labeled archive and update image hashes/aliases.
- [ ] Update English and Chinese documentation together.
- [ ] Check attribution, separate asset terms, and compatibility wording.
- [ ] Remove private paths, account IDs, signed URLs, private receipts, and image metadata.
- [ ] Use a public-safe commit identity and a fresh repository history.
- [ ] Build the two-file runtime ZIP and the separate artwork archive.
- [ ] Publish the matching version tag, verify public raw downloads, and compare release checksums.

Use this checklist when preparing the next release.

## 中文：怎样审查

机械校验和画面审查分开记录。尺寸正确，只说明文件能按预期分格，不能说明画得像、动作顺。

上一版确实漏掉了描线变浅的问题：透明边缘清理把部分黑线混进了头发的浅色，PNG 和 WebP 又都沿用了这份错误，所以只比对两种格式发现不了。v1.0.1 已按清理前的原像素恢复，并重新看过全部 73 帧的浅、深背景。这次还加入了原始描线颜色检查，旧版图片会被回归测试拦下。金棕色的内部发丝线按参考保留，没有一律涂黑。

每帧先对基准图，检查脸型、头身比例、帽子和头发轮廓，再检查发夹是否在观看者右侧、呆毛和蓝布是否在左侧。数清双手，查看袖子连接、眉毛重复、下巴变形，以及电脑是否多出一层键盘或屏盖。

然后看前后帧和整行循环，特别是首尾衔接。小跳看起跳、电脑有没有跟住、落地能否回原位；等待、工作、检查和失落应当像同一个角色的情绪变化。左右移动分别画，不能镜像造成配饰换边。

以原生 192 × 208 小尺寸为主要观感，放大只用于找问题。浅色和深色背景都看一遍，避免白边、黑边、透明洞或裁切。高分辨率原图审过之后，缩放和编码完成仍需再看。

方向盲测把标签和答案藏起来，让审查者判断画面实际朝向。原制作过程最后由 3 名 AI 审查者对 14 组水平、垂直对比做出多数判定，最终通过。相邻角度仍有不够明显的地方，见上面的保留问题。

本次保留的问题是：`045` 与 `067.5` 接近，`225 → 247.5` 的变化较大，眨眼帧被停留显示时仍可能明显。全程睁眼的试验已经退回，因为用户更喜欢有眼睛动作的版本。不要为了一个截帧消除全部表情。

公开校验脚本检查实际发布文件。JSON 报告里的边界按所有非零透明像素计算，不能与原制作记录中采用阈值的可见边界测量直接混算。

以后发布新版本，应重新看改动帧和相邻帧、循环、状态衔接；视线改动还需重做盲测。更新图片索引和双语文档，核对来源与使用范围，清理隐私，打包后下载公开文件再比对哈希。Dot 跟随鼠标转头已确认可用；Windows 仍需实际验收。
