# Hair-outline repair

**English** · [简体中文](OUTLINE-REPAIR.zh-CN.md) · [Documentation](README.md)

**Fixed in v1.0.1.** An export cleanup in v1.0.0 replaced some dark contour colors with nearby blonde or white fills. The affected pixels appeared as pale patches in the hair outline.

## Cause

The edge rule treated partly transparent contour pixels as color spill and averaged neighboring colors into them. Replaying that rule on saved pre-cleanup frames reproduced the distributed pixels exactly. The local installation, cloud copy, and public v1.0.0 package contained the same affected artwork.

Structural validation did not catch the color loss. The PNG and WebP also matched because the error was already present in both.

## Correction

The approved pre-cleanup pixels were recovered, aligned to the existing atlas, and exported directly to lossless WebP. All 73 cells retain the previous alpha and placement. The correction restores colors without changing the blink, motion, proportions, or Dot direction layout.

![Original v1.0.0 pixels and restored v1.0.1 pixels](../art/repair/v1.0.1/before-after.png)

The detail crops use nearest-neighbor enlargement. Three explicit regression cases, using zero-based cell coordinates:

| Frame | Pixel `(x, y)` | v1.0.0 RGB | Restored RGB |
| --- | --- | --- | --- |
| `idle/00` | `(37, 180)` | `(100, 95, 74)` | `(0, 0, 0)` |
| `running-right/03` | `(155, 73)` | `(141, 135, 108)` | `(7, 0, 0)` |
| `running-left/07` | `(138, 108)` | `(148, 140, 113)` | `(8, 1, 0)` |

Gold/brown lines inside the hair are part of the design and retain their original colors.

## Verification

| Check | Result |
| --- | --- |
| Source comparison | All 73 cells match the approved visible pixels; zero mismatches. |
| Color restoration | 88,948 visible RGB pixels restored. |
| Dark ink | 263,885 source pixels checked; zero mismatches. |
| Geometry | Alpha and pose placement identical to v1.0.0. |
| Visual review | All frames on light/dark backgrounds, nine loops, hop transition, and sixteen looks; an independent all-frame pass also completed. |
| Direction review | Three independent AI reviewers; all fourteen majority comparisons passed. |
| Regression checks | The damaged v1.0.0 artifact fails; the restored artifact passes. |

See the [per-frame restoration report](outline-restoration.json), [review evidence](repair-qa/README.md), [light/dark boards](../art/repair/v1.0.1/review-boards), and [current review results](REVIEW.md). The correction is tracked in [issue #1](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues/1).

## Reproduce the repair

```sh
python3 -m pip install -r requirements.txt
python3 scripts/restore_outlines.py --build --output-dir output/outline-restore-v1.0.1
python3 scripts/render_previews.py
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
python3 scripts/package.py
```

`--build` reads the frozen [pre-cleanup source](../art/repair/v1.0.1/source-before-cleanup.png) and exports the historical repair into the chosen new directory. It preserves those pixels without redrawing, resizing, or color averaging. The installed package and current artwork stay in place. [v1.0.0 snapshots](../art/releases/v1.0.0) remain available for comparison.

For future exports, preserve clean native alpha and check contour colors against the approved source. PNG/WebP equality remains an encoding check, alongside the source-color and visual checks.
