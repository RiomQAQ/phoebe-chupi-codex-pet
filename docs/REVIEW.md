# Review and validation

**English** · [简体中文](REVIEW.zh-CN.md) · [Documentation](README.md)

Review the drawings, motion, and distributed files as separate checks. Use the canonical poses for identity and the final WebP for release verification.

## Review each frame

Inspect every occupied cell on a light background and a dark background. Start at the native **192 × 208** size; enlarge a region to diagnose a defect.

| Area | Acceptance criteria |
| --- | --- |
| Identity | Face, hat, hair, clothing, and head/body proportions match the anchors. |
| Accessories | Clip remains on viewer-right; tuft and blue cloth remain on viewer-left. |
| Anatomy | Two intended hands and arms, with clear glove/sleeve connections. |
| Face | Consistent purple eyes, brows, chin, and mouth; no duplicate marks. |
| Laptop | One lid, hinge, and keyboard; hands hold the intended surfaces. |
| Contour | Dark outer lines remain continuous; gold/brown inner hair lines retain their source color. |
| Transparency | No opaque backdrop, clipped extremity, fringe, or interior hole. |
| Registration | Body, laptop, and ground contact stay stable where the pose requires them to. |

Compare a changed frame with its anchor, both neighbors, and another state using the same physical setup. Recheck after normalization and encoding.

## Review the motion

- Play all nine loops at the expected speed and inspect each last-to-first join.
- Watch `idle → jumping → idle` for takeoff, the attached laptop, and the recovered baseline.
- Compare working, waiting, review, and help expressions as one continuous character.
- Check both carry directions for consistent proportions and accessory placement.
- Run all sixteen looks through the wraparound while watching body/laptop drift separately from head cues.

Use the [all-state animation](../previews/all-states.gif), [hop transition](../previews/idle-jump-idle.gif), [direction loop](../previews/look-loop.gif), and [dark previews](../previews/dark). GIF palettes have fewer colors; the [PNG](../art/final/spritesheet.png) and [exact crops](../art/frames) preserve the distributed pixels.

## Direction review

First inspect the labeled direction sheet and ordered loop. Then use unlabeled A/B pairs to check the apparent direction:

1. Compare seven horizontal and seven vertical pairs, with cardinal directions as required passes.
2. Hide the labels and answer key; vary A/B order.
3. Ask three independent reviewers for the visible screen direction and supporting cues. Allow an ambiguous answer.
4. Save the answers before revealing the key, then aggregate by strict per-cell majority.
5. Inspect any disagreement against the ordered sequence before accepting or repairing the pose.

The v1.0.2 review used three independent reviewers and fresh unlabeled A/B pairs. All fourteen strict-majority comparisons passed. Individual answers, the key, and the validation are in [look repair evidence](look-repair-qa/README.md). The earlier v1.0.1 answers remain in the [historical review evidence](repair-qa/README.md).

## Current results

These results apply to the **v1.0.2** WebP, SHA-256 `c00941ef64ce87b76b60f84da2f5dd0045147ad82017cccf349d2a21330106c6`. The [look repair evidence](look-repair-qa/README.md) records its quality checks, direction comparisons, and browser review scope.

| Check | Result |
| --- | --- |
| Layout | 1536 × 2288; 73 occupied cells and 15 transparent cells. |
| Export fidelity | PNG and lossless WebP have identical decoded RGBA pixels. |
| Frame crops | All 73 crops match their atlas cells. |
| Approved artwork | Runtime pixels match the reviewed v1.0.2 PNG baseline. |
| Standard animations | All 57 frames in the first nine rows, including blinking, have the same RGBA pixels as v1.0.1. |
| Look artwork | Twelve complete frames redrawn; original drawings reused for `022.5`, `045`, `067.5`, and `090`. Hat design preserved. |
| Direction comparisons | Three fresh independent reviews; all 14 comparisons passed by strict majority. |
| Quality gate | Official pet-quality script passed with reviewed direction and continuity warnings. |
| Hop | 21 px peak lift; 0 px landing offset. |
| Look registration | Maximum horizontal center drift 3.0 px; maximum width ratio 1.0859375. |
| Browser inspection | Native 192 × 208 old/new stepping and sampled playback snapshots; details below. |
| Source archive | 832 distinct source images; 1,447 working-file occurrences indexed. |

