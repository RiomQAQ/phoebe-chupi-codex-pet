# Review and Validation Guide

**English** · [简体中文](REVIEW.zh-CN.md) · [Documentation](README.md)

When building a desktop pet sprite atlas, **passing a structural script does not guarantee good drawings**, and **matching PNG against WebP cannot catch a visual mistake already present in both files**. For that reason, Phoebe Chupi separates QA into four independent gates—**per-frame visual inspection**, **full-loop motion review**, **unlabeled three-reviewer blind direction testing**, and **automated pixel guards**—using the canonical pose anchors for character identity and the final `spritesheet.webp` for release verification.

```text
+-----------------------------------------------------------------------------+
|  Gate 1: Native 192 × 208 Per-Frame Inspection (light + dark backgrounds)   |
|     │                                                                       |
|     ▼                                                                       |
|  Gate 2: Motion & Transition Review (9 state loops + hop join + 16 looks)   |
|     │                                                                       |
|     ▼                                                                       |
|  Gate 3: 3-Reviewer Unlabeled A/B Blind Direction QA (14 opposite pairs)    |
|     │                                                                       |
|     ▼                                                                       |
|  Gate 4: validate.py + unittest Pixel Guards (baseline lock & row freeze)   |
+-----------------------------------------------------------------------------+
```

---

## Review Each Frame

Inspect all 73 occupied cells on both a light background and a dark background. Always start at the native **192 × 208** (`1×`) cell size to judge overall proportions and silhouette readability; enlarge a region only to diagnose a specific pixel defect:

<p align="center">
  <img src="../art/samples/native-size-comparison.png" width="700" alt="Native 192 × 208 size compared with enlarged inspection views" />
</p>

| Area | Acceptance Criteria |
| --- | --- |
| **Identity** | Face, broad white hat, blonde hair silhouette, clothing, and compact two-head proportions match the canonical anchors. |
| **Accessories** | Blue cross clip remains on **viewer-right**; ahoge tuft and blue cloth remain on **viewer-left**. |
| **Anatomy** | Only the two intended hands and arms appear, with clean glove-to-sleeve connections and no ghost limbs. |
| **Face** | Consistent layered purple eyes, brows, short chin, and mouth; no duplicate stray lines. |
| **Laptop** | Exactly one lid, one hinge, and one keyboard; hands rest on or carry the intended surfaces naturally. |
| **Contour** | Dark outer contour lines remain continuous; gold/brown internal hair lines retain their source color. |
| **Transparency** | At least `1 px` transparent margin on all four sides; no opaque backdrop, clipped extremity, halo fringe, or interior hole. |
| **Registration** | Seated body, laptop, and ground contact stay anchored wherever the pose requires them to remain still. |

Compare every changed frame against its **canonical pose anchor**, **both immediate neighbors**, and **another state sharing the same physical setup**. Recheck after viewport normalization and lossless WebP encoding.

---

## Review the Motion

- **Nine standard state loops**: Play all nine loops at their expected cadence and inspect every last-to-first loop join.
- **Seated hop continuity**: Watch `idle → jumping → idle` for smooth takeoff, attached laptop lift (`21 px` peak), and zero-offset landing recovery back to the idle baseline.
- **Cross-state expression coherence**: Compare `running` (working), `waiting`, `review`, and `failed` (needs help) side by side to confirm they read as one continuous character.
- **Left/right carry balance**: Check `running-right` and `running-left` for matching proportions, stride cadence, and non-mirrored accessory placement.
- **16-angle look sweep**: Run all sixteen Dot look poses through the `337.5° → 000°` wraparound while watching body/laptop stability separately from head and gaze rotation.

Use the [all-state animation](../previews/all-states.gif), [hop transition](../previews/idle-jump-idle.gif), [direction loop](../previews/look-loop.gif), and [dark previews](../previews/dark) for quick playback checks. Because GIF palettes are limited to 256 colors, always verify final edge colors and alpha transitions against the [accepted PNG](../art/final/spritesheet.png) and [73 exact cell crops](../art/frames).

---

## Direction review

To prevent reviewers from guessing gaze directions from filenames like `090.png` or `270.png`, direction QA combines **labeled sequence inspection** with **unlabeled A/B blind testing**:

<p align="center">
  <img src="../art/repair/v1.0.2/review-boards/blind-axis-pairs.png" width="720" alt="Unlabeled A/B opposite-axis blind test board" />
</p>

