# v1.0.2 Look Repair Evidence (Look Repair QA)

**English** · [简体中文](README.zh-CN.md) · [Review guide](../REVIEW.md)

This directory archives the visual comparison boards, six-pose face refinement metrics, three-reviewer unlabeled blind direction tests, and pixel-guard records for the **v1.0.2** Codex Dot 16-angle head-turn repair (rows 9 and 10).

In `v1.0.2`, we adjusted the left, downward, and adjacent upper-left head turns so that Phoebe Chupi's cheeks stay compact as her head rotates back toward the viewer, and the straight-up pose (`000°`) no longer adds extra vertical space below the eyes. Meanwhile, all **57 standard animation frames** across the first nine rows (including the original blinking cycle) retain their exact `v1.0.1` RGBA pixels byte-for-byte.

- **Reviewed runtime artifact**: `pets/phoebe-chupi/spritesheet.webp` (SHA-256: `c00941ef64ce87b76b60f84da2f5dd0045147ad82017cccf349d2a21330106c6`)
- **Provenance triad**: [Approved PNG baseline (`art/approved/v1.0.2/spritesheet.png`)](../../art/approved/v1.0.2/spritesheet.png) · [16-angle source map (`source-map.json`)](../../art/repair/v1.0.2/source-map.json) · [Pixel guard manifest (`approved-runtime.json`)](../../art/approved-runtime.json)

---

## Visual Comparison Boards: Before vs. After

### 1. Cardinal Directions (`000° / 090° / 180° / 270°`) Before & After

<p align="center">
  <img src="../../art/repair/v1.0.2/review-boards/before-after-cardinals.png" width="760" alt="Cardinal directions before and after v1.0.2 repair" />
</p>

### 2. All 16 Look Directions Before & After

Four upper-right/right drawings (`022.5`, `045`, `067.5`, and `090`) were reused from the original pass, while the remaining **12 look poses** were redrawn as complete connected character frames with the built-in image generation tools (preserving the hat design without pasted faces or local warps), followed by a targeted six-pose face refinement across `000`, `157.5`, `247.5`, `292.5`, `315`, and `337.5`:

<p align="center">
  <img src="../../art/repair/v1.0.2/review-boards/before-after-directions.png" width="780" alt="All 16 look directions before and after v1.0.2 repair" />
</p>

### 3. Seated Master Anchor & All 16 Looks at Native Size (`192 × 208`)

<p align="center">
  <img src="../../art/repair/v1.0.2/review-boards/mother-and-sixteen-native.png" width="760" alt="Seated master anchor alongside all 16 look poses at native size" />
</p>

### 4. Critical Upper-Left Return Arc (`270° → 292.5° → 315° → 337.5° → 000°`) on Light & Dark Backgrounds

To verify that the face no longer appears to balloon as the head turns back from upper-left to straight-up while the laptop stays still, we inspected the chain on light and dark backgrounds and at `2×` diagnostic zoom:

<table>
  <tr>
    <td align="center" width="50%">
      <img src="../../art/repair/v1.0.2/review-boards/independent-c-chain-left-up-loop-light.png" width="370" alt="Upper-left return chain on light background" /><br />
      <sub><b>Light Background</b>: Upper-left return chain</sub>
    </td>
    <td align="center" width="50%">
      <img src="../../art/repair/v1.0.2/review-boards/independent-c-chain-left-up-loop-dark.png" width="370" alt="Upper-left return chain on dark background" /><br />
      <sub><b>Dark Background</b>: Clean outer contour alpha check</sub>
    </td>
  </tr>
</table>

<p align="center">
  <img src="../../art/repair/v1.0.2/review-boards/independent-c-zoom-loop-critical-light.png" width="760" alt="Zoomed inspection board of the critical upper-left return arc" />
</p>

> Additional inspection boards are stored in [`art/repair/v1.0.2/review-boards/`](../../art/repair/v1.0.2/review-boards). Browse them alongside the [light direction loop](../../previews/look-loop.gif), [dark direction loop](../../previews/look-dark.gif), and [16 exact PNG cell crops](../../art/frames/look).