The latest face refinements are `000`, `157.5`, `247.5`, `292.5`, `315`, and `337.5`. They address pinched cheeks and apparent face growth during the upward-left return. Each is a complete frame generated with the image tools, without face pasting or local face warps.

Movement measurements use alpha > 16. The raw bounds in [validation.json](validation.json) include any nonzero alpha; keep these two measurement policies distinct. Registration and pixel-difference measurements help locate a transition to inspect; they do not establish facial consistency or smooth motion on their own.

The current browser review checked `270 → 292.5 → 315 → 337.5 → 000` forward and backward at 1×, with 2× diagnostic views. Playback was sampled through successive screenshots, so this is not a continuous-video review. The large whole-face growth seen in earlier candidates was no longer obvious at native size; visible pose steps remain. v1.0.1 was checked in macOS desktop and Dot. The current revision has not been installed and checked in native Dot, and Windows has not been visually tested.

## Known limitations

- `045` and `067.5` remain visually close.
- `225 → 247.5` and `270 → 292.5` remain larger discrete pose steps than their immediate neighbors. The latter includes an upward head lift; `292.5 → 315` also visibly opens the farther eye.
- Dot chooses among sixteen discrete poses, so changes occur in visible angular steps.
- Blink poses include partly closed and closed eyes. Reduced motion or app timing can hold one pose visibly.
- Native Dot verification of v1.0.2 and Windows visual verification remain pending. Earlier direction feedback is preserved in [closed issue #2](https://github.com/RiomQAQ/phoebe-chupi-codex-pet/issues/2).

The [outline repair record](OUTLINE-REPAIR.md) explains the v1.0.0 cleanup error and v1.0.1 correction: 88,948 visible RGB pixels restored and 263,885 dark-ink pixels checked with zero mismatches. These are historical repair counts, not counts of new v1.0.2 artwork. The v1.0.1 snapshot remains in [art/releases/v1.0.1](../art/releases/v1.0.1). Its lesson remains part of the export check: comparing two formats does not detect a mistake already present in both.

## Run the file checks

With Python 3.10+ and the repository dependencies installed:

```sh
python3 scripts/validate.py --report docs/validation.json
python3 -m unittest discover -s tests
```

The validator checks the five-field manifest, static v2 image, cell population and margins, PNG/WebP equality, final crops, approved-source fidelity, archive hashes, decoding, metadata, common private-data markers, file sizes, and distribution checksums. Regression tests preserve coverage of the damaged v1.0.0 atlas and the reported hair pixels, and check the approved runtime and frozen standard rows.

The current pixel guard reads [art/approved-runtime.json](../art/approved-runtime.json), checks the checksum of [art/approved/v1.0.2/spritesheet.png](../art/approved/v1.0.2/spritesheet.png), and compares its full RGBA pixels with the runtime. A separate guard keeps the first nine rows fixed to the v1.0.1 PNG, protecting all 57 standard frames and the transparent cells in those rows. An intentional artwork revision needs a newly reviewed baseline and checksum, with historical sources and regression cases preserved. CI runs the file validator and regression tests; visual review remains a separate step.

## Release checklist

- [ ] Review changed frames, adjacent frames, complete loops, and state transitions.
- [ ] Repeat independent direction comparisons after changing a look pose.
- [ ] Generate previews from the exact WebP to be distributed.
- [ ] Update source records, checksums, and both language editions.
- [ ] Check attribution, metadata, and public-file privacy.
- [ ] Run file validation and regression tests; inspect the package contents.
- [ ] Align `VERSION`, the installer URL, and the version tag.
- [ ] Verify CI on the release commit and compare public downloads with the validated files.