1. **Build 14 opposing axis pairs**: Compare seven horizontal pairs (left vs. right) and seven vertical pairs (up vs. down), with the four cardinal directions (`000`, `090`, `180`, `270`) required to pass unambiguously.
2. **Strip all labels**: Hide filenames, angle numbers, and the answer key, and randomize `A / B` order within each pair.
3. **Collect three independent blind calls**: Ask three isolated reviewers to report the visible screen direction (`left/right` or `up/down`) and supporting visual cues for each image, explicitly allowing an `ambiguous` call.
4. **Lock answers before scoring**: Save all individual responses before consulting the answer key, then aggregate by strict per-cell majority (at least 2 of 3 reviewers agreeing on the intended direction).
5. **Cross-check against the ordered ring**: Inspect any disagreement against the continuous 16-angle sweep before accepting or redrawing a pose.

For `v1.0.2`, three independent reviewers completed a fresh round of unlabeled A/B comparisons, and **all 14 strict-majority comparisons passed**. Individual response sheets, the answer key, and validation outputs are preserved in [look repair evidence](look-repair-qa/README.md); the earlier `v1.0.1` blind-test records remain in [historical review evidence](repair-qa/README.md).

---

## Current results

The results below apply to the distributed **v1.0.2** lossless WebP (`pets/phoebe-chupi/spritesheet.webp`), SHA-256 `c00941ef64ce87b76b60f84da2f5dd0045147ad82017cccf349d2a21330106c6`. Full quality-gate logs, blind direction tables, and browser inspection records are archived in [look repair evidence](look-repair-qa/README.md).

| Check | v1.0.2 Result |
| --- | --- |
| **Layout** | `1536 × 2288` (8 columns × 11 rows, `192 × 208` per cell); **73 occupied cells** and **15 transparent cells**. |
| **Export fidelity** | `art/final/spritesheet.png` and lossless `spritesheet.webp` have identical decoded RGBA pixels. |
| **Frame crops** | All 73 crops under `art/frames/` match their corresponding atlas cells pixel-for-pixel. |
| **Approved artwork** | Runtime pixels match the reviewed `v1.0.2` PNG baseline (`art/approved/v1.0.2/spritesheet.png`). |
| **Standard animations** | All **57 frames** in the first nine rows (including blinking) retain the exact RGBA pixels of `v1.0.1`. |
| **Look artwork** | **12 complete frames redrawn**; original drawings reused for `022.5`, `045`, `067.5`, and `090`. Hat design preserved. |
| **Direction comparisons** | Three fresh independent blind reviews; **all 14 comparisons passed by strict majority**. |
| **Quality gate** | Recorded pet-quality QA report ([`pet-quality.json`](look-repair-qa/pet-quality.json)) passed with reviewed direction and continuity warnings. |
| **Hop metrics** | **21 px** peak lift; **0 px** landing offset. |
| **Look registration** | Maximum horizontal center drift **3.0 px**; maximum width ratio **1.0859375**. |
| **Browser inspection** | Native `192 × 208` (`1×`) old/new stepping and sampled playback snapshots (details below). |
| **Installation & readback** | Local files and the existing active app pet entry updated; stored RGBA pixels match the release. |
| **Source archive** | **832 distinct source images** across **1,447 indexed working-file occurrences**. |

<p align="center">
  <img src="../art/repair/v1.0.2/review-boards/independent-c-zoom-loop-critical-light.png" width="760" alt="Zoomed inspection board for the critical upper-left return arc (270° → 337.5° → 000°)" />
</p>

### Measurement Policies & Inspection Scope

1. **Six-pose face refinement**: The final refinement pass covered `000`, `157.5`, `247.5`, `292.5`, `315`, and `337.5` to resolve pinched cheeks and apparent face growth during the upward-left return. Each frame was generated as a complete connected character without face pasting or local warps.
2. **Alpha measurement thresholds**: Motion and registration metrics use visible bounds at `alpha > 16`, whereas the raw `alpha_bbox` values in [`docs/validation.json`](validation.json) include any nonzero alpha (`alpha > 0`). Keep these two policies distinct. Furthermore, registration numbers and pixel-difference ratios only help locate transitions to inspect by eye—they do not prove facial consistency or smooth motion on their own.
3. **Browser `1×` stepping scope**: The browser inspection stepped forward and backward through `270 → 292.5 → 315 → 337.5 → 000` at native `1×` resolution alongside `2×` diagnostic views. Because automated playback was captured via successive screenshots rather than continuous video recording, it represents sampled still verification. The obvious whole-face growth seen in early candidates is no longer apparent at native size, though discrete pose steps remain visible (`v1.0.1` was previously verified in macOS desktop and native Dot).
4. **Installation readback verification**: The [installation record](look-repair-qa/installation-verification.json) confirms that both local files and the active app pet entry were updated to `v1.0.2`. The app readback returns a PNG whose decoded RGBA pixels match the release WebP while preserving the existing pet identity, active selection, and all 57 standard frames.