---

## What Was Checked

The table below indexes every machine-readable verification report in this folder (note that numeric measurements support visual review—a face bounding box alone cannot distinguish a natural 3D head turn from unwanted head resizing):

| Evidence File | Scope & Verification Summary |
| --- | --- |
| [`direction-semantics.json`](direction-semantics.json) | Documents visible head orientation, cheek fullness, near/far eye foreshortening, and hat-pitch cues for all 16 poses. |
| [`independent-final-art-review.json`](independent-final-art-review.json) | Independent inspection of the complete 16-pose look ring and critical joins (downward chain and upper-left return loop) on light and dark backgrounds. |
| [`ui-visual-review.json`](ui-visual-review.json) | Browser review at native `192 × 208` (`1×`) resolution with forward/reverse single-frame stepping and sampled live-loop snapshots. |
| [`face-continuity-before-after.json`](face-continuity-before-after.json) | Fixed-coordinate before/after comparisons across the six final face corrections (`000`, `157.5`, `247.5`, `292.5`, `315`, and `337.5`). |
| [`protected-standard-rows.json`](protected-standard-rows.json) | Verifies exact RGBA pixel equality across all 57 standard frames (and 15 empty cells) in rows 0–8 against `v1.0.1`. |
| [`installation-verification.json`](installation-verification.json) | Confirms that local files and the existing active Codex app pet entry were updated to `v1.0.2`, and that the app's readback PNG matches the release WebP pixel-for-pixel. |
| [`atlas-validation.json`](atlas-validation.json) · [`standard-frame-review.json`](standard-frame-review.json) | Validates the `1536 × 2288` grid, 73 occupied cells, 15 empty cells, alpha margins, connected components, and frame geometry. |
| [`look-continuity.json`](look-continuity.json) · [`pet-quality.json`](pet-quality.json) | Evaluates neighboring silhouette transitions, head horizontal center stability (`3.0 px` max drift), and hop lift/landing (`21 px` peak lift, `0 px` landing offset). |
| [`chroma-native-alpha.json`](chroma-native-alpha.json) | Confirms that native generated ink and alpha were preserved directly without neighbor-color averaging. |
| [`archive-verification.json`](archive-verification.json) | Verifies all 832 unique source hashes, pixel preservation, metadata stripping, and archive coverage of the selected frames. |

---

## Blind direction checks

Before seeing the answer key, three isolated AI reviewers classified 14 randomized, unlabeled `A / B` opposite-axis pairs with all filenames and angle labels stripped:

<p align="center">
  <img src="../../art/repair/v1.0.2/review-boards/blind-axis-pairs.png" width="720" alt="Unlabeled A/B opposite-axis blind test board for v1.0.2" />
</p>

- **Outcome**: All 7 horizontal pairs and 7 vertical pairs (**14 / 14 strict-majority comparisons**) passed.
- **Archived blind-test records**:
  - Individual reviewer transcripts: [`blind-review-a.json`](blind-review-a.json) · [`blind-review-b.json`](blind-review-b.json) · [`blind-review-c.json`](blind-review-c.json)
  - Aggregation & scoring: [`blind-majority.json`](blind-majority.json) · [`blind-axis-answer-key.json`](blind-axis-answer-key.json) · [`blind-validation.json`](blind-validation.json)

---

## Limits

- **Discrete 16-pose angular stepping**: Because the pet uses sixteen discrete look drawings, the `225 → 247.5` yaw step and `270 → 292.5` upward head lift remain more noticeable than their immediate neighbors.
- **Browser sampling & platform scope**: The revised upper-left sequence was verified against the anchored laptop and body via paused `1×` forward/reverse browser stepping and sampled playback screenshots. Local installation and app image readback are verified; native Dot and Windows desktop visual checks remain pending.
- **Preserved historical baseline**: The earlier [`v1.0.1` outline-repair evidence](../repair-qa/README.md) and [`v1.0.1` release snapshot](../../art/releases/v1.0.1) remain available for side-by-side comparison.
