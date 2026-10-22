# Review evidence

**English** · [简体中文](README.zh-CN.md) · [Review guide](../REVIEW.md)

These reports cover the restored **v1.0.1** WebP. The atlas hash identifies the reviewed file; report paths are repository-relative.

## File and motion measurements

| Report | Records |
| --- | --- |
| [atlas.json](atlas.json) | Image identity, grid, cell population, alpha, and chroma fringe. |
| [frames.json](frames.json) | Standard-frame geometry and final crops. |
| [continuity.json](continuity.json) | Neighboring look poses, silhouette continuity, and the recorded local warning. |
| [chroma-preservation.json](chroma-preservation.json) | Native alpha preserved without neighbor-color averaging. |
| [pet-quality.json](pet-quality.json) | Final file identity, hop lift/landing, and head registration. |

## Visual and direction reviews

| Evidence | Records |
| --- | --- |
| [direction-semantics.json](direction-semantics.json) | Expected direction and visible landmarks for all sixteen poses. |
| [Reviewer A](blind-reviewer-a.json) · [B](blind-reviewer-b.json) · [C](blind-reviewer-c.json) | Independent A/B answers saved before revealing the key. |
| [blind-majority.json](blind-majority.json) | Strict per-cell majority aggregation. |
| [blind-answer-key.json](blind-answer-key.json) | Intended directions and pair mapping. |
| [blind-validation.json](blind-validation.json) | Comparison of majority answers with the key. |
| [independent-all-frames.json](independent-all-frames.json) | Separate visual inspection of all 73 frames on light and dark backgrounds. |

The reviewers were AI agents. The main review also inspected ordered frame boards, complete loops, and native-size browser playback. See the [visual checklist and limits](../REVIEW.md) for the acceptance criteria.

## Inspect the images

[Unlabeled pairs](../../art/repair/v1.0.1) · [Light/dark boards](../../art/repair/v1.0.1/review-boards) · [Direction sheet](../../previews/directions.png) · [Restoration report](../outline-restoration.json)