---

## Known limitations

We document the current visual and platform-testing boundaries transparently:

- **`045` and `067.5` proximity**: These two upper-right poses remain visually close at native `192 × 208` size.
- **Larger discrete steps on two transitions**: `225 → 247.5` and `270 → 292.5` remain larger discrete pose steps than their immediate neighbors. `270 → 292.5` includes an upward head lift, and `292.5 → 315` visibly opens the farther eye.
- **Discrete 16-angle Dot selection**: Because Dot selects among sixteen static poses by cursor angle, rapid cursor sweeps show visible angular steps rather than continuous skeletal interpolation.
- **Blink hold under reduced motion**: The `idle` blink cycle includes half-closed and closed-eye frames; OS reduced-motion settings or app timing can occasionally hold one blink pose visibly.
- **Pending platform checks**: Native Dot verification of `v1.0.2` and Windows desktop visual verification remain pending (earlier direction feedback is tracked in [closed issue #2](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues/2)).

> **Historical Outline-Repair Note**: The [outline repair record](OUTLINE-REPAIR.md) explains the `v1.0.0` export cleanup error and `v1.0.1` restoration (**88,948 visible RGB pixels restored** and **263,885 dark-ink pixels verified with zero mismatches**). Those counts describe the historical `v1.0.1` repair preserved in [`art/releases/v1.0.1`](../art/releases/v1.0.1), not new `v1.0.2` look drawings. Its core lesson remains embedded in our QA pipeline: **comparing PNG against WebP does not detect a defect already present in both.**

---

## Run the File Checks

With Python 3.10+ and the repository dependencies (`Pillow`) installed:

```sh
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
```

- **`scripts/validate.py` coverage**: Checks the five-field `pet.json` manifest, static v2 WebP dimensions and alpha channel, 73 occupied cells and 15 transparent cells, `>= 1 px` cell margins, PNG/WebP decoded pixel equality, all 73 frame crops, approved-source fidelity, all 832 archive SHA-256 hashes, image decoding and clean metadata (no unreviewed EXIF/XMP/comments), public-file privacy markers, file-size limits, and `CHECKSUMS.sha256`.
- **Two-tier pixel guard (`scripts/audit_artwork.py`)**:
  1. Reads [`art/approved-runtime.json`](../art/approved-runtime.json), verifies the SHA-256 of [`art/approved/v1.0.2/spritesheet.png`](../art/approved/v1.0.2/spritesheet.png), and compares its full RGBA buffer against the runtime WebP;
  2. Freezes the first nine rows against the `v1.0.1` PNG ([`art/releases/v1.0.1/spritesheet.png`](../art/releases/v1.0.1/spritesheet.png)), protecting all 57 standard animation frames and unused cells in rows 0–8.
- **Regression suite (`tests/`)**: Preserves negative test coverage against the damaged `v1.0.0` atlas and its three signature pale-outline pixels while verifying the approved `v1.0.2` runtime and frozen standard rows. Any intentional artwork update requires a newly reviewed baseline and updated checksum while keeping historical snapshots and regression tests intact.

---

## Release Checklist

Before tagging any new release:

- [ ] Review all changed frames, adjacent frames, complete loops, and cross-state transitions on light and dark backgrounds.
- [ ] Repeat three-reviewer independent unlabeled A/B direction comparisons after changing any Dot look pose.
- [ ] Regenerate all previews and frame crops from the exact `spritesheet.webp` to be distributed.
- [ ] Update source records, `CHECKSUMS.sha256`, and both Chinese and English documentation.
- [ ] Check attribution notices, image metadata hygiene, and public-file privacy scans.
- [ ] Run `scripts/validate.py` and the `unittest` regression suite; inspect the generated `dist/` archives.
- [ ] Align `VERSION`, the installer URI tag, and the Git release tag.
- [ ] Verify CI on the release commit and compare public release downloads against local SHA-256 checksums.
