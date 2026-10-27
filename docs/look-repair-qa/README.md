# Look repair evidence

**English** · [简体中文](README.zh-CN.md) · [Review guide](../REVIEW.md)

The v1.0.2 artwork adjusts the left, downward, and adjacent head turns. The cheeks stay compact as the head turns back toward the viewer, and the up pose no longer adds extra space below the eyes. All 57 standard animation frames, including the original blinking, retain their v1.0.1 RGBA pixels.

The reviewed WebP is identified by SHA-256 `c00941ef64ce87b76b60f84da2f5dd0045147ad82017cccf349d2a21330106c6`. The [approved source](../../art/approved/v1.0.2/spritesheet.png), [source map](../../art/repair/v1.0.2/source-map.json), and [pixel guard](../../art/approved-runtime.json) connect the drawings to the distributed file.

## What was checked

| Evidence | Purpose |
| --- | --- |
| [Direction observations](direction-semantics.json) | Visible head, cheek, eye, and pitch cues for all sixteen poses. |
| [Independent artwork review](independent-final-art-review.json) | Separate inspection of the complete look family and critical joins on light and dark backgrounds. |
| [Browser review](ui-visual-review.json) | Native-size forward/reverse stepping and samples of the live loop. |
| [Face comparisons](face-continuity-before-after.json) | Fixed-coordinate measurements before and after the six latest face corrections. |
| [Protected actions](protected-standard-rows.json) | Exact RGBA equality for the nine standard rows. |
| [Atlas validation](atlas-validation.json) · [frame review](standard-frame-review.json) | Grid, population, transparency, components, and frame geometry. |
| [Continuity](look-continuity.json) · [quality gate](pet-quality.json) | Neighboring silhouette changes, head registration, and hop lift/landing. |
| [Native alpha](chroma-native-alpha.json) | Preservation of the generated ink and alpha without color averaging. |
| [Source archive](archive-verification.json) | Source hashes, preserved pixels, metadata cleanup, and coverage of the selected frames. |

The [native comparison boards](../../art/repair/v1.0.2/review-boards) show the lower and upper-left joins. Browse the [current direction loop](../../previews/look-loop.gif), [dark loop](../../previews/look-dark.gif), and [exact PNG crops](../../art/frames/look) alongside them. Measurements support visual review; a face bounding box alone cannot distinguish a head turn from unwanted resizing.

## Blind direction checks

Three isolated AI reviewers classified randomized, unlabeled A/B pairs before seeing the answer key. All fourteen strict-majority comparisons passed.

[Reviewer A](blind-review-a.json) · [Reviewer B](blind-review-b.json) · [Reviewer C](blind-review-c.json) · [Majority](blind-majority.json) · [Answer key](blind-axis-answer-key.json) · [Validation](blind-validation.json)

## Limits

The pet has sixteen discrete look poses. The `225 → 247.5` yaw and `270 → 292.5` upward lift remain more noticeable than their immediate neighbors. The revised upper-left sequence was checked against the anchored laptop and body for the reported face-size jump. Browser playback was sampled through screenshots and paused stepping; this revision has not been installed in native Dot. Windows visual verification is also pending.

The earlier [v1.0.1 evidence](../repair-qa/README.md) and [release snapshot](../../art/releases/v1.0.1) remain available for comparison.
